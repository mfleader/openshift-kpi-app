import typing

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# import orjson

from app.api.api_v1.api import api_router
import app.config as config


# class ORJSONResponse(JSONResponse):
#     media_type = "application/json"

#     def render(self, content: typing.Any) -> bytes:
#         return orjson.dumps(content)


cfg = config.get_config()
app = FastAPI(
    # default_response_class=ORJSONResponse
    )
app.add_middleware(
    CORSMiddleware,
    allow_origins=cfg.get('cors_origins'),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)


