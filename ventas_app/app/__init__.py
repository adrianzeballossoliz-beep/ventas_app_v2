from flask import Flask
from .blueprints.auth import auth_bp
from .blueprints.dashboard import dashboard_bp
from .blueprints.main import main_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = 'ventas_supermercado_secret_2024'

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(dashboard_bp)

    return app
