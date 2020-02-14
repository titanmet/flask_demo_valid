from flask import Flask, request
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': '123',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})

def confirm_password(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError('Password not correct')


class UserForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=5, max=35),
        validators.Email
    ])
    password = StringField(label='password:', validators=[
        validators.Length(min=6, max=12)
    ])
    confirm_password = StringField(label='confirm password:', validators=[
        validators.Length(min=6, max=20), confirm_password
    ])


@app.route('/form/user', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        user_form = UserForm(request.form)
        status_output = {0: 'Valid', 1: 'Incorrect'}
        if user_form.validate():
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(user_form.errors)
            return status_check and error_list
    return 'Done !'


if __name__ == '__main__':
    app.run()
