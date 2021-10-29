from flask import Flask, render_template
from patterns import patterns

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', patterns=patterns)


@app.route('/snapshot')
def snapshot():
    return {
        'code': 'success'
    }