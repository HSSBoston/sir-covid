import matplotlib.pyplot as plt 

badDays = 7
goodDays = 7 * 8
totalDays = badDays + goodDays
daysToRecover = 14
I = 1

newlyInfected =[]
totalCases = []
recovered = []
activeCases = []

for x in range(badDays + 1):
    y = I * 3 ** x
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
    
for x in range(badDays + 1, badDays + goodDays + 1):
#    y = activeCases[badDays]
    y = activeCases[badDays] * 0.75 ** (x - badDays) 
    
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
plt.axis( [0, totalDays, 0, 50000] )
plt.grid()
plt.show() 



