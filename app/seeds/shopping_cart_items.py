from app.models import db, shopping_cart_item, environment, SCHEMA
from sqlalchemy.sql import text
from ..models.shopping_cart_item import shopping_cart_items

def seed_shopping_cart_items(users, products):
    items = [
        {'user_id': users[0].id, 'product_id': products[6].id, 'quantity': 1},
        {'user_id': users[0].id, 'product_id': products[7].id,'quantity': 5},
        {'user_id': users[0].id, 'product_id': products[8].id, 'quantity': 2},
        {'user_id': users[0].id, 'product_id': products[9].id, 'quantity': 3},
        {'user_id': users[1].id, 'product_id': products[0].id, 'quantity': 1},
        {'user_id': users[1].id, 'product_id': products[1].id,'quantity': 2},
        {'user_id': users[1].id,'product_id': products[2].id, 'quantity': 3},
        {'user_id': users[2].id, 'product_id': products[3].id, 'quantity': 2},
        {'user_id': users[2].id,'product_id': products[4].id,'quantity': 3},
        {'user_id': users[2].id, 'product_id': products[5].id, 'quantity': 3},
    ]

    db.session.execute(shopping_cart_items.insert(), items)
    db.session.commit()

def undo_shopping_cart_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shopping_cart_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shopping_cart_items"))

    db.session.commit()
