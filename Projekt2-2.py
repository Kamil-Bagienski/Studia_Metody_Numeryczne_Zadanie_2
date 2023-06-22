#Kamil Bagieński, nr indeksu 155623, grupa D1

import numpy as np
import matplotlib.pyplot as plt

# Dane
x = np.array([-1,0,1,2])
y = np.array(input("Podaj wartości punktów y, oddzielone spacją: ").split(), dtype=float)

# Wybór stopnia wielomianu
while True:
    stopien = int(input("Wybierz stopień wielomianu aproksymującego (1, 2 lub 3): "))
    if stopien == 1 or stopien == 2 or stopien == 3:
        break
    print("Nieprawidłowy wybór. Wybierz stopień 2 lub 3.")

# Wyznaczenie współczynników 
wielomian = np.polyfit(x, y, stopien)

# Wyznaczenie wartości 
xi = np.linspace(min(x), max(x), 100)
yi = np.polyval(wielomian, xi)

plt.xlim(min(x)-4, max(x)+4)
plt.ylim(min(y)-4, max(y)+4)

# Rysowanie
plt.plot(x, y, 'o', label='Węzły')
plt.plot(xi, yi, label='Wielomian aproksymujący')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.legend(loc='best')
plt.title('Aproksymacja wielomianowa')
plt.xlabel('x')
plt.ylabel('y')
plt.show()