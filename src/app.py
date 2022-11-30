from init import app, db
import routes


try:
    db.session.execute('CREATE TABLE citations (author varchar, title varchar, year int)')
    db.session.commit()
except:
    print('Table already created to database')
