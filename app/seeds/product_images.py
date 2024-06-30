from app.models import db, ProductImage, environment, SCHEMA
from sqlalchemy.sql import text

def seed_product_images(products):
    image1 = ProductImage(
        product_id=products[0].id, url="image1"
    )
    image2 = ProductImage(
        product_id=products[1].id, url="image2"
    )
    image3 = ProductImage(
        product_id=products[2].id, url="image3"
    )
    image4 = ProductImage(
        product_id=products[3].id, url="image4"
    )
    image5 = ProductImage(
        product_id=products[4].id, url="image5"
    )
    image6 = ProductImage(
        product_id=products[5].id, url="image6"
    )
    image7 = ProductImage(
        product_id=products[6].id, url="image7"
    )
    image8 = ProductImage(
        product_id=products[7].id, url="image8"
    )
    image9 = ProductImage(
        product_id=products[8].id, url="image9"
    )
    image10 = ProductImage(
        product_id=products[9].id, url="image10"
    )

    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)
    db.session.add(image5)
    db.session.add(image6)
    db.session.add(image7)
    db.session.add(image8)
    db.session.add(image9)
    db.session.add(image10)
    db.session.commit()

def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM product_images"))

    db.session.commit()
