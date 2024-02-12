import matplotlib.pyplot as plt
import numpy as np
import math

# Creating a dictionary of allowed names from the math module excluding dunder names
ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

def plot_expression(expression):
    x = np.linspace(-10, 10, 400)
    y_values = []  # Initializing an empty list to store y values
    for x_value in x:
        # Evaluating the expression for each x value using allowed names and appending to y_values
        y_values.append(eval(expression, {**ALLOWED_NAMES, 'x': x_value}))


    plt.plot(x, y_values)
    plt.title('Graph of expression: {}'.format(expression))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(-10, 11, 1))  # Setting x-axis ticks
    plt.yticks(np.arange(-10, 11, 1))  # Setting y-axis ticks
    plt.tick_params(axis='x', direction='in', length=6, width=2)
    plt.tick_params(axis='y', direction='in', length=6, width=2)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)

    # Adding bold black lines representing the x and y axes
    plt.axhline(0, color='black', linewidth=2)
    plt.axvline(0, color='black', linewidth=2)

    plt.show()

# Getting user input for the expression to be plotted
user_input = input("Enter the expression: ")
plot_expression(user_input)







