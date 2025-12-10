from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(
    # create the async engine using the database URL from config
    # echo = true means to log all the SQL statements
    create_engine(url=Config.DATABASE_URL, echo=True))
