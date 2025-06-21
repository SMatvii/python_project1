from flask import Flask
from backend.api import app as api_app

app = Flask(__name__, static_folder="frontend/static", template_folder="frontend/templates")
app.register_blueprint(api_app, url_prefix="/api")