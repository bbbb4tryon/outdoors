#PATH: /p5/outdoors-backend/server/models.py
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db revision --autogenerate -m 'Create tables'
# flask db upgrade
from sqlalchemy_serializer import SerializerMixin
from config import db, bcrypt, Flask, app, SQLAlchemy, MetaData, Dict, Any, re
from sqlalchemy.ext.hybrid import hybrid_property


#NOTE: backrefs are plural
class User(db.Model, SerializerMixin):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    user_type = db.Column(db.String)
    _password_hash = db.Column(db.String) #thisnot the same as the password
    email = db.Column(db.String, nullable = False, unique = True)
    recommendations = db.relationship('Recommendations', backref = 'users')
    serialize_rules = ('-recommendations.users',)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    #create a hybrid property, is essentially the getter
    @hybrid_property
    def password_hash(self):
        print('hybrid.property getter called')
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        print('password_hash Setter called')
        #validations
        # if len(password) > 8:
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        #the table will show nonsense, then decode it
        #is same as a setter functon - we're setting the password and keeping it assigned to that user
        self._password_hash = password_hash.decode('utf-8')
        
    #AUTHENTICATION reverses that, and call it whenever we want to check the password
    
    def authenticate(self, password):
        print('authenticate called')
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    

    # def is_valid_user_data(data: Dict[str, Any]) -> bool:
    #     print('is_valid_USER_data called')
    #     required_fields = ['name', 'password', 'email']
    #     for field in required_fields:
    #         if field not in data:
    #             return False
    #     return True


    # def is_valid_login_data(data: Dict[str, Any]) -> bool:
    #     print('is_valid_LOGIN_data called')
    #     required_fields = ['password', 'email']
    #     for field in required_fields:
    #         if field not in data:
    #             return False
    #     return True


    
class Bringing(db.Model, SerializerMixin):
    __tablename__='what_youre_bringing'
    
    id = db.Column(db.Integer, primary_key = True)
    top = db.Column(db.String)
    bottom = db.Column(db.String)
    recommendations = db.relationship(
        'Recommendations', backref='what_youre_bringing')
    serialize_rules = ('-our_recommendations.what_youre_bringing',)

class Recommendations(db.Model, SerializerMixin):
    __tablename__='our_recommendations'
    
    id = db.Column(db.Integer, primary_key = True)
    doer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bringing_id = db.Column(db.Integer, db.ForeignKey('what_youre_bringing.id'))
    serialize_rules = ('-users.our_recommendations',
                       '-what_youre_bringing.our_recommendations',)
