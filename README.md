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

Le projet propose pour le moment deux heuristiques différentes.
Celles-ci doivent être renseignées dans la commande via l'option `-h`.

- **Insertion** (`-h insert`)
- **Échange** (`-h swap`)

Lors de l'exécution d'une heuristique, deux stratégies sont possibles :

- **Déterministe** (par défaut ; option `-d`) : on prend les visites dans leur ordre d'apparition,
- **Non déterministe** (option `-nd`) : on prend les visites dans un ordre aléatoire.