# Machine Problem 5

# import numpy
import numpy as np
# import matplot for plotting
import matplotlib.pyplot as plt

# defining the range for the equation
n = np.arange(0,200,1)
form = input("Enter an equation of x: ")
x = eval(form)

for n in range(0,200):
    if n == 0:
        y1 = ((-1.5*x*n) + (2*x*(n + 1)) - (0.5*x*(n+2)))
    elif 0 < n < 198:
        y2 = ((0.5*x*(n+1)) - (0.5*x*(n-1)))
    else:
        y3 = ((1.5*x*n) - (2*x*(n-1)) + (0.5*x*(n-2)))

y = y1 + y2 + y3

# plotting the equation

#naming the x and y axis 
plt.ylabel('y-axis')
plt.xlabel('x-axis')

# naming title for the graph
plt.title('Machine Problem 5')

# plotting x and y
plt.plot(x, label = "x")
plt.plot(y, label = "y")

plt.legend(loc="upper right")

# showing the graph
plt.show
# end of code