class InvalidApiKeyError(Exception):
    def __init__(self, message):
        self.message = message

class UnauthorizedError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidParametersError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidEndpointError(Exception):
    def __init__(self, message):
        self.message = message

class InvalidVersionError(Exception):
    def __init__(self, message):
        self.message = message

class DepreciationError(Exception):
    def __init__(self, message):
        self.message = message
