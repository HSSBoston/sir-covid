import matplotlib.pyplot as plt 

days = 30
daysToRecover = 14
I = 1
a = 3

newlyInfected =[]
totalCases = []
recovered = []
activeCases = []

for x in range(days + 1):
    y = I * a ** x
    newlyInfected.append(y)
    
    if x == 0:
        totalCases.append(newlyInfected[x])
    else:
        totalCases.append(totalCases[x-1] + newlyInfected[x])
    
    if x - daysToRecover < 0:
        recovered.append(0)
    else:
        recovered.append(totalCases[x-14])
    
    activeCases.append(totalCases[x] - recovered[x])

print(newlyInfected)
print(totalCases)
print(recovered)
print(activeCases)

plt.plot(activeCases)
plt.xlabel("Days")
plt.ylabel("Active cases")
plt.axis( [0, days, 0, 100] )
plt.grid()
plt.show() 



