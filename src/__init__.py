from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Now we are starting the server")
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
