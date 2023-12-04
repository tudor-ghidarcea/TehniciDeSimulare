import random
import numpy as np



def Gamma( k, theta, v):
    b = v-1
    c = v+b
    s = (2*v-1)**0.5
    while True:
        U = random.uniform(0,1)
        T = s*np.tan(np.pi*(U-0.5))
        Y = b+T
        if(Y>0):
            U1 = random.uniform(0,1)
            if (U1<=np.e**(b*np.log(Y/b)-T+log(1+(T**2)/c))):
                break
    return Y


def generate_gamma(k, theta, v):
    b = k-1
    c = k+(v-1)
    s = (2*k-1)**0.5
    while True:
        U = random.uniform(0,1)
        T = s*np.tan(np.pi*(U-0.5))
        Y = b+T
        if(Y>0):
            U1 = random.uniform(0,1)
            if (U1<=np.e**((b*np.log(Y/b))-T+np.log(1+(T**2)/c))):
                break
    return Y*theta

gamma_var = generate_gamma(2, 3, 7)
print(gamma_var)

# Pentru a calcula Gamma(2,3,7),
# trebuie sa folosim parametrul de shape k = 2,
# cel de scala teta = 3 si parametrul de locatie
# v = 7




def Bernoulli(p):
    U = random.uniform(0, 1)
    if U <= (1 - p):
        return 0
    return 1


def Pascal(k, p):
    j = 0
    X = 0
    while True:
        if Bernoulli(p):
            j += 1
        else:
            X += 1
        if j == k:
            break
    return X
k = int(input())
p = float(input())


# media si dispersia la Pascal
# e e medie, var e dispersie
# e si var sunt calculate dupa formulele din curs, celelalte manual

parray = [0]*1000
media_pascal=0
garray = [0]*1000
media_gamma= 0

for i in range(1000):
    parray[i]=Pascal(k,p)
    garray[i]=generate_gamma(2,3,7)
    media_pascal+=parray[i]
    media_gamma += garray[i]


media_pascal=media_pascal/1000
media_gamma=media_gamma/1000

spascal = 0
sgamma=0
for i in range(1000):
    spascal=spascal+(parray[i]-media_pascal)**2
    sgamma=sgamma+(garray[i]-media_gamma)**2
dpascal = (spascal/1000)
dgamma = np.sqrt(sgamma/1000)
epascal = k*(1-p)/p
egamma = 2+7/3
varpascal=epascal/p
vargamma= 7/9
print( media_pascal, dpascal, epascal, varpascal)
print( media_gamma, dgamma, egamma, vargamma)
