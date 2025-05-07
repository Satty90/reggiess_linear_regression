import math
from data import datapoints


# Callulating Error
# get_y function
def get_y(m, b, x):
    y = m*x + b
    return y


# calculate_error fucntion
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    distance = get_y(m, b, x_point) - y_point
    return abs(distance)


# calculate_all_error fucntion
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error


# possible slope values between -10 and 10 inclusive
possible_ms = [m/10 for m in range(-100, 101)]

# possible intercept values between -20 and 20 inclusive
possible_bs = [b/10 for b in range(-200, 201)]

# working out the smallest error based on datapoints
smallest_error = math.inf
best_m = 0
best_b = 0
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b


print(f"The best slope for our model is {best_m}")
print(f"The best intercept for our model is {best_b}")
print(
    f"The model predicts the bouce height of a ball a with width 6cm is {get_y(best_m, best_b, 6)}")
print("This model predicts the bounce of all kinds of sizes of balls we can choose to include in the pit ball")
