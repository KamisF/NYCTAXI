import pyarrow.parquet as pq
import pandas as pd

trips = pq.read_table('yellow_tripdata_2024-01.parquet')
trips = trips.to_pandas()
print(trips)