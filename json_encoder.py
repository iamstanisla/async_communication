from typing import Any, Dict, Union

from error_message import ErrorMessageBase


class JsonEncoder:

    @staticmethod
    def default(value) -> Union[str, Dict[str, Any]]:
        if isinstance(value, ErrorMessageBase):
            return value.get_message()
        return value
