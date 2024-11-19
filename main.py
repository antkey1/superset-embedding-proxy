from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from supersetapiclient.client import SupersetClient


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='superset_embedding_proxy_',
        env_file='.env',
        env_file_encoding='utf-8',
    )
    superset_host: str
    superset_username: str
    superset_password: str

settings = Settings()


app = FastAPI(title='superset-embedding-proxy')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=['*']
)


class PostGuestTokenRequest(BaseModel):
    resource_id: str


class PostGuestTokenResponse(BaseModel):
    token: str


@app.post(
    path='/superset/guest-token',
    response_model=PostGuestTokenResponse,
)
async def post_guest_token(
        request: PostGuestTokenRequest,
) -> PostGuestTokenResponse:
    client = SupersetClient(
        host=settings.superset_host,
        username=settings.superset_username,
        password=settings.superset_password,
    )
    token = client.guest_token(uuid=request.resource_id)
    return PostGuestTokenResponse(token=token)
