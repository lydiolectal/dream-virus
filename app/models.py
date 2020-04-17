from app import db

class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    email = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), index=True)
    location = db.Column(db.String(64), index=True)
    date = db.Column(db.Date())
    content = db.Column(db.Unicode())
    # submission date
    submit_date = db.Column(db.DateTime())
    # accepted
    accepted = db.Column(db.Boolean(), index=True)
    published = db.Column(db.Boolean(), index=True)
    # TODO:
    # - when to index??

    def __repr__(self):
        return f'Dream #{self.id}'


class ContentWarning:

    def __init__(self, id_, content_warning):
        self.id_ = id_
        self.content_warning = content_warning


class Theme:

    def __init__(self, id_, theme):
        self.id_ = id_
        self.theme = theme
