import matplotlib.pyplot as plt 

y = [0, 2, 4, 6, 8, 10, 12, 14]

plt.plot(y)
plt.xlabel("Days")
plt.ylabel("Number of Newly Infected People")
plt.axis( [0, 8, 0, 15] )
plt.grid()
plt.show() 

