from flask import Flask, request
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

app = Flask(__name__)


def confirm_password(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError('Password not correct')

class UserForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=5, max=35),
        validators.Email()
    ])
    password = StringField(label='password:', validators=[
        validators.Length(min=6, max=12)
    ])
    confirm_password = StringField(label='confirm password:', validators=[
        validators.Length(min=6, max=20), confirm_password
    ])


@app.route('/form/user', methods=['GET', 'POST'])
def post_data():
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


@app.route('/hello/<user>')
def home(user):
    return 'Hello user:' + user


@app.route('/summ/<int:x>/<int:y>')
def home1(x, y):
    return 'Summa x + y = {}'.format(x + y)


@app.route('/concat/<str1>/<str2>/<str3>')
def home2(str1, str2, str3):
    if len(str1) > len(str2) and len(str1) > len(str3):
        return str1
    elif len(str2) > len(str1) and len(str2) > len(str3):
        return str2
    elif len(str3) > len(str1) and len(str3) > len(str2):
        return str3


@app.route('/locales', methods=['GET', 'POST'])
def locales():
    my_loc = {'ru': 'russian', 'en': 'english', 'it': 'italy'}
    return jsonify(my_loc)


@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    return 'Summa : {}'.format(x + y)


@app.route('/greet/<user_name>')
def greet(user_name):
    return 'Hello , {} !'.format(user_name)


if __name__ == '__main__':
    app.run()
