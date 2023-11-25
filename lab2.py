import math
def equation(x):
    return x**3 + 2 * x**2 - 8 * x + 1 + 12 * math.sin(x) - 8 * math.cos(x)

def find_intervals(start, end, step):
    intervals = []
    x = start
    while x <= end:
        if equation(x) * equation(x + step) < 0:
            intervals.append((x, x + step))
        x += step
    return intervals

def bisection_method(interval, epsilon):
    a, b = interval
    step_count = 0
    while (b - a) >= epsilon:
        mid = (a + b) / 2
        if equation(mid) == 0.0:
            return mid, step_count
        elif equation(mid) * equation(a) < 0:
            b = mid
        else:
            a = mid
        step_count += 1
    return round((a + b) / 2.0, 3), step_count


start_interval = -5
end_interval = 5
step_size = 0.1
epsilon = 0.001

intervals = find_intervals(start_interval, end_interval, step_size)

for interval in intervals:
    print(f"Interval: {interval}")
    root, steps = bisection_method(interval, epsilon)
    print(f"Root: {root}, Steps: {steps}")



