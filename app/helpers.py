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
        return {
            "app_name": APP_NAME,
            "app_version": APP_VERSION
        }

    # Convenience wrappers for consistent flash messages
    def flash_success(message):
        flash(message, "success")

    def flash_error(message):
        flash(message, "error")

    # Attach helpers to app for import-free access
    app.flash_success = flash_success
    app.flash_error = flash_error