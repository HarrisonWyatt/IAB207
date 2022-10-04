#import flask module from Flask package
from flask import Flask 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
#create a function that creates a web application
# a web server will run this web application
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.secret_key = 'supersecret'

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///travel.db'
    db.init_app(app)
    #we use this utility module to display forms quickly
    bootstrap = Bootstrap(app)

    

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.mainbp)
    from . import auth
    app.register_blueprint(auth.mainbp)

    return app