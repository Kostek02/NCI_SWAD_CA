"""
run.py
------
Entry point for running the Secure Notes Flask application.

Purpose:
- Imports the create_app() factory from app/__init__.py
- Instantiates the app
- Starts the local Flask development server
"""

# Import the factory function
from app import create_app

# Create the Flask app instance using the factory
app = create_app()

if __name__ == "__main__":
    # Run the Flask development server
    # debug=True is acceptable for local development (will be disabled in secure builds)
    app.run(debug=True)