from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

# from waypi.connector import BaseModel


class User():
    __tablename__ = 'user'

    id = Column(
        Integer,
        name='id',
        nullable=False,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        Text,
        name='name'
    )

    email = Column(
        Text,
        name='email'
    )

    pass_word = Column(
        Text,
        name='pass_word'
    )
