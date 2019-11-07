from .. import db, flask_bcrypt

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user_account"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    confirmation_code = db.Column(db.String(255), nullable=False)
    confirmation_time = db.Column(db.DateTime, nullable=True)
    insert_ts = db.Column(db.DateTime)
    

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.user_name)


class DeleteUser(db.Model):
    """model to store list of deactivated users"""
    __tablename__ = "deactivated_users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_account_id = db.Column(db.Integer, nullable=False)
    in_group_id = db.Column(db.Integer, db.ForeignKey('in_group.id'), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=False)

class InGroup(db.Model):
    """In Group model to store a list of all members of a group"""
    __tablename__ = "in_group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_group.id'), nullable=False)
    user_account_id = db.Column(db.Integer, db.ForeignKey('user_account.id'), nullable=False)
    time_added = db.Column(db.DateTime,  nullable=False)
    time_removed = db.Column(db.DateTime,  nullable=True)
    group_admin = db.Column(db.Boolean, nullable=False)


class UserGroup(db.Model):
    """User Group model - 
    table referencing the selected group type"""
    __tablename__ = "user_group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_group_type_id = db.Column(db.Integer, db.ForeignKey('user_group_type.id'), nullable=False)
    customer_invoice_data = db.Column(db.Text, nullable=False)
    insert_ts = db.Column(db.DateTime, nullable=False)

class UserGroupType(db.Model):
    """User Group Type model - 
    Users can create groups; groups have predefined types.
    A list of all possible group types is stored in the user_group_type table"""
    __tablename__ = "user_group_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(128), nullable=False)
    members_min = db.Column(db.Integer, nullable=False)
    members_max = db.Column(db.Integer, nullable=False)

