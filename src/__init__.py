from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Now we are starting the server")
    await init_db()  # initialize the database when the server starts
    yield  # used to run code before and after the application runs
    print("Server has stopped now.")


version = "v1.0.0"

app = FastAPI(
    title="Book Management API",
    description="A simple FastAPI application to manage a collection of books.",
    version=version,
    lifespan=life_span,
)  # Initialize FastAPI app

# Include book router
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
