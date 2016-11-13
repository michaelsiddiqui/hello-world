# for command line execution
# of check_the_weather

from weather.weather import check_the_weather
import sys


def main(location):
    output = check_the_weather(location)
    return output

if __name__ == "__main__":
    if len(sys.argv) > 1:
        location = sys.argv[1]
    else:
        location = ''
    weather_info = main(location)
    print weather_info
