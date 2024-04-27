import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from app.models import TickerData

def read_json_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Load JSON data from the file
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def json_data_to_db(json_data):
    ticker = json_data['ticker']
    results = json_data['results']
    for result in results:
        v = result['v']
        o = result['o']
        c = result['c']
        h = result['h']
        l = result['l']
        t = result['t']

        item = TickerData(ticker=ticker, date=t, openprice=o, closeprice=o, high=h, low=l, volume=v)
        item.save();
    

file_path = './data.json'  # Replace with your actual file path
json_data = read_json_from_file(file_path)
json_data_to_db(json_data)
TickerData.objects.all().values()