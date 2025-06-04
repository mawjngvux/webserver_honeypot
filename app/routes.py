from flask import Blueprint, render_template, request, redirect, url_for, session, send_from_directory
from app.decorators import login_required
from app.alert import send_discord_alert
from logging_system.loggers.log_request import log_request
from config.config import Config
from app.utils import allowed_file
import os
from werkzeug.utils import secure_filename

honeypot_routes = Blueprint("honeypot", __name__)

@honeypot_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        session["logged_in"] = True
        session["username"] = username

        if username == "admin" or password == "admin":
            send_discord_alert("Admin is logged in!")
            return redirect(url_for("honeypot.admin"))
        else:
            send_discord_alert(f"User {username} is logged in")
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
    filename = None
    if request.method == "POST":
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(Config.UPLOAD_DIR, filename))
    return render_template("upload.html", filename=filename)

@honeypot_routes.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join("..", Config.UPLOAD_DIR), filename)

@honeypot_routes.after_request
def log_all_request(response):
    log_request(request, response.status_code)
    return response