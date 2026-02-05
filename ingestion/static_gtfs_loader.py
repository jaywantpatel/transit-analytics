import zipfile
import pandas as pd
import requests
import os
from sqlalchemy import create_engine

GTFS_URL = "https://oct-gtfs-emasagcnfmcgeham.z01.azurefd.net/public-access/GTFSExport.zip"
GTFS_FILE = "GTFSExport.zip"

if not os.path.exists(GTFS_FILE):
    print("Downloading GTFS data...")
    r = requests.get(GTFS_URL)
    with open(GTFS_FILE, 'wb') as f:
        f.write(r.content)
    print("Download complete.")

engine = create_engine("postgresql://transit:transit@localhost:5432/transitdb")

with zipfile.ZipFile("GTFSExport.zip", 'r') as z:
    for file in ["stops.txt", "routes.txt", "trips.txt", "stop_times.txt"]:
        with z.open(file) as f:
            df = pd.read_csv(f)
            table_name = "raw_" + file.replace(".txt", "")
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Loaded {table_name} with {len(df)} records.")