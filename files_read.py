import os
from flask import Flask


app = Flask(__name__)


@app.route('/serve/<path:filename>', methods =['GET', 'POST'])
def show_file(filename):
    if not os.path.exists('./files/' + filename):
        return '404: File doesnt exist'
    else:
        opened_file = open('./files/' + filename, 'r')
        read_file = opened_file.read()
        opened_file.close()
    return read_file


if __name__ == '__main__':
    app.run()