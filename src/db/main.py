from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(
    # create the async engine using the database URL from config
    # echo = true means to log all the SQL statements
    create_engine(url=Config.DATABASE_URL, echo=True))


async def init_db():  # defining async function to initialize the database
    async with engine.begin() as conn:  # creating an async connection as conn
        statement = text("SELECT 'hello world';")  # Fixed: added closing quote
        # executing the statement asynchronously
        result = await conn.execute(statement)
        print(result.all())  # printing all results
