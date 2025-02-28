import sys
import pandas as pd
import altair as alt
import update.py

def train(mil):
    df = pd.read_csv("data.csv")
    data = df.copy()

    mil = (mil - df["km"].min()) / (df["km"].max() - df["km"].min())
    df["km"] = (df["km"] - df["km"].min()) / (df["km"].max() - df["km"].min()) #max-min method

    theta0 = theta1 = 0
    m = df["km"].size
    learningRate = 0.01

    for _ in range(10000):
        t0 = t1 = 0
        for row in df.itertuples(index=False):
            t0 += update(row[0], theta0, theta1) - row[1] #[0] is km | [1] is price
            t1 += (update(row[0], theta0, theta1) - row[1]) * row[0]
        theta0 -= (learningRate * t0) / m
        theta1 -= (learningRate * t1) / m

    chart = alt.Chart(data).mark_point().encode(x=alt.X('km'), y=alt.Y('price'))
    chart = (chart + chart.transform_regression('km', 'price').mark_line())
    return (theta0, theta1, mil, chart)


if __name__=='__main__':
    try:
        mil = int(input("the mileage: "))
        trained = train(mil)
        print(trained)
        estimatedPrice = update(trained[2], trained[0], trained[1])
        (trained[3] + alt.Chart(pd.DataFrame({'km': [mil], 'price': [estimatedPrice]})).mark_point(color='red').encode(x='km', y='price')).display()
        print(f"estimated price is {estimatedPrice}")
    except IOError:
        print("unreadable file or invalid input for milage")


