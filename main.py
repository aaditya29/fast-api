from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  # Initialize FastAPI application


@app.get("/")  # Define a GET endpoint at the root URL
async def read_root():
    return {"message": "Hello, World!"}  # Return a simple JSON response


@app.get('/greet')  # Defining a GET endpoint
async def greet_name(name: str) -> dict:
    # Return a greeting message with the provided name
    return {"greeting": f"Hello, {name}!"}

# adding query paraemeter with name and age


@app.get('/greet/{username}')  # Defining a GET endpoint with path parameter
async def greet_user(username: Optional[str] = "User", age: int = "0") -> dict:
    # Return a greeting message with the provided username and age
    return {"greeting": f"Hello, {username}! You are {age} years old."}


class BookCreateModel(BaseModel):
    title: str
    author: str


# sending data to server with POST request
# if we are sending data then we also need to validate it using serializers or pydantic models
@app.post('create_book')
# book_data is an instance of BookCreateModel which will contain the data sent by the client
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }
