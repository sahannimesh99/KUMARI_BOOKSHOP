from flask import Blueprint, render_template, request, redirect
from pos.models.emploees import Emploees
from pos.models import db

bp = Blueprint("emploees",__name__)

@bp.route("/")
def index():
	return redirect("/emploees")

@bp.route("/emploees")
def employee_list():
	employee = Emploees.query.all()
	return render_template("emploees/list.html" , emploees=employee)

@bp.route("/emploees/add", methods=["GET","POST"])
def emploees_add():
	if request.method == "GET":
		return render_template("emploees/form_add.html")

	employee = Emploees()
    
	employee.name = request.form['name']
	employee.nic = request.form['nic']
	employee.address = request.form['address']
	employee.contact = request.form['contact']

	db.session.add(employee)
	db.session.commit()

	return redirect("/emploees")


@bp.route("/emploees/update", methods=["GET","POST"])
def emploees_edit():
	if request.method == "GET":
		emp_id = request.args["id"]
		employee = Emploees.query.filter_by(id=emp_id).first()
		return render_template("emploees/form_edit.html", employee=employee)

	emp_id = request.args["id"]
	employee = Emploees.query.filter_by(id=emp_id).first()
	employee.name = request.form['name']
	employee.nic = request.form['nic']
	employee.address = request.form['address']
	employee.contact = request.form['contact']

	db.session.add(employee)
	db.session.commit()
	return redirect("/emploees")

@bp.route("/emploees/delete", methods=["GET"])
def emploees_delete():
	emp_id = request.args["id"]
	employee = Emploees.query.filter_by(id=emp_id).first()
	if employee:
		db.session.delete(employee)
		db.session.commit()
		return redirect("/emploees")