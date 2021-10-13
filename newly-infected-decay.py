import matplotlib.pyplot as plt 

plt.figure(figsize=(6,9))
days = 3
yValues1 = []
yValues2 = []
yValues3 = []
yValues4 = []
yValues5 = []
yValues6 = []

for x in range(days + 1):
    y1 = 10 * 1 ** x
    y2 = 10 * 0.75 ** x
    y3 = 10 * 0.5 ** x
    y4 = 10 * 0.25 ** x
    y5 = 10 * 0.125 ** x
    y6 = 10 * 0 ** x
    yValues1.append(y1)
    yValues2.append(y2)
    yValues3.append(y3)
    yValues4.append(y4)
    yValues5.append(y5)
    yValues6.append(y6)
    
plt.plot(yValues1)
plt.plot(yValues2)
plt.plot(yValues3)
plt.plot(yValues4)
plt.plot(yValues5)
plt.plot(yValues6)
plt.xlabel("Days")
plt.ylabel("Number of Newly Infected People")
plt.axis( [0, days, 0, 100] )
plt.grid()
plt.show() 

