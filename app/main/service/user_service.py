import datetime

from app.main import db
from app.main.models.user import User, UserGroup, InGroup, DeleteUser

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
            'message': 'User already exists. Please Log in.'
        }
        return response_object, 409

def save_user_group(data):
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return response_object, 404
    else:
        user_group = UserGroup(
            user_group_type_id = data['user_group_type_id'],
            customer_invoice_data = data['customer_invoice_data'],
            insert_ts = datetime.datetime.utcnow()
        )
        save_changes(user_group)

        usergroup = get_user_group(user_group.id)

        in_group = InGroup(
            user_group_id = usergroup.id,
            user_account_id = user.id,
            time_added = usergroup.insert_ts,
            time_removed = None,
            group_admin = data['group_admin']
        )
        save_changes(in_group)
        
        response_object = {
            'status': 'success',
            'message': 'Successfully added user group.'
        }
        return response_object, 201


def update_in_group(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return response_object, 404
    else:
        user_group = UserGroup.query.filter_by(user_account_id=user.id).first()

        in_group= InGroup(
            user_group_id = user_group.id,
            user_account_id = user.id,
            time_added = usrgroup.insert_ts,
            time_removed = data['time_removed'],
            group_admin = data['group_admin']
        )

        update_data(in_group)

        response_object = {
            'status': 'success',
            'status_code': 00,
            'message': 'Successfully updated in group.'
        }
        return response_object, 201



def deactivate_user_account(user_email):
    user = User.query.filter_by(email = user_email).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return response_object, 404
    else:
        in_group_data = InGroup.query.filter_by(user_account_id = user.id).first()

        deactivated_user = DeleteUser(
            in_group_id = in_group_data.id,
            user_account_id = user.id,
            first_name = user.first_name,
            last_name = user.last_name,
            user_name = user.user_name,
            password = user.password,
            email = user.email,
            deleted_at = datetime.datetime.utcnow()
        )
        
        save_changes(deactivated_user)

        delete_user(user)

        response_object = {
            'status': 'success',
            'status_code': 00,
            'message': 'User successfully deactivated.'
        }

        return response_object, 201


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
        
""" retreive user group data """
def get_user_group(user_group_id):
    return UserGroup.query.filter_by(id = user_group_id).first() 
    

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_user(data):
    db.session.delete(data)
    db.session.commit()

def update_data(data):
    db.session.update(data)
    db.session.commit()