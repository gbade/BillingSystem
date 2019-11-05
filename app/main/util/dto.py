from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'user_name': fields.String(required=True, description='user username'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'confirmation_code': fields.String(description='user confirmation code'),
        'confirmation_time': fields.DateTime(description='user confirmation time')
    })


class UserGroupDto:
    api = Namespace('user_group', description='User group')
    user_group= api.model('user_group', {

    })


class InGroupDto:
    api = Namespace('in_group', description='Store a list of all group members of a user account')
    in_group = api.model('in_group', {
        'user_group_id': fields.Integer(required=True, description='user first name'),
        'user_account_id': fields.Integer(required=True, description='user account id'),
        'time_added': fields.DateTime(required=True, description='user username'),
        'time_removed': fields.DateTime(required=True, description='user username'),
        'group_admin': fields.Boolean(required=True, description='user username'),
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class DeleteUserDto:
    api = Namespace('deactivated_users', description='List of users deactivated')
    deactivated_users = api.model('deactivated_users', {
        'in_group_id': fields.Integer(required=True, description='in group id'),
        'user_account_id': fields.Integer(required=True, description='user account id'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'user_name': fields.String(required=True, description='user username'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
        'deleted_at': fields.DateTime(required=True, description='time account was deactivated')
    })