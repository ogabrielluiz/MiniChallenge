from datetime import datetime

import requests

from app import app


# Builds the url to contact the OpenWeatherMap API and returns a list of json documents
def get_weather():
    api_key = app.config['API_KEY']
    cidade = 'Ribeirão+Preto'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={cidade}' + f'&APPID={api_key}' + "&units=metric"

    response = requests.get(url)
    data = response.json()

    five_day_forecast = [x for x in data['list']]
    return five_day_forecast

# Converts the data in UNIX format to Python's datetime format
def convert_date(date):
    timestamp = int(date)
    date = datetime.utcfromtimestamp(timestamp)
    return date

# Prepares the data to be accessed by the app, also gets the 40
# observations(one every 3 hours per day) and joins all the data
# into 5 observations, one for each day.

def prepare_data(listed_data):
    prepared_data = []
    for observation in listed_data:
        for obs in listed_data:
            if observation != obs:
                if observation.date == obs.date:
                    observation.set_data(obs, avg=True)

        prepared_data.append(observation)
        if len(prepared_data) > 1:
            if observation.date == prepared_data[-2].date:
                prepared_data[-2].set_data(observation, avg=True)
                del prepared_data[-1]

    prepared_data = set_avgs_on_all_days(prepared_data)
    prepared_data = set_rain_forecast(prepared_data)
    prepared_data = set_max_min_temp(prepared_data)

    return prepared_data

# A list of observations is passed and the average of each type of data calculated
# and set to their respective attribute.
def set_avgs_on_all_days(data):
    for day in data:
        avg_humidity = sum(day.humidity) / len(day.humidity)
        avg_wind_speed = sum(day.wind_speed) / len(day.wind_speed)
        avg_wind_deg = sum(day.wind_deg) / len(day.wind_deg)
        avg_cloudiness = sum(day.cloudiness) / len(day.cloudiness)
        avg_pressure = sum(day.pressure) / len(day.pressure)

        day.avg_humidity = int(avg_humidity)
        day.avg_wind_speed = round(avg_wind_speed, 2)
        day.avg_wind_deg = int(avg_wind_deg)
        day.avg_cloudiness = int(avg_cloudiness)
        day.avg_pressure = round(avg_pressure, 2)

    return data

# Gets the minimum and the maximum temperature for each day and sets them to their respective attribute.
def set_max_min_temp(data):
    for day in data:
        lowest = min(day.temp_min)
        highest = max(day.temp_max)

        day.temp_min = lowest
        day.temp_max = highest
    return data


def set_rain_forecast(data):
    for day in data:
        day.get_rain_forecast()

    return data

# A function that receives a datetime object and returns the equivalent day of the week.
def get_weekday(day):
    date = day.weekday()
    if date == 0:
        return "Monday"
    if date == 1:
        return "Tuesday"
    if date == 2:
        return "Wednesday"
    if date == 3:
        return "Thursday"
    if date == 4:
        return "Friday"
    if date == 5:
        return "Saturday"
    if date == 6:
        return "Sunday"
