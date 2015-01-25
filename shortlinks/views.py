from flask import abort, redirect, render_template, request

from shortlinks import app
from shortlinks.database import db_session
from shortlinks.models import Link

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:id>')
def short(id):
    link = Link.query.filter(Link.id == id).first()
    if link is None:
        abort(404)
    return redirect(link.url, code=301)

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form['link']
    link = Link(url)
    db_session.add(link)
    db_session.commit()
    return str(link.id)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
