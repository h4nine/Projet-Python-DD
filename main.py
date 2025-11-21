from random import randint
import time
from selection import *
from colors import color # libraiaire de couleurs que j'ai trouve en ligne, il suffit de faire  dans le terminal pip install ansicolors pour avoir acces a la librairie
# pour utilisaer la focntion color, il suffit de fqire color("texte","couleur") 
#import keyboard  # on importe le module keyboard

# Variables a definir :
degatsval = {"Contondant": 5, "Tranchant": 10, "Percant": 20, "Feu": 25, "Poison": 30, "Magique": 30}
typedegats = ["Contondant", "Tranchant", "Percant", "Feu", "Poison", "Magique"]
etat = ["empoisonne", "paralyse", "inspire"]
armes = ["claymore", "katana", "THESE HANDS", "special ability"]

# Fonction pour simuler un lancer de de
def de(n):
    return randint(1, n)
#focntion d tri des personne selon celui qui a le nombre de de le plus grand
def trier(personnages):
    for personnage in personnages:
        personnage.de = de(20)
        print(color(f"{personnage.nom} a lancé un {personnage.de}",'#ba8d9e'))
    personnages.sort(key=lambda x: x.de, reverse=True)
    return personnages
# pour afficher les mesages lentement, et avec couleur
def afficher_les_messages_lentement(message, vitesse=0.01):
    for char in message:
        print(color(char,'#e1c4ff'), end="", flush=True)
        time.sleep(vitesse) 
# introduction 
def intro():
    (afficher_les_messages_lentement(f"Bienvenue dans D&D, appuyez sur 'Entree' pour continuer.")) 
    #keyboard.wait('enter')  # Attendre la touche "Entree"  // j'ai commente cette ligne car elle ne marche pas sur mon terminal
    
    afficher_les_messages_lentement(f"Veuillez choisir votre personnage. \n")

    global hero, monstre

    combat()

class Creature:
    def __init__(self, nom, desc, typedegats, degats,pv, etat,de):
        self.nom = nom
        self.desc = desc
        self.typedegats = typedegats
        self.degats = degats
        self.pv = pv
        self.etat = etat
        self.de = de
    def isdead(self) :
        return self.pv <= 0
    def attaque(self, cible):
        n = de(20)
        if n > cible.defense :
            cible.pv -= int(self.degats)
            print(f"{self.nom} attaque {cible.nom} et inflige {self.degats} degats!")
        else : 
            print("AWh, l'attaque a echoue!")

    # fonctions buff/debuff :
    def buff(self,n) :
        self.degats = self.degats * n # n est un multiplicateur de dégats

    def debuff(self,cible,n) :
        cible.degats = cible.degats / n # n : diviseur de dégats 


class Personnage(Creature):
    def __init__(self, nom, desc, pv,typedegats, degats, etat, arme,de):
        super().__init__(nom, desc, pv, typedegats, degats, etat,de)
        self.arme = arme

    def __str__(self):
        return f"Nom: {self.nom}, Desc: {self.desc}, Type: {self.typedegats}, Degats: {self.degats}, Arme: {self.arme}"

    def volpv(self, cible):
        soin = randint(5, 10)
        print(f"{self.nom} recupere {soin} PV en volant la vie de {cible.nom}.")
        self.pv += soin
        cible.pv -= soin
    def htpurple(self,cible) :
        print("Hollow technique : Purple.")
        print(f"{self.nom} utilise sa capacite speciale sur {cible.nom}, bro is cooked.")
        cible.pv -= 60
    def bankai(self,cible) :
        print("Bankai !")
        
        print(f"{self.nom} utilise sa capacite speciale sur {cible.nom}, bro is BEYOND cooked.")
        print("multiple slashes later...")
        cible.pv -= 100




class Monstre(Creature):
    def __init__(self, nom, description, pv, typedegats,defense, degats, etat,resistance,de):
        super().__init__(nom, description, pv,typedegats, degats,etat,de)
        self.resistance = resistance
        self.defense = defense
    def __str__(self):
        return f"Nom: {self.nom}, Desc: {self.desc}, Type: {self.typedegats}, Degats: {self.degats}, Resistance :{self.resistance}"

    def atkmonstre(self, cible):
        degats = randint(1, self.degats)
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} degats!")
        cible.pv -= degats
    def dabiflame(self, cible) :
        degats = randint(1,self.degats)*3
        print(f"{self.nom} attaque continuously {cible.nom} et inflige {degats} degats!")
        cible.pv -= degats 
        cible.etat = "Burning"
        print(f"oh no ! {cible.nom} is burning, too bad.")
                    


