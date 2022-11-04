from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from api.auth import GlobalAuth
from api.exceptions import register_handlers, WrongNumberTypeException, ExistingNumberException
from api.schemas import EnglishNumberOut, Error, EnglishNumberIn
from full_written_numbers.models import EnglishNumbers
from full_written_numbers.services.full_written_numbers import get_full_written_number

api = NinjaAPI(auth=GlobalAuth())
register_handlers(api)

ENDPOINT = "/num_to_english"


@api.get(ENDPOINT, response=({422: Error, 404: Error, 200: EnglishNumberOut}))
def num_to_english(request, number: int):
    english_number = get_object_or_404(EnglishNumbers, number=number)
    return EnglishNumberOut(status="ok", num_to_english=english_number.written_number)


@api.post(ENDPOINT, response=({422: Error, 404: Error, 200: EnglishNumberOut}))
def create_written_number(request, english_number: EnglishNumberIn):
    try:
        number = int(english_number.number)
        written_number = get_full_written_number(number)
        result = EnglishNumbers.objects.create(number=number, written_number=written_number)
        return EnglishNumberOut(status="ok", num_to_english=result.written_number)
    except ValueError as ve:
        raise WrongNumberTypeException() from ve
    except IntegrityError as ie:
        raise ExistingNumberException() from ie

