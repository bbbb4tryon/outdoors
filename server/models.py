#PATH: /p5/outdoors-backend/server/models.py
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables'
# flask db upgrade
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt, Flask, app, SQLAlchemy, MetaData
from sqlalchemy.ext.hybrid import hybrid_property

#NOTE: backrefs are plural
class User(db.Model, SerializerMixin):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    _password_hash = db.Column(db.String) #tells us this is not the same as the password
    recommendations = db.relationship('Recommendations', backref = 'users')
    serialize_rules = ('-recommendations.users')
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    #create a hybrid property, is essentially the getter
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        #validations
        if len(password) > 8:
            password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
            #the table will show nonsense, then decode it
            #is same as a setter functon - we're setting the password and keeping it assigned to that user
            self._password_hash = password_hash.decode('utf-8')
            
    #AUTHENTICATION reverses that, and call it whenever we want to check the password
    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'<User {self.name}>'
    
    
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
    doer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bringing_id = db.Column(db.Integer, db.ForeignKey('what_youre_bringing.id'))
    serialize_rules = ('-users.our_recommendations',
                       '-what_youre_bringing.our_recommendations')
