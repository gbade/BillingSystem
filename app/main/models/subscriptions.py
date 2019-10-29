from .. import db, flask_bcrypt

class PlanHistory(db.Model):
    """ Plan History Model for storing user plan changes """
    __tablename__ = "plan_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    insert_ts = db.Column(db.DateTime, nullable=False)


class Subscription(db.Model):
    """ Subscription Model for storing user subscriptions """
    __tablename__ = "subscription"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_group.id'), nullable=False)
    trial_period_start_date = db.Column(db.DateTime, nullable=True)
    trial_period_end_date = db.Column(db.DateTime, nullable=True)
    subscribe_after_trial = db.Column(db.Boolean, nullable=False)
    current_plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'), nullable=True)
    offer_start_date = db.Column(db.DateTime, nullable=True)
    offer_end_date = db.Column(db.DateTime, nullable=True)
    date_subscribed = db.Column(db.DateTime, nullable=False)
    valid_to = db.Column(db.DateTime, nullable=False)
    date_unsubscribed = db.Column(db.DateTime, nullable=True)
    insert_ts = db.Column(db.DateTime, nullable=False)


class Invoice(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "invoice"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_invoice_data = db.Column(db.Text, nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    plan_history_id = db.Column(db.Integer, db.ForeignKey('plan_history.id'), nullable=False)
    invoice_period_start_date = db.Column(db.DateTime, nullable=False)
    invoice_period_end_date = db.Column(db.DateTime, nullable=False)
    invoice_description =  db.Column(db.String(255), nullable=False)
    invoice_amount = db.Column(db.Numeric(8,2), nullable=False)
    invoice_created_ts = db.Column(db.DateTime, nullable=False)
    invoice_due_ts = db.Column(db.DateTime, nullable=False)
    invoice_paid_ts = db.Column(db.DateTime, nullable=True)
