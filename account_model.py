db = SQLAlchemy()

class Account(db.Model):
    """Class that represents an account"""

    id = db.Column(db.Int,primary_key=True)
    name=db.Column(db.String)
    email=db.Column(db.String)
    number=db.Column(db.String, nullable=True)
    disabled = db.olumn(db.Boolean(), nullable=False, default=False)
    date_joined = db.Column(db.DateTime, nullable=False)