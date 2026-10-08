import csv
import sys

try :
    with open ('result.csv', 'r') as result_file :
        reader = csv.reader(result_file, delimiter=',')
        for row in reader :       
            tetha0 = float(row[0])
            tetha1 = float(row[1])

except FileNotFoundError :
    sys.exit("Error : file not found")
except PermissionError :
    sys.exit ("Error : permission denied")


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


estimate_price = []
for i in kms :
    estimate_price.append(tetha0 + tetha1 * i)


# calcule du coefficient de determination R2
# R2 = 1 - (somme des carres des residuels = SSR / somme des carres des ecarts = TSS)

tss = 0
ssr = 0

# calcule de la moyenne des prix reels
moy_prix = sum(prices) / line_nb

# calcule TSS
for i in range (line_nb) :
    tss = tss + (prices[i] - moy_prix ) ** 2

# calcule SSR
for i in range (line_nb) :
    ssr = ssr + (prices[i] - estimate_price[i]) ** 2

coef_deter = 1 - (ssr / tss)
print (coef_deter)