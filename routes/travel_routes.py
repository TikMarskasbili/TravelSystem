from flask import Blueprint, render_template, request, redirect, url_for
from models import db, TravelIntent

bp = Blueprint('travel', __name__)

@bp.route('/travel_intents')
def list_travel_intents():
    intents = TravelIntent.query.all()
    return render_template('travel_intent.html', intents=intents)

@bp.route('/add_travel_intent', methods=['GET', 'POST'])
def add_travel_intent():
    if request.method == 'POST':
        member_id = request.form['member_id']
        destination = request.form['destination']
        travel_time = request.form['travel_time']
        budget = request.form['budget']
        companion_requirements = request.form['companion_requirements']
        new_intent = TravelIntent(member_id=member_id, destination=destination, travel_time=travel_time, budget=budget, companion_requirements=companion_requirements)
        db.session.add(new_intent)
        db.session.commit()
        return redirect(url_for('travel.list_travel_intents'))
    return render_template('add_travel_intent.html')
