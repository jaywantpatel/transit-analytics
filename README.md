# Ottawa Transit Reliability Analytics Platform

This project builds an end-to-end data engineering pipeline ingesting GTFS static and GTFS realtime vehicle feeds from OC Transpo into a PostgreSQL warehouse using Docker and Python.

The system continuously collects live vehicle telemetry every 30 seconds and stores raw transit data for later modeling, delay analysis, and dashboard visualization.

## Tech Stack

- Python (pandas, requests, sqlalchemy)
- PostgreSQL
- Docker
- GTFS Static + Realtime feeds

## How to Run

```bash
docker compose up -d
pip install -r requirements.txt
python ingestion/static_gtfs_loader.py
python ingestion/realtime_fetcher.py
