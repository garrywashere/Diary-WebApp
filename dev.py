from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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
    return render_template("main.html", fname=config.FNAME.capitalize())

@app.route("/login", methods=["post", "get"])
def login():
    error = False
    email = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        try:
            remember = True if request.form["remember"] == "on" else False
        except:
            remember = False
        if email == "garry@garrynet.co.uk" and password == "garry53":
            return redirect("/")
        else:
            error = True
    return render_template("login.html", error=error, email=email)

@app.route("/logout")
def logout():
    return redirect("/login")

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
