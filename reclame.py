from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    nieuwe_prijs = prijs - korting * 4
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro.")

aanbieding_1("aardbei",4,0.1)

inkomsten = [10,20,15,16,13,12,10]
# totaal is 96
# btw is 8.64

def inkomsten_totaal(inkomsten,btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.")

inkomsten_totaal([10,20,15,16,13,12,10],0.09)

mijn_lijst = [15,40,2,30,13,12,10]
# totaal is 122
# gemiddelde is 122/7 = 17,43 afgerond

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    print(f"Het laagste inkomen deze week was {laagste} euro, en het hoogste inkomen deze week was {hoogste} euro.")

laag_en_hoog(mijn_lijst)

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    bedrag = totaal / len(mijn_lijst)
    print(f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")

gemiddelde(mijn_lijst)

invoer_lijst = [2,6,4,8,99,1,55]

def meervoudig(invoer_lijst):
    mijn_lijstje = [min(invoer_lijst),max(invoer_lijst)]
    print(mijn_lijstje)

meervoudig(invoer_lijst)

invoer_lijst_2 = [33,22,23,5,77,1,24]

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer