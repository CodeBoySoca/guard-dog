from flask import Flask , render_template, request
from flask_wtf.csrf import CSRFProtect
from models import *
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'This is what dreams are made of'
csrf = CSRFProtect(app)

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

@app.route('/dashboard/password-generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
           password_generator = PasswordGenerator(length=int(request.form.get('password_length')), characters=str(request.form.get('password_characters')))
           return render_template('password-generator.html', password=password_generator.generate_password())
    return render_template('password-generator.html')

@app.route('/dashboard/notes')
def notes():
  notes = Users.objects(name='Johann Austin')
  return render_template('notes.html', notes=notes)

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