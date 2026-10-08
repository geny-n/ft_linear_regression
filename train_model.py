import csv
import sys
import matplotlib.pyplot as plt

try :
    with open('data.csv', 'r') as data_file :
        reader = csv.DictReader(data_file, delimiter=',')
        kms = []
        prices = []
        line_nb = 0
        for ligne in reader :
            kms.append(float(ligne['km']))
            prices.append(float(ligne['price']))
            line_nb += 1
except FileNotFoundError :
    sys.exit("Error : file not found")
except PermissionError :
    sys.exit ("Error : permission denied") 


# normalisaiont des km et prix entre 0 et 1
# x = (x - xmin) / (xmax - xmin)
def normalisation (data):
    result = []
    for i in range (line_nb) :
        normal = (data[i] - min(data)) / (max(data) - min(data))
        result.append(normal)
    return result


km_norm = normalisation(kms)
prices_norm = normalisation(prices)
new_tetha0 = 0
new_tetha1 = 0
rate = 0.1
somme0 = 0
somme1 = 0


# calcule du gradient TETHA 0 (de combien il faut corriger Tetha0)
def gap_tmpT0 (tetha0, tetha1):
    somme0 = 0
    for i in range(line_nb) : 
        res = tetha0 + tetha1 * km_norm[i] - prices_norm[i]
        somme0 += res
    tmpT0 = rate * (somme0 / line_nb)
    return (tmpT0)


# calcule du gradient TETHA 1 (de combien il faut corriger Tetha1)
def gap_tmpT1 (tetha0, tetha1):
    somme1 = 0
    for i in range(line_nb) :
        res = ((tetha0 + tetha1 * km_norm[i]) - prices_norm[i]) * km_norm[i]
        somme1 += res
    tmpT1 = rate * (somme1 / line_nb)
    return (tmpT1)


# iteration pour avoir les bonnes valeur de T0 et T1
# calcule de T0 et T1 a chaque iteration pour minimiser l ecart entre les prix predits et les vrai prix
for i in range (1000) : 
    gapT0 = gap_tmpT0(new_tetha0, new_tetha1)
    gapT1 = gap_tmpT1(new_tetha0, new_tetha1)

    new_tetha0 = new_tetha0 - gapT0
    new_tetha1 = new_tetha1 - gapT1

# denormalisation de T0 et T1 (vrai valeurs)
tetha1 = (new_tetha1 * (max(prices) - min(prices))) / (max(kms) - min(kms))
tetha0 = new_tetha0 * (max(prices) - min(prices)) + min(prices) - min(kms) * tetha1

estimate_price = []
for i in kms :
    estimate_price.append(tetha0 + tetha1 * i)

try :
    with open('result.csv', 'w') as f :
        toWrite = csv.writer(f, delimiter=',')
        toWrite.writerow([tetha0, tetha1])
except PermissionError :
    sys.exit ("Error : permission denied") 

# calcule du coefficient de determination R2
# R2 = 1 - (somme des carre des residuels = SSR / somme des carres des ecarts = TSS)

# tss = 0
# ssr = 0

# # calcule de la moyenne des prix reels
# moy_prix = sum(prices) / line_nb

# # calcule TSS
# for i in range (line_nb) :
#     tss = tss + (prices[i] - moy_prix ) ** 2

# # calcule SSR
# for i in range (line_nb) :
#     ssr = ssr + (prices[i] - estimate_price[i]) ** 2

# coef_deter = 1 - (ssr / tss)
# print (coef_deter)

# affichage graphe
plt.plot(kms, prices, 'o')
plt.plot(kms, estimate_price)

plt.title("data.csv")
plt.xlabel("km")
plt.ylabel("price")
plt.savefig('fig.png')
print ("graphique sauvegarde")
