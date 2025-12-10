from fastapi import FastAPI
from src.books.routes import book_router

version = "v1.0.0"

app = FastAPI(
    title="Book Management API",
    description="A simple FastAPI application to manage a collection of books.",
    version=version
)  # Initialize FastAPI app

# Include book router
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["Books"])
