"""Module for all different routes of the app."""
from flask import render_template, request, redirect, send_file
from init import app, db
from services import Service

service = Service(db)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Page for viewing all references."""
    if request.method == 'GET':
        references = service.get_db_contents()
        return render_template(
            'check_references.html',
            count=len(references),
            references=references
        )
    else:
        ref_id = int(request.form["id"])
        service.remove_from_db(ref_id)
        return redirect('/')

@app.route('/type')
def choose_reference_type():
    """Page for choosing refence type."""
    return render_template('choose_reference_type.html')

@app.route('/edit', methods=['GET', 'POST'])
def send_reference():
    """New reference page."""
    if request.method == 'GET':
        return render_template('send_reference.html')
    else:
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
