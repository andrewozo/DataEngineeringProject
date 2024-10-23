from configparser import ConfigParser

from sqlalchemy import create_engine, MetaData, Table, select

try:
    config = ConfigParser()
    config.read('../config.ini')
    user = config.get('database','user')
    password = config.get('database','password')
except Exception as config_error:
    print(f'Error reading config file: {config_error}')
    exit(1)



connection_string = f'postgresql://{user}:{password}@localhost/AOzoria'

engine = create_engine(connection_string)
metadata = MetaData()



try:
    people_table = Table('transaction', metadata, autoload_with=engine)
    

    # Perform query using table object
    with engine.connect() as connection:
        query = select(people_table)  # Equivalent to SELECT * FROM people
        result = connection.execute(query)
        print(result)
        
        # Fetch and print results
        for row in result:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")

