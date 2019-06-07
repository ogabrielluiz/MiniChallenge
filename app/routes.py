from datetime import datetime

from flask import render_template

from app import app
from app.models import Forecast
from app.util import get_weather, prepare_data


@app.route('/')
@app.route('/index')
def index():
    data = get_weather()
    list_of_observations = []
    umbrella_days = []
    for observation in data:
        fcast = Forecast()
        fcast.set_data(observation, avg=False)
        list_of_observations.append(fcast)

    prepared_data = prepare_data(list_of_observations)

    today_date = datetime.today().date().strftime('%d/%m')

    for day in prepared_data:
        if day.umbrella:
            umbrella_days.append(day.date)

    if len(umbrella_days) > 1:
        phrase = "You should take an umbrella in these days:"
    else:
        phrase = "You should take an umbrella on the following day:"

    umbrella_days = ','.join(umbrella_days)

    return render_template('index.html',
                           prepared_data=prepared_data,
                           today_date=today_date,
                           umbrella_days=umbrella_days, phrase=phrase)


if __name__ == '__main__':
    app.run()
