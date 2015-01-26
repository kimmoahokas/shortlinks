from flask import abort, redirect, render_template, request

from shortlinks import app
from shortlinks.links import add_link, get_link, get_most_popular_links
from shortlinks.validators import LinkForm

@app.route('/')
def index():
    return render_template('index.html', links=get_most_popular_links())

@app.route('/<int:id>')
def short(id):
    app.logger.debug('Request short link with id {}'.format(id))
    link = get_link(id)
    if link is None:
        abort(404)
    return redirect(link, code=301)

@app.route('/shorten', methods=['POST'])
def shorten():
    app.logger.debug('Shorten url: {}'.format(request.form['link']))
    if LinkForm(request.form).validate():
        url = request.form['link']
        link_id = add_link(url)
        return str(link_id)
    app.logger.debug('Invalid link')
    abort(400)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.template_filter('format_datetime')
def format_datetime(dt):
    return dt.strftime('%c')
