from json import dumps
from typing import Any, Dict, List, Union

from error_message import T_ErrorMessage
from json_encoder import JsonEncoder


class ResponseBody:
    json_encoder = JsonEncoder()

    def response_ok(self, payload: Union[List[Any], Dict[str, Any], None]) -> str:
        return dumps(
            obj={
                'error': False,
                'payload': payload,
                'error_log': list()
            },
            default=self.json_encoder.default,
        )

    def response_error(self, error_log: List[T_ErrorMessage]) -> str:
        assert bool(error_log), "error list cannot be empty"
        assert isinstance(error_log, list), "error list cannot be empty"
        return dumps(
            obj={
                'error': True,
                'payload': list(),
                'error_log': error_log
            },
            default=self.json_encoder.default,
        )

