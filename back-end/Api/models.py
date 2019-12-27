from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Table, VARCHAR, INT, Text
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:WZX085415a@127.0.0.1:3306/test?charset=utf8mb4"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
session_maker = sessionmaker(bind=engine)
session = sessionmaker(engine)()
Base = declarative_base(engine)

# 复合键
user_and_book = Table('user_and_book', Base.metadata, 
					Column('book_id', Integer, ForeignKey('book.id')),
					Column('user_id', Integer, ForeignKey('user.id')))
class User(Base):
	"""user table"""
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True, autoincrement = True)
	user_name = Column(String(32), nullable = False)
	user_telephone = Column(Integer, nullable = False, unique = True)


class Book(Base):
	"""book tables"""
	__tablename__ = 'book'
	id = Column(Integer, primary_key = True, autoincrement = True)
	book_name = Column(String(100), nullable = False)
	book_url = Column(String(200), nullable = False, unique = True)
	book_image_url = Column(String(200), nullable = False, unique = True)
	book_describe = Column(Text, nullable = True, default = 'None')
	book_fire = Column(Integer, default = 0)
	book_author = Column(Text, nullable=True, default = 'None')
