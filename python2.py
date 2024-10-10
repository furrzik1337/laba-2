'''прямая y = 3 (x<-3)

окружность (x-0)^2+(y-3)^2=9
y = 3+sqrt(9-x^2) -3<=x<3

y =kx+b

вторая прямая  -2x - 9 ; 3<=x<6


последняя прямая y =kx+b

x-9; 6<=x<=11'''

from math import *
x = float (input('x='))

if x < -3: y = 1

if x >= -3 and x < 3: y = 3+sqrt(9-x**2)

if x >= 3 and x < 6: y = -2*x - 9

if x >= 6: y = x - 9

print('X={0:.2f}    Y={1:2f}'.format(x,y))