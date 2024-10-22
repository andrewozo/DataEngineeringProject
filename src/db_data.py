import configparser

from sqlalchemy import create_engine, text

config = configparser.ConfigParser()
config.read('config.ini')
user = config.get('database','user')
password = config.get('database','password')


connection_string = f'postgresql://{user}:{password}@localhost/postgres'