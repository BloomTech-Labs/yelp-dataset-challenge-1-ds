from decouple import config
from flask import Flask, render_template, request
from .models import DB, Business
from api import yelp_business_reviews

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
    
    # add business and business/<name>
    @app.route('/business', methods=['POST']) # trigger this if post request (adding to db)
    @app.route('/business/<name>', methods=['GET']) # trigger this if get request (pulling existing from db)
    def user(name=None, message=''):
        name = name or request.values['business_name']
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "Business {} successfully added!".format(name)
            reviews = Business.query.filter(Business.name == name).one().reviewss # 'one()' means pull first user
        except Exception as e:
            message = "Error adding {}: {}".format(name, e)
            reviews = []
        return render_template('user.html', title=name, reviews=reviews,
                               message=message)
        
    return app