from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms import validators
 
class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name!")])
    email = TextField("Email", [validators.Required("Please enter email!")])
    subject = TextField("Subject", [validators.Required("Please enter subject!")])
    message = TextAreaField("Message", [validators.Required("Please enter Message")])
    submit = SubmitField("Send")