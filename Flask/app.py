from flask import Flask, render_template, request
from .models import DB, Business

def create_app():
    # Create and configure the app
    app = Flask(__name__)