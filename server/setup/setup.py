"""Database setup."""


import asyncio
import os

import asyncpg

from ..database import db


class Setup:
    """Class methods for setup."""

    pool: asyncpg.pool.Pool
    database: db.PlayerDB

    async def connect(self) -> None:
        """
        Connect to and set the database.

        Uses asyncpg to connect to the database. Fetches keys from the environment.
        """
        self.pool = await asyncpg.create_pool(
            user='postgres',
            password='knfTlGQ7XFMtZw5kIkth',
            host='containers-us-west-36.railway.app',
            port=6074,
            database='railway',
            ssl="require",
            loop=asyncio.get_event_loop(),
        )

    async def setup(self) -> None:
        """Set up all connections"""
        await self.connect()

        self.database = db.PlayerDB()
        await self.database.set_table(self.pool)

    async def close(self) -> None:
        """Close all connections"""
        await self.pool.close()
