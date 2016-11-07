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
