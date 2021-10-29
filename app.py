from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/snapshot')
def snapshot():
    return {
        'code': 'success'
    }