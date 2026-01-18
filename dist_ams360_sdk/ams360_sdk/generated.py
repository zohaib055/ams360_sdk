from dataclasses import asdict, is_dataclass
from typing import Any, Dict, Optional, Union
from .models import (
    BankGetByCodeRequest,
    BrokerGetByCodeRequest,
    BrokerGetByShortNameRequest,
    BrokerGetListByLastNamePrefixRequest,
    ClaimGetByIdRequest,
    ClaimGetListByCustomerIdRequest,
    ClaimGetListByPolicyIdRequest,
    CommonNoteInsertRequest,
    CommonSuspenseDeleteRequest,
    CommonSuspenseGetBySuspenseIdRequest,
    CommonSuspenseGetListByEntityIdRequest,
    CommonSuspenseInsertRequest,
    CommonSuspenseUpdateRequest,
    CompanyGetByCodeRequest,
    CompanyGetByShortNameRequest,
    CompanyGetListByNamePrefixRequest,
    CompanyGetListByParentCompanyCodeRequest,
    CompanyGetListByTypeRequest,
    CustomerActivityInsertRequest,
    CustomerGetByIdRequest,
    CustomerGetByNumberRequest,
    CustomerGetListByNamePrefixRequest,
    CustomerInsertRequest,
    CustomerNoteInsertRequest,
    CustomerServicePersonnelGetListRequest,
    CustomerServicePersonnelModifyListRequest,
    CustomerSuspenseDeleteRequest,
    CustomerSuspenseGetBySuspenseIdRequest,
    CustomerSuspenseGetListByCustomerIdRequest,
    CustomerSuspenseInsertRequest,
    CustomerSuspenseUpdateRequest,
    CustomerUpdateRequest,
    EmployeeGetByCodeRequest,
    EmployeeGetByShortNameRequest,
    EmployeeGetListByLastNamePrefixRequest,
    EmployeeGetListByTypeRequest,
    EmployeeInsertRequest,
    EmployeeUpdateRequest,
    FileChunkBeginRequest,
    FileChunkEndRequest,
    FileChunkSendRequest,
    GLBranchGetByCodeRequest,
    GLBranchGetByShortNameRequest,
    GLBranchGetListByGLDivisionCodeRequest,
    GLBranchGetListByNamePrefixRequest,
    GLDepartmentGetByCodeRequest,
    GLDepartmentGetByShortNameRequest,
    GLDepartmentGetListByGLBranchCodeRequest,
    GLDepartmentGetListByNamePrefixRequest,
    GLDivisionGetByCodeRequest,
    GLDivisionGetByShortNameRequest,
    GLDivisionGetListByNamePrefixRequest,
    GLGroupGetByCodeRequest,
    GLGroupGetByShortNameRequest,
    GLGroupGetListByGLDepartmentCodeRequest,
    GLGroupGetListByNamePrefixRequest,
    LineOfBusinessGetByCodeRequest,
    LineOfBusinessGetListRequest,
    LoginRequest,
    PersonalNoteGetListRequest,
    PersonalNoteInsertRequest,
    PlanTypeGetByCodeRequest,
    PlanTypeGetListByCompanyCodeRequest,
    PolicyCorrectRequest,
    PolicyEndorseRequest,
    PolicyGetListByCustomerIdRequest,
    PolicyGetListByCustomerNumberRequest,
    PolicyGetListByPolicyNumberAndDateRequest,
    PolicyGetListByPolicyNumberRequest,
    PolicyGetRequest,
    SearchByPhoneNumberRequest,
    ValueListGetRequest,
    VendorGetByCodeRequest,
    VendorGetListByIsCompanyRequest,
    VendorGetListByLastNamePrefixRequest,
    VendorInvoiceGetByIdRequest,
    VendorInvoiceGetListByVendorRequest,
)
from .client import AMS360Client

