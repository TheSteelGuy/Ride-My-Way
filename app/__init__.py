'''
___init__.py
main API config  file
'''

from flask_api import FlaskAPI

# local imports
from app.config import CONFIGS
from .Auth.views import auth_blueprint


def create_app(config_param):
    ''' function that receives configaration and creates the app'''
    app = FlaskAPI(__name__)
    app.config.from_object(CONFIGS[config_param])
    app.url_map.strict_slashes = False
    app.register_blueprint(auth_blueprint)
    return app
