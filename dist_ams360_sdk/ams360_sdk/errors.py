class AMS360Error(Exception):
    pass

class AMS360AuthError(AMS360Error):
    pass

class AMS360SoapError(AMS360Error):
    pass
