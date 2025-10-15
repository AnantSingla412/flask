from flask import Flask


# intialize the Flask application
app = Flask(__name__)

#url biding
@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/page2')
def hello_2():
    return "Hello, World! This is page 2"

app.run()