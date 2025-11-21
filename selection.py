from projet_poo_FINAL import *
from colors import color
def selection(x): 
    

    equipe = []
    print(color("Veuillez choisir vos creatures pour le combat.",'#ecadcb'))
 

    for i, p in enumerate(x): 
        print(f"{i + 1}: {p}") 
 
    while len(equipe) < 2: 
        choix = input(color("Choisissez un hero (1-3): ",'#dbdce2'))

        if choix.isdigit() and 1 <= int(choix) <= 3: 
            choix = int(choix) - 1 
            if x[choix] not in equipe:
                equipe.append(x[choix]) 
                print(color(f"{x[choix].nom} a été ajouté à votre équipe.", '#cce2b5') )
            else: 
                print(color("déjà été choisi, choisissez autrement.",'#FAA0A0'))
        else: 
            print(color("Choix invalide, veuillez entrer un nombre entre 1 et 3.",'#FAA0A0')) 
    print("Vos creatures sont prêtes!")
 
    return equipe
