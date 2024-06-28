from flask import Blueprint, render_template, request, redirect, url_for
from models import db, TravelRoad
from datetime import datetime

bp = Blueprint('road', __name__)

@bp.route('/travel_road')
def list_travel_roads():
    roads = TravelRoad.query.all()
    return render_template('travel_road.html', roads = roads)

@bp.route('/add_travel_road', methods=['GET', 'POST'])
def add_travel_road():
    if request.method == 'POST':
        department = request.form['department']
        destination = request.form['destination']
        road = request.form['road']
        content = request.form['content']
        rating = request.form['rating']
        new_road = TravelRoad(department=department, destination=destination,road=road,content=content, rating=rating)
        db.session.add(new_road)
        db.session.commit()
        return redirect(url_for('road.list_travel_roads'))
    return render_template('add_travel_road.html')
