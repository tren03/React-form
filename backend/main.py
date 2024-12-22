from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.logger.logger import custom_logger
from backend.v1.routes import router as v1_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Need middleware to extract auth from httponly cookie of incoming request,
# and and that as auth header since that is what is accepted by our backend


@app.middleware("http")
async def create_auth_header(
    request: Request,
    call_next,
):
    """
    Check if there are cookies set for authorization. If so, construct the
    Authorization header and modify the request (unless the header already
    exists!)
    """
    custom_logger.info(request.cookies)
    if "Authorization" not in request.headers and "access_token" in request.cookies:
        access_token = request.cookies["access_token"]

        request.headers.__dict__["_list"].append(
            (
                "authorization".encode(),
                f"Bearer {access_token}".encode(),
            )
        )
        print(request.headers)

    response = await call_next(request)
    return response


app.include_router(v1_router, prefix="/v1", tags=["Version 1"])
