# Reggie's Linear Regression

This project implements a simple linear regression model using a brute force approach to find the optimal slope and intercept for a best-fit line.

---

## Overview

The linear regression model finds the line (y = mx + b) that best fits a set of datapoints by minimizing the total error between the predicted values and actual values.

---

## Files

- `Reggie_Linear_Regression.py`: Main implementation of the linear regression algorithm  
- `data.py`: Contains training and test datapoints  
- `test.py`: Unit tests for the implementation

---

## Functionality

The implementation includes:

- **Linear Function**: Calculates y values using the formula y = mx + b  
- **Error Calculation**: Measures the absolute difference between predicted and actual values  
- **Model Optimization**: Tests multiple slope and intercept values to find the combination with minimal error

---

## How to Use
```
# Import the necessary functions
from Reggie_Linear_Regression import get_y, calculate_error, calculate_all_error

# Use the existing trained model
# The script automatically prints the best slope and intercept
# as well as a prediction for a ball with width 6cm

# To make your own predictions
from Reggie_Linear_Regression import best_m, best_b, get_y
prediction = get_y(best_m, best_b, x_value)
```

### Running the Tests

Execute the test suite by running:

`python test.py`

The tests verify the functionality of the core methods used in the linear regression implementation.

---

## Implementation Details

The algorithm works by:

- Trying a range of slopes from -10 to 10 (in 0.1 increments)  
- Trying a range of intercepts from -20 to 20 (in 0.1 increments)  
- Calculating the total error for each combination  
- Selecting the slope and intercept with the smallest total error  

This brute force approach is educational but would not be efficient for large datasets.
