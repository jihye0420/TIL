import os
from pathlib import Path

import environ

# Set the project base directory
# BASE_DIR = Path(__file__).resolve().parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
print(os.path.abspath(__file__))
# print(Path(__file__))
# print(Path(__file__).resolve())
# print(Path(__file__).resolve().parent)
# print(Path(__file__).resolve().parent.parent)

# Takee nvironment variables from .env file
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = env('DEBUG')

print(SECRET_KEY)
print(DEBUG)
