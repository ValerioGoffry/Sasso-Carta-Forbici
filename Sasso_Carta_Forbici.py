import random

mosse = ["sasso", "carta", "forbici"]
scelta_pc = random.choice(mosse)

print("Benvenuto al gioco sasso carta forbici")
nome = input("Come ti chiami? ")
print(f"Ottimo! {nome} si inizia a giocare!!")


def scelte(punteggio_giocatore=0, punteggio_pc=0):
    if scelta_pc == scelta_utente:
        print(f"Parità!")
        punteggio_giocatore += 0
        punteggio_pc += 0
    elif scelta_pc == "carta" and scelta_utente == "sasso":
        print("Ha vinto il computer")
        punteggio_pc += 1
    elif scelta_pc == "forbici" and scelta_utente == "carta":
        print("Ha vinto il computer!")
        punteggio_pc += 1
    elif scelta_pc == "sasso" and scelta_utente == "forbici":
        print("Ha vinto il computer!")
        punteggio_pc += 1
    elif scelta_utente == "carta" and scelta_pc == "sasso":
        print(f"Ha vinto {nome}!")
        punteggio_giocatore = punteggio_giocatore + 1
    elif scelta_utente == "forbici" and scelta_pc == "carta":
        print(f"Ha vinto {nome}!")
        punteggio_giocatore += 1
    elif scelta_utente == "sasso" and scelta_pc == "forbici":
        print(f"Ha vinto {nome}!")
        punteggio_giocatore += 1
    print(f"Punteggio {nome}: {punteggio_giocatore}")
    print(f"Punteggio PC: {punteggio_pc}")


while True:
    scelta_utente = input("Scegli sasso,carta,forbici: ")
    if scelta_utente == "sasso" or scelta_utente == "carta" or scelta_utente:
        print(f"{nome} ha scelto: {scelta_utente.lower()}")
        print(f"Il Computer ha scelto: {scelta_pc}")
        scelte()
    else:
        print("Devi per forza inserire sasso, carta o forbici")
