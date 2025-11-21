# D&D Lite – Jeu de Combat Tour par Tour (Python)

D&D Lite est un mini-jeu inspiré de *Donjons & Dragons*. Ce jeu propose des combats stratégiques entre personnages et monstres, avec un système de tours intégrant des points de vie, des dégâts, des buffs et des debuffs.

## Fonctionnalités principales

- **Initiative** : Lancer de dé (d20) pour déterminer l’ordre des actions.
- **Attaques normales** : Différents types de dégâts selon les personnages et monstres.
- **Attaques spéciales** : Capacités uniques pour chaque personnage ou monstre.
- **Buffs et debuffs** : Augmentation ou réduction des dégâts.
- **Gestion des points de vie** : Suivi des PV et détection automatique de la mort.

## Personnages jouables

- **Gojo Satoru** : Attaque spéciale – *Technique Purple*.
- **Dazai Osamu** : Attaque spéciale – *Vol de vie*.
- **Kurosaki Ichigo** : Attaque spéciale – *Bankai*.

## Monstres disponibles

- **Goblin**
- **Ruin Guard**
- **Dabi** : Seul monstre avec une attaque spéciale.

## Pré-requis

Le programme utilise la librairie `ansicolors` pour un affichage coloré dans le terminal.

### Installation

Pour installer la librairie, exécutez la commande suivante dans le terminal :

```bash
pip install ansicolors
```

## Lancement du jeu

Pour démarrer le jeu, exécutez la commande suivante dans le terminal :

```bash
python main.py
```

Le jeu se lancera automatiquement.

## Commandes en jeu

### Choisir une cible

- **1** : Première cible  
- **2** : Deuxième cible  

### Choisir une action

#### Pour un personnage :

- **1** : Attaque normale  
- **2** : Attaque spéciale  
- **3** : Buff  
- **4** : Debuff  

#### Pour un monstre :

- **1** : Attaque normale  
- **2** : Attaque spéciale (uniquement pour Dabi)  
- **3** : Buff  
- **4** : Debuff  

## Fin de partie

Le combat se termine lorsque :

- **Victoire** : Tous les monstres sont vaincus.  
- **Défaite** : Tous les personnages sont morts.

---

Amusez-vous bien et que la meilleure équipe gagne !