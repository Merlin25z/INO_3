import numpy as np
import matplotlib.pyplot as plt

# Создаем массив x с шагом 0.01
xarr = np.arange(0, 4, 0.01)

# Определяем функцию y(x)
def y(x):
    return np.cos(20 * x) / (x + 0.1)

# Вычисляем y для всех значений xarr
yarr = y(xarr)

# Функция для построения графика
def plot_function(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции y(x) = cos(20x) / (x + 0.1)')
    plt.grid(True)
    plt.show()

# Вызываем функцию для построения графика
plot_function(xarr, yarr)