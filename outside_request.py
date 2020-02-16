from flask import Flask, request
import os

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    #SECRET_KEY=os.environ['S'],
    WTF_CSRF_ENABLED=False,
)
app.config['DEBUG'] = True
# app.config['SECRET_KEY'] = os.environ['S']


@app.route('/', methods=['GET', 'POST'])
def home():
    # x = 5 / 0
    return 'hello world!', 200

#print(request, type(request), request.method)

with app.test_request_context('/'):
    print(request, type(request), request.method)


if __name__ == '__main__':
    app.run()
