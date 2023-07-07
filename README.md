# Résolvez des problèmes en utilisant des algorithmes en Python

## Description
Ce projet a pour objectif de développer un algorithme capable de maximiser le profit des clients après deux ans d'investissement dans des actions. 
L'algorithme générera une liste des actions les plus rentables à acquérir. 
Pour une explication plus approfondie du fonctionnement des algorithmes, veuillez consulter le fichier diapositives.pdf.

### Contraintes 
L'algorithme doit adhérer à trois contraintes :

- Une action ne peut être achetée qu'une seule fois.
- Il est impossible d'acheter une fraction d'action.
- L'investissement maximal par client est limité à 500 euros.

### Algorithme de force brute
L'algorithme de force brute teste toutes les combinaisons d'actions possibles qui respectent les contraintes. 
Le programme lit un fichier contenant des informations sur les actions, explore toutes les combinaisons possibles et affiche l'investissement le plus rentable.


### Optimisation d'algorithme
Le nouvel algorithme n'a pas besoin d'explorer toutes les combinaisons possibles, ce qui permet d'accélérer son exécution.

## Procédure d'installation

### Import du dépôt Github
Dans un répertoire de travail, importez le dépôt Github et naviguez jusqu'au répertoire du projet :

```sh
$ git clone https://github.com/lcourdes/Developpez-des-problemes-en-utilisant-des-algorithmes-en-python.git
$ cd Developpez-des-problemes-en-utilisant-des-algorithmes-en-python
```

### Création d'un environnement virtuel
Il est recommandé de créer un environnement virtuel pour ce projet. Voici comment procéder :

- Si ce n'est pas déjà fait, installez le package *virtualenv* :
```sh
$ pip install virtualenv
```

- Créez un environnement virtuel et activez-le :
```sh
$ virtualenv env
$ source env/bin/activate
```

### Installation des librairies
Aucune librairie supplémentaire n'est nécessaire pour exécuter les programmes de ce projet.

## Utilisation du programme

### Démarrage des algorithmes
Avant de lancer les programmes, assurez-vous que l'environnement virtuel est activé. 
Trois fichiers Python sont disponibles :

- bruteforce.py, 
- optimized-glouton.py (utilise un algorithme glouton)
- optimized-dynamic.py (utilise un algorithme de programmation dynamique)

```sh
$ python3 bruteforce.py
$ python3 optimized-glouton.py
$ python3 optimized-dynamic.py
```

### Les bases de données de tests

Les scripts python peuvent être utilisés avec différentes bases de données au format csv. 
Nous fournissons ici trois bases : 
- bruteforce_dataset.csv
- dataset1_Python+P7.csv
- dataset2_Python+P7.csv

Il est recommandé d'utiliser le fichier bruteforce.py uniquement avec la base de données bruteforce_dataset.csv. 
En effet, ce script n'utilise pas un algorithme optimisé, il est donc préférable de l'utiliser avec une base de données de taille réduite.