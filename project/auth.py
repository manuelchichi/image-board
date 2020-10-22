from flask import Blueprint,request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from project import mongo
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    loginUserJson = mongo.db.users.find_one( { "name": username } )

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not loginUserJson or not loginUserJson['password'] == password:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    loginuser = User(loginUserJson)
    login_user(loginuser)
    return redirect(url_for('main.menu'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    name = request.form.get('name')
    password = request.form.get('password')

    userJson = mongo.db.users.find_one( { "name": name } ) # if this returns a user, then the email already exists in database

    if userJson: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Account already exists')
        return redirect(url_for('auth.signup'))

    mongo.db.users.insert({'name':name,'password':password,'images':[]})

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))