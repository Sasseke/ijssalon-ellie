def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

bedrag = int(input("Welk bedrag zit er in de fooienpot?"))
personen = int(input("Over hoeveel mensen moet de pot verdeeld worden?"))

def fooi_pp(bedrag,personen):
    try:
       bedrag_pp = bedrag / personen
    except:
       bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro."

print(fooi_pp(bedrag,personen))