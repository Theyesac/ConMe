from wtforms import Form, BooleanField, PasswordField, SubmitField, TextField, validators

restricted_names = ['register', 'login', 'logout', 'admin', 'root', 'index']

class RegistrationForm(Form):
	name         = TextField(u'Username', [validators.Length(min=4, max=25),
		validators.NoneOf(restricted_names, message=u'The name you have choosen is restricted.', values_formatter=None)])
	password     = PasswordField(u'Password', [validators.Length(min=4, max=25)])
	email        = TextField(u'Email Address', [validators.Length(min=6, max=35)])
	accept_rules = BooleanField(u'I accept the site rules', [validators.Required()])
	submit       = SubmitField(u'Submit')

class LoginForm(Form):
	name         = TextField(u'Username', [validators.Length(min=4, max=25)])
	password     = PasswordField(u'Password', [validators.Length(min=4, max=25)])
	submit       = SubmitField(u'Submit')
