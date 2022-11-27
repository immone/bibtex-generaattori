from init import app, db

def get_start_date():
    start_date = db.session.scalars('SELECT start_date FROM start_dates').first()
    return start_date