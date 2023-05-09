#!/usr/bin/env python3
#PATH: server/app.py

from flask import request, jsonify, Flask, make_response, session
# session here is unique, stores the secret key and cookie throughout refreshes
# Local imports
from config import app, db, api, CORS, SQLAlchemy, Flask, Resource, bcrypt, Migrate
from models import User, Bringing, Recommendations

app.secret_key = b'\x80\x1b\x1a \xb4\x9c\x9c\x014+\xab\xf3\xbdb2\xd3'
# % python -c 'import os; print(os.urandom(16))'
# TODO: mimic this file for the RESOURCES below
# # visited = bool
# class Visited(Resource):
#     def get(self):
#         session['visited'] = True
#         json_obj = {'Type':'Get'}
#         res = make_response(jsonify(json_obj), 200)
#         return res
# api.add_resource(Visited, '/visited')

# class AllUsers(Resource):
#     def get(self):
#         print('RESTful')
#         users = User.query.all()
#         all_users = []
#         for user in users:
#             all_users.append(user.to_dict())
#             res = make_response(jsonify(all_users), 200)
#             return res
#     def post(self):
#         jsoned_request = request.get_json()
#         print(jsoned_request)
#         new_user = User(name=jsoned_request['name'], email=jsoned_request['email'], password=jsoned_request['password'])
#         db.session.add(new_user)
#         db.session.commit()
#         res = make_response(jsonify(new_user.to_dict()), 200)
#         return res
# api.add_resource(AllUsers, '/allusers')
# NOTE: createuser starts at 27: 51 https: // vimeo.com/817104676/d801a8722c
class CreateUser(Resource):
    def post(self):
        jsoned_request = request.get_json()
        new_user = User(name = jsoned_request['name'])
        new_user.password_hash = jsoned_request['password']
        db.session.add(new_user)
        db.session.commit()
api.add_resource(CreateUser, '/signup')

class Index(Resource):
    def get(self):
        json_obj = {'message':'Welcome to the Outdoors!'}
        res = make_response(jsonify(json_obj), 200)
        return res


api.add_resource(Index, '/')
class Login(Resource):
    #post because SENDING data when we login
    def post(self):
        jsoned_request = request.get_json()
        user = User.query.filter(User.name==jsoned_request['name']).first()
        if user:
            #'user_id' and session act together to store the user - eg, if they leave the page and come back, they're still logged in and their data is still there BUT is not stored in the tables
            session['user_id'] = user.id
            res = make_response(jsonify(user.to_dict()), 200)
            return res
        else:
            res = make_response(jsonify({'login': 'User not found'}), 404)
            return res
api.add_resource(Login, '/login')

        # Authenticate user with name and password
        # If successful, return a response with a JWT token
        # If unsuccessful, return a 401 Unauthorized response
        # return jsonify({"token": "myjwttoken"})


class check_Login(Resource):
    # since we're not sending data, we use GET
    def get(self):
        user_id =  session.get('user_id')
        if user_id:
            user = User.query.filter(User.id == session["user_id"]).first()
            res = make_response(jsonify(user.to_dict()), 200)
api.add_resource(check_Login, '/checklogin')

class Logout(Resource):
    def delete(self):
        session['user`_id'] = None
        res = make_response(jsonify({'login': 'logged out'}), 200)
        return res
api.add_resource(Logout, '/logout')


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
