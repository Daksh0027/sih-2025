from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "<p> Login </p>"


@auth.route('/logout')
def logout():
    return '<p> Logout </p>'


@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    return '<p> SignUp </p>'
