#!/usr/bin/env python3
#PATH: server/app.py
# * Serving Flask app 'app.py'
# * Debug mode: off
# * Running on http: // 127.0.0.1: 5555

import re
from flask import request, jsonify, make_response, session
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash
from models import User, db
from config import app, api, bcrypt, CORS

app.secret_key = b'\x80\x1b\x1a \xb4\x9c\x9c\x014+\xab\xf3\xbdb2\xd3'
# % python -c 'import os; print(os.urandom(16))'

class Index(Resource):
    def get(self):
        # json_obj = {'message':'Welcome to the Outdoors!'}
        # res = make_response(jsonify(json_obj), 200)
        # return res
        return {'message': 'Welcome to the Outdoors!'}
api.add_resource(Index, '/')

# NOTE: Signup starts at 27: 51 https: // vimeo.com/817104676/d801a8722c
class Signup(Resource):
    def post(self):
        # print("testtttttttt")
        #extract form data
        name = request.get_json()['name']
        print(name)
        password = request.get_json()['password']
        # ok print(password)
        email = request.get_json()['email']  
        # ok print(email) 
        #Validate form data
        # TODO: take these out of --commentedout
        # if not name or not password or not email:
        #     # print(name, password, email)
        #     return {'error': 'Nope, all inputs need to filled'}, 400
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #     return {'error': 'Not a real email'}, 400
        # if not re.match(r"[A-Za-z0-9@#$%^&+=]{2,}", password):
        #     return {'error': 'At least 2 characters long'}, 400
        #Create New User:
        new_user = User(name=name, email=email,
                        password_hash=generate_password_hash(password))
        print(new_user)
        new_user.password_hash = password
        try:
            
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            # print(session['user_id'])
        #Return success message:
            print({'message': 'You\'re in the Outdoors'}, 200)
        except Exception:

            print('signup in app.py failed')

            return {'error': '422 Unprocessable Entity'}, 422
        # jsoned_request = request.get_json()
        # #Validate Email Address:
        # email = jsoned_request.get('email')
        # if not email:
        #     return {'error': 'Email is required'}, 400
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #     return {'error': 'Please provide a valid email address'}, 400

        
        # #Create New User:
        # new_user = User(name = jsoned_request['name'])
        # new_user.password_hash = jsoned_request['password']
        # db.session.add(new_user)
        # db.session.commit()
        
            
api.add_resource(Signup, '/signup')

# @app.route('/signup', methods=['POST'])
# def signup_user():
#     data = request.get_json()
#     name = data.get('name')
#     password = data.get('password')
#     email = data.get('email')
#     user = User(name=name, password_hash=generate_password_hash(password), email=email)
#     db.session.add(user)
#     db.session.commit()
#     return jsonify(user.to_dict()), 201, {'message': 'User created successfully'}
    
class login(Resource):
    #post because SENDING data when we login
    def post(self):
        jsoned_request = request.get_json()
        user = User.query.filter(User.name==jsoned_request['name']).first()
        # print(jsoned_request['password'])
        if user.authenticate(jsoned_request['password']):
            
            #'user_id' and session act together to store the user - eg, if they leave the page and come back, they're still logged in and their data is still there BUT is not stored in the tables
            # print("TTTTTTTEEEEEESSSSSSSSTTTT")
            session['user_id'] = user.id
            res = make_response(jsonify(user.to_dict()), 200)
            return res
        else:
            res = make_response(jsonify({'login': 'User not found'}), 404)
            return res
api.add_resource(login, '/login')
# @app.route('/login', methods=['POST'])
# def login_valid():
#     data = request.get_json()
#     if not is_valid_login_data(data):
#         return {'error': 'Invalid login data'}, 400
    
        # Authenticate user with name and password
        # If successful, return a response with a JWT token
        # If unsuccessful, return a 401 Unauthorized response
        # return jsonify({"token": "myjwttoken"})


class check_Login(Resource):
    # since we're not sending data, we use GET
    def get(self):
        user_id =  session.get('user_id')
        # print("am i innnnnnnn")
        if user_id:
            user = User.query.filter(User.id == session["user_id"]).first()
            # print(User.to_dict(user))
            res = make_response(jsonify(user.to_dict()), 200)
            # print(user.to_dict())
        else:
            res = make_response(jsonify({'login': 'Not logged in'}), 401)
api.add_resource(check_Login, '/checklogin')

class logout(Resource):
    def delete(self):
        print('logoutttttttttt')
        session['user`_id'] = None
        res = make_response(jsonify({'login': 'logged out'}), 200)
        return res
api.add_resource(logout, '/logout')


class get_type(Resource):
    def get(self):
        if session.get("valid"):
            user = User.query.filter(User.id == session["user_id"]).first()
            res = make_response(jsonify({"user_type": user.user_type}), 200)
            return res
        else:
            res = make_response(jsonify({"login": "invalid user"}), 400)
            return res


api.add_resource(get_type, '/get_type')
# @app.after_request
# def print_hello_user():
    
#     user = User.query.filter(User.id==session.get('user_id')).first()
#     if user:
#         print(f'You\'re Outdoors!')
#     else:
#         print('Login, or stay inside!')


if __name__ == '__main__':
    # with app.app_context():
        # db.session.commit()

# commit the changes to the database before starting the application, in other words, keep this last
    app.run(port=5555, debug=True)
