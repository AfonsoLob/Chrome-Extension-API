from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import blueprints
    from .views import views
    from .auth import auth
    from .database import setup_database, cleanup_database
    # Register blueprints
    # cleanup_database()
    setup_database() # Create tables such as user table

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,  url_prefix='/')

    return app