"""
app/__init__.py
---------------
Main application factory for the Secure Notes App

Purpose:
- Implements the Flask "application factory" pattern.
- Loads configuration from config.py
- Defines simple base route to verify the app runs.
- Prepares for future blueprint registration (auth, notes, admin).
"""

from flask import Flask

def create_app():
    """
    Factory function for creating and configuring the Flask app.

    Why a factory:
    - It allows flexible setup (testing, production, etc.)
    - Prevents circular imports
    - Supports extension loading and blueprints cleanly

    Returns:
        A fully configured Flask app instance.
    """

    # Step 1: Create Flask instance
    app = Flask(__name__)

    # Step 2: Load configuratoin from config.py (Config class)
    app.config.from_object("config.Config")

    # Step 3: Define a simple root route for v0.1 testing
    @app.route("/")
    def index():
        """
        Root route for testing Flask setup.

        Returns:
            A plain text response confirming the app runs.
        """
        return "The App Runs"

    # Step 4: Return the configured Flask app
    return app 