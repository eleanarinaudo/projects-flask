from wtforms import Form, StringField, validators
from wtforms_validators import AlphaNumeric

class SearchProfileForm(Form):
    username = StringField(
        'Username', [validators.required(), validators.Length(min=3, max=25), AlphaNumeric(message="Must only contain alphanumeric characters")])
