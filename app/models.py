from app.util import convert_date, get_weekday


class Forecast:

    def __init__(self):
        self.date = None
        self.hour = []
        self.humidity = []
        self.temp_min = []
        self.temp = []
        self.temp_max = []
        self.cloudiness = []
        self.wind_speed = []
        self.wind_deg = []
        self.pressure = []
        self.text = []
        self.avg_humidity = None
        self.avg_wind_speed = None
        self.avg_wind_deg = None
        self.avg_cloudiness = None
        self.avg_pressure = None
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
            self.temp_max.append(int(data.temp_min[0]))
            self.temp_min.append(int(data.temp_max[0]))

        else:
            date = convert_date(data['dt'])
            self.humidity.append(data['main']['humidity'])
            self.date = str(date.date().strftime('%d/%m'))
            self.hour.append(date.hour)
            self.temp_max.append(int(data['main']['temp_max']))
            self.temp = int(data['main']['temp'])
            self.temp_min.append(int(data['main']['temp_min']))
            self.cloudiness.append(data['clouds']['all'])
            self.wind_speed.append(data['wind']['speed'])
            self.wind_deg.append(data['wind']['deg'])
            self.pressure.append(data['main']['pressure'])
            self.weekday = get_weekday(date)

    def get_rain_forecast(self):

        if self.avg_humidity == 0:
            self.text = "No chance of rain"
        elif self.avg_humidity < 20:
            self.text = "Slight chance of isolated rains"
        elif self.avg_humidity < 30:
            self.text = "A small chance of rain"
        elif self.avg_humidity < 60:
            self.text = "A small chance of rain"
        elif self.avg_humidity < 80:
            self.text = "Scattered rain"
        elif self.avg_humidity <= 100:
            self.text = "Rainy (strong or weak)"

        if self.avg_humidity > 70:
            self.umbrella = True
