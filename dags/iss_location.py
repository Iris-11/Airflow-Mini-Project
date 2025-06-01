from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
import requests

default_args={
        'owner': 'airflow',
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    }
with DAG(
    dag_id="iss_dag",
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
    default_args = default_args
) as dag:
    @task
    def print_iss_location():
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        position = data['iss_position']
        latitude = position['latitude']
        longitude = position['longitude']
        timestamp = data['timestamp']
        print(f"ISS Current Location at {datetime.utcfromtimestamp(timestamp)} UTC:")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        return [latitude,longitude]
    @task
    def reverse_geocode(location):
        lat = location[0]
        long = location[1]
        #OpenStreetMaps free api for reverse geocoding(getting address from lat and long) - https://nominatim.org/release-docs/develop/api/Reverse/
        url = f'https://nominatim.openstreetmap.org/reverse'
        params = {
        'lat': lat,
        'lon': long,
        'format': 'json'
        }
        headers = {
            'User-Agent': 'airflow-demo (ishita,lele11@gmail.com)'
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Extract address info
        address = data.get('display_name', 'No address found')
        print(f"The ISS currently is above: {address}.\n latitude:{lat}\nlongitude:{long}\n :)")
        return address


    location = print_iss_location()
    reverse_geocode(location)

    