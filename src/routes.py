"""Module for all different routes of the app."""
from flask import render_template, request, redirect
from init import app
from services import Services

service = Services()

@app.route('/', methods=['GET', 'POST'])
def index():
    """Page for viewing all references."""
    if request.method == 'GET':
        citations = service.get_db_contents()
        return render_template(
            'check_references.html',
            count=len(citations),
            citations=citations
        )
    else:
        ref_id = int(request.form["id"])
        service.remove_from_db(ref_id)
        return redirect('/')

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
    #Download functionality here
    print('Downloading references...')
    return redirect('/')
