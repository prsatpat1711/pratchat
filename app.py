import json
import os
from flask_migrate import Migrate
from flask import (
    Flask,
    Response,
    request,
    jsonify,
    send_from_directory,
    render_template,
)
from db import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity
from user.views import user_bp
from socket_funcs.views import socket_blueprint, socketio

app = Flask(__name__, static_url_path="/static")

# Enable CORS for all origins
CORS(app)

app.config['JWT_SECRET_KEY'] = 'jasdbksajbdhkasbdjlasdblasdowqeiwhqhwqpfasifsaipfi'  # Change this to a random long string for security
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.register_blueprint(socket_blueprint, url_prefix='/socket/')
app.register_blueprint(user_bp, url_prefix="/api/user/")

db.init_app(app)
socketio.init_app(app)
migrate = Migrate(app, db)

@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify({'message':'Hi'})

def create_tables():
    with app.app_context():
        db.create_all()
        
if __name__ == "__main__":
    create_tables()
    socketio.run(app, debug=True)
