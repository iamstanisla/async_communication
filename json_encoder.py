from error_message import ErrorMessageBase


class JsonEncoder:

    @staticmethod
    def default(value):
        if isinstance(value, ErrorMessageBase):
            return value.get_message()
