from flask import Blueprint, render_template, request, redirect, url_for, session
from app.decorators import login_required

honeypot_routes = Blueprint("honeypot", __name__)

@honeypot_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        session["logged_in"] = True
        session["username"] = username

        if username == "admin" or password == "admin":
            return redirect(url_for("honeypot.admin"))
        else:
            return redirect(url_for("honeypot.index", username=username))
        
    return render_template("login.html") 

@honeypot_routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("honeypot.login"))

@honeypot_routes.route("/")
@login_required
def index():
    return render_template("index.html") 

@honeypot_routes.route("/admin")
@login_required
def admin():
    return render_template("admin.html")

@honeypot_routes.route("/search")
@login_required
def search():
    query = request.args.get("q", "")
    return render_template("search.html", query=query)

@honeypot_routes.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    return render_template("upload.html")