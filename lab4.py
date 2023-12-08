def parabola(x):
    return x**2

# Функция для численного интегрирования методом прямоугольников
def integrate_rectangles(func, a, b, n):
    delta_x = (b - a) / n
    result = 0
    for i in range(n):
        x_i = a + i * delta_x
        result += func(x_i) * delta_x
    return result

a, b = 0, 10
num_rectangles = 100


length = integrate_rectangles(lambda x: (1 + (parabola(x))**2)**0.5, a, b, num_rectangles)

print(f"Длина параболы на интервале от 0 до 10: {length}")