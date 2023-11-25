import math
def equation(x):
    return x**3 + 2 * x**2 - 8 * x + 1 + 12 * math.sin(x) - 8 * math.cos(x)

def answer(start, end, step):
    curent_start = start
    while curent_start <= end:
        if equation(curent_start) * equation(curent_start + step) < 0:
            print("Intervals: [", curent_start, ";", curent_start + step)
            print("Answer:", round(curent_start, 3))
        curent_start = curent_start + step

start = -5.0000
end = 5.0000
step = 0.0001

answer(start, end, step)