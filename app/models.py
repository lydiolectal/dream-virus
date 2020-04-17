from datetime import datetime

from app import db


dreams_to_themes = db.Table(
    'themes',
    db.Column('dream_id', db.Integer, db.ForeignKey('dream.id'), primary_key=True),
    db.Column('theme_id', db.Integer, db.ForeignKey('theme.id'), primary_key=True)
)


dreams_to_content_warnings = db.Table(
    'content_warnings',
    db.Column('dream_id', db.Integer, db.ForeignKey('dream.id'), primary_key=True),
    db.Column('content_warning_id', db.Integer, db.ForeignKey('content_warning.id'), primary_key=True)
)


class Dream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(64), index=True, nullable=False)
    date = db.Column(db.Date(), index=True, nullable=False)
    content = db.Column(db.Unicode(), nullable=False)
    timestamp = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
    is_accepted = db.Column(db.Boolean(), index=True, nullable=False)

    themes = db.relationship(
        'Theme', 
        secondary=dreams_to_themes,
        lazy='joined',
        back_populates='dreams',
    )
    content_warnings = db.relationship(
        'ContentWarning',
        secondary=dreams_to_content_warnings,
        lazy='joined',
        back_populates='dreams',
    )

    def __repr__(self):
        return f'<Dream #{self.id}: {self.title}>'


class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(128), index=True, nullable=False)
    dreams = db.relationship(
        'Dream',
        secondary=dreams_to_themes,
        lazy='joined',
        back_populates='themes',
    )


class ContentWarning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_warning = db.Column(db.String(128), index=True, nullable=False)
    dreams = db.relationship(
        'Dream',
        secondary=dreams_to_content_warnings,
        lazy='select',
        back_populates='content_warnings',
    )

