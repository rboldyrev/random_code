import numpy as np
import matplotlib.pyplot as plt


#Функция, которая возращает количество нулей в конце значения соответствующего факториала
def f_zeros(n):
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

#Считаем набор значений
length = 200
n = range(length)
y = []
for i in n:
    y.append(f_zeros(i))

#Определяем угловой коэфициент
k = y[length-1]/length

#Вычисляем прямую с угловым коэфициентом 
x0 = np.linspace(0, length, length)
y0 = k * x

#Строим графики
plt.plot(n,y, label = f'tg(a) = {k}')
plt.plot(x0,y0)
plt.legend()
plt.savefig('pic.png', dpi = 300)
plt.show()
