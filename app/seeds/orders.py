from app.models import db, Order, environment, SCHEMA
from sqlalchemy.sql import text

def seed_orders(users):
    order1 = Order(
        purchaser_id=users[0].id, total=122.81, discount=0, status='pending')
    order2 = Order(
        purchaser_id=users[1].id, total=85.45, discount=0, status='pending')
    order3 = Order(
        purchaser_id=users[2].id, total=107.34, discount=0, status='pending')

    all_orders = [order1, order2, order3]
    add_orders = [db.session.add(order) for order in all_orders]
    db.session.commit()
    return all_orders

def undo_orders():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))

    db.session.commit()
