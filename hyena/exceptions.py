class InvalidApiKeyError(Exception):
    """
    Raised when the API key given is invalid
    """
    def __init__(self, message):
        self.message = message

class UnauthorizedError(Exception):
    """
    Raised when the API key is not given
    """
    def __init__(self, message):
        self.message = message

class InvalidParametersError(Exception):
    """
    Raised when the Parameters given didn't 
    satify the requirements
    """
    def __init__(self, message):
        self.message = message

class InvalidEndpointError(Exception):
    """
    Raised when the status code is 404
    """
    def __init__(self, message):
        self.message = message

class InvalidVersionError(Exception):
    """
    Raised when the version provided is
    not valid
    """
    def __init__(self, message):
        self.message = message

class DepreciationError(Exception):
    """
    Raised when the version provided is
    Depreciated
    """
    def __init__(self, message):
        self.message = message
