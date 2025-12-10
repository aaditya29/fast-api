from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid


class Book(SQLModel):

    __tablename__ = "books"  # defining the table name
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,  # using PostgreSQL UUID type
            primary_key=True,  # making it primary key
            unique=True,  # unique constraint
            nullable=False,  # not nullable
            default=uuid.uuid4()  # default value is generated using uuid4
        )
    )
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    created_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now))  # timestamp when the record is created
    updated_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now))  # timestamp when the record is updated

    # special method to represent the object as a string
    def __repr__(self) -> str:
        return f"<Book {self.title}>"  # representing the book by its title
