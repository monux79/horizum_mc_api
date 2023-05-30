from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Define the list of authorized users
users = {
    "admin": "password",
    "user": "password2"
}

# Define the authentication function
@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username

# Define a protected endpoint
@app.route('/api')
@auth.login_required
def api():
    return 'Hello, world!'

