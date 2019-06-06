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
        self.weekday = None

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
            self.date = str(date.date().strftime('%d-%m'))
            self.hour.append(date.hour)
            self.temp_max = data['main']['temp_max']
            self.temp = data['main']['temp']
            self.temp_min = data['main']['temp_min']
            self.cloudiness.append(data['clouds']['all'])
            self.wind_speed.append(data['wind']['speed'])
            self.wind_deg.append(data['wind']['deg'])
            self.pressure.append(data['main']['pressure'])
            self.weekday = get_weekday(date)

    def get_rain_forecast(self):
        for i in range(len(self.humidity)):

            if self.humidity[i] == 0:
                self.text.append("No chance of rain")

            elif self.humidity[i] < 15:
                self.text.append("Slight chance of isolated rains")
            elif 15 <= self.humidity[i] < 30:
                self.text.append("A small chance of rain")
            elif 30 <= self.humidity[i] < 60:
                self.text.append("A small chance of rain")
            elif 60 <= self.humidity[i] < 80:
                self.text.append("Scattered rain")
            elif 80 <= self.humidity[i]:
                self.text.append("Rainy (strong or weak)")

