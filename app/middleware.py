"""
app/middleware.py
-----------------
Simple middleware hooks for the Secure Notes App.

Purpose:
- Demonstrate use of Flask's before_request and after_request decorators.
- Adds timing header to responses for debugging/performance observation.
- Prepares foundation for future logging or request validation middleware.
"""

import time
from flask import g, request

def register_middleware(app):
    """
    Registers simple before_request and after_request middleware hooks.
    """

    @app.before_request
    def start_timer():
        """Store start time before each request."""
        g._start_time = time.time()

    @app.after_request
    def add_timing_header(response):
        """Add response time header for basic request monitoring."""
        elapsed = time.time() - getattr(g, "_start_time", time.time())
        response.headers["X-Response-Time"] = f"{elapsed:.4f}s"
        response.headers["X-Request-Path"] = request.path
        return response