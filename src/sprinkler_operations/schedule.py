import requests
import sys
import json
from datetime import *

service_url = "http://austin-water-rules.mybluemix.net/schedule"


def get_coa_json(address, property_type):
    payload = {'address': int(address), 'type': int(property_type)}
    headers = {"Content-Type":"application/json"}

    r = requests.post(service_url, headers=headers, data=json.dumps(payload))
    request_json = r.json()


def get_if_watering_restriction(address, property_type, time):
    request_json = get_coa_json(address, property_type)
    day = request_json[0]
    times = request_json[1]
    allowed_time = times[u'Watering Times:']
    time_array = allowed_time.split(" ")
    allowed_day = day[u'Watering Day:']

    today = datetime.now().strftime('%A')
    if(allowed_day != today):
        return False

    start_time = datetime.strptime(time_array[0] + " " + time_array[1], '%I:%M %p')
    end_time = datetime.strptime(time_array[3] + " " + time_array[4], '%I:%M %p')
    current_time = datetime.now().hour
    if(current_time > start_time.hour and current_time < end_time.hour):
        return True


def get_next_watering_time(address, property_type):
    return get_coa_json()