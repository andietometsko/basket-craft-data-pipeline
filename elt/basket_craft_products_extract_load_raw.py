''' 
1. Import necessary libraries. 
2. Load source MySQL and destination Postgres connection details.
3. Build connection strings and create database engines.
4. Read products table from MySQL and load data into a DataFrame.
5. Write DataFrame to products table in Postgres. (raw schema)
'''
# %%

import pandas as pd
from sqlalchemy import create_engine

# %%
# MySQL database connection details 
mysql_user ='analyst'
mysql_password ='go_lions'
mysql_host ='db.isba.co'
mysql_db ='basket_craft'

# Postgres database connection details 
pg_user ='postgres'
pg_password ='isba_4715'
pg_host ='isba-dev-02.cxcoakgsc7ha.us-east-1.rds.amazonaws.com'
pg_db ='basket_craft'
# %%
# Build connection strings
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}:@{mysql_host}/{mysql_db}'
# pg_conn_str = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
# %%
# Create database engines
mysql_engine = create_engine(mysql_conn_str)
# pg_engine = create_engine(pg_conn_str)
# %%
# Read products table from MySQL
df = pd.read_sql('SELECT * FROM products', mysql_engine)
# %%
df
# %%
