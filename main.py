from flask import Flask , render_template
from models import *

app = Flask(__name__)

@app.route('/')
def index():
  pass

@app.route('/logout')
def logout():
    pass

@app.route('/sign-up')
def signup():
    pass

@app.route('/sign-in')
def signin():
    pass

@app.route('/dashboard')
def dashboard():
    pass

@app.route('/dashboard/password-generator')
def password_generator():
    pass

@app.route('/dashboard/notes')
def notes():
  pass

@app.route('/dashboard/account-manager')
def account_manager():
    pass

if __name__ == '__main__':
    app.run(debug=True)