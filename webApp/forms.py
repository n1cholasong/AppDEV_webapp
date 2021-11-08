from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')

    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=8, max=15), validators.DataRequired()])
    confirm_password = PasswordField('Confirm Password', [validators.EqualTo('password', message='Password do not match!'), validators.DataRequired()])

    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default=None)
    remarks = TextAreaField('Remarks', [validators.Optional()])
