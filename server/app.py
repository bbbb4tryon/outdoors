#!/usr/bin/env python3
# path: 

from flask import Flask, request, jsonify
from flask_restful import Resource
#instance of the Flask app is in config app = Flask(__name__)

# Local imports
from config import app, db, api
from models import Doer, Bringing, Recommendations

@app.route('/')
def index():
    return '<h1>Outdoors Backend</h1>'

#return a list of object from the model with API endpoints - using POSTMAN to log
@app.route('/doers')
def get_doers():
    doers = Doer.query.all()
    return jsonify([doer.to_dict() for doer in doers])


@app.route('/what_youre_bringing')
def get_what_youre_bringing():
    what_youre_bringing = Bringing.query.all()
    return jsonify([bringing.to_dict() for bringing in what_youre_bringing])


@app.route('/our_recommendations')
def get_our_recommendations():
    our_recommendations = Recommendations.query.all()
    return jsonify([recommendation.to_dict() for recommendation in our_recommendations])


if __name__ == '__main__':
    app.run(port=5555, debug=True)
