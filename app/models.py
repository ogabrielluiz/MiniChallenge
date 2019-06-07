from app.util import convert_date, get_weekday


class Forecast:

    def __init__(self):
        self.date = None
        self.hour = []
        self.humidity = []
        self.temp_min = None
        self.temp = None
        self.temp_max = None
        self.cloudiness = []
        self.wind_speed = []
        self.wind_deg = []
        self.pressure = []
        self.text = []
        self.avg_humidity = None
        self.weekday = ''
        self.umbrella = False

    def set_data(self, data, avg):
        if avg:
            self.humidity.append(data.humidity[0])
            self.hour.append(data.hour[0])
            self.cloudiness.append(data.cloudiness[0])
            self.wind_speed.append(data.wind_speed[0])
            self.wind_deg.append(data.wind_deg[0])
            self.pressure.append(data.pressure[0])
        else:
            date = convert_date(data['dt'])
            self.humidity.append(data['main']['humidity'])
            self.date = str(date.date().strftime('%d/%m'))
            self.hour.append(date.hour)
            self.temp_max = int(data['main']['temp_max'])
            self.temp = int(data['main']['temp'])
            self.temp_min = int(data['main']['temp_min'])
            self.cloudiness.append(data['clouds']['all'])
            self.wind_speed.append(data['wind']['speed'])
            self.wind_deg.append(data['wind']['deg'])
            self.pressure.append(data['main']['pressure'])
            self.weekday = get_weekday(date)

    def get_rain_forecast(self):

        if self.avg_humidity == 0:
            self.text = "No chance of rain"
        elif self.avg_humidity < 15:
            self.text = "Slight chance of isolated rains"
        elif 15 <= self.avg_humidity < 30:
            self.text = "A small chance of rain"
        elif 30 <= self.avg_humidity < 60:
            self.text = "A small chance of rain"
        elif 60 <= self.avg_humidity < 80:
            self.text = "Scattered rain"
        elif 80 <= self.avg_humidity:
            self.text = "Rainy (strong or weak)"
        if self.avg_humidity > 70:
            self.umbrella = True

