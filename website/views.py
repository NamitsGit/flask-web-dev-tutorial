from flask import Blueprint, redirect, render_template, request
from .models import Student
from website import db
from datetime import date

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html"), 201

@views.route("/students")
def view_students():
    return render_template("students.html")

@views.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        f_name = request.form.get("firstName")
        l_name = request.form.get("lastName")
        sex = request.form.get("sex")
        dob = date(int(request.form.get("dobYear")), int(request.form.get("dobMonth")), int(request.form.get("dobDay")))
        phone = request.form.get("phone")
        email = request.form.get("email")

        student = Student(first_name=f_name, last_name=l_name, sex=sex, dob=dob, regd_phone_no=phone, regd_email=email)
        db.session.add(student)
        db.session.commit()
        return redirect("/student-add-success")
    if request.method == "GET":
        return render_template("students.html")
    
@views.route("/student-add-success")
def add_student_success():
    return render_template("student_add_success.html")