class Generated:
    def __init__(self, ams: AMS360Client) -> None:
        self.ams = ams

    @staticmethod
    def _normalize_request(request: Any) -> Any:
        if request is None:
            return None
        if hasattr(request, "to_dict"):
            return request.to_dict()
        if is_dataclass(request):
            return asdict(request)
        return request

    def call(self, operation: str, **kwargs: Any) -> Any:
        return self.ams.call(operation, **kwargs)

    def call_json(self, operation: str, **kwargs: Any) -> Dict[str, Any]:
        return self.ams.call_json(operation, **kwargs)

    def ams360_agency_url_get(self, **kwargs: Any) -> Any:
        """AMS360AgencyUrlGet"""
        return self.ams.call('AMS360AgencyUrlGet', **kwargs)

    def ams360_agency_url_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """AMS360AgencyUrlGet (JSON)"""
        return self.ams.call_json('AMS360AgencyUrlGet', **kwargs)

    def AMS360AgencyUrlGet(self, **kwargs: Any) -> Any:
        """AMS360AgencyUrlGet (original op name wrapper)"""
        return self.ams.call('AMS360AgencyUrlGet', **kwargs)

    def agency_info_get(self, **kwargs: Any) -> Any:
        """AgencyInfoGet"""
        return self.ams.call('AgencyInfoGet', **kwargs)

    def agency_info_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """AgencyInfoGet (JSON)"""
        return self.ams.call_json('AgencyInfoGet', **kwargs)

    def AgencyInfoGet(self, **kwargs: Any) -> Any:
        """AgencyInfoGet (original op name wrapper)"""
        return self.ams.call('AgencyInfoGet', **kwargs)

    def bank_get_by_code(self, request: Optional[Union[BankGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BankGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BankGetByCode', **kwargs)

    def bank_get_by_code_json(self, request: Optional[Union[BankGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """BankGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('BankGetByCode', **kwargs)

    def BankGetByCode(self, request: Optional[Union[BankGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BankGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BankGetByCode', **kwargs)

    def bank_get_list_all(self, **kwargs: Any) -> Any:
        """BankGetListAll"""
        return self.ams.call('BankGetListAll', **kwargs)

    def bank_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """BankGetListAll (JSON)"""
        return self.ams.call_json('BankGetListAll', **kwargs)

    def BankGetListAll(self, **kwargs: Any) -> Any:
        """BankGetListAll (original op name wrapper)"""
        return self.ams.call('BankGetListAll', **kwargs)

    def bank_get_list_by_account_type(self, **kwargs: Any) -> Any:
        """BankGetListByAccountType"""
        return self.ams.call('BankGetListByAccountType', **kwargs)

    def bank_get_list_by_account_type_json(self, **kwargs: Any) -> Dict[str, Any]:
        """BankGetListByAccountType (JSON)"""
        return self.ams.call_json('BankGetListByAccountType', **kwargs)

    def BankGetListByAccountType(self, **kwargs: Any) -> Any:
        """BankGetListByAccountType (original op name wrapper)"""
        return self.ams.call('BankGetListByAccountType', **kwargs)

    def bank_get_list_by_bank_name_prefix(self, **kwargs: Any) -> Any:
        """BankGetListByBankNamePrefix"""
        return self.ams.call('BankGetListByBankNamePrefix', **kwargs)

    def bank_get_list_by_bank_name_prefix_json(self, **kwargs: Any) -> Dict[str, Any]:
        """BankGetListByBankNamePrefix (JSON)"""
        return self.ams.call_json('BankGetListByBankNamePrefix', **kwargs)

    def BankGetListByBankNamePrefix(self, **kwargs: Any) -> Any:
        """BankGetListByBankNamePrefix (original op name wrapper)"""
        return self.ams.call('BankGetListByBankNamePrefix', **kwargs)

    def broker_get_by_code(self, request: Optional[Union[BrokerGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BrokerGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BrokerGetByCode', **kwargs)

    def broker_get_by_code_json(self, request: Optional[Union[BrokerGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """BrokerGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('BrokerGetByCode', **kwargs)

    def BrokerGetByCode(self, request: Optional[Union[BrokerGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BrokerGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BrokerGetByCode', **kwargs)

    def broker_get_by_short_name(self, request: Optional[Union[BrokerGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BrokerGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BrokerGetByShortName', **kwargs)

    def broker_get_by_short_name_json(self, request: Optional[Union[BrokerGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """BrokerGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('BrokerGetByShortName', **kwargs)

    def BrokerGetByShortName(self, request: Optional[Union[BrokerGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BrokerGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BrokerGetByShortName', **kwargs)

    def broker_get_list_all(self, **kwargs: Any) -> Any:
        """BrokerGetListAll"""
        return self.ams.call('BrokerGetListAll', **kwargs)

    def broker_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """BrokerGetListAll (JSON)"""
        return self.ams.call_json('BrokerGetListAll', **kwargs)

    def BrokerGetListAll(self, **kwargs: Any) -> Any:
        """BrokerGetListAll (original op name wrapper)"""
        return self.ams.call('BrokerGetListAll', **kwargs)

    def broker_get_list_by_last_name_prefix(self, request: Optional[Union[BrokerGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BrokerGetListByLastNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BrokerGetListByLastNamePrefix', **kwargs)

    def broker_get_list_by_last_name_prefix_json(self, request: Optional[Union[BrokerGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """BrokerGetListByLastNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('BrokerGetListByLastNamePrefix', **kwargs)

    def BrokerGetListByLastNamePrefix(self, request: Optional[Union[BrokerGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """BrokerGetListByLastNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('BrokerGetListByLastNamePrefix', **kwargs)

    def claim_get_by_id(self, request: Optional[Union[ClaimGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ClaimGetById"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ClaimGetById', **kwargs)

    def claim_get_by_id_json(self, request: Optional[Union[ClaimGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """ClaimGetById (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('ClaimGetById', **kwargs)

    def ClaimGetById(self, request: Optional[Union[ClaimGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ClaimGetById (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ClaimGetById', **kwargs)

    def claim_get_list_by_customer_id(self, request: Optional[Union[ClaimGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ClaimGetListByCustomerId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ClaimGetListByCustomerId', **kwargs)

    def claim_get_list_by_customer_id_json(self, request: Optional[Union[ClaimGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """ClaimGetListByCustomerId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('ClaimGetListByCustomerId', **kwargs)

    def ClaimGetListByCustomerId(self, request: Optional[Union[ClaimGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ClaimGetListByCustomerId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ClaimGetListByCustomerId', **kwargs)

    def claim_get_list_by_policy_id(self, request: Optional[Union[ClaimGetListByPolicyIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ClaimGetListByPolicyId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ClaimGetListByPolicyId', **kwargs)

    def claim_get_list_by_policy_id_json(self, request: Optional[Union[ClaimGetListByPolicyIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """ClaimGetListByPolicyId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('ClaimGetListByPolicyId', **kwargs)

    def ClaimGetListByPolicyId(self, request: Optional[Union[ClaimGetListByPolicyIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ClaimGetListByPolicyId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ClaimGetListByPolicyId', **kwargs)

    def common_activity_insert(self, **kwargs: Any) -> Any:
        """CommonActivityInsert"""
        return self.ams.call('CommonActivityInsert', **kwargs)

    def common_activity_insert_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CommonActivityInsert (JSON)"""
        return self.ams.call_json('CommonActivityInsert', **kwargs)

    def CommonActivityInsert(self, **kwargs: Any) -> Any:
        """CommonActivityInsert (original op name wrapper)"""
        return self.ams.call('CommonActivityInsert', **kwargs)

    def common_note_get_note_text_by_id(self, **kwargs: Any) -> Any:
        """CommonNoteGetNoteTextById"""
        return self.ams.call('CommonNoteGetNoteTextById', **kwargs)

    def common_note_get_note_text_by_id_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CommonNoteGetNoteTextById (JSON)"""
        return self.ams.call_json('CommonNoteGetNoteTextById', **kwargs)

    def CommonNoteGetNoteTextById(self, **kwargs: Any) -> Any:
        """CommonNoteGetNoteTextById (original op name wrapper)"""
        return self.ams.call('CommonNoteGetNoteTextById', **kwargs)

    def common_note_insert(self, request: Optional[Union[CommonNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonNoteInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonNoteInsert', **kwargs)

    def common_note_insert_json(self, request: Optional[Union[CommonNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CommonNoteInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CommonNoteInsert', **kwargs)

    def CommonNoteInsert(self, request: Optional[Union[CommonNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonNoteInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonNoteInsert', **kwargs)

    def common_note_update_note_text(self, **kwargs: Any) -> Any:
        """CommonNoteUpdateNoteText"""
        return self.ams.call('CommonNoteUpdateNoteText', **kwargs)

    def common_note_update_note_text_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CommonNoteUpdateNoteText (JSON)"""
        return self.ams.call_json('CommonNoteUpdateNoteText', **kwargs)

    def CommonNoteUpdateNoteText(self, **kwargs: Any) -> Any:
        """CommonNoteUpdateNoteText (original op name wrapper)"""
        return self.ams.call('CommonNoteUpdateNoteText', **kwargs)

    def common_suspense_delete(self, request: Optional[Union[CommonSuspenseDeleteRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseDelete"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseDelete', **kwargs)

    def common_suspense_delete_json(self, request: Optional[Union[CommonSuspenseDeleteRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CommonSuspenseDelete (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CommonSuspenseDelete', **kwargs)

    def CommonSuspenseDelete(self, request: Optional[Union[CommonSuspenseDeleteRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseDelete (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseDelete', **kwargs)

    def common_suspense_get_by_suspense_id(self, request: Optional[Union[CommonSuspenseGetBySuspenseIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseGetBySuspenseId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseGetBySuspenseId', **kwargs)

    def common_suspense_get_by_suspense_id_json(self, request: Optional[Union[CommonSuspenseGetBySuspenseIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CommonSuspenseGetBySuspenseId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CommonSuspenseGetBySuspenseId', **kwargs)

    def CommonSuspenseGetBySuspenseId(self, request: Optional[Union[CommonSuspenseGetBySuspenseIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseGetBySuspenseId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseGetBySuspenseId', **kwargs)

    def common_suspense_get_list_by_entity_id(self, request: Optional[Union[CommonSuspenseGetListByEntityIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseGetListByEntityId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseGetListByEntityId', **kwargs)

    def common_suspense_get_list_by_entity_id_json(self, request: Optional[Union[CommonSuspenseGetListByEntityIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CommonSuspenseGetListByEntityId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CommonSuspenseGetListByEntityId', **kwargs)

    def CommonSuspenseGetListByEntityId(self, request: Optional[Union[CommonSuspenseGetListByEntityIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseGetListByEntityId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseGetListByEntityId', **kwargs)

    def common_suspense_insert(self, request: Optional[Union[CommonSuspenseInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseInsert', **kwargs)

    def common_suspense_insert_json(self, request: Optional[Union[CommonSuspenseInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CommonSuspenseInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CommonSuspenseInsert', **kwargs)

    def CommonSuspenseInsert(self, request: Optional[Union[CommonSuspenseInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseInsert', **kwargs)

    def common_suspense_update(self, request: Optional[Union[CommonSuspenseUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseUpdate"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseUpdate', **kwargs)

    def common_suspense_update_json(self, request: Optional[Union[CommonSuspenseUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CommonSuspenseUpdate (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CommonSuspenseUpdate', **kwargs)

    def CommonSuspenseUpdate(self, request: Optional[Union[CommonSuspenseUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CommonSuspenseUpdate (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CommonSuspenseUpdate', **kwargs)

    def company_get_by_code(self, request: Optional[Union[CompanyGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetByCode', **kwargs)

    def company_get_by_code_json(self, request: Optional[Union[CompanyGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CompanyGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CompanyGetByCode', **kwargs)

    def CompanyGetByCode(self, request: Optional[Union[CompanyGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetByCode', **kwargs)

    def company_get_by_short_name(self, request: Optional[Union[CompanyGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetByShortName', **kwargs)

    def company_get_by_short_name_json(self, request: Optional[Union[CompanyGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CompanyGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CompanyGetByShortName', **kwargs)

    def CompanyGetByShortName(self, request: Optional[Union[CompanyGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetByShortName', **kwargs)

    def company_get_list_all(self, **kwargs: Any) -> Any:
        """CompanyGetListAll"""
        return self.ams.call('CompanyGetListAll', **kwargs)

    def company_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CompanyGetListAll (JSON)"""
        return self.ams.call_json('CompanyGetListAll', **kwargs)

    def CompanyGetListAll(self, **kwargs: Any) -> Any:
        """CompanyGetListAll (original op name wrapper)"""
        return self.ams.call('CompanyGetListAll', **kwargs)

    def company_get_list_by_name_prefix(self, request: Optional[Union[CompanyGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetListByNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetListByNamePrefix', **kwargs)

    def company_get_list_by_name_prefix_json(self, request: Optional[Union[CompanyGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CompanyGetListByNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CompanyGetListByNamePrefix', **kwargs)

    def CompanyGetListByNamePrefix(self, request: Optional[Union[CompanyGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetListByNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetListByNamePrefix', **kwargs)

    def company_get_list_by_parent_company_code(self, request: Optional[Union[CompanyGetListByParentCompanyCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetListByParentCompanyCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetListByParentCompanyCode', **kwargs)

    def company_get_list_by_parent_company_code_json(self, request: Optional[Union[CompanyGetListByParentCompanyCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CompanyGetListByParentCompanyCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CompanyGetListByParentCompanyCode', **kwargs)

    def CompanyGetListByParentCompanyCode(self, request: Optional[Union[CompanyGetListByParentCompanyCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetListByParentCompanyCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetListByParentCompanyCode', **kwargs)

    def company_get_list_by_type(self, request: Optional[Union[CompanyGetListByTypeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetListByType"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetListByType', **kwargs)

    def company_get_list_by_type_json(self, request: Optional[Union[CompanyGetListByTypeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CompanyGetListByType (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CompanyGetListByType', **kwargs)

    def CompanyGetListByType(self, request: Optional[Union[CompanyGetListByTypeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CompanyGetListByType (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CompanyGetListByType', **kwargs)

    def customer_activity_insert(self, request: Optional[Union[CustomerActivityInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerActivityInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerActivityInsert', **kwargs)

    def customer_activity_insert_json(self, request: Optional[Union[CustomerActivityInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerActivityInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerActivityInsert', **kwargs)

    def CustomerActivityInsert(self, request: Optional[Union[CustomerActivityInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerActivityInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerActivityInsert', **kwargs)

    def customer_contact_delete(self, **kwargs: Any) -> Any:
        """CustomerContactDelete"""
        return self.ams.call('CustomerContactDelete', **kwargs)

    def customer_contact_delete_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerContactDelete (JSON)"""
        return self.ams.call_json('CustomerContactDelete', **kwargs)

    def CustomerContactDelete(self, **kwargs: Any) -> Any:
        """CustomerContactDelete (original op name wrapper)"""
        return self.ams.call('CustomerContactDelete', **kwargs)

    def customer_contact_get(self, **kwargs: Any) -> Any:
        """CustomerContactGet"""
        return self.ams.call('CustomerContactGet', **kwargs)

    def customer_contact_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerContactGet (JSON)"""
        return self.ams.call_json('CustomerContactGet', **kwargs)

    def CustomerContactGet(self, **kwargs: Any) -> Any:
        """CustomerContactGet (original op name wrapper)"""
        return self.ams.call('CustomerContactGet', **kwargs)

    def customer_contact_get_list(self, **kwargs: Any) -> Any:
        """CustomerContactGetList"""
        return self.ams.call('CustomerContactGetList', **kwargs)

    def customer_contact_get_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerContactGetList (JSON)"""
        return self.ams.call_json('CustomerContactGetList', **kwargs)

    def CustomerContactGetList(self, **kwargs: Any) -> Any:
        """CustomerContactGetList (original op name wrapper)"""
        return self.ams.call('CustomerContactGetList', **kwargs)

    def customer_contact_insert(self, **kwargs: Any) -> Any:
        """CustomerContactInsert"""
        return self.ams.call('CustomerContactInsert', **kwargs)

    def customer_contact_insert_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerContactInsert (JSON)"""
        return self.ams.call_json('CustomerContactInsert', **kwargs)

    def CustomerContactInsert(self, **kwargs: Any) -> Any:
        """CustomerContactInsert (original op name wrapper)"""
        return self.ams.call('CustomerContactInsert', **kwargs)

    def customer_contact_update(self, **kwargs: Any) -> Any:
        """CustomerContactUpdate"""
        return self.ams.call('CustomerContactUpdate', **kwargs)

    def customer_contact_update_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerContactUpdate (JSON)"""
        return self.ams.call_json('CustomerContactUpdate', **kwargs)

    def CustomerContactUpdate(self, **kwargs: Any) -> Any:
        """CustomerContactUpdate (original op name wrapper)"""
        return self.ams.call('CustomerContactUpdate', **kwargs)

    def customer_dependent_delete(self, **kwargs: Any) -> Any:
        """CustomerDependentDelete"""
        return self.ams.call('CustomerDependentDelete', **kwargs)

    def customer_dependent_delete_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerDependentDelete (JSON)"""
        return self.ams.call_json('CustomerDependentDelete', **kwargs)

    def CustomerDependentDelete(self, **kwargs: Any) -> Any:
        """CustomerDependentDelete (original op name wrapper)"""
        return self.ams.call('CustomerDependentDelete', **kwargs)

    def customer_dependent_get(self, **kwargs: Any) -> Any:
        """CustomerDependentGet"""
        return self.ams.call('CustomerDependentGet', **kwargs)

    def customer_dependent_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerDependentGet (JSON)"""
        return self.ams.call_json('CustomerDependentGet', **kwargs)

    def CustomerDependentGet(self, **kwargs: Any) -> Any:
        """CustomerDependentGet (original op name wrapper)"""
        return self.ams.call('CustomerDependentGet', **kwargs)

    def customer_dependent_get_list(self, **kwargs: Any) -> Any:
        """CustomerDependentGetList"""
        return self.ams.call('CustomerDependentGetList', **kwargs)

    def customer_dependent_get_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerDependentGetList (JSON)"""
        return self.ams.call_json('CustomerDependentGetList', **kwargs)

    def CustomerDependentGetList(self, **kwargs: Any) -> Any:
        """CustomerDependentGetList (original op name wrapper)"""
        return self.ams.call('CustomerDependentGetList', **kwargs)

    def customer_dependent_insert(self, **kwargs: Any) -> Any:
        """CustomerDependentInsert"""
        return self.ams.call('CustomerDependentInsert', **kwargs)

    def customer_dependent_insert_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerDependentInsert (JSON)"""
        return self.ams.call_json('CustomerDependentInsert', **kwargs)

    def CustomerDependentInsert(self, **kwargs: Any) -> Any:
        """CustomerDependentInsert (original op name wrapper)"""
        return self.ams.call('CustomerDependentInsert', **kwargs)

    def customer_dependent_update(self, **kwargs: Any) -> Any:
        """CustomerDependentUpdate"""
        return self.ams.call('CustomerDependentUpdate', **kwargs)

    def customer_dependent_update_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerDependentUpdate (JSON)"""
        return self.ams.call_json('CustomerDependentUpdate', **kwargs)

    def CustomerDependentUpdate(self, **kwargs: Any) -> Any:
        """CustomerDependentUpdate (original op name wrapper)"""
        return self.ams.call('CustomerDependentUpdate', **kwargs)

    def customer_get_by_id(self, request: Optional[Union[CustomerGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerGetById"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerGetById', **kwargs)

    def customer_get_by_id_json(self, request: Optional[Union[CustomerGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerGetById (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerGetById', **kwargs)

    def CustomerGetById(self, request: Optional[Union[CustomerGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerGetById (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerGetById', **kwargs)

    def customer_get_by_number(self, request: Optional[Union[CustomerGetByNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerGetByNumber"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerGetByNumber', **kwargs)

    def customer_get_by_number_json(self, request: Optional[Union[CustomerGetByNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerGetByNumber (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerGetByNumber', **kwargs)

    def CustomerGetByNumber(self, request: Optional[Union[CustomerGetByNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerGetByNumber (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerGetByNumber', **kwargs)

    def customer_get_list_by_name_prefix(self, request: Optional[Union[CustomerGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerGetListByNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerGetListByNamePrefix', **kwargs)

    def customer_get_list_by_name_prefix_json(self, request: Optional[Union[CustomerGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerGetListByNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerGetListByNamePrefix', **kwargs)

    def CustomerGetListByNamePrefix(self, request: Optional[Union[CustomerGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerGetListByNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerGetListByNamePrefix', **kwargs)

    def customer_insert(self, request: Optional[Union[CustomerInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerInsert', **kwargs)

    def customer_insert_json(self, request: Optional[Union[CustomerInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerInsert', **kwargs)

    def CustomerInsert(self, request: Optional[Union[CustomerInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerInsert', **kwargs)

    def customer_note_get_note_text_by_id(self, **kwargs: Any) -> Any:
        """CustomerNoteGetNoteTextById"""
        return self.ams.call('CustomerNoteGetNoteTextById', **kwargs)

    def customer_note_get_note_text_by_id_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerNoteGetNoteTextById (JSON)"""
        return self.ams.call_json('CustomerNoteGetNoteTextById', **kwargs)

    def CustomerNoteGetNoteTextById(self, **kwargs: Any) -> Any:
        """CustomerNoteGetNoteTextById (original op name wrapper)"""
        return self.ams.call('CustomerNoteGetNoteTextById', **kwargs)

    def customer_note_insert(self, request: Optional[Union[CustomerNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerNoteInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerNoteInsert', **kwargs)

    def customer_note_insert_json(self, request: Optional[Union[CustomerNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerNoteInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerNoteInsert', **kwargs)

    def CustomerNoteInsert(self, request: Optional[Union[CustomerNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerNoteInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerNoteInsert', **kwargs)

    def customer_note_update_note_text(self, **kwargs: Any) -> Any:
        """CustomerNoteUpdateNoteText"""
        return self.ams.call('CustomerNoteUpdateNoteText', **kwargs)

    def customer_note_update_note_text_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerNoteUpdateNoteText (JSON)"""
        return self.ams.call_json('CustomerNoteUpdateNoteText', **kwargs)

    def CustomerNoteUpdateNoteText(self, **kwargs: Any) -> Any:
        """CustomerNoteUpdateNoteText (original op name wrapper)"""
        return self.ams.call('CustomerNoteUpdateNoteText', **kwargs)

    def customer_profile_answer_delete(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerDelete"""
        return self.ams.call('CustomerProfileAnswerDelete', **kwargs)

    def customer_profile_answer_delete_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerProfileAnswerDelete (JSON)"""
        return self.ams.call_json('CustomerProfileAnswerDelete', **kwargs)

    def CustomerProfileAnswerDelete(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerDelete (original op name wrapper)"""
        return self.ams.call('CustomerProfileAnswerDelete', **kwargs)

    def customer_profile_answer_get(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerGet"""
        return self.ams.call('CustomerProfileAnswerGet', **kwargs)

    def customer_profile_answer_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerProfileAnswerGet (JSON)"""
        return self.ams.call_json('CustomerProfileAnswerGet', **kwargs)

    def CustomerProfileAnswerGet(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerGet (original op name wrapper)"""
        return self.ams.call('CustomerProfileAnswerGet', **kwargs)

    def customer_profile_answer_get_list(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerGetList"""
        return self.ams.call('CustomerProfileAnswerGetList', **kwargs)

    def customer_profile_answer_get_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerProfileAnswerGetList (JSON)"""
        return self.ams.call_json('CustomerProfileAnswerGetList', **kwargs)

    def CustomerProfileAnswerGetList(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerGetList (original op name wrapper)"""
        return self.ams.call('CustomerProfileAnswerGetList', **kwargs)

    def customer_profile_answer_update(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerUpdate"""
        return self.ams.call('CustomerProfileAnswerUpdate', **kwargs)

    def customer_profile_answer_update_json(self, **kwargs: Any) -> Dict[str, Any]:
        """CustomerProfileAnswerUpdate (JSON)"""
        return self.ams.call_json('CustomerProfileAnswerUpdate', **kwargs)

    def CustomerProfileAnswerUpdate(self, **kwargs: Any) -> Any:
        """CustomerProfileAnswerUpdate (original op name wrapper)"""
        return self.ams.call('CustomerProfileAnswerUpdate', **kwargs)

    def customer_service_personnel_get_list(self, request: Optional[Union[CustomerServicePersonnelGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerServicePersonnelGetList"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerServicePersonnelGetList', **kwargs)

    def customer_service_personnel_get_list_json(self, request: Optional[Union[CustomerServicePersonnelGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerServicePersonnelGetList (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerServicePersonnelGetList', **kwargs)

    def CustomerServicePersonnelGetList(self, request: Optional[Union[CustomerServicePersonnelGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerServicePersonnelGetList (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerServicePersonnelGetList', **kwargs)

    def customer_service_personnel_modify_list(self, request: Optional[Union[CustomerServicePersonnelModifyListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerServicePersonnelModifyList"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerServicePersonnelModifyList', **kwargs)

    def customer_service_personnel_modify_list_json(self, request: Optional[Union[CustomerServicePersonnelModifyListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerServicePersonnelModifyList (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerServicePersonnelModifyList', **kwargs)

    def CustomerServicePersonnelModifyList(self, request: Optional[Union[CustomerServicePersonnelModifyListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerServicePersonnelModifyList (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerServicePersonnelModifyList', **kwargs)

    def customer_suspense_delete(self, request: Optional[Union[CustomerSuspenseDeleteRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseDelete"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseDelete', **kwargs)

    def customer_suspense_delete_json(self, request: Optional[Union[CustomerSuspenseDeleteRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerSuspenseDelete (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerSuspenseDelete', **kwargs)

    def CustomerSuspenseDelete(self, request: Optional[Union[CustomerSuspenseDeleteRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseDelete (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseDelete', **kwargs)

    def customer_suspense_get_by_suspense_id(self, request: Optional[Union[CustomerSuspenseGetBySuspenseIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseGetBySuspenseId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseGetBySuspenseId', **kwargs)

    def customer_suspense_get_by_suspense_id_json(self, request: Optional[Union[CustomerSuspenseGetBySuspenseIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerSuspenseGetBySuspenseId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerSuspenseGetBySuspenseId', **kwargs)

    def CustomerSuspenseGetBySuspenseId(self, request: Optional[Union[CustomerSuspenseGetBySuspenseIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseGetBySuspenseId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseGetBySuspenseId', **kwargs)

    def customer_suspense_get_list_by_customer_id(self, request: Optional[Union[CustomerSuspenseGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseGetListByCustomerId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseGetListByCustomerId', **kwargs)

    def customer_suspense_get_list_by_customer_id_json(self, request: Optional[Union[CustomerSuspenseGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerSuspenseGetListByCustomerId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerSuspenseGetListByCustomerId', **kwargs)

    def CustomerSuspenseGetListByCustomerId(self, request: Optional[Union[CustomerSuspenseGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseGetListByCustomerId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseGetListByCustomerId', **kwargs)

    def customer_suspense_insert(self, request: Optional[Union[CustomerSuspenseInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseInsert', **kwargs)

    def customer_suspense_insert_json(self, request: Optional[Union[CustomerSuspenseInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerSuspenseInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerSuspenseInsert', **kwargs)

    def CustomerSuspenseInsert(self, request: Optional[Union[CustomerSuspenseInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseInsert', **kwargs)

    def customer_suspense_update(self, request: Optional[Union[CustomerSuspenseUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseUpdate"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseUpdate', **kwargs)

    def customer_suspense_update_json(self, request: Optional[Union[CustomerSuspenseUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerSuspenseUpdate (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerSuspenseUpdate', **kwargs)

    def CustomerSuspenseUpdate(self, request: Optional[Union[CustomerSuspenseUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerSuspenseUpdate (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerSuspenseUpdate', **kwargs)

    def customer_update(self, request: Optional[Union[CustomerUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerUpdate"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerUpdate', **kwargs)

    def customer_update_json(self, request: Optional[Union[CustomerUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CustomerUpdate (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('CustomerUpdate', **kwargs)

    def CustomerUpdate(self, request: Optional[Union[CustomerUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """CustomerUpdate (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('CustomerUpdate', **kwargs)

    def employee_get_by_code(self, request: Optional[Union[EmployeeGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetByCode', **kwargs)

    def employee_get_by_code_json(self, request: Optional[Union[EmployeeGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('EmployeeGetByCode', **kwargs)

    def EmployeeGetByCode(self, request: Optional[Union[EmployeeGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetByCode', **kwargs)

    def employee_get_by_short_name(self, request: Optional[Union[EmployeeGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetByShortName', **kwargs)

    def employee_get_by_short_name_json(self, request: Optional[Union[EmployeeGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('EmployeeGetByShortName', **kwargs)

    def EmployeeGetByShortName(self, request: Optional[Union[EmployeeGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetByShortName', **kwargs)

    def employee_get_list_all(self, **kwargs: Any) -> Any:
        """EmployeeGetListAll"""
        return self.ams.call('EmployeeGetListAll', **kwargs)

    def employee_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeGetListAll (JSON)"""
        return self.ams.call_json('EmployeeGetListAll', **kwargs)

    def EmployeeGetListAll(self, **kwargs: Any) -> Any:
        """EmployeeGetListAll (original op name wrapper)"""
        return self.ams.call('EmployeeGetListAll', **kwargs)

    def employee_get_list_by_last_name_prefix(self, request: Optional[Union[EmployeeGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetListByLastNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetListByLastNamePrefix', **kwargs)

    def employee_get_list_by_last_name_prefix_json(self, request: Optional[Union[EmployeeGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeGetListByLastNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('EmployeeGetListByLastNamePrefix', **kwargs)

    def EmployeeGetListByLastNamePrefix(self, request: Optional[Union[EmployeeGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetListByLastNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetListByLastNamePrefix', **kwargs)

    def employee_get_list_by_type(self, request: Optional[Union[EmployeeGetListByTypeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetListByType"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetListByType', **kwargs)

    def employee_get_list_by_type_json(self, request: Optional[Union[EmployeeGetListByTypeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeGetListByType (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('EmployeeGetListByType', **kwargs)

    def EmployeeGetListByType(self, request: Optional[Union[EmployeeGetListByTypeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeGetListByType (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeGetListByType', **kwargs)

    def employee_insert(self, request: Optional[Union[EmployeeInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeInsert', **kwargs)

    def employee_insert_json(self, request: Optional[Union[EmployeeInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('EmployeeInsert', **kwargs)

    def EmployeeInsert(self, request: Optional[Union[EmployeeInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeInsert', **kwargs)

    def employee_update(self, request: Optional[Union[EmployeeUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeUpdate"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeUpdate', **kwargs)

    def employee_update_json(self, request: Optional[Union[EmployeeUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """EmployeeUpdate (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('EmployeeUpdate', **kwargs)

    def EmployeeUpdate(self, request: Optional[Union[EmployeeUpdateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """EmployeeUpdate (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('EmployeeUpdate', **kwargs)

    def file_chunk_begin(self, request: Optional[Union[FileChunkBeginRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """FileChunkBegin"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('FileChunkBegin', **kwargs)

    def file_chunk_begin_json(self, request: Optional[Union[FileChunkBeginRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """FileChunkBegin (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('FileChunkBegin', **kwargs)

    def FileChunkBegin(self, request: Optional[Union[FileChunkBeginRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """FileChunkBegin (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('FileChunkBegin', **kwargs)

    def file_chunk_end(self, request: Optional[Union[FileChunkEndRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """FileChunkEnd"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('FileChunkEnd', **kwargs)

    def file_chunk_end_json(self, request: Optional[Union[FileChunkEndRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """FileChunkEnd (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('FileChunkEnd', **kwargs)

    def FileChunkEnd(self, request: Optional[Union[FileChunkEndRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """FileChunkEnd (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('FileChunkEnd', **kwargs)

    def file_chunk_send(self, request: Optional[Union[FileChunkSendRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """FileChunkSend"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('FileChunkSend', **kwargs)

    def file_chunk_send_json(self, request: Optional[Union[FileChunkSendRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """FileChunkSend (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('FileChunkSend', **kwargs)

    def FileChunkSend(self, request: Optional[Union[FileChunkSendRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """FileChunkSend (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('FileChunkSend', **kwargs)

    def gl_branch_get_by_code(self, request: Optional[Union[GLBranchGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetByCode', **kwargs)

    def gl_branch_get_by_code_json(self, request: Optional[Union[GLBranchGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLBranchGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLBranchGetByCode', **kwargs)

    def GLBranchGetByCode(self, request: Optional[Union[GLBranchGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetByCode', **kwargs)

    def gl_branch_get_by_short_name(self, request: Optional[Union[GLBranchGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetByShortName', **kwargs)

    def gl_branch_get_by_short_name_json(self, request: Optional[Union[GLBranchGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLBranchGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLBranchGetByShortName', **kwargs)

    def GLBranchGetByShortName(self, request: Optional[Union[GLBranchGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetByShortName', **kwargs)

    def gl_branch_get_list_all(self, **kwargs: Any) -> Any:
        """GLBranchGetListAll"""
        return self.ams.call('GLBranchGetListAll', **kwargs)

    def gl_branch_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """GLBranchGetListAll (JSON)"""
        return self.ams.call_json('GLBranchGetListAll', **kwargs)

    def GLBranchGetListAll(self, **kwargs: Any) -> Any:
        """GLBranchGetListAll (original op name wrapper)"""
        return self.ams.call('GLBranchGetListAll', **kwargs)

    def gl_branch_get_list_by_gl_division_code(self, request: Optional[Union[GLBranchGetListByGLDivisionCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetListByGLDivisionCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetListByGLDivisionCode', **kwargs)

    def gl_branch_get_list_by_gl_division_code_json(self, request: Optional[Union[GLBranchGetListByGLDivisionCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLBranchGetListByGLDivisionCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLBranchGetListByGLDivisionCode', **kwargs)

    def GLBranchGetListByGLDivisionCode(self, request: Optional[Union[GLBranchGetListByGLDivisionCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetListByGLDivisionCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetListByGLDivisionCode', **kwargs)

    def gl_branch_get_list_by_name_prefix(self, request: Optional[Union[GLBranchGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetListByNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetListByNamePrefix', **kwargs)

    def gl_branch_get_list_by_name_prefix_json(self, request: Optional[Union[GLBranchGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLBranchGetListByNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLBranchGetListByNamePrefix', **kwargs)

    def GLBranchGetListByNamePrefix(self, request: Optional[Union[GLBranchGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLBranchGetListByNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLBranchGetListByNamePrefix', **kwargs)

    def gl_department_get_by_code(self, request: Optional[Union[GLDepartmentGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetByCode', **kwargs)

    def gl_department_get_by_code_json(self, request: Optional[Union[GLDepartmentGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDepartmentGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDepartmentGetByCode', **kwargs)

    def GLDepartmentGetByCode(self, request: Optional[Union[GLDepartmentGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetByCode', **kwargs)

    def gl_department_get_by_short_name(self, request: Optional[Union[GLDepartmentGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetByShortName', **kwargs)

    def gl_department_get_by_short_name_json(self, request: Optional[Union[GLDepartmentGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDepartmentGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDepartmentGetByShortName', **kwargs)

    def GLDepartmentGetByShortName(self, request: Optional[Union[GLDepartmentGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetByShortName', **kwargs)

    def gl_department_get_list_all(self, **kwargs: Any) -> Any:
        """GLDepartmentGetListAll"""
        return self.ams.call('GLDepartmentGetListAll', **kwargs)

    def gl_department_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """GLDepartmentGetListAll (JSON)"""
        return self.ams.call_json('GLDepartmentGetListAll', **kwargs)

    def GLDepartmentGetListAll(self, **kwargs: Any) -> Any:
        """GLDepartmentGetListAll (original op name wrapper)"""
        return self.ams.call('GLDepartmentGetListAll', **kwargs)

    def gl_department_get_list_by_gl_branch_code(self, request: Optional[Union[GLDepartmentGetListByGLBranchCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetListByGLBranchCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetListByGLBranchCode', **kwargs)

    def gl_department_get_list_by_gl_branch_code_json(self, request: Optional[Union[GLDepartmentGetListByGLBranchCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDepartmentGetListByGLBranchCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDepartmentGetListByGLBranchCode', **kwargs)

    def GLDepartmentGetListByGLBranchCode(self, request: Optional[Union[GLDepartmentGetListByGLBranchCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetListByGLBranchCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetListByGLBranchCode', **kwargs)

    def gl_department_get_list_by_name_prefix(self, request: Optional[Union[GLDepartmentGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetListByNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetListByNamePrefix', **kwargs)

    def gl_department_get_list_by_name_prefix_json(self, request: Optional[Union[GLDepartmentGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDepartmentGetListByNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDepartmentGetListByNamePrefix', **kwargs)

    def GLDepartmentGetListByNamePrefix(self, request: Optional[Union[GLDepartmentGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDepartmentGetListByNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDepartmentGetListByNamePrefix', **kwargs)

    def gl_division_get_by_code(self, request: Optional[Union[GLDivisionGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDivisionGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDivisionGetByCode', **kwargs)

    def gl_division_get_by_code_json(self, request: Optional[Union[GLDivisionGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDivisionGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDivisionGetByCode', **kwargs)

    def GLDivisionGetByCode(self, request: Optional[Union[GLDivisionGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDivisionGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDivisionGetByCode', **kwargs)

    def gl_division_get_by_short_name(self, request: Optional[Union[GLDivisionGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDivisionGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDivisionGetByShortName', **kwargs)

    def gl_division_get_by_short_name_json(self, request: Optional[Union[GLDivisionGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDivisionGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDivisionGetByShortName', **kwargs)

    def GLDivisionGetByShortName(self, request: Optional[Union[GLDivisionGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDivisionGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDivisionGetByShortName', **kwargs)

    def gl_division_get_list_all(self, **kwargs: Any) -> Any:
        """GLDivisionGetListAll"""
        return self.ams.call('GLDivisionGetListAll', **kwargs)

    def gl_division_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """GLDivisionGetListAll (JSON)"""
        return self.ams.call_json('GLDivisionGetListAll', **kwargs)

    def GLDivisionGetListAll(self, **kwargs: Any) -> Any:
        """GLDivisionGetListAll (original op name wrapper)"""
        return self.ams.call('GLDivisionGetListAll', **kwargs)

    def gl_division_get_list_by_name_prefix(self, request: Optional[Union[GLDivisionGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDivisionGetListByNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDivisionGetListByNamePrefix', **kwargs)

    def gl_division_get_list_by_name_prefix_json(self, request: Optional[Union[GLDivisionGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLDivisionGetListByNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLDivisionGetListByNamePrefix', **kwargs)

    def GLDivisionGetListByNamePrefix(self, request: Optional[Union[GLDivisionGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLDivisionGetListByNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLDivisionGetListByNamePrefix', **kwargs)

    def gl_group_get_by_code(self, request: Optional[Union[GLGroupGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetByCode', **kwargs)

    def gl_group_get_by_code_json(self, request: Optional[Union[GLGroupGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLGroupGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLGroupGetByCode', **kwargs)

    def GLGroupGetByCode(self, request: Optional[Union[GLGroupGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetByCode', **kwargs)

    def gl_group_get_by_short_name(self, request: Optional[Union[GLGroupGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetByShortName"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetByShortName', **kwargs)

    def gl_group_get_by_short_name_json(self, request: Optional[Union[GLGroupGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLGroupGetByShortName (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLGroupGetByShortName', **kwargs)

    def GLGroupGetByShortName(self, request: Optional[Union[GLGroupGetByShortNameRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetByShortName (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetByShortName', **kwargs)

    def gl_group_get_list_all(self, **kwargs: Any) -> Any:
        """GLGroupGetListAll"""
        return self.ams.call('GLGroupGetListAll', **kwargs)

    def gl_group_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """GLGroupGetListAll (JSON)"""
        return self.ams.call_json('GLGroupGetListAll', **kwargs)

    def GLGroupGetListAll(self, **kwargs: Any) -> Any:
        """GLGroupGetListAll (original op name wrapper)"""
        return self.ams.call('GLGroupGetListAll', **kwargs)

    def gl_group_get_list_by_gl_department_code(self, request: Optional[Union[GLGroupGetListByGLDepartmentCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetListByGLDepartmentCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetListByGLDepartmentCode', **kwargs)

    def gl_group_get_list_by_gl_department_code_json(self, request: Optional[Union[GLGroupGetListByGLDepartmentCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLGroupGetListByGLDepartmentCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLGroupGetListByGLDepartmentCode', **kwargs)

    def GLGroupGetListByGLDepartmentCode(self, request: Optional[Union[GLGroupGetListByGLDepartmentCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetListByGLDepartmentCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetListByGLDepartmentCode', **kwargs)

    def gl_group_get_list_by_name_prefix(self, request: Optional[Union[GLGroupGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetListByNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetListByNamePrefix', **kwargs)

    def gl_group_get_list_by_name_prefix_json(self, request: Optional[Union[GLGroupGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """GLGroupGetListByNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('GLGroupGetListByNamePrefix', **kwargs)

    def GLGroupGetListByNamePrefix(self, request: Optional[Union[GLGroupGetListByNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """GLGroupGetListByNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('GLGroupGetListByNamePrefix', **kwargs)

    def line_of_business_get_all_list(self, **kwargs: Any) -> Any:
        """LineOfBusinessGetAllList"""
        return self.ams.call('LineOfBusinessGetAllList', **kwargs)

    def line_of_business_get_all_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """LineOfBusinessGetAllList (JSON)"""
        return self.ams.call_json('LineOfBusinessGetAllList', **kwargs)

    def LineOfBusinessGetAllList(self, **kwargs: Any) -> Any:
        """LineOfBusinessGetAllList (original op name wrapper)"""
        return self.ams.call('LineOfBusinessGetAllList', **kwargs)

    def line_of_business_get_by_code(self, request: Optional[Union[LineOfBusinessGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """LineOfBusinessGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('LineOfBusinessGetByCode', **kwargs)

    def line_of_business_get_by_code_json(self, request: Optional[Union[LineOfBusinessGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """LineOfBusinessGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('LineOfBusinessGetByCode', **kwargs)

    def LineOfBusinessGetByCode(self, request: Optional[Union[LineOfBusinessGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """LineOfBusinessGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('LineOfBusinessGetByCode', **kwargs)

    def line_of_business_get_list(self, request: Optional[Union[LineOfBusinessGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """LineOfBusinessGetList"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('LineOfBusinessGetList', **kwargs)

    def line_of_business_get_list_json(self, request: Optional[Union[LineOfBusinessGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """LineOfBusinessGetList (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('LineOfBusinessGetList', **kwargs)

    def LineOfBusinessGetList(self, request: Optional[Union[LineOfBusinessGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """LineOfBusinessGetList (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('LineOfBusinessGetList', **kwargs)

    def login(self, request: Optional[Union[LoginRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """Login"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('Login', **kwargs)

    def login_json(self, request: Optional[Union[LoginRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Login (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('Login', **kwargs)

    def Login(self, request: Optional[Union[LoginRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """Login (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('Login', **kwargs)

    def logout(self, **kwargs: Any) -> Any:
        """Logout"""
        return self.ams.call('Logout', **kwargs)

    def logout_json(self, **kwargs: Any) -> Dict[str, Any]:
        """Logout (JSON)"""
        return self.ams.call_json('Logout', **kwargs)

    def Logout(self, **kwargs: Any) -> Any:
        """Logout (original op name wrapper)"""
        return self.ams.call('Logout', **kwargs)

    def personal_note_get_list(self, request: Optional[Union[PersonalNoteGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PersonalNoteGetList"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PersonalNoteGetList', **kwargs)

    def personal_note_get_list_json(self, request: Optional[Union[PersonalNoteGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PersonalNoteGetList (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PersonalNoteGetList', **kwargs)

    def PersonalNoteGetList(self, request: Optional[Union[PersonalNoteGetListRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PersonalNoteGetList (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PersonalNoteGetList', **kwargs)

    def personal_note_get_list_all(self, **kwargs: Any) -> Any:
        """PersonalNoteGetListAll"""
        return self.ams.call('PersonalNoteGetListAll', **kwargs)

    def personal_note_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PersonalNoteGetListAll (JSON)"""
        return self.ams.call_json('PersonalNoteGetListAll', **kwargs)

    def PersonalNoteGetListAll(self, **kwargs: Any) -> Any:
        """PersonalNoteGetListAll (original op name wrapper)"""
        return self.ams.call('PersonalNoteGetListAll', **kwargs)

    def personal_note_get_note_text_by_id(self, **kwargs: Any) -> Any:
        """PersonalNoteGetNoteTextById"""
        return self.ams.call('PersonalNoteGetNoteTextById', **kwargs)

    def personal_note_get_note_text_by_id_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PersonalNoteGetNoteTextById (JSON)"""
        return self.ams.call_json('PersonalNoteGetNoteTextById', **kwargs)

    def PersonalNoteGetNoteTextById(self, **kwargs: Any) -> Any:
        """PersonalNoteGetNoteTextById (original op name wrapper)"""
        return self.ams.call('PersonalNoteGetNoteTextById', **kwargs)

    def personal_note_insert(self, request: Optional[Union[PersonalNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PersonalNoteInsert"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PersonalNoteInsert', **kwargs)

    def personal_note_insert_json(self, request: Optional[Union[PersonalNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PersonalNoteInsert (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PersonalNoteInsert', **kwargs)

    def PersonalNoteInsert(self, request: Optional[Union[PersonalNoteInsertRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PersonalNoteInsert (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PersonalNoteInsert', **kwargs)

    def personal_note_update_note_text(self, **kwargs: Any) -> Any:
        """PersonalNoteUpdateNoteText"""
        return self.ams.call('PersonalNoteUpdateNoteText', **kwargs)

    def personal_note_update_note_text_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PersonalNoteUpdateNoteText (JSON)"""
        return self.ams.call_json('PersonalNoteUpdateNoteText', **kwargs)

    def PersonalNoteUpdateNoteText(self, **kwargs: Any) -> Any:
        """PersonalNoteUpdateNoteText (original op name wrapper)"""
        return self.ams.call('PersonalNoteUpdateNoteText', **kwargs)

    def plan_type_get_by_code(self, request: Optional[Union[PlanTypeGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PlanTypeGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PlanTypeGetByCode', **kwargs)

    def plan_type_get_by_code_json(self, request: Optional[Union[PlanTypeGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PlanTypeGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PlanTypeGetByCode', **kwargs)

    def PlanTypeGetByCode(self, request: Optional[Union[PlanTypeGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PlanTypeGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PlanTypeGetByCode', **kwargs)

    def plan_type_get_list_all(self, **kwargs: Any) -> Any:
        """PlanTypeGetListAll"""
        return self.ams.call('PlanTypeGetListAll', **kwargs)

    def plan_type_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PlanTypeGetListAll (JSON)"""
        return self.ams.call_json('PlanTypeGetListAll', **kwargs)

    def PlanTypeGetListAll(self, **kwargs: Any) -> Any:
        """PlanTypeGetListAll (original op name wrapper)"""
        return self.ams.call('PlanTypeGetListAll', **kwargs)

    def plan_type_get_list_by_company_code(self, request: Optional[Union[PlanTypeGetListByCompanyCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PlanTypeGetListByCompanyCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PlanTypeGetListByCompanyCode', **kwargs)

    def plan_type_get_list_by_company_code_json(self, request: Optional[Union[PlanTypeGetListByCompanyCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PlanTypeGetListByCompanyCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PlanTypeGetListByCompanyCode', **kwargs)

    def PlanTypeGetListByCompanyCode(self, request: Optional[Union[PlanTypeGetListByCompanyCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PlanTypeGetListByCompanyCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PlanTypeGetListByCompanyCode', **kwargs)

    def policy_contact_delete(self, **kwargs: Any) -> Any:
        """PolicyContactDelete"""
        return self.ams.call('PolicyContactDelete', **kwargs)

    def policy_contact_delete_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyContactDelete (JSON)"""
        return self.ams.call_json('PolicyContactDelete', **kwargs)

    def PolicyContactDelete(self, **kwargs: Any) -> Any:
        """PolicyContactDelete (original op name wrapper)"""
        return self.ams.call('PolicyContactDelete', **kwargs)

    def policy_contact_get(self, **kwargs: Any) -> Any:
        """PolicyContactGet"""
        return self.ams.call('PolicyContactGet', **kwargs)

    def policy_contact_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyContactGet (JSON)"""
        return self.ams.call_json('PolicyContactGet', **kwargs)

    def PolicyContactGet(self, **kwargs: Any) -> Any:
        """PolicyContactGet (original op name wrapper)"""
        return self.ams.call('PolicyContactGet', **kwargs)

    def policy_contact_get_list(self, **kwargs: Any) -> Any:
        """PolicyContactGetList"""
        return self.ams.call('PolicyContactGetList', **kwargs)

    def policy_contact_get_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyContactGetList (JSON)"""
        return self.ams.call_json('PolicyContactGetList', **kwargs)

    def PolicyContactGetList(self, **kwargs: Any) -> Any:
        """PolicyContactGetList (original op name wrapper)"""
        return self.ams.call('PolicyContactGetList', **kwargs)

    def policy_contact_insert(self, **kwargs: Any) -> Any:
        """PolicyContactInsert"""
        return self.ams.call('PolicyContactInsert', **kwargs)

    def policy_contact_insert_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyContactInsert (JSON)"""
        return self.ams.call_json('PolicyContactInsert', **kwargs)

    def PolicyContactInsert(self, **kwargs: Any) -> Any:
        """PolicyContactInsert (original op name wrapper)"""
        return self.ams.call('PolicyContactInsert', **kwargs)

    def policy_contact_update(self, **kwargs: Any) -> Any:
        """PolicyContactUpdate"""
        return self.ams.call('PolicyContactUpdate', **kwargs)

    def policy_contact_update_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyContactUpdate (JSON)"""
        return self.ams.call_json('PolicyContactUpdate', **kwargs)

    def PolicyContactUpdate(self, **kwargs: Any) -> Any:
        """PolicyContactUpdate (original op name wrapper)"""
        return self.ams.call('PolicyContactUpdate', **kwargs)

    def policy_correct(self, request: Optional[Union[PolicyCorrectRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyCorrect"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyCorrect', **kwargs)

    def policy_correct_json(self, request: Optional[Union[PolicyCorrectRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyCorrect (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyCorrect', **kwargs)

    def PolicyCorrect(self, request: Optional[Union[PolicyCorrectRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyCorrect (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyCorrect', **kwargs)

    def policy_delete(self, **kwargs: Any) -> Any:
        """PolicyDelete"""
        return self.ams.call('PolicyDelete', **kwargs)

    def policy_delete_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyDelete (JSON)"""
        return self.ams.call_json('PolicyDelete', **kwargs)

    def PolicyDelete(self, **kwargs: Any) -> Any:
        """PolicyDelete (original op name wrapper)"""
        return self.ams.call('PolicyDelete', **kwargs)

    def policy_delete_remark(self, **kwargs: Any) -> Any:
        """PolicyDeleteRemark"""
        return self.ams.call('PolicyDeleteRemark', **kwargs)

    def policy_delete_remark_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyDeleteRemark (JSON)"""
        return self.ams.call_json('PolicyDeleteRemark', **kwargs)

    def PolicyDeleteRemark(self, **kwargs: Any) -> Any:
        """PolicyDeleteRemark (original op name wrapper)"""
        return self.ams.call('PolicyDeleteRemark', **kwargs)

    def policy_endorse(self, request: Optional[Union[PolicyEndorseRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyEndorse"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyEndorse', **kwargs)

    def policy_endorse_json(self, request: Optional[Union[PolicyEndorseRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyEndorse (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyEndorse', **kwargs)

    def PolicyEndorse(self, request: Optional[Union[PolicyEndorseRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyEndorse (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyEndorse', **kwargs)

    def policy_get(self, request: Optional[Union[PolicyGetRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGet"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGet', **kwargs)

    def policy_get_json(self, request: Optional[Union[PolicyGetRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyGet (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyGet', **kwargs)

    def PolicyGet(self, request: Optional[Union[PolicyGetRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGet (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGet', **kwargs)

    def policy_get_list_by_customer_id(self, request: Optional[Union[PolicyGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByCustomerId"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByCustomerId', **kwargs)

    def policy_get_list_by_customer_id_json(self, request: Optional[Union[PolicyGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyGetListByCustomerId (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyGetListByCustomerId', **kwargs)

    def PolicyGetListByCustomerId(self, request: Optional[Union[PolicyGetListByCustomerIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByCustomerId (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByCustomerId', **kwargs)

    def policy_get_list_by_customer_number(self, request: Optional[Union[PolicyGetListByCustomerNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByCustomerNumber"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByCustomerNumber', **kwargs)

    def policy_get_list_by_customer_number_json(self, request: Optional[Union[PolicyGetListByCustomerNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyGetListByCustomerNumber (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyGetListByCustomerNumber', **kwargs)

    def PolicyGetListByCustomerNumber(self, request: Optional[Union[PolicyGetListByCustomerNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByCustomerNumber (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByCustomerNumber', **kwargs)

    def policy_get_list_by_policy_number(self, request: Optional[Union[PolicyGetListByPolicyNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByPolicyNumber"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByPolicyNumber', **kwargs)

    def policy_get_list_by_policy_number_json(self, request: Optional[Union[PolicyGetListByPolicyNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyGetListByPolicyNumber (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyGetListByPolicyNumber', **kwargs)

    def PolicyGetListByPolicyNumber(self, request: Optional[Union[PolicyGetListByPolicyNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByPolicyNumber (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByPolicyNumber', **kwargs)

    def policy_get_list_by_policy_number_and_date(self, request: Optional[Union[PolicyGetListByPolicyNumberAndDateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByPolicyNumberAndDate"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByPolicyNumberAndDate', **kwargs)

    def policy_get_list_by_policy_number_and_date_json(self, request: Optional[Union[PolicyGetListByPolicyNumberAndDateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """PolicyGetListByPolicyNumberAndDate (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('PolicyGetListByPolicyNumberAndDate', **kwargs)

    def PolicyGetListByPolicyNumberAndDate(self, request: Optional[Union[PolicyGetListByPolicyNumberAndDateRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """PolicyGetListByPolicyNumberAndDate (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('PolicyGetListByPolicyNumberAndDate', **kwargs)

    def policy_get_remark(self, **kwargs: Any) -> Any:
        """PolicyGetRemark"""
        return self.ams.call('PolicyGetRemark', **kwargs)

    def policy_get_remark_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyGetRemark (JSON)"""
        return self.ams.call_json('PolicyGetRemark', **kwargs)

    def PolicyGetRemark(self, **kwargs: Any) -> Any:
        """PolicyGetRemark (original op name wrapper)"""
        return self.ams.call('PolicyGetRemark', **kwargs)

    def policy_insert(self, **kwargs: Any) -> Any:
        """PolicyInsert"""
        return self.ams.call('PolicyInsert', **kwargs)

    def policy_insert_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyInsert (JSON)"""
        return self.ams.call_json('PolicyInsert', **kwargs)

    def PolicyInsert(self, **kwargs: Any) -> Any:
        """PolicyInsert (original op name wrapper)"""
        return self.ams.call('PolicyInsert', **kwargs)

    def policy_insert_remark(self, **kwargs: Any) -> Any:
        """PolicyInsertRemark"""
        return self.ams.call('PolicyInsertRemark', **kwargs)

    def policy_insert_remark_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyInsertRemark (JSON)"""
        return self.ams.call_json('PolicyInsertRemark', **kwargs)

    def PolicyInsertRemark(self, **kwargs: Any) -> Any:
        """PolicyInsertRemark (original op name wrapper)"""
        return self.ams.call('PolicyInsertRemark', **kwargs)

    def policy_renew(self, **kwargs: Any) -> Any:
        """PolicyRenew"""
        return self.ams.call('PolicyRenew', **kwargs)

    def policy_renew_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyRenew (JSON)"""
        return self.ams.call_json('PolicyRenew', **kwargs)

    def PolicyRenew(self, **kwargs: Any) -> Any:
        """PolicyRenew (original op name wrapper)"""
        return self.ams.call('PolicyRenew', **kwargs)

    def policy_service_personnel_get_list(self, **kwargs: Any) -> Any:
        """PolicyServicePersonnelGetList"""
        return self.ams.call('PolicyServicePersonnelGetList', **kwargs)

    def policy_service_personnel_get_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyServicePersonnelGetList (JSON)"""
        return self.ams.call_json('PolicyServicePersonnelGetList', **kwargs)

    def PolicyServicePersonnelGetList(self, **kwargs: Any) -> Any:
        """PolicyServicePersonnelGetList (original op name wrapper)"""
        return self.ams.call('PolicyServicePersonnelGetList', **kwargs)

    def policy_service_personnel_modify_list(self, **kwargs: Any) -> Any:
        """PolicyServicePersonnelModifyList"""
        return self.ams.call('PolicyServicePersonnelModifyList', **kwargs)

    def policy_service_personnel_modify_list_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyServicePersonnelModifyList (JSON)"""
        return self.ams.call_json('PolicyServicePersonnelModifyList', **kwargs)

    def PolicyServicePersonnelModifyList(self, **kwargs: Any) -> Any:
        """PolicyServicePersonnelModifyList (original op name wrapper)"""
        return self.ams.call('PolicyServicePersonnelModifyList', **kwargs)

    def policy_transaction_premium_delete(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumDelete"""
        return self.ams.call('PolicyTransactionPremiumDelete', **kwargs)

    def policy_transaction_premium_delete_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyTransactionPremiumDelete (JSON)"""
        return self.ams.call_json('PolicyTransactionPremiumDelete', **kwargs)

    def PolicyTransactionPremiumDelete(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumDelete (original op name wrapper)"""
        return self.ams.call('PolicyTransactionPremiumDelete', **kwargs)

    def policy_transaction_premium_get(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumGet"""
        return self.ams.call('PolicyTransactionPremiumGet', **kwargs)

    def policy_transaction_premium_get_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyTransactionPremiumGet (JSON)"""
        return self.ams.call_json('PolicyTransactionPremiumGet', **kwargs)

    def PolicyTransactionPremiumGet(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumGet (original op name wrapper)"""
        return self.ams.call('PolicyTransactionPremiumGet', **kwargs)

    def policy_transaction_premium_get_list_for_policy(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumGetListForPolicy"""
        return self.ams.call('PolicyTransactionPremiumGetListForPolicy', **kwargs)

    def policy_transaction_premium_get_list_for_policy_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyTransactionPremiumGetListForPolicy (JSON)"""
        return self.ams.call_json('PolicyTransactionPremiumGetListForPolicy', **kwargs)

    def PolicyTransactionPremiumGetListForPolicy(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumGetListForPolicy (original op name wrapper)"""
        return self.ams.call('PolicyTransactionPremiumGetListForPolicy', **kwargs)

    def policy_transaction_premium_insert(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumInsert"""
        return self.ams.call('PolicyTransactionPremiumInsert', **kwargs)

    def policy_transaction_premium_insert_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyTransactionPremiumInsert (JSON)"""
        return self.ams.call_json('PolicyTransactionPremiumInsert', **kwargs)

    def PolicyTransactionPremiumInsert(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumInsert (original op name wrapper)"""
        return self.ams.call('PolicyTransactionPremiumInsert', **kwargs)

    def policy_transaction_premium_update(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumUpdate"""
        return self.ams.call('PolicyTransactionPremiumUpdate', **kwargs)

    def policy_transaction_premium_update_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyTransactionPremiumUpdate (JSON)"""
        return self.ams.call_json('PolicyTransactionPremiumUpdate', **kwargs)

    def PolicyTransactionPremiumUpdate(self, **kwargs: Any) -> Any:
        """PolicyTransactionPremiumUpdate (original op name wrapper)"""
        return self.ams.call('PolicyTransactionPremiumUpdate', **kwargs)

    def policy_update_remark(self, **kwargs: Any) -> Any:
        """PolicyUpdateRemark"""
        return self.ams.call('PolicyUpdateRemark', **kwargs)

    def policy_update_remark_json(self, **kwargs: Any) -> Dict[str, Any]:
        """PolicyUpdateRemark (JSON)"""
        return self.ams.call_json('PolicyUpdateRemark', **kwargs)

    def PolicyUpdateRemark(self, **kwargs: Any) -> Any:
        """PolicyUpdateRemark (original op name wrapper)"""
        return self.ams.call('PolicyUpdateRemark', **kwargs)

    def s1099_get_list_all(self, **kwargs: Any) -> Any:
        """S1099GetListAll"""
        return self.ams.call('S1099GetListAll', **kwargs)

    def s1099_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """S1099GetListAll (JSON)"""
        return self.ams.call_json('S1099GetListAll', **kwargs)

    def S1099GetListAll(self, **kwargs: Any) -> Any:
        """S1099GetListAll (original op name wrapper)"""
        return self.ams.call('S1099GetListAll', **kwargs)

    def search_by_phone_number(self, request: Optional[Union[SearchByPhoneNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """SearchByPhoneNumber"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('SearchByPhoneNumber', **kwargs)

    def search_by_phone_number_json(self, request: Optional[Union[SearchByPhoneNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """SearchByPhoneNumber (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('SearchByPhoneNumber', **kwargs)

    def SearchByPhoneNumber(self, request: Optional[Union[SearchByPhoneNumberRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """SearchByPhoneNumber (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('SearchByPhoneNumber', **kwargs)

    def value_list_get(self, request: Optional[Union[ValueListGetRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ValueListGet"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ValueListGet', **kwargs)

    def value_list_get_json(self, request: Optional[Union[ValueListGetRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """ValueListGet (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('ValueListGet', **kwargs)

    def ValueListGet(self, request: Optional[Union[ValueListGetRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """ValueListGet (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('ValueListGet', **kwargs)

    def vendor_get_by_code(self, request: Optional[Union[VendorGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorGetByCode"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorGetByCode', **kwargs)

    def vendor_get_by_code_json(self, request: Optional[Union[VendorGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """VendorGetByCode (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('VendorGetByCode', **kwargs)

    def VendorGetByCode(self, request: Optional[Union[VendorGetByCodeRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorGetByCode (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorGetByCode', **kwargs)

    def vendor_get_list_all(self, **kwargs: Any) -> Any:
        """VendorGetListAll"""
        return self.ams.call('VendorGetListAll', **kwargs)

    def vendor_get_list_all_json(self, **kwargs: Any) -> Dict[str, Any]:
        """VendorGetListAll (JSON)"""
        return self.ams.call_json('VendorGetListAll', **kwargs)

    def VendorGetListAll(self, **kwargs: Any) -> Any:
        """VendorGetListAll (original op name wrapper)"""
        return self.ams.call('VendorGetListAll', **kwargs)

    def vendor_get_list_by_is_company(self, request: Optional[Union[VendorGetListByIsCompanyRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorGetListByIsCompany"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorGetListByIsCompany', **kwargs)

    def vendor_get_list_by_is_company_json(self, request: Optional[Union[VendorGetListByIsCompanyRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """VendorGetListByIsCompany (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('VendorGetListByIsCompany', **kwargs)

    def VendorGetListByIsCompany(self, request: Optional[Union[VendorGetListByIsCompanyRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorGetListByIsCompany (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorGetListByIsCompany', **kwargs)

    def vendor_get_list_by_last_name_prefix(self, request: Optional[Union[VendorGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorGetListByLastNamePrefix"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorGetListByLastNamePrefix', **kwargs)

    def vendor_get_list_by_last_name_prefix_json(self, request: Optional[Union[VendorGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """VendorGetListByLastNamePrefix (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('VendorGetListByLastNamePrefix', **kwargs)

    def VendorGetListByLastNamePrefix(self, request: Optional[Union[VendorGetListByLastNamePrefixRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorGetListByLastNamePrefix (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorGetListByLastNamePrefix', **kwargs)

    def vendor_invoice_get_by_id(self, request: Optional[Union[VendorInvoiceGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorInvoiceGetById"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorInvoiceGetById', **kwargs)

    def vendor_invoice_get_by_id_json(self, request: Optional[Union[VendorInvoiceGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """VendorInvoiceGetById (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('VendorInvoiceGetById', **kwargs)

    def VendorInvoiceGetById(self, request: Optional[Union[VendorInvoiceGetByIdRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorInvoiceGetById (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorInvoiceGetById', **kwargs)

    def vendor_invoice_get_list_by_vendor(self, request: Optional[Union[VendorInvoiceGetListByVendorRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorInvoiceGetListByVendor"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorInvoiceGetListByVendor', **kwargs)

    def vendor_invoice_get_list_by_vendor_json(self, request: Optional[Union[VendorInvoiceGetListByVendorRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Dict[str, Any]:
        """VendorInvoiceGetListByVendor (JSON)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call_json('VendorInvoiceGetListByVendor', **kwargs)

    def VendorInvoiceGetListByVendor(self, request: Optional[Union[VendorInvoiceGetListByVendorRequest, Dict[str, Any]]] = None, **kwargs: Any) -> Any:
        """VendorInvoiceGetListByVendor (original op name wrapper)"""
        if request is not None:
            kwargs["Request"] = self._normalize_request(request)
        return self.ams.call('VendorInvoiceGetListByVendor', **kwargs)

