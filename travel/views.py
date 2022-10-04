from flask import Blueprint, render_template, session, request, redirect

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

