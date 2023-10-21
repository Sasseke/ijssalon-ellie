mijn_dict = {
    "vis" : 10,
    "vlees" : 25,
    "overig" : 15
}

totaal = 50

def presenteer(dictionary,totaal):
    for k, v in dictionary.items():
        print(k, " : ", v, " euro")
    print(26 * "=")
    print(f"Totaal : {totaal}")