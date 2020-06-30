from flask import Flask
app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['UPLOAD_FOLDER'] = '\\app\\files'
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
app_wsgi = Flask.wsgi_app
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(app)
from app import routes