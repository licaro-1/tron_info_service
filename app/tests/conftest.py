from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from main import app
from app.core.db import Base, get_async_session


TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(TEST_DATABASE_URL)
TestAsynсSession = sessionmaker(
    test_engine,
    class_=AsyncSession
)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def db_session():
    async with TestAsynсSession() as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def override_get_async_session(db_session: AsyncSession):
    """Override FastAPI Depends on get_async_session to test_db_session."""
    app.dependency_overrides[get_async_session] = lambda: db_session
    yield
    app.dependency_overrides.clear()


@pytest_asyncio.fixture(scope="session")
async def ac() -> AsyncClient:
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test") as ac:
        yield ac
