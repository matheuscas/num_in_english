from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, Schema

from full_written_numbers.models import EnglishNumbers

api = NinjaAPI()


class EnglishNumberOut(Schema):
    status: str
    num_to_english: str


class Error(Schema):
    status: str
    num_to_english: str


ENDPOINT = "/num_to_english"


@api.get(ENDPOINT, response=({422: Error, 404: Error, 200: EnglishNumberOut}))
def num_to_english(request, number: int):
    english_number = get_object_or_404(EnglishNumbers, number=number)
    return EnglishNumberOut(status="ok", num_to_english=english_number.written_number)
