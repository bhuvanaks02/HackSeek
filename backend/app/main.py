from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.api.v1 import auth, hackathons, chat, users

def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        docs_url=f"{settings.api_v1_prefix}/docs",
        redoc_url=f"{settings.api_v1_prefix}/redoc"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router, prefix=settings.api_v1_prefix)
    app.include_router(hackathons.router, prefix=settings.api_v1_prefix)
    app.include_router(chat.router, prefix=settings.api_v1_prefix)
    app.include_router(users.router, prefix=settings.api_v1_prefix)

    @app.get("/")
    async def root():
        return JSONResponse(content={
            "message": f"Welcome to {settings.app_name}",
            "version": settings.app_version,
            "docs": f"{settings.api_v1_prefix}/docs"
        })

    @app.get("/health")
    async def health_check():
        return JSONResponse(content={"status": "healthy"})

    return app

app = create_application()