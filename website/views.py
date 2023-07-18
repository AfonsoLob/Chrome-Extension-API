from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from .auth import session
from .database import *
from werkzeug.security import generate_password_hash, check_password_hash


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST request from Chrome Extension
        data = request.get_json()
        response_data = {'message': 'Received POST request from the Chrome Extension'}
        return jsonify(response_data)