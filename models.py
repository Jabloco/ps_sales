import logging

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import backref, relationship
from sqlalchemy.exc import InvalidRequestError, IntegrityError

from db import Base, db_session

logging.basicConfig(handlers=[logging.FileHandler('req_error.log', 'a', 'utf-8')],
                    format='%(asctime)s - %(levelname)s - %(message)s')



def get_or_create(model, **kwargs):
    """
    Функция делает запрос в БД.

    При наличии определенной записи возвращает ее,

    при отсутствии, создаем и возвращаем.
    """
    try:
        model_object = model.query.filter_by(**kwargs).first()
    # Лишний аргумент в запросе.
    except InvalidRequestError as error:
        logging.exception(error)
        return None, None
    if model_object:
        return model_object, False

    model_object = model(**kwargs)
    db_session.add(model_object)
    try:
        db_session.commit()
    # Один из аргументов Unique уже существует.
    except IntegrityError as error:
        logging.exception(error)
        return None, None
    return model_object, True


# связующая таблица  для м2м
user_product = Table('users_products', Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('product_id', ForeignKey('products.id'), primary_key=True)
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(Integer, unique=True)
    username = Column(String)
    products = relationship('Product', secondary=user_product)

    @classmethod
    def insert(cls, t_name, t_phone, t_username):
        """
        Запись данных о пользователе в таблицу.

        t_name, t_phone, t_username - данные из телеграм
        """
        model_object, _ = get_or_create(
            cls,
            name=t_name,
            phone=t_phone,
            username=t_username
        )
        return model_object

    def __repr__(self):
        return f'User {self.name} {self.phone} {self.username}'


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    description = Column(String())
    url = Column(String())

    @classmethod
    def insert(
        cls,
        parsed_title,
        parsed_description,
        parsed_url
        ):
        model_object, _ = get_or_create(
            cls,
            title=parsed_title,
            description=parsed_description,
            url=parsed_url
        )
        return model_object

    def __repr__(self):
        return f'Product {self.id} {self.description}'


class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True)
    id_product = Column(Integer, ForeignKey(Product.id), index=True, nullable=False)
    price_final = Column(String, nullable=True)
    price_original = Column(String, nullable=True)
    price_is_ps_plus = Column(Boolean)
    date_change = Column(DateTime)
    product = relationship('Product', backref='products')

    @classmethod
    def insert(
        cls,
        geted_id_product,
        parsed_price_final,
        parsed_price_original,
        parsed_is_ps_plus_price,
        date
    ):
        model_object, _ = get_or_create(
            cls,
            id_product=geted_id_product,
            price_final=parsed_price_final,
            price_original=parsed_price_original,
            price_is_ps_plus=parsed_is_ps_plus_price,
            date_change=date
        )
        return model_object

    def __repr__(self):
        return f'Price final {self.price_final}, price original {self.price_original}'
