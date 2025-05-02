# %%
# Import necessary libraries 
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
# %%
# Load environment variables from .env file
load_dotenv()
# %%
os.environ['MYSQL_USER']
# %%
# MySQL database connection details 
mysql_user =os.environ['MYSQL_USER']
mysql_password =os.environ['MYSQL_PASSWORD']
mysql_host =os.environ['MYSQL_HOST']
mysql_db =os.environ['MYSQL_DB']

# Postgres database connection details 
pg_user =os.environ['PG_USER']
pg_password =os.environ['PG_PASSWORD']
pg_host =os.environ['PG_HOST']
pg_db =os.environ['PG_DB']
# %%
mysql_engine = create_engine(
    f"mysql+pymysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@{os.environ['MYSQL_HOST']}/{os.environ['MYSQL_DB']}"
)

query = """
SELECT *
FROM website_sessions
WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59';
"""

df = pd.read_sql(query, mysql_engine)
# %%
pg_engine = create_engine(
    f"postgresql+psycopg2://{os.environ['PG_USER']}:{os.environ['PG_PASSWORD']}@{os.environ['PG_HOST']}/{os.environ['PG_DB']}"
)
# %%
# Load into schema.table: raw.website_sessions
df.to_sql("website_sessions", pg_engine, schema="raw", if_exists="replace", index=False)
# %%
