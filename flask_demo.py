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



@app.route('/admin')
def hello_admin():
    return "Hello, Admin! This is the admin page"

app.run(debug=True) # with debug=True, the server will automatically reload for code changes and show a debugger in case of an error

# to change port app.run(port = 8000) first port is available port
