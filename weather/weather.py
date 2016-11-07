# module containing simple functions
# to wrap API calls to wunderground.com
# and return information about the weather

import json
import sys
import os
import requests

# set globals for GET request
API_KEY = os.environ["WUNDERGROUND_KEY"]
url_root = 'http://api.wunderground.com/api/'
geo_conditions = '/geolookup/conditions/q/'


# ask user location choice
def interactive_location():
    '''helper function to ask the user for what location
    would he/sheS like to check the weather conditions
    '''
    print 'choose where to check the weather'
    location = raw_input('location: ')

    # wunderground can choose location by ip address
    if location in ['here', '']:
        location = 'autoip'
    return location


# function to check the weather via
# an API call to wunderground
def check_the_weather(location=''):
    """check the current weather and temp
    for a specified location
    """
    if not location:
        location = interactive_location()
    url = url_root + API_KEY + geo_conditions + location
    response = requests.get(url + '.json')
    weather_dict = json.loads(response.content)
    try:
        city = weather_dict['location']['city']
        state = weather_dict['location']['state']
        temp = weather_dict['current_observation']['temperature_string']
        weather = weather_dict['current_observation']['weather']
    except:
        error = "something didn't work"
        return error
    line1 = "Weather for " + city + ', ' + state + ' is'
    line2 = weather + ' and the temperature is ' + temp
    output_string = line1 + '\n' + line2
    return output_string

