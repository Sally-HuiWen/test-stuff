from app.models import db, order_items, environment, SCHEMA
from sqlalchemy.sql import text
from ..models.order_items import order_items

def seed_order_items(orders, products):
    order_items_values = [
        {'order_id': orders[0].id, 'product_id': products[6].id, 'quantity': 1},
        {'order_id': orders[0].id, 'product_id': products[7].id, 'quantity': 5},
        {'order_id': orders[0].id, 'product_id': products[8].id, 'quantity': 2},
        {'order_id': orders[0].id, 'product_id': products[9].id, 'quantity': 3},
        {'order_id': orders[1].id, 'product_id': products[0].id, 'quantity': 1},
        {'order_id': orders[1].id, 'product_id': products[1].id, 'quantity': 2},
        {'order_id': orders[1].id, 'product_id': products[2].id, 'quantity': 3},
        {'order_id': orders[2].id, 'product_id': products[3].id, 'quantity': 2},
        {'order_id': orders[2].id, 'product_id': products[4].id, 'quantity': 3},
        {'order_id': orders[2].id, 'product_id': products[5].id, 'quantity': 3},
    ]

    db.session.execute(order_items.insert(), order_items_values)
    db.session.commit()

def undo_order_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM order_items"))

    db.session.commit()
