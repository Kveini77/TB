import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERENCE_TABLE_QUERY)

        try:
            self.connection.execute(sql_queries.ALTER_TABLE_USER_QUERY)
            self.connection.execute(sql_queries.ALTER_TABLE_USER_QUERYV2)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None, 0)
        )
        self.connection.commit()

    def select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def insert_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, tg_id, 1)
        )
        self.connection.commit()

    def update_ban_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_COUNT_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def insert_profile(self, tg_id, nickname, biography, age, married, gender, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_QUERY,
            (None, tg_id, nickname, biography, age, married, gender, photo)
        )
        self.connection.commit()

    def select_all_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "married": row[5],
            "gender": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_LEFT_JOIN_PROFILE_QUERY,
            (tg_id, tg_id, tg_id,)
        ).fetchall()

    def insert_like_profile(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker)
        )
        self.connection.commit()

    def select_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "married": row[5],
            "gender": row[6],
            "photo": row[7],
        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def update_profile(self, nickname, biography, age, married, gender, photo, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_PROFILE_QUERY,
            (nickname, biography, age, married, gender, photo, tg_id,)
        )
        self.connection.commit()

    def delete_profile(self, tg_id):
        self.cursor.execute(
            sql_queries.DELETE_PROFILE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def insert_dislike_profile(self, owner, disliker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker)
        )
        self.connection.commit()

    def update_user_link(self, link, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_QUERY,
            (link, tg_id,)
        )
        self.connection.commit()

    def select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
            "balance": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def update_owner_balance(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def insert_reference_user(self, owner, reference):
        self.cursor.execute(
            sql_queries.INSERT_REFERENCE_QUERY,
            (None, owner, reference,)
        )
        self.connection.commit()

    def select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
            "balance": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def select_reference_user_info(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "count": row[1],
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERENCE_USER_INFO_QUERY,
            (tg_id,)
        ).fetchone()

    def select_reference_users(self):
        self.cursor.row_factory = lambda cursor, row: {
            "first_name": row[0]
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERENCE_USERS_QUERY,
            ()
        ).fetchall()
