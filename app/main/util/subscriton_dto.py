from flask_restplus import Namespace, fields

class CustomerInvoiceResponse:
    api = Namespace('customer_invoice', description='payment details of customer transactions')
    customer_invoice = api.model('customer_invoice', {
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'user_name': fields.String(required=True, description='user username'),
        'email': fields.String(required=True, description='user email address'),
        'user_group_type_name': fields.String(required=True, description='user password'),
        'customer_invoice_data': fields.String(description='user confirmation code'),
        'date_subscribed': fields.DateTime(description='date of subscription'),
        'valid_to': fields.DateTime(description='expiration date'),
        'invoice_period_start_date': fields.DateTime(description='user confirmation time'),
        'invoice_period_end_date': fields.DateTime(description='user confirmation time'),
        'invoice_description': fields.String(description='user confirmation time'),
        'invoice_amount': fields.Decimal(description=''),
        'invoice_created': fields.DateTime(description='user confirmation time'),
        'invoice_due': fields.DateTime(description='user confirmation time'),
        'invoice_paid': fields.DateTime(description='user confirmation time'),
    })