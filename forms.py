from flask_wtf import FlaskForm
from flask_wtf.recaptcha import widgets
from wtforms import PasswordField, SubmitField, BooleanField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class Formlogin(FlaskForm):
    username = EmailField('USERNAME', [DataRequired(message='User required'), Email()])
    password = PasswordField('PASSWORD')
    checkbox = BooleanField('Remember my password')
    button = SubmitField('Log in')

class FormSignin(FlaskForm):
    name = TextField('Name',render_kw={"placeholder": "Name"})
    lastname = TextField('Lastname', render_kw={"placeholder":'Lastname'})
    email = EmailField('Email', [DataRequired(message='User required'), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password',  render_kw={"placeholder": "Password"})
    confirmpassword = PasswordField('Confirm Password', render_kw={"placeholder": "Confirm Password"})
    agreement = BooleanField('Agree with terms and conditions')
    checkbox = BooleanField('Remember my password')
    button = SubmitField('Sing in')