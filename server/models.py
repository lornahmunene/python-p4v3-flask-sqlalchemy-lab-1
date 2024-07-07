from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model):
    __tablename__ = 'earthquakes'
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Numeric(10, 1), nullable=False)
    location = db.Column(db.String)
    year = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'

    def to_dict(self):
        return {
            'id': self.id,
            'magnitude': f'{self.magnitude:.1f}',  # Format magnitude to one decimal place as string
            'location': self.location,
            'year': self.year
        }
