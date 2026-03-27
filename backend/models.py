from config import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(1200), unique=True, nullable=False)
    
    def to_json(self):   #this converts all the ^ into python dict and then into json(to communicate with API)
        return{
            "id": self.id, #camelcase cuz to match the json convention
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }
        