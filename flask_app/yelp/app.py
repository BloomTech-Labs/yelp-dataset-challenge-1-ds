from decouple import config
from flask import Flask, render_template, request
from .models import DB, Business

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    
    # config link to database and env from .env file
    # remove flask shell warning about tracking modifications
    # initiate app
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    
    # create route to pass Users to application
    # populate user object in html template
    # sets title of application
    @app.route('/')
    def root():
        businesses = Business.query.all()
        return render_template('home.html',
                               title = 'Home',
                               businesses = businesses)