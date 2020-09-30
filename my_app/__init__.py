from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

def create_app():
	app = Flask(__name__)
	db.init_app(app)
	return app


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tmp/uefa_comps.db"
app.secret_key = b'vsarTest/'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') +'\\my_app\\static\\uploads'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "uefa_comps.login"



from my_app.uefa_comps.views import uefa_comps
app.register_blueprint(uefa_comps)
db.create_all()


