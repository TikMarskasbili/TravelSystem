from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Member

bp = Blueprint('member', __name__)

@bp.route('/members')
def list_members():
    members = Member.query.all()
    return render_template('member.html', members=members)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        hobbies = request.form['hobbies']
        new_member = Member(username=username, email=email, hobbies=hobbies)
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('member.list_members'))
    return render_template('register.html')
