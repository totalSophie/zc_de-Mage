import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f"Preprocessing: Rows with zero passengers {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: Rows with zero trip miles {data['trip_distance'].isin([0]).sum()}")


    # Rename columns
    data.columns = [camel_to_snake(col) for col in data.columns]

    # Convert the timestamp column to a datetime object
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime'])
    data['lpep_dropoff_date'] = pd.to_datetime(data['lpep_dropoff_datetime'])
    filtered_df = data[(data['lpep_pickup_date'].dt.date == pd.to_datetime('2019-09-18').date()) &(data['lpep_dropoff_date'].dt.date == pd.to_datetime('2019-09-18').date())]

    filtered_data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    #print(filtered_data)

        # Get distinct values from the 'vendor_id' column
    print(filtered_data['vendor_id'].unique())

    return filtered_data

# Function to convert Camel Case to Snake Case
def camel_to_snake(column_name):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    return s2.replace(" ", "_")  # Replace spaces with underscores




@test
def test_vendor_id(output, *args) -> None:
    assert 2.0 in output['vendor_id'].values, "vendor_id must be one of the existing values in the column"

@test
def test_passenger_count(output, *args) -> None:
    assert (output['passenger_count'] > 0).all(), "passenger_count must be greater than 0"


@test
def test_trip_distance(output, *args) -> None:
    assert (output['trip_distance'] > 0).all(), "trip_distance must be greater than 0"

