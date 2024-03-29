import datetime
import os

import jwt


def generate_access_token(user):
    access_token_payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(
        access_token_payload, os.getenv("JWT_SECRET_KEY"), algorithm="HS256"
    )
    return access_token


def generate_refresh_token(user):
    refresh_token_payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7),
        "iat": datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(
        refresh_token_payload, os.getenv("REFRESH_SECRET_KEY"), algorithm="HS256"
    )

    return refresh_token
