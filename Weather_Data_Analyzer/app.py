from flask import Flask, render_template, request
from weather_api import get_weather
from database import init_db, store_data, get_data
from analysis import plot_graph, predict_temp

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    city = request.form['city']

    data = get_weather(city)

    if data:
        temp = data['temp']
        humidity = data['humidity']

        # store data in DB
        store_data(city, temp, humidity)

        # fetch historical data
        df = get_data(city)

        # create graph
        plot_graph(df)

        # prediction
        prediction = predict_temp(df)

        # simple insights
        avg_temp = round(df['temperature'].mean(), 2)
        max_temp = df['temperature'].max()

        insight = "Temperature seems stable"
        if temp > avg_temp:
            insight = "Temperature is higher than average"
        else:
            insight = "Temperature is lower than average"

        return render_template(
            'result.html',
            city=city,
            temp=temp,
            humidity=humidity,
            prediction=round(prediction, 2),
            avg_temp=avg_temp,
            max_temp=max_temp,
            insight=insight
        )

    return "Error fetching data"

if __name__ == '__main__':
    app.run(debug=True)