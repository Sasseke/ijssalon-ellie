from presentatie import *
import csv

inkomsten = {
    "Aardbeijen-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

def som(dictionary):
    totaal = 0
    for i in dictionary.values():
       totaal += i
    return totaal

totaal_inkomsten = som(inkomsten)

presenteer(inkomsten, totaal_inkomsten)

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])