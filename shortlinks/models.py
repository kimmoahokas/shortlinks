from sqlalchemy import Column, Integer, String, DateTime
from shortlinks.database import Base
from datetime import datetime

class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    url = Column(String(256), unique=True)
    added = Column(DateTime, default=datetime.now)
    hits = Column(Integer, default=0)

    def __init__(self, url, added=None):
        self.url = url
        if added is not None:
            self.added = added

    def __repr__(self):
        return '<Link %r>' % (self.url)

    def hit(self):
        self.hits += 1
