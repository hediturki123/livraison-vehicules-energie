# Livraison avec des véhicules électriques

## Question 1

### Voisinage 1 : Prendre un élément dans la liste et l'insérer autre part dans la liste
- **Taille du voisinage** : n-1, parce qu'on a une liste de taille n, on prend un élément de la liste et on l'insère à autre endroit où il était placé initialement, d'où le fait que la taille du voisinage soit de n-1.
- **Taille polynomiale ?** Oui elle est linéaire
- **Voisinage contient des solutions non réalisables ?** Non

### Voisinage 2 : Echanger deux éléments dans la liste
- **Taille du voisinage** : n-1, parce qu'on a une liste de taille n, on échange un élément avec un autre élément de la liste sauf avec lui-même, d'où le fait que la taille du voisinage soit n-1.
- **Taille polynomiale ?** Oui, elle est linéaire
- **Voisinage contient des solutions non réalisables ?** Non

### Voisinage 3 : Décaler trois élements dans la liste
- **Taille du voisinage** : n
- **Taille polynomiale ?** Oui, elle est linéaire
- **Voisinage contient des solutions non réalisables ?** Non

## Question 2

Nous avons choisi de prendre comme exemple l'instance `lyon_40_1_1` en utilisant les trois heuristiques que nous avons défini (insertion, échange et décalage de 3 éléments) et en utilisant l'approche déterministe :

|                                      | Heuristique d'insertion | Heuristique d'échange | Heuristique de décalage |
|--------------------------------------|-------------------------|-----------------------|-------------------------|
| **Première solution du voisinage**   | `84.275 km`             | `78.58 km`            | `109.87 km`             |
| **Meilleure solution du voisinage**  | `86.165 km`             | `74.19 km`            | `116.17 km`             | 

## Question 3

On reprend le même exemple que la question précédente avec l'instance `lyon_40_1_1` en utilisant les trois heuristiques que nous avons défini (insertion, échange et décalage de 3 éléments) mais cette fois-ci en utilisant l'approche non déterministe.
Vu que le c'est une approche non déterministe, nous avons lancé le programme 5 fois pour chaque instance et chaque cas (première ou meilleure solution) :

|                                     | Heuristique d'insertion                                                 | Heuristique d'échange                                                    | Heuristique de décalage                                                        |
|-------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Première solution du voisinage**  | `78.98 km` <br/>`86.37 km`<br/>`80.42 km`<br/>`87.45 km`<br/>`91.55 km` | `82.05 km` <br/>`71.56 km` <br/>`71.83 km` <br/>`78.8 km` <br/>`74.8 km` | `111.86 km`<br/>`108.37 km` <br/>`108.46 km` <br/>`121.27 km` <br/>`117.14 km` |
| **Meilleure solution du voisinage** | `72.5 km`<br/>`69.45 km` <br/>`79.06 km`<br/>`81.02 km`<br/>`74.77 km`  | `70.49 km` <br/>`80.2 km` <br/>`68.5 km` <br/>`70.9 km` <br/>`74.25 km`  | `111.3 km` <br/>`143.28 km` <br/>`108.29 km` <br/>`111.18 km` <br/>`110.7 km`  | 


# Vitesse de rechargement et flotte de véhicule

## Question 4

...

## Question 5

...

## Question 6

...
