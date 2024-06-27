from flask import render_template, request, redirect, url_for
from app import app

@app.route("/", methods=["GET","POST"])
def index():
    user_data = None
    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'city': request.form['city'],
            'hobby': request.form['hobby'],
            'age': request.form['age']
        }
    return render_template('user_form.html', user_data=user_data)