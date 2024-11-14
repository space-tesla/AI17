#Q.1) Python program that demonstrates the hill climbing algorithm to find the maximum of a mathematical function.**


def hill_climbing(func, x_start, step_size=0.1, max_iter=100):
    x = x_start
    for _ in range(max_iter):
        next_x = x + step_size
        if func(next_x) > func(x):
            x = next_x
        else:
            break
    return x, func(x)

def function(x):
    return -x**2 + 4*x

x_max, y_max = hill_climbing(function, x_start=0)
print("Maximum x:", x_max)
print("Maximum f(x):", y_max)


"""Output:

Maximum x: 2.0
Maximum f(x): 4.0
"""


