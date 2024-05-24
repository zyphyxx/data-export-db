import pandas as pd
from sqlalchemy import create_engine

from Var import Path_Variables

LOCAL = Path_Variables.LOCAL

df = pd.read_csv(LOCAL)

print(df.head())

db_url = Path_Variables.db_url

engine = create_engine(db_url)

df.to_sql(LOCAL, con=engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso")






