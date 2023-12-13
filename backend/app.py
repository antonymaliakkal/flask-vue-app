from models import User

from celery_app import app
from db_instance import db
# if __name__ == '__main__':
#     app.run(debug = True)


with app.app_context():
    db.create_all() 
    user = User.query.filter_by(role='admin').all()
    if user == []:
        user = User(username = "admin", password = "admin", role = "admin")
        db.session.add(user)
        db.session.commit()

import routes
