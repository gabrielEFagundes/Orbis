from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    type = db.Column(db.Enum('worker', 'customer', name='user_types'), nullable=False)

class TripPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destiny = db.Column(db.String(200), nullable=False)
    period = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isDisponible = db.Column(db.Boolean, default=True)
    category = db.Column(db.String(100), nullable=False)
    vacancies = db.Column(db.Integer, nullable=False)
    responsable = db.Column(db.String(150), nullable=False)

class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    trip_package_id = db.Column(db.Integer, db.ForeignKey('trip_package.id'), nullable=False)
    date_reserved = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pending')
    
    user = db.relationship('User', backref=db.backref('reserves', lazy=True))
    trip_package = db.relationship('TripPackage', backref=db.backref('reserves', lazy=True))