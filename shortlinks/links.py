from sqlalchemy.exc import IntegrityError

from shortlinks.database import db_session
from shortlinks.models import Link

def add_link(url):
    try:
        link = Link(url)
        db_session.add(link)
        db_session.commit()
        return link.id
    except IntegrityError as e:
        # link exists, return it's id
        db_session.rollback()
        link = Link.query.filter(Link.url == url).first()
        if link is not None:
            return link.id
        return None

def get_link(id):
    link = Link.query.filter(Link.id == id).first()
    if link is not None:
        link.hits += 1
        db_session.commit()
        return link.url
    return None

def get_most_popular_links():
    links = Link.query.order_by(Link.hits.desc()).limit(10).all()
    return links
