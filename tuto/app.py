from flask import Flask
from flask_bootstrap import Bootstrap5
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

def mkpath (p):
    return os.path. normpath (
        os.path.join(
            os.path. dirname ( __file__ ),
            p))


app.config['SECRET_KEY'] = "c790387d-9cdf-43f0-981b-2de8c14db788"
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"