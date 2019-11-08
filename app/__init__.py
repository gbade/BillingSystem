from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.user_controller import dea as user_dea
from .main.controller.user_controller import usg as user_grp

blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title='REST API AUTH WITH JWT',
          version='1.0',
          description='an api for a billing system'
          )

register = Blueprint('dea', __name__)
dea = Api(register)

reg_usrgrp = Blueprint('usg', __name__)
usg = Api(reg_usrgrp)

api.add_namespace(user_ns, path='/user')
api.add_namespace(user_dea, path='/deactivate_user')
api.add_namespace(user_grp, path='/user_group')