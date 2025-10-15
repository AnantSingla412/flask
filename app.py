from flask import Flask


# intialize the Flask application
app = Flask(__name__)

#url biding
@app.route('/')
def hello():
    return "Hello, World!"

app.run()