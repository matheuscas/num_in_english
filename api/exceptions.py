from http import HTTPStatus

from django.http import Http404
from ninja import NinjaAPI
from ninja.errors import ValidationError


class WrongNumberTypeException(Exception):
    pass


class ExistingNumberException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


def register_handlers(api: NinjaAPI):
    @api.exception_handler(Http404)
    def not_found(request, exc):
        return api.create_response(
            request,
            {
                "status": f"{request.GET['number']} not found",
                "num_to_english": ""
            },
            status=HTTPStatus.NOT_FOUND
        )

    @api.exception_handler(ValidationError)
    def validation_errors(request, _):
        if request.method == 'GET':
            if 'number' not in request.GET:
                return api.create_response(
                    request,
                    {
                        "status": "Missing query param 'number'",
                        "num_to_english": ""
                    },
                    status=HTTPStatus.UNPROCESSABLE_ENTITY
                )

            if type(request.GET["number"]) != int:
                return api.create_response(
                    request,
                    {
                        "status": "Wrong query param 'number' type. It must be an integer",
                        "num_to_english": ""
                    },
                    status=HTTPStatus.UNPROCESSABLE_ENTITY
                )
        else:
            return api.create_response(
                request,
                {
                    "status": "Wrong payload structure",
                    "num_to_english": ""
                },
                status=HTTPStatus.UNPROCESSABLE_ENTITY
            )

    @api.exception_handler(WrongNumberTypeException)
    def type_number_error(request, _):
        return api.create_response(
            request,
            {"status": "'number' must be a valid integer", "num_to_english": ""},
            status=HTTPStatus.UNPROCESSABLE_ENTITY
        )

    @api.exception_handler(ExistingNumberException)
    def type_number_error(request, _):
        return api.create_response(
            request,
            {"status": "Number already exists", "num_to_english": ""},
            status=HTTPStatus.BAD_REQUEST
        )

    @api.exception_handler(UnauthorizedException)
    def unauthorized(request, _):
        return api.create_response(
            request,
            {"status": "Unauthorized. Missing Bearer token", "num_to_english": ""},
            status=HTTPStatus.UNAUTHORIZED
        )
