from flask import Flask

app = Flask(__name__)


@app.route('/hello/<user>')
def home(user):
    return 'Hello user:' + user


@app.route('/summ/<int:x>/<int:y>')
def home1(x, y):
    return 'Summa x + y = {}'.format(x+y)


@app.route('/concat/<str1>/<str2>/<str3>')
def home2(str1,str2,str3):
    if len(str1)>len(str2) and len(str1)>len(str3):
        return str1
    elif len(str2)>len(str1) and len(str2)>len(str3):
        return str2
    elif len(str3)>len(str1) and len(str3)>len(str2):
        return str3


if __name__ == '__main__':
    app.run()
