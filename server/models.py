# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables'
# flask db upgrade
from sqlalchemy_serializer import SerializerMixin
from config import db

#NOTE: backrefs are plural
class Doer(db.Model, SerializerMixin):
    __tablename__='doers'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    recommendations = db.relationship('Recommendations', backref = 'doers')
    serialize_rules = ('-recommendations.doers')

    def __repr__(self):
        return f'<Doer {self.username}>'
    
    
class Bringing(db.Model, SerializerMixin):
    __tablename__='what_youre_bringing'
    
    id = db.Column(db.Integer, primary_key = True)
    top = db.Column(db.String)
    bottom = db.Column(db.String)
    recommendations = db.relationship(
        'Recommendations', backref='what_youre_bringing')
    serialize_rules = ('-our_recommendations.what_youre_bringing')

class Recommendations(db.Model, SerializerMixin):
    __tablename__='our_recommendations'
    
    id = db.Column(db.Integer, primary_key = True)
    doer_id = db.Column(db.Integer, db.ForeignKey('doers.id'))
    bringing_id = db.Column(db.Integer, db.ForeignKey('what_youre_bringing.id'))
    serialize_rules = ('-doers.our_recommendations',
                       '-what_youre_bringing.our_recommendations')
