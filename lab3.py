import matplotlib.pyplot as plt
import numpy as np

def calculate_area(x1, x2, f1, f2, h=0.001):
    x = x1
    S = 0
    while x < x2:
        S += h * (f1(x) - f2(x))
        x += h
    return S


f1 = lambda x: x**3 + 2*x**2 - 8*x + 1
f2 = lambda x: -12 * np.sin(x) + 8 * np.cos(x)


x1_interval1 = -4.495
x2_interval1 = -1.386
x1_interval2 = -1.386
x2_interval2 = 0.850


area1 = calculate_area(x1_interval1, x2_interval1, f1, f2)
area2 = calculate_area(x1_interval2, x2_interval2, f1, f2)
total_area = area1 + area2


x1 = np.linspace(-5, 5, 1000)
y1 = f1(x1)
y2 = f2(x1)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x1, y1, label='y1 = x^3 + 2x^2 - 8x + 1')
ax.plot(x1, y2, label='y2 = -12sin(x) + 8cos(x)')


ax.fill_between(x1[(x1 >= x1_interval1) & (x1 <= x2_interval1)], y1[(x1 >= x1_interval1) & (x1 <= x2_interval1)], y2[(x1 >= x1_interval1) & (x1 <= x2_interval1)],
                interpolate=True, alpha=0.3, color='gray', label='Shaded Area 1')

ax.fill_between(x1[(x1 >= x1_interval2) & (x1 <= x2_interval2)], y1[(x1 >= x1_interval2) & (x1 <= x2_interval2)], y2[(x1 >= x1_interval2) & (x1 <= x2_interval2)],
                interpolate=True, alpha=0.3, color='blue', label='Shaded Area 2')


legend_text = f'Total Area = {total_area:.4f}'
ax.text(0.5, 0.02, legend_text, transform=ax.transAxes, fontsize=10, ha='center')

ax.legend()
plt.show()