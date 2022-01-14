from flask import Blueprint, render_template, request, redirect
from pos.models.suppliers import Suppliers
from pos.models import db

bp = Blueprint("suppliers",__name__)

@bp.route("/")
def index():
	return redirect("/suppliers")

@bp.route("/suppliers")
def supplier_list():
	supplier = Suppliers.query.all()
	return render_template("suppliers/list.html" , suppliers=supplier)

@bp.route("/suppliers/add", methods=["GET","POST"])
def suppliers_add():
	if request.method == "GET":
		return render_template("suppliers/form_add.html")

	suppliers = Suppliers()
    
	suppliers.name = request.form['name']
	suppliers.proName = request.form['proName']
	suppliers.nic = request.form['nic']
	suppliers.address = request.form['address']
	suppliers.contact = request.form['contact']

	db.session.add(suppliers)
	db.session.commit()

	return redirect("/suppliers")


@bp.route("/suppliers/update", methods=["GET","POST"])
def suppliers_edit():
	if request.method == "GET":
		sup_id = request.args["id"]
		supplier = Suppliers.query.filter_by(id=sup_id).first()
		return render_template("suppliers/form_edit.html", supplier=supplier)

	sup_id = request.args["id"]
	supplier = Suppliers.query.filter_by(id=sup_id).first()
	supplier.name = request.form['name']
	supplier.proName = request.form['proName']
	supplier.nic = request.form['nic']
	supplier.address = request.form['address']
	supplier.contact = request.form['contact']

	db.session.add(supplier)
	db.session.commit()
	return redirect("/suppliers")

@bp.route("/suppliers/delete", methods=["GET"])
def supplier_delete():
	sup_id = request.args["id"]
	supplier = Suppliers.query.filter_by(id=sup_id).first()
	if supplier:
		db.session.delete(supplier)
		db.session.commit()
		return redirect("/suppliers")