# Fonction de combat
def combat():
    global hero, monstre

    listep = [
        Personnage("Gojo Satoru", "top tier sorcerer", typedegats[5],degatsval[typedegats[5]], 60, "", armes[2],0),
        Personnage("Dazai Osamu", "a suicidal genius", typedegats[5],degatsval[typedegats[5]], 60, "", armes[3],0),
        Personnage("Kurosaki Ichigo", "Un Shinigami", typedegats[2],degatsval[typedegats[2]],60, "", armes[1],0)
    ]
    listem = [
        Monstre("Goblin", "ugly fugly creature", typedegats[0],degatsval[typedegats[0]],10,50,  "", "Feu",0),
        Monstre("Ruin Guard", "Automated robot built ", typedegats[2],degatsval[typedegats[2]],10,50,  "", "rien",0),
        Monstre("Dabi", "Supervillain with high flame power", typedegats[3],degatsval[typedegats[3]],5,50,  "", "Feu",0)
    ]
    # focntion de selection des creatures, definir que 2/3 qui vont jouer
    listep = selection(listep)  
    listem = selection(listem)  

    

    # Création et tri de la liste des combattants
    listefinale = listep + listem
    listefinale = trier(listefinale)

    print(color("\n FIGHT! :",'#cbb5e2'))
    for combattant in listefinale:
        print(color(f"- {combattant.nom} ({combattant.pv} PV)",'#ba93b2'))
    # Boucle principale du combat
    while True:
        for combattant in listefinale:
            if combattant.isdead():
                continue  

            print(color(f"\n C'est au tour de {combattant.nom} d'attaquer !",'#b5cce2'))

            # Déterminer la cible (si c'est un personnage, attaque un monstre, et vice versa)
            cibles = listem if isinstance(combattant, Personnage) else listep
            cibles = [c for c in cibles ]  

            if not cibles:  
                continue
            while True:
                a = input("choisissez votre cible : 1 ou 2 :")
                if a == '1' and not cibles[0].isdead(): # si la cible est morte, on ne peut pas la selectionner
                    cible = cibles[0]
                    break
                elif a == '2' and not cibles[1].isdead():
                    cible = cibles[1]
                    break
                else: 
                    print(color("Choix invalide! veuillez entrer 1 ou 2 (si la cible est morte, on ne peut pas la selectionner.)",'#FAA0A0')) 
                   
                
             
            if isinstance(combattant, Personnage): # isinstqnce permet de savoir si un objet est une instance d'une classe, dans ce cas, si c'est un personnage
                while True:
                    methode = input(f"{combattant.nom}! Choisis ta méthode d'attaque : 1-Normal 2-Spécial 3-Buff 4-Debuff l'ennemi : ")
                    if methode == '1': 
                        combattant.attaque(cible)
                        break
                    elif methode == '2': # capacite speciale, chacun a sa propre capacite speciale
                        if combattant.nom == "Gojo Satoru": 
                            combattant.htpurple(cible)
                        elif combattant.nom == "Dazai Osamu": 
                            combattant.volpv(cible)
                        else:
                            combattant.bankai(cible)
                        break
                    elif methode == '3':
                        multiplier = randint(2,3)
                        decidor = randint(0,10)
                        if decidor > 3: # 70% de chance de reussite
                            combattant.buff(multiplier)
                            print(f"{combattant.nom} a buff ses degats de {multiplier}!")
                        else: 
                            print("le buff a echoue.")
                        break
                    elif methode == '4':
                        dividor = randint(2,3)
                        decidor = randint(0,10)
                        if decidor > 3: # 70% de chance de reussite
                            combattant.debuff(cible,dividor)
                            print(f"{combattant.nom} a debuff les degats de {cible.nom} de {dividor}!")
                        else: 
                            print("le debuff a echoue.")
                        break
                    else:
                        print(color("Choix invalide! veuillez entrer 1,2,3 ou 4.",'#FAA0A0'))  

            
            elif isinstance(combattant, Monstre): # si c'est un monstre
                while True:
                    methode = input(f"{combattant.nom}! Choisis ta méthode d'attaque : 1-Normal 2-Spécial (ONLY DABI) 3-Buff 4-Debuff l'ennemi : ")
                    if methode == '1':
                        combattant.atkmonstre(cible)
                        break
                    elif methode == '2' and combattant.nom == "Dabi": # Dabi est le seul qui peut utiliser la methode 2
                        combattant.dabiflame(cible)
                        break
                    elif methode == '3':
                        multiplier = de(2)
                        decidor = randint(0,10)
                        if decidor > 3: # 70% de chance de reussite
                            combattant.buff(multiplier)
                            print(f"{combattant.nom} a buff ses degats de {multiplier}!")
                        else: 
                            print("le buff a echoue.")
                        break
                    elif methode == '4':
                        dividor = de(4)
                        decidor = randint(0,10)
                        if decidor > 3: # 70% de chance de reussite
                            combattant.debuff(cible,dividor)
                            print(f"{combattant.nom} a debuff les degats de {cible.nom} de {dividor}!")
                        else: 
                            print("le debuff a echoue.") 
                        break
                    else:
                        print(color("Choix invalide ! Veuillez entrer 1, 2 (seul Dabi peut utiliser 2), 3 ou 4.",'#FAA0A0'))  

            # Afficher les PV après chaque attaque
            print(color(f"{combattant.nom} a {combattant.pv} PV !",'#b5cce2'))
            print(color(f"{cible.nom} a {cible.pv} PV !",'#b5cce2'))

            
            if all(m.isdead() for m in listem):  # si tous les monstres sont morts
                print(color("\nFélicitations, vous avez vaincu tous les monstres !",'#cce2b5'))
                return
            if all(p.isdead() for p in listep): # si tous les personnages sont morts
                print(color("\nDéfaite... Tous les héros sont morts.",'#e06666'))
                return


if __name__ == "__main__":
    intro()
    print(color("Fin du jeu.",'#8e7cc3'))




    