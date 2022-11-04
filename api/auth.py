from django.http import HttpRequest
from ninja.security import HttpBearer
from typing import Optional, Any

from api.exceptions import UnauthorizedException
from djangoProject.settings import SECRET_KEY


class GlobalAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        if token == SECRET_KEY:
            return token
        raise UnauthorizedException
