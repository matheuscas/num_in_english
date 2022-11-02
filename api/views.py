from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

from api.exceptions import register_handlers
from api.schemas import EnglishNumberOut, Error
from full_written_numbers.models import EnglishNumbers

api = NinjaAPI()
register_handlers(api)

ENDPOINT = "/num_to_english"


@api.get(ENDPOINT, response=({422: Error, 404: Error, 200: EnglishNumberOut}))
def num_to_english(request, number: int):
    english_number = get_object_or_404(EnglishNumbers, number=number)
    return EnglishNumberOut(status="ok", num_to_english=english_number.written_number)
