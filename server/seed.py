#!/usr/bin/env python3
# PATH: /p5/outdoors-backend/server/seed.py

# Standard library imports
# from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from config import app, func, re
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    
    with app.app_context():
        print("Starting seed...")
                # Seed code goes here!
        # User.query.delete()
        users = []
        for i in range(5):
            name = fake.name()
            user = User(name=name, password_hash='a1', email=fake.email())
            users.append(user)
        db.session.add_all(users)
        db.session.commit()
        
                
# for i in range(13, 16):
#     name = 'new_user_' + str(i)
#     user = User(name=name, password_hash='a1', email=fake.email(),
#                 age=fake.random_int(min=18, max=65),
#                 address=fake.address(),
#                 job=fake.job())
#     db.session.add(user)
# db.session.commit()
