#import flask module from Flask package
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

app=Flask(__name__)

def create_app():
    bootstrap = Bootstrap(app)
    
      # this is the name of the module/package that is calling this app
    app.secret_key = 'supersecret'

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///travel.db'
    db.init_app(app)
    #we use this utility module to display forms quickly
    
    #initialize the login manager
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    #add Blueprints
    from . import views
    app.register_blueprint(views.bp)
    from . import destinations
    app.register_blueprint(destinations.bp)
    from . import auth
    app.register_blueprint(auth.bp)

    return app

@app.errorhandler(404) 
# error as parameter 
def not_found(e): 
  return render_template("404.html")
@app.errorhandler(500) 
# error as parameter 
def not_found(e): 
  return render_template("404.html")