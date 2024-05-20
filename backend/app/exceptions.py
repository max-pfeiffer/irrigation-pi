"""Application Exceptions."""

from typing import Any, Dict, Optional

from fastapi import HTTPException
from typing_extensions import Annotated, Doc


class ActiveScheduleExistsError(HTTPException):
    """Raised when an active schedule already exists."""

    def __init__(
        self,
        detail: Annotated[
            Any,
            Doc(
                """
                Any data to be sent to the client in the `detail` key of the JSON
                response.
                """
            ),
        ] = None,
        headers: Annotated[
            Optional[Dict[str, str]],
            Doc(
                """
                Any headers to send to the client in the response.
                """
            ),
        ] = None,
    ) -> None:
        """Class initializer.

        :param detail:
        :param headers:
        """
        if detail is None:
            detail = "An active schedule already exists"
        super().__init__(status_code=409, detail=detail, headers=headers)
