from flask import Flask, render_template, url_for, request, redirect, session
from datetime import timedelta
from website import create_app

app = create_app() # create_app() in __init__.py
app.config['SECRET_KEY'] = b'*51_.2S7H2F\n\xec]/'
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == "__main__":
    app.run()