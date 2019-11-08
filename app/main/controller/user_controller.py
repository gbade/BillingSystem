from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto, DeleteUserResponse, SaveUserGroupDto
from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.user_service import save_user_group, deactivate_user_account

api = UserDto.api
dea = DeleteUserResponse.api
usg = SaveUserGroupDto.api

_user = UserDto.user
_deactivated = DeleteUserResponse.deactivated_users
_user_group = SaveUserGroupDto.group_model


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)



@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/<email>')
@api.param('email', 'user identifier')
@api.response(404, 'user not found.')
class DeleteUser(Resource):
    @api.response(201, 'User successfully deactivated.')
    @api.doc('deactivate a user')
    @api.marshal_with(_deactivated)
    def delete(self, email):
        """deactivate a user account given its identifier"""
        return deactivate_user_account(email)


@api.route('/user_group')
class UserGroup(Resource):
    @api.response(201, 'User group successfully created.')
    @api.expect(_user_group, validate=True)
    @api.doc('create a new user group')
    def post(self):
        """Creates a new user group """
        data = request.json
        return save_user_group(data=data)