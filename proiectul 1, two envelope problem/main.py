import numpy as np
import matplotlib.pyplot as plt

procentCastig=0
vector_rata_castig=np.array([])
def twoEnvelopes(incercari):
    global vector_rata_castig
    creste, scade = 0, 0
    index=0

    for i in range(incercari):
        index=index+1
        plicuri = [100, 200]
        alegere = np.random.choice(range(0,2))
        curent = plicuri[alegere]
        nou = plicuri[0] if alegere == 1 else plicuri[1]

        if nou > curent:
            creste += 1
            aux_vector_rata_castig= np.append(round(creste / int(index) * 100, 2), vector_rata_castig)
            vector_rata_castig=aux_vector_rata_castig
        else:
            scade += 1
            aux_vector_rata_castig=np.append(round(creste / int(index) * 100, 2), vector_rata_castig)
            vector_rata_castig=aux_vector_rata_castig

    procentCastig = round(creste / int(incercari) * 100, 2)

    print(f"Incercari: {incercari}")
    print(f"Schimbarea plicului a rezultat in castig intr-un procent de {procentCastig}%.")

incercari=input("introduceti numarul de incercari: ")

twoEnvelopes(int(incercari))
x=vector_rata_castig
plt.plot(x)
plt.show()