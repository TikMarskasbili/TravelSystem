from flask import Flask, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, EditProfileForm
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

USER_DATA_FILE = 'users.xlsx'

def read_users():
    try:
        return pd.read_excel(USER_DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=['username', 'email', 'password'])

def save_users(users_df):
    users_df.to_excel(USER_DATA_FILE, index=False)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users_df = read_users()
        if form.email.data in users_df['email'].values:
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = {'username': form.username.data, 'email': form.email.data, 'password': hashed_password}
        users_df = users_df.append(new_user, ignore_index=True)
        save_users(users_df)
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users_df = read_users()
        user = users_df[users_df['email'] == form.email.data]
        if not user.empty and check_password_hash(user.iloc[0]['password'], form.password.data):
            session['user_email'] = form.email.data
            flash('Logged in successfully!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_email' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))
    
    users_df = read_users()
    user = users_df[users_df['email'] == session['user_email']].iloc[0]
    form = EditProfileForm(obj=user)
    if form.validate_on_submit():
        users_df.loc[users_df['email'] == session['user_email'], 'username'] = form.username.data
        users_df.loc[users_df['email'] == session['user_email'], 'email'] = form.email.data
        save_users(users_df)
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))
    return render_template('profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
