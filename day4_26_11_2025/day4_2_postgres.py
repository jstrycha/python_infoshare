import psycopg2
from sqlalchemy import create_engine, text

# SQL Alchemy Core

DATABASE_URL = "postgresql+psycopg2://weblink_intel:iSA#Intel#2025@pgsql.cyber-folks.pl:5432/weblink_intel"
engine = create_engine(DATABASE_URL, echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT name, age FROM users"))
    for row in result:
        print("name:", row.name)
