from flask import Flask, request, jsonify
from flask import current_app, g
from decouple import config
import os
import sys

local_db_name = 'test.sqlite3'

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # If environment vairables not set, will default to development expected paths and names
    app.config.from_mapping(
        DEBUG=config('DEBUG', default=False),  # Make sure to change debug to False in production env
        SECRET_KEY=config('SECRET_KEY', default='dev'),  # CHANGE THIS!!!!
        DATABASE_URI=config('DATABASE_URI', 'sqlite:///' + os.path.join(os.getcwd(), local_db_name)),  # For in-memory db: default='sqlite:///:memory:'),
        LOGFILE=config('LOGFILE', os.path.join(app.instance_path, 'logs/debug.log')),
        CACHE_TYPE=config('CACHE_TYPE', 'simple'),  # Configure caching
        CACHE_DEFAULT_TIMEOUT=config('CACHE_DEFAULT_TIMEOUT', 300), # Long cache times probably ok for ML api
