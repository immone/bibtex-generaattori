from app import app, db
from flask import render_template, request, redirect


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit', methods=['GET', 'POST'])
def send_reference():
    if request.method == 'GET':
        return render_template('send_reference.html')

    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        year = request.form['year']
        save_to_db(author, title, year)
        return redirect('/')

def save_to_db(author, title, year):
    print('Save to db', author, title, year)
    sql = 'INSERT INTO citations (author, title, year) VALUES (:author, :title, :year)'
    db.session.execute(sql, {'author':author, 'title':title, 'year':year})
    db.session.commit()

@app.route('/references')
def check_db_contents():
    sql = 'SELECT * FROM citations'
    citations = db.session.execute(sql).fetchall()
    return render_template("check_references.html", count=len(citations), citations=citations)