# Livraison avec des véhicules électriques

## À propos

Pour des raisons de compatibilité entre Windows et MacOS, ce projet utilise **[Poetry](https://python-poetry.org/docs)** en tant qu'outil de management des dépendances.

La version de Python utilisée est la **3.10**.

## Commandes usuelles

Pour installer les dépendances du projet à l'aide de **Poetry** :
```sh
poetry install
```

Pour lancer le projet :
```sh
poetry run python src/__init__.py <nom_instance> -h <heuristique>

poetry run python src/__init__.py lyon_40_1_1 -h insert
```

Pour plus d'information sur la commande :
```sh
poetry run python src/__init__.py --help
```

## Heuristiques et stratégies

Le projet propose pour le moment trois heuristiques différentes.
Celles-ci doivent être renseignées dans la commande via l'option `-h`.

- **Insertion** (`-h insert`)
- **Échange** (`-h swap`)
- **Décalage par triplet** (`-h triplet_shift_heuristic`)

Lors de l'exécution d'une heuristique, plusieurs aspects sont paramétrables :
- **Déterminisme au départ :**
    - **Déterministe** (par défaut ; option `-d`) : on démarre avec les visites dans leur ordre d'apparition,
    - **Non déterministe** (option `-nd`) : on démarre avec les visites dans un ordre aléatoire.
- **Arrêt en fonction de la solution :**
    - **Première solution améliorante** (par défaut, option `-fs`) : on arrête l'exécution de l'algorithme à la première solution rencontrée meilleure que la solution initiale.
    - **Meilleure solution** (option `-bs`) : on arrête l'algorithme lorsque deux itérations consécutives ont la même solution.

Il est possible de jouer sur d'autres paramètres comme la sortie (`-o`) ou le seuil de rechargement des véhicules (`-t`).
Pour plus d'information sur les paramètres disponibles, voir le `--help` de la commande.

## Tests

Pour s'assurer de la cohérence du code produit, des tests unitaires ont été mis en place (voir le dossier `tests`).
La commande suivante permet de les lancer :
```sh
poetry run python -m unittest discover -s tests -v
```

## Démonstrations d'exécution

Les sorties des exécutions de différentes heuristiques avec divers paramètres possibles sont disponibles dans le dossier `outputs/demo`.

Les valeurs du seuil de rechargement et la vitesse de chargement ont respectivement été fixées à 20% et "moyenne".

Le nom des fichiers de sortie explicite l'exécution effectuée.
Par exemple, le fichier `lyon_100_1_1__insert__d_fs.txt` correspond à l'exécution de l'heuristique d'insertion (`insert`) sur l'instance `lyon_100_1_1` avec départ déterministe (`d`) et en prenant la première solution du voisinnage qui améliore la solution (`fs`).

Le contenu d'un fichier contient l'historisque des visites fait par les véhicules (un véhicule/une tournée par ligne). En reprenant l'exemple ci-dessus, le contenu du fichier est le suivant :
```
13,11,10,15,32,3,R,18,19,4,20,21,5,30,R,34,25,29,31,22,35,R,26,24,37,14,38,23,40,R,6,45,44,47,36,46,R,7,48,41,43,16,28,49,50,R,51,52,53,54,17,55,56,57,C,R
58,2,59,60,39,61,62,33,R,63,64,65,66,12,67,68,R,42,69,70,8,71,72,R,73,74,27,75,1,76,77,78,R,79,80,81,82,83,84,R,85,86,87,88,89,90,C,R
91,92,93,94,9,R,95,96,97,98,99,100
```

Ces sorties ont été produites à partir du script *Bash* `generate_output.sh` présent dans le dossier `scripts` (le script doit être exécuté depuis ce dossier).

## Réponses aux questions

Vous trouverez les réponses aux questions du TP dans le fichier [`explanations.md`](docs/explanations.md) du dossier `docs`.
