
class Dream:

    def __init__(self, id_, email, initials, location, date, content):
        self.id_ = id_
        self.email = email
        self.initials = initials
        self.location = location
        self.date = date
        self.content = content


class ContentWarning:

    def __init__(self, id_, content_warning):
        self.id_ = id_
        self.content_warning = content_warning


class Theme:

    def __init__(self, id_, theme):
        self.id_ = id_
        self.theme = theme