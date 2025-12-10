from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.books.models import Book
from sqlmodel import SQLModel
from src.config import Config

engine = AsyncEngine(
    # create the async engine using the database URL from config
    # echo = true means to log all the SQL statements
    create_engine(url=Config.DATABASE_URL, echo=True))


async def init_db():  # defining async function to initialize the database
    async with engine.begin() as conn:  # creating an async connection as conn
        await conn.run_sync(SQLModel.metadata.create_all)  # create all tables
