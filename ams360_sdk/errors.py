class AMS360Error(Exception):
    pass

class AMS360AuthError(AMS360Error):
    pass

class AMS360SoapFault(AMS360Error):
    pass

class AMS360OperationNotFound(AMS360Error):
    pass
