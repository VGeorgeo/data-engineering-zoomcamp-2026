import pandas as pd
# from tqdm.auto import tqdm
from sqlalchemy import create_engine
import numpy as np
import click


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    # Ingestion logic here
    pass


path_trips = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
path_zones = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
df_trips = pd.read_parquet(path_trips)
df_zones = pd.read_csv(path_zones)


## Create Database Connection
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


## create green_tripdata
df_trips.head(n=0).to_sql(name='green_tripdata', con=engine, if_exists='replace')

iterate = np.concat([np.arange(0, df_trips.shape[0], 10000),[df_trips.shape[0]+1] ])
first = True

for start, finish in zip(iterate[:-1], iterate[1:]):

    if first:
        # Create table schema (no data)
        df_trips.loc[start:finish,:].head(0).to_sql(
            name="green_tripdata",
            con=engine,
            if_exists="replace"
        )
        first = False
        print("Table created")

    # Insert chunk
    df_trips.loc[start:finish,:].to_sql(
        name="green_tripdata",
        con=engine,
        if_exists="append"
    )

    print("Inserted:", len(df_trips.loc[start:finish,:]))


## create green_tripdata
dtype = {
    "LocationID": "Int64"}

df_zones = pd.read_csv(
    path_zones,
    dtype=dtype)

df_zones.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace')




