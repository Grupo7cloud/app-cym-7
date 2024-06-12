from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")
    
@app.route ("/register_page")
def register_page():
    return render_template("register.html")
    
@app.route("/register_user", methods=["post"])
def register_user():
    id = request.form["id"]
    Name = request.form["Name"]
    Last_Name = request.form["Last_Name"]
    Birthday = request.form["Birthday"]
    print(id, Name, Last_Name, Birthday)
    return "ok"

if __name__ == "__main__":
    host = '0.0.0.0'
    port = '8080'
    app.run(host, port)

