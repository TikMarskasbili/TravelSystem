from flask import Blueprint, render_template, request, redirect, url_for
from models import db, TravelLog, TravelGuide

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    return render_template('home.html')