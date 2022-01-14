from flask import Blueprint, render_template, request, redirect
from pos.models.products import Products
from pos.models.transactions import Transactions
from pos.models.transactions_products import TransactionProducts
from pos.models import db

bp = Blueprint("transactions",__name__)

@bp.route("/transactions")
def transactions_list():
	transactions = Transactions.query.all()
	return render_template("transactions/list.html",transactions=transactions)

@bp.route("/transactions/add", methods=["GET","POST"])
def transactions_add():
	if request.method == "POST":
		
		products = request.form.getlist("products")
		products_qty = request.form.getlist("products_qty")

		transactions = Transactions()
		db.session.add(transactions)
	
		db.session.flush()

		for i, product in enumerate(products):
			
			transactions_products = TransactionProducts()
			transactions_products.transaction_id = transactions.id
			transactions_products.product_id = int(product)
			transactions_products.product_qty = int(products_qty[i])
			result = db.session.query(Products).filter(Products.id == product).all()
			db.session.add(transactions_products)
			db.session.flush()

		db.session.commit()
		return redirect("/transactions")
	return render_template("transactions/form_add.html")