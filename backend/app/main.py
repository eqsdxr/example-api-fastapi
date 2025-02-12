from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import main_router

app = FastAPI()


app.include_router(main_router)

origins = [
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


