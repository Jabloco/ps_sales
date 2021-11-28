from sqlalchemy import Column, Integer, String

from db import Base, engine

class product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())

    def __repr__(self):
        return f'Product {self.id} {self.description}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
