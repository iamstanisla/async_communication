from typing import List, Generic

from error_message import T_ErrorMessage, ErrorMessageBase


class ErrorPicker(Generic[T_ErrorMessage]):
    pool: List[T_ErrorMessage] = list()

    def add(self, error_template: T_ErrorMessage) -> None:
        assert isinstance(error_template, ErrorMessageBase)
        self.pool.append(error_template)

    def get_errors(self) -> List[T_ErrorMessage]:
        return self.pool
