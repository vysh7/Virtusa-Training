import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def plot_graph(df):
    if len(df) == 0:
        return

    plt.figure()

    plt.plot(df['temperature'])
    plt.title("Temperature Trend")

    plt.savefig("static/temp_plot.png")
    plt.close()


def predict_temp(df):
    if len(df) < 2:
        return df['temperature'].iloc[-1]

    X = np.arange(len(df)).reshape(-1, 1)
    y = df['temperature'].values

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(df)]])
    prediction = model.predict(next_day)

    return prediction[0]