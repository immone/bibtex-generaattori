"""Module for all different routes of the app."""
from flask import render_template, request, redirect
from init import app
from services import Services

service = Services()

@app.route('/')
def index():
    """Index page."""
    return render_template('index.html')


@app.route('/edit', methods=['GET', 'POST'])
def send_reference():
    """New reference page."""
    if request.method == 'GET':
        return render_template('send_reference.html')

    author = request.form['author']
    title = request.form['title']
    year = request.form['year']
    service.save_to_db(author, title, year)
    return redirect('/')


@app.route('/references')
def check_db_contents():
    """Page for viewing all references."""
    citations = service.get_db_contents()
    return render_template(
        'check_references.html',
        count=len(citations),
        citations=citations
    )
