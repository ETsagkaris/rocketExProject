CONTACT_CREATION_FAILED = "contact_creation_failed"
CONTACT_UPDATE_FAILED = "contact_update_failed"
COMPANY_CREATION_FAILED = "company_creation_failed"
CONTACT_UPDATE_FAILED = "company_update_failed"


def camel_case(s):
    return s[0].lower() + s[1:]


class JsonException(Exception):
    def __init__(self, message='', data={}, details='', name='', code=500):
        self.message = message
        self.details = details
        self.data = data
        if not hasattr(self, 'code'):
            self.code = code
        self.name = name or camel_case(self.__class__.__name__)
        Exception.__init__(self, message, details, self.name, self.code)
