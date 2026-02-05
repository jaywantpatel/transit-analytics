import requests
import time
from datetime import datetime
from sqlalchemy import create_engine, text 

engine = create_engine("postgresql://transit:transit@localhost:5432/transitdb")

URL = "https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-vp/beta/v1/VehiclePositions"

while True:
    try:
        r = requests.get(URL, timeout=10)
        data = r.content

        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO raw_vehicle_positions (fetched_at, data)
                    VALUES (:fetched_at, :data)
                """),
                {
                    "fetched_at": datetime.utcnow(),
                    "data": data
                }
            )

        print("Fetched at", datetime.utcnow())

    except Exception as e:
        print("Error during fetch:", e)
    
    time.sleep(30)  # Fetch every 30 seconds
