from json import dumps
from typing import Any, Dict, List, Union

from error_message import T_ErrorMessage


class ResponseBody:
    @staticmethod
    def response_ok(payload: Union[List[Any], Dict[str, Any], None]) -> str:
        return dumps({
            'error': False,
            'payload': payload,
            'error_log': list()
        })

    @staticmethod
    def response_error(error_log: List[T_ErrorMessage]) -> str:
        assert bool(error_log), "error list cannot be empty"
        assert isinstance(error_log, list), "error list cannot be empty"
        return dumps({
            'error': True,
            'payload': list(),
            'error_log': error_log
        })

