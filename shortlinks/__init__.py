from flask import Flask
app = Flask(__name__)
app.config.from_object('shortlinks.config')

import shortlinks.views
from shortlinks.database import db_session, init_db

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()
