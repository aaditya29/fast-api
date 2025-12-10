from fastapi import APIRouter, status, HTTPException
from src.books.book_data import books
from src.books.schemas import Book, BookUpdateModel
from typing import List
book_router = APIRouter()


@book_router.get("/", response_model=List[Book])
async def get_books():
    return books  # return all books


# post endpoint to create a book
@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    # model_dump() is used to convert pydantic model to dictionary
    new_book = book_data.model_dump()
    books.append(new_book)  # add the new book to the books list
    return new_book  # return the newly created book


@book_router.get("/{book_id}")  # get a book by id
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")


@book_router.patch("/{book_id}")  # update a book by id
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
@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")
