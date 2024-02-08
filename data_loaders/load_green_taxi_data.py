import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url1 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url2 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url3 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    url_list = [url1, url2, url3]
    final_df = []

       # Best practice is to map data types        
    taxi_dtypes = {
        'VendorID': float,
        'store_and_fwd_flag': str,
        'RatecodeID': float,
        'PULocationID': int,
        'DOLocationID': int,
        'passenger_count': float,
        'trip_distance': float,
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'ehail_fee': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'payment_type': float,
        'trip_type': float,        
        'congestion_surcharge': float
    }
    for url in url_list:        
        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        df = pd.read_csv(url, sep=",", compression = "gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        print(df.shape)
        final_df.append(df)

    final_df = pd.concat(final_df)

    print(final_df.shape)
    
    return final_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
