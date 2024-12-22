from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.auth.auth import router as auth_router
from backend.crud.crud import router as crud_router
from backend.logger.logger import custom_logger

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


app.include_router(crud_router, prefix="/crud", tags=["crud operations"])
app.include_router(auth_router, prefix="/auth", tags=["auth operations"])
