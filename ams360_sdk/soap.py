from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional
import time
import requests

from zeep import Client, Settings
from zeep.transports import Transport
from zeep.plugins import HistoryPlugin
from zeep.exceptions import Fault

from .config import AMS360Config
from .errors import AMS360SoapFault

@dataclass
class SoapDebug:
    last_sent: str = ""
    last_received: str = ""

class SoapClient:
    """
    Thin Zeep wrapper:
    - persistent requests.Session
    - history plugin for debugging raw SOAP
    - simple retry on transient failures
    """
    def __init__(self, cfg: AMS360Config) -> None:
        self.cfg = cfg
        self.history = HistoryPlugin()
        self.debug = SoapDebug()

        session = requests.Session()
        session.verify = cfg.verify_tls

        transport = Transport(
            session=session,
            timeout=cfg.timeout_seconds,
            operation_timeout=cfg.operation_timeout_seconds,
        )

        settings = Settings(strict=False, xml_huge_tree=True)

        self.client = Client(
            wsdl=cfg.wsdl_url,
            transport=transport,
            settings=settings,
            plugins=[self.history],
        )

        # Force service address to your endpoint (helps if WSDL lists different host)
        for service in self.client.wsdl.services.values():
            for port in service.ports.values():
                port.binding_options["address"] = cfg.endpoint_url

    def _capture_debug(self) -> None:
        try:
            sent = self.history.last_sent["envelope"]
            recv = self.history.last_received["envelope"]
            self.debug.last_sent = sent.decode("utf-8") if hasattr(sent, "decode") else str(sent)
            self.debug.last_received = recv.decode("utf-8") if hasattr(recv, "decode") else str(recv)
        except Exception:
            # best effort
            pass

    def call(self, op_name: str, retries: int = 2, backoff: float = 0.8, **kwargs: Any) -> Any:
        """
        Call an operation with light retry. Raises AMS360SoapFault on SOAP Fault.
        """
        fn = getattr(self.client.service, op_name, None)
        if not fn:
            raise AttributeError(f"Operation '{op_name}' not found on WSDL client.service")

        last_exc: Optional[Exception] = None
        for attempt in range(retries + 1):
            try:
                res = fn(**kwargs)
                self._capture_debug()
                return res
            except Fault as f:
                self._capture_debug()
                # SOAP fault is not transient in most cases; surface it immediately.
                raise AMS360SoapFault(str(f)) from f
            except Exception as e:
                self._capture_debug()
                last_exc = e
                if attempt < retries:
                    time.sleep(backoff * (2 ** attempt))
                    continue
                raise
        raise last_exc  # unreachable
