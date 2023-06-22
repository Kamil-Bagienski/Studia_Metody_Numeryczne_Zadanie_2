#Kamil Bagieński, numer indeksu 155623, grupa D1
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Poly

# Dane
x = np.array([-1, 0, 1, 2])
y = np.array(input("Podaj wartości punktów y, oddzielone spacją: ").split(), dtype=float)

# Funkcja pomocnicza
def interpolacja(xi, x, y):
    n = len(x)
    L = np.zeros(n)
    for i in range(n):
        L[i] = np.prod([(xi - x[j]) / (x[i] - x[j]) for j in range(n) if j != i])
    return np.sum(L * y)

# Wyznaczenie wartości
xi = np.linspace(min(x), max(x), 100)
yi = np.array([interpolacja(xi_i, x, y) for xi_i in xi])

# Dodanie dodatkowych punktów 
x_kst = np.concatenate(([x[0]-1], x, [x[-1]+1]))
y_kst = np.concatenate(([y[0]], y, [y[-1]]))

# Wyznaczenie wartości ekstrapolowanych
xi_kst = np.linspace(min(x)-2, max(x)+2, 100)
yi_kst = np.array([interpolacja(xi_i, x_kst, y_kst) for xi_i in xi_kst])

plt.xlim(min(x)-4, max(x)+4)
plt.ylim(min(y)-4, max(y)+4)

# Rysowanie
plt.plot(x, y, 'o', color='green', label='Węzły interpolacyjne')
plt.plot(xi_kst, yi_kst, color='blue', label='Wielomian ekstrapolacyjny')
plt.plot(xi, yi, color='orange', label='Wielomian interpolacyjny')

# Wyznaczenie i formatowanie równania wielomianu interpolacyjnego
x_sym = symbols('x')
p = Poly(np.polyfit(x, y, len(x)-1), x_sym)
p_str = str(p.as_expr().evalf(round(2))).replace("**", "^")

plt.plot([],[], ' ', label=f'$Wielomian:\ {p_str}$')

plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.legend(loc='lower right')
plt.title('Interpolacja wielomianowa')
plt.xlabel('x')
plt.ylabel('y')
plt.show()