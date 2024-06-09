from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from models import db, Member
bp = Blueprint('member', __name__)

@bp.route('/members')
def list_members():
    members = Member.query.all()
    return render_template('member.html', members=members)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # 查询数据库以验证用户
    user = Member.query.filter_by(username=username, pwd=password).first()
    
    if user:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['pwd']

        # Validate inputs
        if not username or not email or not pwd:
            flash("All fields are required")
            return redirect(url_for('member.register'))

        # Check for existing user
        existing_user = Member.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken")
            return redirect(url_for('member.register'))

        existing_email = Member.query.filter_by(email=email).first()
        if existing_email:
            flash("Email already registered")
            return redirect(url_for('member.register'))
        
        new_member = Member(username=username, email=email, pwd=pwd)
        db.session.add(new_member)
        db.session.commit()
        return redirect(url_for('member.list_members'))
    return render_template('register.html')
