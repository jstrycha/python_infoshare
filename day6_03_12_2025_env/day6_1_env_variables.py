import os
from dotenv import load_dotenv

# w terminalu cmd: set ENV=kopytko &&  python day6_1_env_variables.py && echo %ENV%
print(os.environ.get('ENV'))
print(os.getenv('USER'))

