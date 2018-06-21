'''views.py'''

# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from models.user import User

auth_blueprint = Blueprint('auth', __name__)
