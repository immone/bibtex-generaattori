"""Module for all different routes of the app."""
from flask import render_template, request, redirect, send_file
from init import app
from services import Services
from init import db

service = Services(db)

@app.route('/')
def index():
    """Page for viewing all references."""
    citations = service.get_db_contents()
    service.create_bibtex_file()
    return render_template(
        'check_references.html',
        count=len(citations),
        citations=citations
    )

@app.route('/type')
def choose_reference_type():
    """Page for choosing refence type."""
    return render_template('choose_reference_type.html')

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

@app.route('/download', methods=['POST'])
def download_references():
    """Download all references."""
    service.create_bibtex_file()
    
    return send_file('references.bib', as_attachment=True)
