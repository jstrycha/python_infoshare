from sqlalchemy import create_engine, text, String, Column, Integer, select, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload, DeclarativeBase

DATABASE_URL = "postgresql+psycopg2://weblink_intel:iSA#Intel#2025@pgsql.cyber-folks.pl:5432/weblink_intel"
engine = create_engine(DATABASE_URL, echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    emails = relationship("Email", back_populates="user", cascade="all, delete-orphan")

    def print_age(self):
        print(self.age)

    def __repr__(self): # representation - analogiczna do __str__, ale używana bardziej dla celów programistycznych niż dla userów
        return f"User(id={self.id}, name='{self.name}', age={self.age})"

    # def unique(self, email):
    #     self.email = unique(self.email)
    #     return self - takie kontrukcje robimy żeby móc robić chainowanie funkcji


class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="emails")

    def __repr__(self):
        return f"Email(id={self.id}, email='{self.email}', user_id={self.user_id})"


Base.metadata.create_all(engine)

with Session(engine) as session:
    ## dodawanie rekordów
    # session.add_all([
    #     User(name="Jan", age=22),
    #     User(name="Ewa", age=35),
    #     User(name="Tomasz", age=45, emails=[Email(email="m1@wp.pl"), Email(email="m2@wp.pl")])
    # ])
    # session.commit()

    ## pobieranie danych
    stmt = select(User).where(User.name.ilike("j%")).options(joinedload(User.emails))
    # stmt - statement
    rows = session.execute(stmt).unique().scalars().all()

    ## podgląd zapytania ze statementu
    # sql_query = stmt.compile(engine)
    # print(sql_query)
    # print(sql_query.params)

    ## iteracja po wynikach
    for user in rows:
        user.print_age()
        # print(user.emails)
        ## modyfikacja danych w bazie przez obiekty (trzeba pamiętać o commicie)
        #user.emails.append(Email(email="noreply@isa.pl"))

    #session.commit()
