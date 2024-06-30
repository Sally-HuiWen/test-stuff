from app.models import db, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime
from ..models.review import reviews

def seed_reviews(users, products):
    review_values = [
        {'product_id': products[0].id, 'user_id': users[1].id, 'review': 'Good', 'stars': 4, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[1].id, 'user_id': users[1].id, 'review': 'Fair', 'stars': 3, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[2].id, 'user_id': users[1].id, 'review': 'Bad', 'stars': 2, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[3].id, 'user_id': users[2].id, 'review': 'Excellent', 'stars': 5, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[4].id, 'user_id': users[2].id, 'review': 'Awful', 'stars': 1, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[5].id, 'user_id': users[2].id, 'review': 'Not bad', 'stars': 3, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[6].id, 'user_id': users[0].id, 'review': 'OK', 'stars': 3, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[7].id, 'user_id': users[0].id, 'review': 'Best', 'stars': 5, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[8].id, 'user_id': users[0].id, 'review': 'Worst', 'stars': 1, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
        {'product_id': products[9].id, 'user_id': users[0].id, 'review': 'Barely serviceable', 'stars': 2, 'created_at': datetime.utcnow(), 'updated_at':datetime.utcnow()},
    ]

    db.session.execute(reviews.insert(), review_values)
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
