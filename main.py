from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routes import register_routes

__API_VERSION__ = "v1"

def create_app():
    app = FastAPI()
    register_routes(app, root="/api/{}".format(__API_VERSION__))
    return app

app = create_app()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Open API",
        version=__API_VERSION__,
        routes=app.routes,
        description="OpenAPI, a verion for testing propose.",
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
