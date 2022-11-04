import os
from typing import Any
from unittest import mock

import pytest

from api.schemas import Error, EnglishNumberOut
from api.views import ENDPOINT
from http import HTTPStatus
from api.views import api

from ninja.testing import TestClient

from djangoProject.settings import SECRET_KEY
from full_written_numbers.models import EnglishNumbers

from django.test import override_settings


class AuthenticatedClient(TestClient):
    @override_settings(SECRET_KEY="token")
    def request(self, method, path, data={}, json=None, **request_params: Any):
        headers = {"Authorization": f"Bearer {SECRET_KEY}"}
        request_params.setdefault("headers", headers)
        return super().request(method, path, data, json, **request_params)


client = AuthenticatedClient(api)


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


def test_post_payload_structure():
    response = client.post(ENDPOINT)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == Error(status="Wrong payload structure", num_to_english="").dict()


def test_post_payload_number_type():
    response = client.post(ENDPOINT, json={"number": "12A3"})
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json() == Error(status="'number' must be a valid integer", num_to_english="").dict()


@pytest.mark.django_db
def test_existing_number_failure():
    EnglishNumbers(number=99, written_number="ninety nine").save()
    response = client.post(ENDPOINT, json={"number": "99"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == Error(status="Number already exists", num_to_english="").dict()


@pytest.mark.django_db
def test_number_conversion_successful():
    response = client.post(ENDPOINT, json={"number": "99"})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == EnglishNumberOut(
        status="ok",
        num_to_english="ninety nine"
    )


@pytest.mark.django_db
def test_unauthorized_request():
    response = client.post(
        ENDPOINT,
        json={"number": "99"},
        headers={"Authorization": f"Bearer wrong"}
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == EnglishNumberOut(
        status="Unauthorized. Missing Bearer token",
        num_to_english=""
    )
