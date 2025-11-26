from sqlalchemy import create_engine, text, String, Column, Integer
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///moja_baza.db"
engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    with engine.begin() as connection:
        connection.execute(
            text("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER
                );"""),
        )


def get_users():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id, name, age FROM users"))
        # print(result.fetchall())
        for row in result:
            print("id: ", row.id)
            print("name: ", row.name)
            # print("age: ", row.age)


def add_user(name, age):
    with engine.begin() as connection:
        # connection.execute(text("INSERT INTO users (name, age) VALUES ('{}', '{}')".format(name, age)))
        connection.execute(text("INSERT INTO users (name, age) VALUES (:name, :age)"),
                           {"name": name, "age": age} # bindowanie parametrów
        )

def drop_table():
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE users"))

    connection.commit()

init_db()
# drop_table()
add_user("aaaa", 123)
get_users()