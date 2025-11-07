"""
app/notes/routes.py
-------------------
Notes blueprint for the Secure Notes App.

Purpose:
- Manages CRUD operations for user notes.
- Provides isolated blueprint structure for modular development.
- Prepares for secure data ownership and validation logic.
"""

from flask import Blueprint, render_template

# Blueprint definition
notes_bp = Blueprint("notes", __name__)

@notes_bp.route("/")
def notes_home():
    """
    Notes dashboard route.

    Returns:
        Renders the notes dashboard page.
    """
    return render_template("notes/dashboard.html", title="Notes Dashboard - Secure Notes")


@notes_bp.route("/create")
def create_note():
    """
    Note creation route.

    Returns:
        Renders the note creation page.
    """
    return render_template("notes/create.html", title="Create Note - Secure Notes")


@notes_bp.route("/view/<int:note_id>")
def view_note(note_id):
    """
    Note viewing route.

    Args:
        note_id (int): ID of the note to view.

    Returns:
        Renders the note viewing page.
    """
    return render_template("notes/view.html", title=f"View Note {note_id} - Secure Notes", note_id=note_id)


@notes_bp.route("/edit/<int:note_id>")
def edit_note(note_id):
    """
    Note editing route.

    Args:
        note_id (int): ID of the note to edit.

    Returns:
        Renders the note editing page.
    """
    return render_template("notes/edit.html", title=f"Edit Note {note_id} - Secure Notes", note_id=note_id)