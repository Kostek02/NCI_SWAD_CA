"""
app/db.py
---------
SQLite helper for the Secure Notes App (insecure baseline for v0.4).
"""

import sqlite3
from pathlib import Path
from flask import current_app, g


def get_db():
    """Retrieve a database connection tied to the Flask app context."""
    if "db" not in g:
        db_path = Path(current_app.instance_path) / "secure_notes.db"
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """Close the database connection if one exists."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Initialise the database using instance/schema.sql."""
    db = get_db()
    schema_path = Path(current_app.instance_path) / "schema.sql"

    with schema_path.open("r", encoding="utf-8") as f:
        db.executescript(f.read())

    db.commit()


def init_app(app):
    """Register teardown + CLI init-db command with Flask."""
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    app.teardown_appcontext(close_db)

    @app.cli.command("init-db")
    def init_db_command():
        """Flask CLI command: 'flask init-db'."""
        init_db()
        print("Database initialised successfully.")