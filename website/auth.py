from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from .database import verify_user, add_user, get_user_password
from werkzeug.security import generate_password_hash, check_password_hash
import re  # used to validate email

regex = '^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$'
auth = Blueprint('auth', __name__)


# Routes related to authentication

@auth.route('/login', methods=['POST'])
def extension_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(data)
    if username and password:
        if verify_user(username):
            if check_password_hash(get_user_password(username), password):
                session.permanent = True
                session['user'] = {'email': username}
                return jsonify({'success': True, 'message': 'Login successful'})
            else:   
                return jsonify({'success': False, 'error': 'Incorrect password'})
        else:
            return jsonify({'success': False, 'error': 'User does not exist'})
    else:
        return jsonify({'success': False, 'error': 'Invalid data'})


@auth.route('/sign-up', methods=['POST'])
def extension_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        if re.search(regex, username) is None:
            return jsonify({'success': False, 'error': 'Invalid email format'})
        elif len(password) < 8:
            return jsonify({'success': False, 'error': 'Password should be at least 8 characters long'})

        if not verify_user(username):
            add_user(username, password)
            return jsonify({'success': True, 'message': 'Signup successful'})
        else:
            return jsonify({'success': False, 'error': 'Email already in use'})
    else:
        return jsonify({'success': False, 'error': 'Invalid data'})


@auth.route('/logout', methods=['GET'])
def logout():
    if 'user' in session:
        session.pop('user')
    return jsonify({'success': True})
