from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict
from typing import TypeVar

connection_pool = list()

ok_status_got_count = 0


class ErrorMessageBase(metaclass=ABCMeta):

    @abstractmethod
    def get_message(self) -> Dict[str, Any]:
        pass


@dataclass
class ErrorMessage(ErrorMessageBase):
    message: str

    def get_message(self) -> Dict[str, Any]:
        return {
            'message': self.message
        }


T_ErrorMessage = TypeVar('T_ErrorMessage', bound='ErrorMessageBase')


