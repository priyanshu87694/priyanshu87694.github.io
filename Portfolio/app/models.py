from app import db

class Message(db.Model):
    mesg_id   =   db.Column(db.Integer(), primary_key=True)
    name      =   db.Column(db.String(length=30), nullable=False)
    email     =   db.Column(db.String(length=50), nullable=False)
    text      =   db.Column(db.String(length=150), nullable=False)
    
    def __repr__(self):
        return f"{self.name}:{self.mesg_id}"