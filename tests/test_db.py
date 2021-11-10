import sqlite3
import json
import pytest
from fruitpal.db import get_db


def test_get_close_db(app):
    #get db and ensure it exists
    with app.app_context():
        db = get_db()
        assert db is get_db()

    #ensure db closes properly after closing context
    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True
    #researched and got this test
    monkeypatch.setattr('fruitpal.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called

def test_price_check_exists(app):
    with app.app_context():
        db=get_db()
        r = db.execute("SELECT count(1) FROM price_check").fetchone()[0]
        assert r > 0
        