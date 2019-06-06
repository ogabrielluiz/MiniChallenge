from app import app
from flask import render_template
from app.models import Forecast
from app.util import get_weather, prepare_data, create_graph


@app.route('/')
@app.route('/index')
def index():


    data = get_weather()
    list_of_observations = []
    for observation in data:
        fcast = Forecast()
        fcast.set_data(observation, graph=False)
        fcast.get_rain_forecast()
        list_of_observations.append(fcast)

    chart_data = prepare_data(list_of_observations)

    chart_list = create_graph(chart_data)

    return render_template('index.html', chart_data=chart_data, chart_list=chart_list)


if __name__ == '__main__':
    app.run()
