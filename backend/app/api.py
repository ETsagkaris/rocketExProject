from fastapi.routing import APIRoute
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ValidationError
from typing import Callable

from app import errors


async def do_or_error(
    to_be_called, **kwargs
):
    try:
        return await to_be_called(**kwargs)
    except errors.JsonException as exc:
        status_code = exc.code
        content = {
            "message": exc.message,
            "detail": exc.details,
            "data": exc.data,
        }
    except (RequestValidationError, ValidationError) as exc:
        status_code = 422
        content = {
            "message": str(exc),
            "detail": "",
            "data": {},
        }

    return JSONResponse(status_code=status_code, content=content)


class Wrapper(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            return await do_or_error(
                to_be_called=original_route_handler,
                request=request,
            )
        return custom_route_handler
