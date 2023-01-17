import sqlite3

from eb808.orm import Database


def test_create_db():
    db = Database("./test.db")

    assert isinstance(db.conn, sqlite3.Connection)
    assert db.tables == []
