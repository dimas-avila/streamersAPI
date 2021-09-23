from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Streamers(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    subs = db.Column(db.Integer)
    followers = db.Column(db.Integer)

    def __init__(self, name, subs, followers):
        super().__init__()
        self.name = name
        self.subs = subs
        self.followers = followers
        

    def __str__(self):
        return "\nNombre: {}. Subs: {}. Followers: {}.\n".format(
            self.name,
            self.subs,
            self.followers
        )

    def serialize(self):
        return {
            "rowid": self.rowid,
            "name": self.name,
            "subs": self.subs,
            "followers": self.followers
        }