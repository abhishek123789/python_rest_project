from db import db
# Line 8 lazy="dynamic" means that it wont fetch items until we tell it to
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")





