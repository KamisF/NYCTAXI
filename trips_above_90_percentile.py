import pyarrow.parquet as pq
import pandas as pd


#ler o arquivo .parquet
trips = pq.read_table('yellow_tripdata_2024-01.parquet')
#vou me referir a tabela sendo df de dataframe
df = trips.to_pandas()

#filtrar a coluna trip distance e usar a funcao quantile por se tratar de um float.
percentile_90 = df['trip_distance'].quantile(0.9)

#filtrar a coluna trip distance e filtrar tudo acima de 0.9.
trips_above_90_percentile = df[df['trip_distance'] > percentile_90]

print(trips_above_90_percentile)
