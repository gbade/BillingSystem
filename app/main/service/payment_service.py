import datetime

from app.main import db
from app.main.models.subscriptions import Subscription, PlanHistory, Invoice
from app.main.models.user import User, UserGroup, InGroup, UserGroupType

def get_customer_invoice(account_id):
    customer = get_a_user(account_id)

    if not customer:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return response_object, 404
    else:
        in_group = get_user_ingroup(customer.id)

        if not in_group:
            response_object = {
                'status': 'fail',
                'message': 'in group data does not exist'
            }
            return response_object, 404
        else:
            usr_group = get_usergroup_of_customer(in_group.user_group_id)

            #get the type_name
            usr_group_type = get_usergroup_type(usr_group.user_group_type_id) 

            #gets subscription
            user_subscription = get_user_subscription(usr_group.id)

            payment = []
            
            payment_details = db.session.query(Invoice, Subscription) \
                                        .filter(Invoice.subscription_id == user_subscription.id) \
                                        .all()
            
            for invoice, subscription in payment_details:
                customer_invoice = {
                    'date_subscribed': subscription.date_subscribed,
                    'valid_to': subscription.valid_to,
                    'invoice_period_start_date': invoice.invoice_period_start_date,
                    'invoice_period_end_date': invoice.invoice_period_end_date,
                    'invoice_description': invoice.invoice_description,
                    'invoice_amount': invoice.invoice_amount,
                    'invoice_created': invoice.invoice_created,
                    'invoice_due': invoice.invoice_due,
                    'invoice_paid': invoice.invoice_paid
                }

                payment.append(customer_invoice)

            response_object = {
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'user_name': customer.user_name,
                'email': customer.email,
                'user_group_type_name': usr_group_type.type_name,
                'payment_details': payment
            }
            return response_object, 201 


def create_subscription(data):
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return response_object, 404
    else:
        in_group = get_user_ingroup(user.id)
        usergroup = get_usergroup_of_customer(in_group.usergroup_id)

        if not in_group:
            response_object = {
                'status': 'fail',
                'message': 'in group data does not exist'
            }
            return response_object, 404

        #complete this in the morning
        new_subscription = Subscription(
            user_group_id = usergroup.id,
            trial_period_start_date = data['trial_period_start_date'],
            trial_period_end_date = data['trial_period_end_date'],
            subscribe_after_trial = data['subscribe_after_trial'],
            current_plan_id = data,
            offer_id = some_id,
            offer_start_date = data['offer_start_date'],
            offer_end_date = data['offer_end_date'],
            date_subscribed = data['date_subscribed'],
            valid_to = data['valid_to'],
            date_unsubscribed = data['date_unsubscribed'],
            insert_ts = datetime.datetime.utcnow()
        )
        save_changes(new_subscription)

        response_object = {
            'status': 'success',
            'status_code': 00,
            'message': 'Successfully created.'
        }

        return response_object, 201


def get_user_ingroup(user_id):
    return InGroup.query.filter_by(user_account_id = user_id).first()

def get_usergroup_of_customer(usergroup_id):
    return UserGroup.query.filter_by(user_group_id = usergroup_id).first()

def get_usergroup_type(group_type_id):
    return UserGroupType.query.filter_by(user_group_type_id = group_type_id).first()

def get_a_user(id):
    return User.query.filter_by(id=id).first()

def get_user_subscription(id):
    return Subscription.query.filter_by(user_group_id = id)

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_user(data):
    db.session.delete(data)
    db.session.commit()

def update_data(data):
    db.session.update(data)
    db.session.commit()