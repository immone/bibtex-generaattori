from app import app
from flask import render_template
import functions

@app.route('/')
def index():
    start_date = functions.get_start_date()
    return render_template('index.html', start_date=start_date)

@app.route('/edit')
def send_reference():
    return render_template('send_reference.html')
