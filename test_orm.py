import sqlite3

import pytest

from eb808.orm import Database, Table, Column, ForeignKey


def test_create_db():
    db = Database("./test.db")

    assert isinstance(db.conn, sqlite3.Connection)
    assert db.tables == []


# fixtures


@pytest.fixture
def Taxonomy():
    class Taxonomy(Table):
        name = Column(str)
        ott_id = Column(int)

    return Taxonomy
