from configparser import ConfigParser

from sqlalchemy import create_engine, MetaData, Table, select

import pandas as pd

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
    transaction_table = Table('transaction', metadata, autoload_with=engine)
    

    
    with engine.connect() as connection:
        query = select(transaction_table)  
        result = connection.execute(query)
        
        df = pd.DataFrame(result.fetchall(),columns=result.keys())

        df.to_csv('transaction_data.csv',index=False)
        print("Data exported to be transaction_data.csv")
        
except Exception as e:
    print(f"An error occurred: {e}")

