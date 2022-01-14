from flask import Blueprint, render_template, request, redirect
from pos.models.customers import Customers
from pos.models import db

bp = Blueprint("customers",__name__)

@bp.route("/")
def index():
	return redirect("/customers")

@bp.route("/customers")
def customer_list():
	customer = Customers.query.all()
	return render_template("customers/list.html" , customers=customer)

@bp.route("/customers/add", methods=["GET","POST"])
def customers_add():
	if request.method == "GET":
		return render_template("customers/form_add.html")

	customer = Customers()
    
	customer.name = request.form['name']
	customer.nic = request.form['nic']
	customer.address = request.form['address']
	customer.contact = request.form['contact']

	db.session.add(customer)
	db.session.commit()

	return redirect("/customers")


@bp.route("/customers/update", methods=["GET","POST"])
def customers_edit():
	if request.method == "GET":
		cust_id = request.args["id"]
		customer = Customers.query.filter_by(id=cust_id).first()
		return render_template("customers/form_edit.html", customer=customer)

	cust_id = request.args["id"]
	customer = Customers.query.filter_by(id=cust_id).first()
	customer.name = request.form['name']
	customer.nic = request.form['nic']
	customer.address = request.form['address']
	customer.contact = request.form['contact']

	db.session.add(customer)
	db.session.commit()
	return redirect("/customers")

@bp.route("/customers/delete", methods=["GET"])
def customer_delete():
	cust_id = request.args["id"]
	customer = Customers.query.filter_by(id=cust_id).first()
	if customer:
		db.session.delete(customer)
		db.session.commit()
		return redirect("/customers")