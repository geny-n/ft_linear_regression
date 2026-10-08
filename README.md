# ft_linear_regression
Install matplotlib :
```pip3 install matplotlib```

If pip3 doesn't exist :
```python3 -m pip install matplotlib```

## Train model

Trains the linear regression model using data.csv. It calculates theta0 and theta1 (result.csv + fig.png).

price = theta0 + theta1 * km

```python3 train_model.py```

## Predict price
Use theta0 and theta1 to predict the price of a car based on its mileage.
If the program runs before the train model (theta0 = 0, theta1 = 0), regardless of the mileage, the result will be 0.

```python3 predict_price.py```

## Precition
It's used to check if the line is correct.

```python3 precision.py```
