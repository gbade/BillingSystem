import datetime

from app.main import db
from app.main.models.user import User

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            first_name = data['first_name'],
            last_name = data['last_name'],
            user_name = data['user_name'],
            email=data['email'],
            password=data['password'],
            confirmation_code = data['confirmation_code'],
            confirmation_time= data['confirmation_time'],
            insert_ts = datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def get_user_group(data):
    user = get_a_user(id)

    if not user:
        response_object = {
           'status': 'fail',
           'message':'The user does not exist.' 
        }
        return response_object, 400
    else:
        

    user_group = 


def save_changes(data):
    db.session.add(data)
    db.session.commit()