""" 
config.py 
---------
Central configuration file for the Secure Notes Web Application.

Purpose:
- Load environment variables from .env file
- Provide a central point for application configuration
- Allow different configurations (Development, Production, etc.)

This design follows the Singleton pattern to ensure a 
    single instance of the configuration is used throughout the application and 
    follows the SOLID principles and follows Flask's best practice of separating 
    configuration from application logic.
"""

import os 

# Load environment variables from .env file
from dotenv import load_dotenv

# Load all variables from the .env file into the system environment
load_dotenv()

class Config:
    """ 
    The Config class defines key configuration options for the Flask app.

    Attributes:
        SECRET_KEY: The secret key for the application
        DEBUG: Enable/Disable debug mode
        FLASK_ENV: Controls the runtime environment (Development, Production, etc.)
    """

    # The secret key for the application
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key') 
    
    # Enable/Disable debug mode (convert to boolean)
    DEBUG = os.getenv('DEBUG', 'True').lower() in ('true', '1', 't')
    
    # Controls the runtime environment (Development, Production, etc.)
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')