# views.py
import os
from flask import url_for, request, render_template, redirect, flash
from werkzeug.utils import secure_filename
from app import app

app.secret_key = b'\xbf/q|vow\xca>\x13\xc8k\x8a\x8e\x99\x15'
UPLOAD_DIR = "upload-data"
UPLOAD_BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
ALLOWED_EXTENSIONS = set(['gpx'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("show.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Validate uploaded file
        if 'gpx-file' not in request.files:
            flash("No file uploaded", "error")
            return redirect(request.url)
        gpx_file = request.files['gpx-file']
        if gpx_file.filename == '':
            flash("No file selected", "error")
            return redirect(request.url)
        if not allowed_file(gpx_file.filename):
            flash("Only .gpx files supported!", "error")
            return redirect(request.url)

        # Store gpx file in filesystem
        gpx_filename = secure_filename(gpx_file.filename)
        gpx_fspath = os.path.join(UPLOAD_BASE_DIR, UPLOAD_DIR, gpx_filename)
        os.makedirs(os.path.dirname(gpx_fspath), exist_ok=True)
        gpx_file.save(gpx_fspath)

        flash("Track added sucessfully.", "info")
        return redirect(url_for("index"))
    else:
        return render_template("add.html")
