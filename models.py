from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship

from db import Base, engine


# связующая таблица  для м2м
user_product = Table('users_products', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('product_id', ForeignKey('products.id'), primary_key=True)
)


def get_or_create():
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(Integer, unique=True)
    username = Column(String)
    products = relationship('Products', secondary=user_product)

    def __repr__(self):
        return f'User {self.name} {self.phone} {self.username}'


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())
    prices = relationship('Price', backref='prices')

    def __repr__(self):
        return f'Product {self.id} {self.description}'


class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True)
    id_product = Column(Integer, ForeignKey(Product.id), index=True, nullable=False)
    price_final = Column(Integer, nullable=True)
    price_original = Column(Integer, nullable=True)
    date_change = Column(Date)

    def __repr__(self):
        return f'Price final {self.price_final}, price original {self.price_original}'




if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
