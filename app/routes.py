from app import app
from flask import render_template
from app.models import Forecast
from app.util import get_weather, prepare_data
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():

    data = get_weather()
    list_of_observations = []
    for observation in data:
        fcast = Forecast()
        fcast.set_data(observation, avg=False)
        list_of_observations.append(fcast)

    prepared_data = prepare_data(list_of_observations)

    today_date = datetime.today().date().strftime('%d/%m')

    return render_template('index.html', prepared_data=prepared_data, today_date=today_date)


if __name__ == '__main__':
    app.run()
