from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "5b814a7a42fb9c2841b698b5581879c6e2981caa84c2c53635c0571478b394009402282135e26c6f928b66049117e5c44860ee4062f8566d3e83ba75942bad0b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class users(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))
    fname = db.Column(db.String(100))

    def __init__(self, email, password, fname):
        self.email = email
        self.password = password
        self.fname = fname

class entries(db.Model):
    belongsTo = db.Column(db.String(100))
    urlSafeTitle = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.String(10))
    title = db.Column(db.String(100))
    password = db.Column(db.String(100))
    body = db.Column(db.String(1000000))

    def __init__(self, belongsTo, urlSafeTitle, date, title, password, body):
        self.belongsTo = belongsTo
        self.urlSafeTitle = urlSafeTitle
        self.date = date
        self.title = title
        self.password = password
        self.body = body


class config:
    HOST = "localhost"
    PORT = 8080
    DEBUG = True

@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

@app.route("/")
def main():
    if "loggedIn" in session and "email" in session:
        email = session["email"]
        entryList = entries.query.filter_by(belongsTo=email).all()
        entryList = [entry.title for entry in entryList]
        user = users.query.filter_by(email=email).first()
        return render_template("main.html", fname=user.fname, entries=entryList)
    else:
        return redirect("/login")

@app.route("/login", methods=["post", "get"])
def login():
    error = False
    if "email" in session:
        email = session["email"]
    else:
        email = ""
    if "loggedIn" in session and "email" in session:
        return redirect("/")
    if request.method == "POST":
        email = request.form["email"].strip()
        password = request.form["password"].strip()
        try:
            user = users.query.filter_by(email=email).first()
            if user.email == email and user.password == password:
                session["loggedIn"] = True
                session["email"] = email
                return redirect("/")
            else:
                error = True
        except:
            error = True
    return render_template("login.html", error=error, email=email)

@app.route("/logout")
def logout():
    if "loggedIn" in session and "email" in session:
        session.pop("loggedIn", None)
        return redirect("/login")
    else:
        return redirect("/404")

@app.route("/forget")
def forget():
    session.clear()
    return redirect("/login")

@app.route("/signup", methods=["post", "get"])
def signup():
    error = False
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"].strip()
        fname = request.form["fname"].strip().capitalize()
        user = users(email, password, fname)
        try:
            db.session.add(user)
            db.session.commit()
            session["email"] = email
            return redirect("/login")
        except:
            error = True
    return render_template("signup.html", error=error)

@app.route("/new_entry", methods=["post", "get"])
def new_entry():
    if "loggedIn" in session and "email" in session:
        if request.method == "POST":
            belongsTo = session["email"]
            date = request.form["date"]
            title = request.form["title"].strip()
            password = request.form["password"].strip()
            body = request.form["body"].strip()
            entry = entries(belongsTo, title.replace(" ", "-").lower(), date, title, password, body)
            db.session.add(entry)
            db.session.commit()
        return render_template("new_entry.html")
    else:
        return redirect("/404")

@app.route("/fetch_entry/<entryTitle>")
def fetch_entry(entryTitle):
    if "loggedIn" in session and "email" in session:
        entry = entries.query.filter_by(urlSafeTitle=entryTitle).first()
        return render_template("fetch_entry.html", entry=entry)
    else:
        return redirect("/404")

# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
