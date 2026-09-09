from flask import Flask, request

app = Flask(__name__)

DATABASE_PASSWORD = "Bank12345!"

@app.route("/user")
def user():
    username = request.args.get("username")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query
