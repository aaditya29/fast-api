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
from fastapi import FastAPI
app = FastAPI()  # Initialize FastAPI application


books = [
    {
        "id": 1,
        "title": "Surely You're Joking, Mr. Feynman!",
        "author": "Richard P. Feynman",
        "publisher": "W. W. Norton & Company",
        "published_date": "1985-01-01",
        "page_count": 350,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future",
        "author": "Ashlee Vance",
        "publisher": "HarperCollins",
        "published_date": "2015-05-19",
        "page_count": 400,
        "language": "English",
    },
    {
        "id": 3,
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "publisher": "Bantam Books",
        "published_date": "1988-04-01",
        "page_count": 256,
        "language": "English",
    },
    {
        "id": 4,
        "title": "The Selfish Gene",
        "author": "Richard Dawkins",
        "publisher": "Oxford University Press",
        "published_date": "1976-01-01",
        "page_count": 360,
        "language": "English",
    },
    {
        "id": 5,
        "title": "The Double Helix: A Personal Account of the Discovery of the Structure of DNA",
        "author": "James D. Watson",
        "publisher": "Simon & Schuster",
        "published_date": "1968-02-01",
        "page_count": 256,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Cosmos",
        "author": "Carl Sagan",
        "publisher": "Random House",
        "published_date": "1980-01-01",
        "page_count": 396,
        "language": "English",
    },
]

# defining endpoints


@app.get("/books")
async def get_books():
    pass

# post endpoint to create a book


@app.post("/books")
async def create_a_book() -> dict:
    pass

# get a book by id


@app.post("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    pass

# update a book by id


@app.post("/book/{book_id}")
async def update_book(book_id: int) -> dict:
    pass


# delete a book by id
@app.post("/book/{book_id}")
async def delete_book(book_id: int) -> dict:
    pass
