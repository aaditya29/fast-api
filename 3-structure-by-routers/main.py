"""
Building a simple CRUD application with FastAPI to manage a collection of books.
CRUD operations include:
- Create a new book
- Read all books
- Read a specific book by ID
- Update a book by ID
- Delete a book by ID

Our simple CRUD API will have a few endpoints to perform CRUD operations on a simple in-memory database of books. Here's a list of endpoints that we shall have in our CRUD API.

Endpoint	Method	Description
/books	     Get	Read all books
/books	    POST	Create a book
/book/{book_id}	GET	Get a book by id
/book/{book_id}	PATCH	Update a book by id
/book/{book_id}	DELETE	Delete a book by id

"""
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import Optional, List
from schemas import Book, BookUpdateModel
from book_data import books
app = FastAPI()  # Initialize FastAPI application


# defining endpoints

# we use response_model to define the response schema from class Books
@app.get("/books", response_model=List[Book])
async def get_books():
    return books  # return all books


# post endpoint to create a book
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    # model_dump() is used to convert pydantic model to dictionary
    new_book = book_data.model_dump()
    books.append(new_book)  # add the new book to the books list
    return new_book  # return the newly created book


@app.get("/book/{book_id}")  # get a book by id
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


@app.patch("/book/{book_id}")  # update a book by id
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:  # found the book to be updated
            book['title'] = book_update_data.title  # update title
            book['publisher'] = book_update_data.publisher  # update publisher
            book['page_count'] = book_update_data.page_count  # update page count
            book['language'] = book_update_data.language  # update language

            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


# delete a book by id
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")
