import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def run_model():
    data = {
        'ad_budget': [500, 700, 800, 1200, 1500, 2000],
        'units_sold': [50, 65, 80, 110, 140, 200]
    }
    df = pd.DataFrame(data)

    X = df[['ad_budget']]
    y = df['units_sold']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("Predictions:", predictions)
    print("MSE:", mean_squared_error(y_test, predictions))

if __name__ == "__main__":
    run_model()
