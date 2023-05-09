#!/usr/bin/env python3
# PATH: /p5/outdoors-backend/server/seed.py

# Standard library imports
# from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from config import app, func
from models import db, User

if __name__ == '__main__':
    # fake = Faker()
    
    with app.app_context():
        print("Starting seed...")
                # Seed code goes here!
        # User.query.delete()
        
        # new_user_1 = User(name='McTesterson')
        # new_user_2 = User(name='McTestFace')
        # new_user_3 = User(name='McTestJerk')
        # users = [new_user_1, new_user_2, new_user_3]
        # db.session.add_all(users)
        # db.session.commit()
        
                
                

        # # create 3 instances of the Doer model
        # for i in range(3):
        #     doer = Doer(username=fake.user_name())
        #     db.session.add(doer)
        # # create 3 instances of the Bringing model
        # for i in range(3):
        #     bringing = Bringing(top=fake.word(), bottom=fake.word())
        #     db.session.add(bringing)
        # # create 3 instances of the Recommendations model
        # for i in range(3):
        #     doer = Doer.query.order_by(func.random()).first()
        #     bringing = Bringing.query.order_by(func.random()).first()
        #     recommendation = Recommendations(doer=doer, bringing=bringing)
        #     db.session.add(recommendation)
