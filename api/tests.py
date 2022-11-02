import pytest

from api.views import ENDPOINT
from http import HTTPStatus
from api.views import api

from ninja.testing import TestClient as NinjaTestClient

from full_written_numbers.models import EnglishNumbers

client = NinjaTestClient(api)


def test_missing_number_query_param():
    response = client.get(ENDPOINT)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == {
        "status": "Missing query param 'number'",
        "num_to_english": ""
    }


def test_wrong_type_query_param():
    response = client.get(f"{ENDPOINT}?number='123'")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == {
        "status": "Wrong query param 'number' type. It must be an integer",
        "num_to_english": ""
    }


@pytest.mark.django_db
def test_no_number_found():
    number = 123
    EnglishNumbers(number=37, written_number="thirty seven").save()
    EnglishNumbers(number=99, written_number="ninety nine").save()
    response = client.get(f"{ENDPOINT}?number={number}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        "status": f"{number} not found",
        "num_to_english": ""
    }


@pytest.mark.django_db
def test_number_found():
    number = 123
    written_number = "one hundred twenty three"
    EnglishNumbers(number=number, written_number=written_number).save()
    EnglishNumbers(number=99, written_number="ninety nine").save()
    response = client.get(f"{ENDPOINT}?number={number}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "status": "ok",
        "num_to_english": written_number
    }

