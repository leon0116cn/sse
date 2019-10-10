import requests
from requests.exceptions import HTTPError


CTRIP_POI_URL = "https://flights.ctrip.com/itinerary/api/poi/get"
REQUESTS_HEADERS = {'user-agent': 'Mozilla/5.0'}
REQUESTS_TIMEOUT = 10


def get_flight_poi():
    try:
        r = requests.get(CTRIP_POI_URL, headers=REQUESTS_HEADERS, timeout=REQUESTS_TIMEOUT)
        r.raise_for_status()
        poi_json_data = r.json()
        if poi_json_data and poi_json_data.get('msg') == 'success':
            return poi_json_data.get('data') 
    except HTTPError as e:
        print('{0} requests ERROR!'.format(CTRIP_POI_URL))
        print(e)


def parser_flight_poi(json_data, poi_data):
    for item_first in json_data.values():
        if isinstance(item_first, dict):
            for item_second in item_first.values():
                for item in item_second:
                    poi_item = item.get('data').split('|')
                    poi_item.append(item.get('display'))
                    poi_data.append(poi_item)


def print_flight_poi(poi_data):
    print(poi_data)


def main():
    poi_data = []
    json_data = get_flight_poi()
    parser_flight_poi(json_data, poi_data)
    print_flight_poi(poi_data) 


if __name__ == '__main__':
    main()