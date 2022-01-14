# from flask import Blueprint, render_template, request, redirect
# from pos.models import privilage
# from pos.models.privilage import Privilage
# from pos.models import db

# bp = Blueprint("privilage",__name__)

# @bp.route("/")
# def index():
# 	return redirect("/privilages")

# @bp.route('/privilage/login', methods=['GET', 'POST'])
# def login():
#     form = request.form
#     for account in privilage:
#         if form['holderName'] == account['holderName'] and form['holderName'] == account['holderName']:
#             return redirect('base.html')
#     context = {
#         'error': 'Invalid username or password.'
#     }
#     return render_template('landingpage.html', **context)


# @bp.route('/privilage/signup', methods=['GET', 'POST'])
# def signup():
#     context = {}
#     form = request.form
#     for account in privilage:
#         if form['holderName'] == account['holderName']:
#             context['error'] = 'Username already exists'
#             return render_template('landingpage.html', **context)
#     if form['holderName'] is None:
#         context['error'] = 'Invalid username'
#         return render_template('landingpage.html', **context)
#     if form['password'] is None:
#         context['error'] = 'Invalid password'
#         return render_template('landingpage.html', **context)
#     privilage.append({
#         'holderId': int(form['holderID']),
#         'holderName': form['holderName'],
#         'password': form['password']
#     })
#     return redirect('base.html')