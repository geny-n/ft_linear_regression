import sys
import csv
import os

tetha0 = 0
tetha1 = 0

try :
    with open ('result.csv', 'r') as result_file :
        reader = csv.reader(result_file, delimiter=',')
        for row in reader :       
            tetha0 = float(row[0])
            tetha1 = float(row[1])

except FileNotFoundError :
    pass
except PermissionError :
    sys.exit ("Error : permission denied")

try :
    input_mileage = float(input ("Enter a mileage : "))
    if (input_mileage < 0) :
        sys.exit ("Error : the mileage must be positive")
    
except ValueError:
    sys.exit ("Error : the mileage must be a number")

estimatePrice = tetha0 + (tetha1 * input_mileage)
print (estimatePrice)