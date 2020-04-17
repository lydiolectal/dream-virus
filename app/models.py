from datetime import datetime

from app import db

class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    email = db.Column(db.String(64))
    name = db.Column(db.String(64))
    location = db.Column(db.String(64), index=True)
    date = db.Column(db.Date(), index=True)
    content = db.Column(db.Unicode())
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    is_accepted = db.Column(db.Boolean(), index=True)

    def __repr__(self):
        return f'<Dream #{self.id}: {self.title}>'


# class ContentWarning:

#     def __init__(self, id_, content_warning):
#         self.id_ = id_
#         self.content_warning = content_warning


# class Theme:

#     def __init__(self, id_, theme):
#         self.id_ = id_
#         self.theme = theme
