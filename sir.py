import matplotlib.pyplot as plt 

P = 15000
I0 = 750
R0 = 12700
S0 = P - I0 - R0

a = 10
k = 0.075
d = 17
days = 365

susceptible = [S0]
recovered = [R0]
infected = [I0]

for x in range(days + 1):
    S = ((-a * k/P) * infected[x] + 1) * susceptible[x]
    R = (1/d) * infected[x] + recovered[x]
    I = ((a * susceptible[x]/P) * k - 1/d + 1) * infected[x]
    
    susceptible.append(S)
    recovered.append(R)
    infected.append(I)                   
                



print(susceptible)
print(recovered)
print(infected)

plt.plot(susceptible, label="Susceptible")
plt.plot(recovered, label="Recovered")
plt.plot(infected, label="Infected")
plt.legend()
plt.xlabel("Days")
plt.ylabel("Number of people")
plt.axis( [0, days, 0, 15000] )
plt.grid()
plt.show() 



