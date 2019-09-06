from flask import Flask, Blueprint
from flask_session import Session
from flask_cors import CORS

from app import __settings
from app.api import api, juggling_namespace

app = Flask(__name__)
app.secret_key = "Hi there"
Session(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = __settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = __settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = __settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = __settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('app', __name__, url_prefix='')
    api.init_app(blueprint)
    api.add_namespace(juggling_namespace)
    flask_app.register_blueprint(blueprint)


initialize_app(app)
    # app.run(host="0.0.0.0", debug=True, port=os.environ["BACKEND_PORT"])
