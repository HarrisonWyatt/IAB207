from flask import Blueprint, render_template, session, request, redirect, url_for
from .models import *
from .forms import DestinationForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

bp = Blueprint('destination',__name__, url_prefix='/destinations')

@bp.route('/<id>')
def show(id):
    destination = Destination.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('destinations/shows.html', destination=destination, form=cform)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = DestinationForm()
  if form.validate_on_submit():
    #checks and returns image
    db_file_path=check_upload_file(form)
    destination=Destination(name=form.name.data,description=form.description.data, 
    image=db_file_path,currency=form.currency.data)
    db.session.add(destination)
    db.session.commit()
    print('Successfully created new travel destination', 'success')
    #redirect
    return redirect(url_for('destination.create'))
  return render_template('destinations/create.html', form=form)

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  BASE_PATH=os.path.dirname(__file__)
  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  db_upload_path='/static/image/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<id>/comment', methods = ['GET', 'POST'])  
@login_required
def comment(id):  
    form = CommentForm()  
    destination_obj = Destination.query.filter_by(id=id).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        destination=destination_obj,
                        user=current_user) 
      db.session.add(comment) 
      db.session.commit() 
      print('Your comment has been added', 'success') 
    return redirect(url_for('destination.show', id=id))

@bp.route('/fun/<id>')
def fun(id):
    txt = "you entered {}".format(id) 
    return txt