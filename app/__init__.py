import os
from flask import Flask
from dotenv import load_dotenv
from .db import db
from .routes import order_bp
from flask_cors import CORS


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("MYSQL_DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})  # <- FIXED

    app.register_blueprint(order_bp)

    with app.app_context():
        db.create_all()

    return app
