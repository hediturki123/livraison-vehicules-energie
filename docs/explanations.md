# Livraison avec des véhicules électriques

## Question 1

### Voisinage 1 : Prendre un élément dans la liste et l'insérer autre part dans la liste
- **Taille du voisinage** : n-1, parce qu'on a une liste de taille n, on prend un élément de la liste et on l'insère à autre endroit où il était placé initialement, d'où le fait que la taille du voisinage soit de n-1.
- **Taille polynomiale ?** Oui, elle est linéaire
- **Voisinage contient des solutions non réalisables ?** Non

### Voisinage 2 : Échanger deux éléments dans la liste
- **Taille du voisinage** : n-1, parce qu'on a une liste de taille n, on échange un élément avec un autre élément de la liste sauf avec lui-même, d'où le fait que la taille du voisinage soit n-1.
- **Taille polynomiale ?** Oui, elle est linéaire
- **Voisinage contient des solutions non réalisables ?** Non

### Voisinage 3 : Décaler trois éléments dans la liste
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
Vu qu'il s'agit d'une approche non déterministe, nous avons lancé le programme 5 fois pour chaque instance et chaque cas (première ou meilleure solution) :

|                                     | Heuristique d'insertion                                                 | Heuristique d'échange                                                    | Heuristique de décalage                                                        |
|-------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Première solution du voisinage**  | `78.98 km` <br/>`86.37 km`<br/>`80.42 km`<br/>`87.45 km`<br/>`91.55 km` | `82.05 km` <br/>`71.56 km` <br/>`71.83 km` <br/>`78.8 km` <br/>`74.8 km` | `111.86 km`<br/>`108.37 km` <br/>`108.46 km` <br/>`121.27 km` <br/>`117.14 km` |
| **Meilleure solution du voisinage** | `72.5 km`<br/>`69.45 km` <br/>`79.06 km`<br/>`81.02 km`<br/>`74.77 km`  | `70.49 km` <br/>`80.2 km` <br/>`68.5 km` <br/>`70.9 km` <br/>`74.25 km`  | `111.3 km` <br/>`143.28 km` <br/>`108.29 km` <br/>`111.18 km` <br/>`110.7 km`  | 


# Vitesse de rechargement et flotte de véhicule

## Question 4

### Calculs

Pour calculer le nombre de véhicules utilisés en moyenne ainsi que le nombre de recharges effectuées en moyenne par type d'instance (i.e. nombre de visites), nous avons réalisé un script ([`process_vehicle_data.sh`](../scripts/process_vehicle_data.sh) dans le dossier `scripts`).

Les résultats fournis par ce script sont présents dans le dossier [`outputs/vehicle_data`](../outputs/vehicle_data), et présente une liste de nombres correspondant aux comptes de véhicles et des recharges pour chaque exécution d'instance, suivi de la moyenne de cette même liste.

Pour clarifier les résultats précédemment obtenus, nous avons choisi de les représenter sous forme de tableaux présentés ci-dessous.
Les différentes vitesses de charge sont représentées par les colonnes tandis que les instances groupées par nombre de visites sont en lignes.

### Tableau du nombre de véhicules utilisés en moyenne

|         | **Lente** | **Moyenne** | **Rapide** |
|:-------:|:---------:|:-----------:|:----------:|
| **40**  |     1     |      1      |     1      |
| **100** |   1.96    |    1.93     |    1.93    |
| **150** |   3.11    |    3.05     |     3      |
| **200** |     4     |    4.06     |     4      |

### Tableau du nombre de recharges effectuées en moyenne

|         | **Lente** | **Moyenne** | **Rapide** |
|:-------:|:---------:|:-----------:|:----------:|
| **40**  |     0     |      0      |     0      |
| **100** |   2.96    |    2.93     |    2.74    |
| **150** |   4.11    |      4      |    3.83    |
| **200** |     5     |      5      |    4.83    |

### Tableau des ratios nombre de recharges sur nombre de véhicules

|         | **Lente** | **Moyenne** | **Rapide** |
|:-------:|:---------:|:-----------:|:----------:|
| **40**  |     0     |      0      |     0      |
| **100** |   1.51    |    1.52     |    1.42    |
| **150** |   1.32    |    1.31     |    1.28    |
| **200** |   1.25    |    1.23     |    1.21    |

### Analyse critique

Sans prendre en compte le temps mis et la distance parcourue, on observe que le nombre de véhicules utilisés et le nombre de recharges effectuées ne varie que peu d'une vitesse de charge à une autre.
Cela est probablement lié au fait que les heuristiques abordées (insertion, échange et décalage) ont un comportement similaire temporellement parlant, le focus étant mis sur la distance que l'on cherche à minimiser.

D'un point de vue du nombre de recharges, la charge rapide est tout de même sensiblement plus intéressante avec une différence d'environ 0.18 par rapport à la charge moyenne.

En se penchant sur les ratios du dernier tableau, on peut aussi supposer que plus le nombre de visites à effectuer est grand, plus le nombre de recharges effectuées par un véhicule tend vers 1, quelle que soit la vitesse de charge.

## Question 5

Nous conseillerions d'utiliser la charge rapide pour la flotte de véhicules vis-à-vis de la légère économie en nombre de recharges que cela apporte.

Néanmoins, il est intéressant de noter qu'une telle décision n'influe par sur la minimisation de la distance parcourue par les véhicules.
En effet, jouer sur le paramètre de la vitesse de chargement ne changera pas l'ordre "optimal" dans lequel seront effectuées les visites, et donc la distance entre chaque visite. Cela peut, en revanche, amener à utiliser davantage de véhicules par manque de temps.
