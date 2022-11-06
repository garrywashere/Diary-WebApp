from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "5b814a7a42fb9c2841b698b5581879c6e2981caa84c2c53635c0571478b394009402282135e26c6f928b66049117e5c44860ee4062f8566d3e83ba75942bad0b"

class config:
    HOST = "localhost"
    PORT = 8080
    DEBUG = True
    FNAME = "garry"

@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

@app.route("/")
def main():
    if "loggedIn" in session and "email" in session:
        return render_template("main.html", fname=config.FNAME.capitalize())
    else:
        return redirect("/login")

@app.route("/login", methods=["post", "get"])
def login():
    error = False
    email = ""
    if "loggedIn" in session and "email" in session:
        return redirect("/")
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            remember = True if request.form["remember"] == "on" else False
        except:
            remember = False
        if email == "garry@garrynet.co.uk" and password == "garry53":
            session["loggedIn"] = True
            session["email"] = email
            return redirect("/")
        else:
            error = True
    return render_template("login.html", error=error, email=email)

@app.route("/logout")
def logout():
    if "loggedIn" in session and "email" in session:
        session.pop("loggedIn", None)
        return redirect("/login")
    else:
        return "Error: not logged in dumbass..."

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
