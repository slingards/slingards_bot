from flask import Flask
def create_app():
    app = Flask(__name__)

    from app.routes.paste_route import paste_bp
    app.register_blueprint(paste_bp)

    return app
