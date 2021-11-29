from sqlalchemy import Column, Integer, String

from db import Base, engine


# связующая таблица  для м2м
user_product = pass

def get_or_create():
    pass

class product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())

    def __repr__(self):
        return f'Product {self.id} {self.description}'


class price(Base):
    pass


class user(Base):
    pass


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
