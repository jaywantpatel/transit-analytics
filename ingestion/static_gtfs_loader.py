import zipfile
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://transit:transit@localhost:5432/transitdb")

with zipfile.ZipFile("GTFSExport.zip", 'r') as z:
    for file in ["stops.txt", "routes.txt", "trips.txt", "stop_times.txt"]:
        with z.open(file) as f:
            df = pd.read_csv(f)
            table_name = "raw_" + file.replace(".txt", "")
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Loaded {table_name} with {len(df)} records.")