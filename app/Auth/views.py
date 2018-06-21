'''views.py'''

# third party imports
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
# local imports
from app.models.user import User

auth_blueprint = Blueprint('auth', __name__)



class AuthenticationView(MethodView):
    users = []
    ''' a view class with all authentication methods '''
    def post(self):
        ''' class method which allows user to sign up'''
        username = request.json.get('username')
        phone = request.json.get('phone')
        password = request.json.get('password')
        confirm_password = request.json.get('confirm_password')
        user = User(username, phone, password, confirm_password)
        if password != confirm_password:
            return make_response(jsonify(
                {'message': 'Ensure password and confirm password matches.'}
            )), 409
        users.append(user)
        return make_response(jsonify(
            {'message': 'Welcome, to ridemyway{}'.format(user.username)}
        )), 201

auth_blueprint.add_url_rule(
    '/signup', view_func=AuthenticationView.as_view('signup'), methods=['POST'])