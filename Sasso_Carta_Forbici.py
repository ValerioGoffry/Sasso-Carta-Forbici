import random

mosse = ["sasso", "carta", "forbici"]
scelta_pc = random.choice(mosse)
scelta_utente = str(input("Scegli sasso,carta,forbici: "))


def pari():
    if scelta_pc == "sasso" and scelta_utente == "sasso":
        print("Parità")
    elif scelta_pc == "carta" and scelta_utente == "carta":
        print("Parità")
    elif scelta_pc == "forbici" and scelta_utente == "forbici":
        print("Parità")


def pc():
    if scelta_pc == "carta" and scelta_utente == "sasso":
        print("Ha vinto il pc")
    elif scelta_pc == "forbici" and scelta_utente == "carta":
        print("Ha vinto il pc")
    elif scelta_pc == "sasso" and scelta_utente == "forbici":
        print("Ha vinto il pc")


def utente():
    if scelta_utente == "carta" and scelta_pc == "sasso":
        print("Ha vinto il Giocatore")
    elif scelta_utente == "forbici" and scelta_pc == "carta":
        print("Ha vinto il Giocatore")
    elif scelta_utente == "sasso" and scelta_pc == "forbici":
        print("Ha vinto il Giocatore")


print(f"Giocatore: {scelta_utente}".lower())
print(f"Pc: {scelta_pc}")
pari()
pc()
utente()
