from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.crud.crud import router as crud_router
from backend.auth.auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(crud_router, prefix="/crud", tags=["crud operations"])
app.include_router(auth_router, prefix="/auth", tags=["auth operations"])
