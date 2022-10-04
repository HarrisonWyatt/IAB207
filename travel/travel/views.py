from flask import Blueprint, render_template, request, redirect,url_for
from .models import Destination 

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    destinations = Destination.query.all()    
    return render_template('index.html', destinations=destinations)

@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + "%"
        destinations = Destination.query.filter(Destination.description.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))