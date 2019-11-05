from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='REST API AUTH WITH JWT',
          version='1.0',
          description='an api for a billing system'
          )

api.add_namespace(user_ns, path='/user')