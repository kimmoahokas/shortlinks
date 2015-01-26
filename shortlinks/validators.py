from wtforms import Form, StringField, validators

class LinkForm(Form):
    link = StringField('Url to shorten',
                      validators=[validators.InputRequired(),
                                  validators.Length(min=5, max=256),
                                  validators.URL()])
