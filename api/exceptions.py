from http import HTTPStatus

from django.http import Http404
from ninja.errors import ValidationError

from api.views import api


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
