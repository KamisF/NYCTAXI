import pyarrow.parquet as pq
trips = pq.read_table('trips.parquet')
trips = trips.to_pandas()

# Ler o .parquet

table2 = pq.read_table('NYCTAXI\YellowTaxiTripRecord\yellow_tripdata_2024-01.parquet')
table2.to_pandas()