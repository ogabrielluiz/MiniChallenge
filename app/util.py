import requests
from pygal.style import CleanStyle

from app import app
from datetime import datetime
import pygal


def get_weather():
    API_KEY = app.config['API_KEY']
    cidade = 'Ribeirão+Preto'
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={cidade}' + f'&APPID={API_KEY}' + "&units=metric"

    response = requests.get(url)
    data = response.json()

    five_day_forecast = [x for x in data['list']]
    return five_day_forecast


def convert_date(date):
    timestamp = int(date)
    date = datetime.utcfromtimestamp(timestamp)
    return date


# def create_graph(prepared_data):
#     chart_list = []
#     for data in prepared_data:
#         title = f'{data.date}'
#         chart = pygal.Line(width=800,
#                            height=600,
#                            range=(0, 100),
#                            title=title,
#                            style=CleanStyle)
#         chart.x_labels = data.hour
#         chart.add('Humidity in %', data.humidity)
#
#         chart_list.append(chart)
#
#     return chart_list


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

    set_avg_hu_on_all_days(prepared_data)
    return prepared_data

def set_avg_hu_on_all_days(data):

    for day in data:
        avg_humidity = sum(day.humidity) / len(day.humidity)
        day.avg_humidity = int(avg_humidity)

    return data


def get_weekday(date):
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
