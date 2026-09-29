from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "hello flask"

@app.route("/user/<username>")
def user(username):
    if username == "admin":
        return redirect(url_for('admin'))
    else:
        # comment: fo adding for users
        return redirect(url_for('users', username= username))


@app.route("/admin/")
def admin():
    return "hello admin"

@app.route("/users/<username>")
def users(username):
    return f"hello user {username}"




if __name__ == "__main__":
    app.run(debug= True)

