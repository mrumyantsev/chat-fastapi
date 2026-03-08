from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'title text too long "{self.text[:255]}..."'


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return 'text cannot be empty'
