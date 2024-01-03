from flask import Flask , render_template
from models import *
import uuid

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

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
    user_accounts=Users.objects(name='Johann Austin')
    return render_template('account-manager.html', accounts=user_accounts)

@app.route('/update')
def update():
    pass

@app.route('/remove')
def remove():
    pass

if __name__ == '__main__':
    app.run(debug=True)