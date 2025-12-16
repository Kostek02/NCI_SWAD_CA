"""
app/helpers.py
---------------
Provides helper utilities and context processors for the Secure Notes App.

Purpose:
- Inject global template variables (app name, version, etc.)
- Provide reusable helper functions for flash messages and formatting
- Register safely through init_app() from app factory
"""

from flask import flash

APP_NAME = "Secure Notes Web Application"
APP_VERSION = "v0.5"

def init_app(app):
    """
    Register global helpers and template context processors.

    Args:
        app (Flask): The Flask application instance.
    """

    # Global variables available in all templates
    @app.context_processor
    def inject_globals():
        """
        Inject global variables into all template contexts.
        Ensures current_user is always available (Flask-Login provides anonymous user if not logged in).
        """
        from flask_login import current_user
        # current_user is provided by Flask-Login automatically
        # It will be an AnonymousUser if not logged in, which is safe to use
        return {
            "app_name": APP_NAME,
            "app_version": APP_VERSION,
            "current_user": current_user
        }

    # Convenience wrappers for consistent flash messages
    def flash_success(message):
        flash(message, "success")

    def flash_error(message):
        flash(message, "error")

    # Attach helpers to app for import-free access
    app.flash_success = flash_success
    app.flash_error = flash_error