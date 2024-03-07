import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    env: str = os.getenv("EVN", "dev")
    app_name: str = os.getenv("APP_NAME", "My Api")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost/Phone",
    )
    secret_key: str = os.getenv("SECRET_KEY", "9cfe4731588484c858a3900c71f57833")
    jwt_issuer: str = os.getenv("JWT_ISSUER", "3b532505bb1afbbe537527343f78e048")
    jwt_audience: str = os.getenv("JWT_AUDIENCE", "95b7be500ae9a66cc355a5e1880e42f7")
    jwt_KEY: str = os.getenv("JWT_KEY", "719e8a88dc6bdc382a7a540a21daca61")
