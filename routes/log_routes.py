# routes/log_routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, TravelLog, TravelGuide

bp = Blueprint('log', __name__)

@bp.route('/logs')
def list_logs():
    logs = TravelLog.query.all()
    guides = TravelGuide.query.all()
    return render_template('logs.html', logs=logs, guides=guides)

@bp.route('/add_log', methods=['GET', 'POST'])
def add_log():
    if request.method == 'POST':
        member_id = request.form['member_id']
        title = request.form['title']
        content = request.form['content']
        rating = request.form['rating']
        new_log = TravelLog(member_id=member_id, title=title, content=content, rating=rating)
        db.session.add(new_log)
        db.session.commit()
        return redirect(url_for('log.list_logs'))
    return render_template('add_log.html')

@bp.route('/add_guide', methods=['GET', 'POST'])
def add_guide():
    if request.method == 'POST':
        destination = request.form['destination']
        content = request.form['content']
        new_guide = TravelGuide(destination=destination, content=content)
        db.session.add(new_guide)
        db.session.commit()
        return redirect(url_for('log.list_logs'))
    return render_template('add_guide.html')
