'''
POST_DATA = {
    "flightWay":"Oneway",
    "classType":"ALL",
    "searchIndex":1,
    "airportParams":[
        {
            "dcity":"SZX",
            "acity":"SHA",
            "date":"2019-10-11"
        }
    ],
    "token":"536bc24712ea27bb5109f78178533ba7"
}
'''

import requests
from requests.exceptions import HTTPError
import json
from datetime import datetime, timedelta


POST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'referer': 'https://flights.ctrip.com/itinerary/oneway/sha-sia'
}
POST_TIMEOUT = 5
POST_URL = 'https://flights.ctrip.com/itinerary/api/12808/products'


def get_post_data(dcity='SHA', acity='SIA', days=0, flight_way='Oneway', class_type='ALL'):
    airport_params = []
    qdate = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
    airport_params.append(dict(dcity=dcity, acity=acity, date=qdate))
    post_data = {}
    post_data = dict(flightWay=flight_way, classType=class_type, searchIndex=1, airportParams=airport_params, token='536bc24712ea27bb5109f78178533ba7')
    return post_data


def get_route_list(post_data):
    try:
        r = requests.post(POST_URL, headers=POST_HEADERS, json=post_data, timeout=POST_TIMEOUT)
        r.raise_for_status()
        flight_data = r.json()
        if flight_data and flight_data.get('msg') == 'success':
            return flight_data.get('data').get('routeList')
    except HTTPError as e:
        print('{0} requests ERROR!'.format(POST_URL))
        print(e)


def parser_route_list(route_list, route_data):
    for route in route_list:
        if route.get('routeType') == 'Flight':
            leg = route.get('legs')[0]
            flight_id = leg.get('flightId')
            leg_type = leg.get('legType')

            #航班价格信息
            characteristic = leg.get('characteristic')
            lowest_price = characteristic.get('lowestPrice')
            lowest_child_price = characteristic.get('lowestChildPrice')

            #航班信息
            flight = leg.get('flight')
            airline_code = flight.get('airlineCode')
            airline_name = flight.get('airlineName')
            flight_number = flight.get('flightNumber')
            departure_date = flight.get('departureDate')
            arrival_date = flight.get('arrivalDate')
            punctuality_rate = flight.get('punctualityRate')
            craft_kind = flight.get('craftKind')
            craft_type_code = flight.get('craftTypeCode')
            craft_type_kind_display_name = flight.get('craftTypeKindDisplayName')
            craft_type_name = flight.get('craftTypeName')
            duration_days = flight.get('durationDays')
            fid = flight.get('id') 
            meal_flag = flight.get('mealFlag')
            meal_type = flight.get('mealType')
            shared_flight_name = flight.get('sharedFlightName')
            shared_flight_number = flight.get('sharedFlightNumber')
            if shared_flight_name is not None:
                shared_flight = True
            else:
                shared_flight = False

            #到达机场信息
            arrival_airport_info = leg.get('flight').get('arrivalAirportInfo')
            arrival_airport_name = arrival_airport_info.get('airportName')
            arrival_airport_tlc = arrival_airport_info.get('airportTlc')
            arrival_city_name = arrival_airport_info.get('cityName')
            arrival_city_tlc = arrival_airport_info.get('cityTlc')
            arrival_terminal_name = arrival_airport_info.get('terminal').get('name')
            arrival_terminal_id = arrival_airport_info.get('terminal').get('id')
            arrival_terminal_short_name = arrival_airport_info.get('terminal').get('shortName')

            #起飞机场信息
            departure_airport_info = leg.get('flight').get('departureAirportInfo')
            departure_airport_name = departure_airport_info.get('airportName')
            departure_airport_tlc = departure_airport_info.get('airportTlc')
            departure_city_name = departure_airport_info.get('cityName')
            departure_city_tlc = departure_airport_info.get('cityTlc')
            departure_terminal_name = departure_airport_info.get('terminal').get('name')
            departure_terminal_id = departure_airport_info.get('terminal').get('id')
            departure_terminal_short_name = departure_airport_info.get('terminal').get('shortName')

            route_data.append((airline_name, flight_number, lowest_price, departure_date, departure_airport_name, departure_terminal_name, arrival_date, arrival_airport_name, arrival_terminal_name, punctuality_rate, shared_flight_name, shared_flight_number, craft_type_name, craft_type_kind_display_name, meal_flag))
#            print((airline_name, flight_number, lowest_price, departure_date, departure_city_name, departure_airport_name, departure_terminal_name, arrival_date, arrival_city_name, arrival_airport_name, arrival_terminal_name, punctuality_rate, shared_flight, shared_flight_name, shared_flight_number, craft_type_name, craft_type_kind_display_name, meal_flag))
    return route_data

def print_route_data(route_data):
    for route in route_data:
        print(route)


def main():
    post_data = get_post_data(days=2)
    route_list = get_route_list(post_data)
    route_data = []
    parser_route_list(route_list, route_data)
    print_route_data(route_data)


if __name__ == '__main__':
    main()