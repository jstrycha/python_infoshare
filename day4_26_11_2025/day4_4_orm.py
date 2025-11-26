# dokumentacja:https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html
from typing import Optional

from sqlalchemy import create_engine, select, ForeignKey, Column, Integer
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship, Session


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users" # właściwość klasowa - nazwa tabeli; klasę robimy w liczbie pojedynczej, w tabeli mamy liczbę mnogą

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[Optional[int]]
    addresses = relationship("Address", back_populates="user")

class Address(Base):
    __tablename__ = "addresses" # właściwość klasowa - nazwa tabeli; klasę robimy w liczbie pojedynczej, w tabeli mamy liczbę mnogą

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str]
    street: Mapped[str]

    # KLUCZ OBCY DO users.id
    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")


DATABASE_URL = "sqlite:///moja_baza_orm.db"
engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    statement = select(User).filter_by(name="aaa")
    user_obj = session.scalars(statement).all()
    print(user_obj)