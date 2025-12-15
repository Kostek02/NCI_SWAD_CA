"""
app/notes/routes.py
-------------------
Notes blueprint for the Secure Notes App.

Purpose:
- Manages CRUD operations for user notes.
- Provides isolated blueprint structure for modular development.

v0.9.1: Functional baseline - INTENTIONALLY INSECURE
- Uses string concatenation for SQL queries (SQL injection vulnerable)
- No input sanitisation
- No ownership checks
- No CSRF protection
- Security hardening will be added in v2.x
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.db import get_db
from flask_login import login_required, current_user
from app.notes.forms import NoteForm

# Blueprint definition
notes_bp = Blueprint("notes", __name__)


@notes_bp.route("/")
@login_required
def notes_home():
    '''
    Notes dashboard route - displays notes.
    
    v0.9.3: Shows all notes (no filtering yet - IDOR vulnerable)
    Will add user filtering in v2.2.1 with ownership checks.
    
    Returns:
        Renders the notes dashboard page with a list of notes.
    '''
    db = get_db()
    # INSECURE: No filtering by user_id - shows all notes (IDOR vulnerability)
    # No ownership checks - anyone can see/edit/delete any note
    notes = db.execute(
        "SELECT * FROM notes ORDER BY created_at DESC"
    ).fetchall()
    return render_template(
        "notes/dashboard.html",
        title="Notes Dashboard - Secure Notes",
        notes=notes
    )


@notes_bp.route("/create", methods=["GET", "POST"])
@login_required
def create_note():
    """
    Note creation route - handles both GET (show form) and POST (create note).

    Returns:
        GET: Renders the note creation form.
        POST: Creates note in DB and redirects to dashboard.
    """
    form = NoteForm()
    
    if form.validate_on_submit():
        title = form.title.data.strip()
        content = form.content.data.strip()
        user_id = current_user.id
        
        # Insert note into database
        # INSECURE: String concatenation - vulnerable to SQL injection
        # Note: Will be fixed with parameterized queries
        db = get_db()
        insert_query = f"INSERT INTO notes (title, content, user_id) VALUES ('{title}', '{content}', {user_id})"
        db.execute(insert_query)
        db.commit()

        flash("Note created successfully!", "success")
        return redirect(url_for("notes.notes_home"))
    
    # GET request or validation failed - show form
    return render_template(
        "notes/create.html",
        title="Create Note - Secure Notes",
        form=form
    )

@notes_bp.route("/view/<int:note_id>")
@login_required
def view_note(note_id):
    """
    Note viewing route - displays a single note in read-only mode.

    Args:
        note_id (int): ID of the note to view.

    Returns:
        Renders the note viewing page, or 404 if note not found.
    """
    db = get_db()
    # INSECURE: String concatenation - vulnerable to SQL injection
    # No ownership check - anyone can view any note
    query = f"SELECT * FROM notes WHERE id = {note_id}"
    note = db.execute(query).fetchone()

    if note is None:
        flash("Note not found.", "error")
        return redirect(url_for("notes.notes_home"))

    return render_template(
        "notes/view.html",
        title=f"View Note - Secure Notes",
        note=note
    )


@notes_bp.route("/edit/<int:note_id>", methods=["GET", "POST"])
@login_required
def edit_note(note_id):
    """
    Note editing route - handles both GET (show form) and POST (update note).

    Args:
        note_id (int): ID of the note to edit.

    Returns:
        GET: Renders the note editing form with pre-filled data.
        POST: Updates note in DB and redirects to dashboard.
    """
    db = get_db()
    
    # Fetch note for editing
    # INSECURE: String concatenation - vulnerable to SQL injection
    query = f"SELECT * FROM notes WHERE id = {note_id}"
    note = db.execute(query).fetchone()

    if note is None:
        flash("Note not found.", "error")
        return redirect(url_for("notes.notes_home"))
    
    form = NoteForm()
    
    if form.validate_on_submit():
        title = form.title.data.strip()
        content = form.content.data.strip()

        # Update note in database
        # INSECURE: String concatenation - vulnerable to SQL injection
        # Note: Will be fixed with parameterized queries
        query = f"UPDATE notes SET title = '{title}', content = '{content}' WHERE id = {note_id}"
        db.execute(query)
        db.commit()

        flash("Note updated successfully!", "success")
        return redirect(url_for("notes.notes_home"))
    
    # GET request - pre-fill form with existing data
    if request.method == "GET":
        form.title.data = note['title']
        form.content.data = note['content']
    
    return render_template(
        "notes/edit.html",
        title=f"Edit Note - Secure Notes",
        form=form,
        note=note
    )

@notes_bp.route("/delete/<int:note_id>")
@login_required
def delete_note(note_id):
    """
    Note deletion route - removes a note from the database.

    Args:
        note_id (int): ID of the note to delete.

    Returns:
        Redirects to dashboard after deletion.
    """
    db = get_db()

    # Check if note exists
    # INSECURE: String concatenation - vulnerable to SQL injection
    query = f"SELECT * FROM notes WHERE id = {note_id}"
    note = db.execute(query).fetchone()

    if note is None:
        flash("Note not found.", "error")
        return redirect(url_for("notes.notes_home"))

    # Delete note
    # INSECURE: String concatenation - vulnerable to SQL injection
    # No ownership check - anyone can delete any note (IDOR vulnerability)
    query = f"DELETE FROM notes WHERE id = {note_id}"
    db.execute(query)
    db.commit()

    flash("Note deleted successfully!", "success")
    return redirect(url_for("notes.notes_home"))