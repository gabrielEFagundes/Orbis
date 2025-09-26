from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange
from app import bcrypt, db
from app.models import User, TripPackage, Reserve

class UserLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def save(self):
        user = User.query.filter_by(email=self.email.data).first()

        if user:
            if bcrypt.check_password_hash(user.password, self.password.data.encode('utf-8')):
                return user;
            
            else:
                raise Exception("Wrong Password or Email!")
        
        else:
            raise Exception("No User Found!")
    
class UserSignin(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3)])
    type = SelectField('Type', choices=[('customer', 'Customer'), ('worker', 'Worker')], validators=[DataRequired()])
    submit = SubmitField('Sign In!')

    def save(self):
        password = bcrypt.generate_password_hash(self.password.data.encode('utf-8'))

        user = User(
            name = self.name.data,
            email = self.email.data,
            password = password.decode('utf-8'),
            type = self.type.data
        )

        db.session.add(user)
        db.session.commit()

        return user
    
class TripPackageForm(FlaskForm):
    destiny = StringField('Destiny', validators=[DataRequired()])
    period = DateField('Duration (Days)', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    category = StringField('Category', validators=[DataRequired()])
    vacancies = IntegerField('Vacancies', validators=[DataRequired(), NumberRange(min=1)])
    responsable = StringField('Responsable', validators=[DataRequired()])
    submit = SubmitField('Create Package')

    def save(self):
        package = TripPackage(
            destiny=self.destiny.data,
            period=self.period.data,
            price=self.price.data,
            category=self.category.data,
            vacancies=self.vacancies.data,
            responsable=self.responsable.data
        )

        db.session.add(package)
        db.session.commit()

        return package