"""Module for all different routes of the app."""
from flask import render_template, request, redirect
from init import app, db, Reference


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
    save_to_db(author, title, year)
    return redirect('/')


def save_to_db(author, title, year):
    """Save form data to database."""
    print('Save to db', author, title, year)
    new = Reference(
        author=author,
        title=title,
        booktitle=None,
        year=year,
        type_id=1
    )
    db.session.add(new)  # pylint: disable=no-member
    db.session.commit()  # pylint: disable=no-member


@app.route('/references')
def check_db_contents():
    """Page for viewing all references."""
    citations = Reference.query.all()
    return render_template(
        "check_references.html",
        count=len(citations),
        citations=citations
    )
