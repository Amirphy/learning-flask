from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "this is home page"

@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method== "POST":
        #username = request.args.get("username")
        #email= request.args.get("Email")
#here i used Get methodes and test it. i changed my methodes
        username= request.form['username']
        email= request.form['Email']

    return f"username:{username} & email:{email}" 

if __name__ == "__main__":
    app.run(debug = True)







