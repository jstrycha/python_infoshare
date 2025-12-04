import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env.default') # ładujemy pierwsze

# nadpisywanie defaultu
env = os.getenv('ENV')
if env is not None:
    load_dotenv(dotenv_path='.env.' + env, override=True)
    # np. przy pliku .env.default wpisujemy dokładnie .env.default

print(os.getenv('DATABASE_DSN'))

# w terminalu cmd:
# set ENV=kopytko &&  python day6_2_dotenv.py && echo %ENV% -> user:pass@localhost:5432 z .env.default
# set ENV=test &&  python day6_2_dotenv.py && echo %ENV% -> dhdhdhd z .env.test