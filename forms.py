from flask_wtf import FlaskForm
from flask_wtf.recaptcha import widgets
from wtforms import PasswordField, SubmitField, BooleanField, TextField, RadioField, FileField
from wtforms.fields.html5 import DecimalField, EmailField
from wtforms.validators import DataRequired, Email
from markupsafe import Markup

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

class FormSearch(FlaskForm):
    searchbar = TextField('Searchbar', render_kw={"placeholder": "Search product, mark and category..."})
    Searchicon = Markup('<i class= fas fa-search></i>')
    button = SubmitField(Searchicon)

class FormBuy(FlaskForm):
    button = SubmitField('Buy')
    comment = TextField('Name',render_kw={"placeholder": "write a comment..."})
    radio = RadioField('Star', choices=[1,2,3,4,5])

class FormAddproduct(FlaskForm):
    image = FileField('Image')
    product = TextField('Product name',render_kw={"placeholder": "Product name"})
    price = DecimalField('Price',render_kw={"placeholder": "Price"})
    product_description = TextField('Product description',render_kw={"placeholder": "Product description"})
    add_product = SubmitField('Add Product')