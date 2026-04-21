# Weather Data Analyzer & Forecast Dashboard

A simple Python-based application that fetches weather data, stores it, and provides basic analysis and predictions.

---

## About the Project

This project focuses on analyzing weather data instead of just displaying it. It collects real-time weather information using an API, stores it in a database, and uses that data to generate trends and simple predictions.

---

## Features

* Fetch real-time temperature and humidity
* Store historical data using SQLite
* Visualize temperature trends using graphs
* Predict next temperature using Linear Regression
* Provide basic insights such as average and maximum temperature
* Simple web interface using Flask

---

## Tech Stack

* Python
* Flask
* SQLite
* Pandas
* Matplotlib
* Scikit-learn

---

## Installation & Setup

1. Clone the repository:

```
git clone <your-repo-link>
```

2. Navigate to the project folder:

```
cd weather-dashboard
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Add your API key in `weather_api.py`:

```
API_KEY = "your_api_key_here"
```

---

## How to Run

Run the application using:

```
python app.py
```

After running, open your browser and go to:

```
http://127.0.0.1:5000/
```

Enter a city name to view weather details, trends, and prediction.

---

## Output

### Home Page

(Add screenshot here)

### Result Page

(Add screenshot here)

---

## How it Works

1. The user enters a city name
2. Weather data is fetched using an API
3. Data is stored in a database
4. A graph is generated from stored data
5. A simple prediction is made using past values

---

## Limitations

* Prediction is basic and intended for learning purposes
* Requires multiple entries to generate meaningful graphs
* API key activation may take a few minutes

---

## Future Improvements

* Add humidity trend visualization
* Improve user interface
* Use more advanced prediction models
* Add multi-day forecasting

---

## Author

Vyshnavi Pola

---

This project was developed as part of a learning exercise to understand APIs, databases, and basic data analysis using Python.
