from init import app, db
import routes

def get_start_date():
    start_date = db.session.scalars('SELECT start_date FROM start_dates').first()
    return start_date

# Delete everything below, when we have actual database code
import signal, os
@app.before_first_request
def write_to_db():
    db.session.execute('CREATE TABLE start_dates (start_date int)')
    db.session.execute("INSERT INTO start_dates VALUES (datetime('now'))")
    db.session.commit()

def shutdown(signum, frame):
    if os.path.exists('instance/app.db'):
        os.remove('instance/app.db')
    exit(0)

signal.signal(signal.SIGINT, shutdown)
