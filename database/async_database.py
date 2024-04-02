import sqlite3
import aiosqlite
from database import sql_queries


class AsyncDatabase:
    def __init__(self, db_path='db.sqlite3'):
        self.db_path = db_path

    async def create_tables(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(sql_queries.CREATE_USER_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
            await db.execute(sql_queries.CREATE_REFERENCE_TABLE_QUERY)

            try:
                await db.execute(sql_queries.ALTER_TABLE_USER_QUERY)
                await db.execute(sql_queries.ALTER_TABLE_USER_V2_QUERY)
            except sqlite3.OperationalError:
                pass

            await db.commit()

    async def execute_query(self, query, params=None, fetch="none"):
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(query, params or ())

            if fetch == "one":
                data = await cursor.fetchone()
                return dict(data) if data else None
            elif fetch == 'all':
                data = await cursor.fetchall()
                return [dict(row) for row in data] if data else []
            elif fetch == 'none':
                await db.commit()
                return
