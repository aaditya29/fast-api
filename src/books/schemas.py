from pydantic import BaseModel
# we build this class to define the structure of a book


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

# we build this class to update the book details because if
# we don't provide all the fields then it will throw an error due to missing fields


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
