import pandas as pd
from sqlalchemy import create_engine

from Var import Path_Variables

#conexão com db
db_url = Path_Variables.db_url;
engine = create_engine(db_url);

# sql query
sql = Path_Variables.sql_query


df = pd.read_sql(sql,con=engine);

file_path = Path_Variables.file_path;

df.to_csv(file_path, sep='\t', index=False)

print(f"Dados exportados para o arquivo")


