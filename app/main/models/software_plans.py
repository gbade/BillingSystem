from .. import db, flask_bcrypt

class Software(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "software"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    software_name = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text, nullable=True)
    access_link = db.Column(db.Text, nullable=False)


class Option(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "option"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    option_name = db.Column(db.String(255), nullable=False)

class OptionIncluded(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "option_included"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    date_removed = db.Column(db.DateTime, nullable=True)

class Plan(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "plan"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_name = db.Column(db.String(255), nullable=False)
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'), nullable=False)
    user_group_type_id = db.Column(db.Integer, db.ForeignKey('user_group_type.id'), nullable=False)
    current_price = db.Column(db.Boolean, nullable=False)
    insert_ts = db.Column(db.DateTime, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

class Include(db.Model):
    """ Model for storing invoice of payments """
    __tablename__ = "include"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)

class Prerequisite(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "prerequisite"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)

class Offer(db.Model):
    """ Subscription Model for storing invoice of payments """
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    offer_name = db.Column(db.String(255), nullable=False)
    offer_start_date = db.Column(db.DateTime, nullable=False)
    offer_end_date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.Text, nullable=False)
    discount_amount = db.Column(db.Numeric(8,2), nullable=True)
    discount_percentage = db.Column(db.Numeric(5,2), nullable=True)
    duration_months = db.Column(db.Integer, nullable=True)
    duration_end_date = db.Column(db.DateTime, nullable=True)