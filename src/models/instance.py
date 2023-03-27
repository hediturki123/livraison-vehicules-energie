import copy
import csv
import os.path
import numpy as np
import src.environment as env

from src.models.visit import Visit
from src.models.vehicle import Vehicle
from src.models.instance_file import InstanceFile


class Instance:
    def __init__(self, instance_name: str):
        # Vérification de l'existence du dossier de l'instance
        if os.path.isdir(env.ROOT_DIR + '/data/instances/' + instance_name):
            self.INSTANCE_DIR = env.ROOT_DIR + '/data/instances/' + instance_name
            self.files_paths: dict[InstanceFile, str] = {}  # Chemins pour les fichiers d'instance

            # Vérification de l'existence de tous les fichiers d'instance
            for instance_file in InstanceFile:
                filename: str = instance_file.value
                filepath: str = self.INSTANCE_DIR + '/' + filename
                if os.path.isfile(filepath):
                    self.files_paths[instance_file] = filepath
                else:
                    raise Exception('instance "' + instance_name + '" is missing file "' + filename + '"')

            # Initialisation des visites
            self.visits_to_do: dict[int, Visit] = {}
            self.__initialize_visits()

            # Initialisation du dépôt
            self.warehouse: Visit = self.visits_to_do[0]
            self.visits_to_do.pop(0)

            # Initialisation des données de véhicule
            Vehicle.initialize(self.files_paths[InstanceFile.VEHICLE])

            # Initialisation de la matrice des distances (en kilomètres)
            self.distances: list[list[float]] = []
            self.__initialize_distances()

            # Initialisation de la matrice des temps de trajet (en secondes)
            self.times: list[list[int]] = []
            self.__initialize_times()

            # Préparation des véhicules
            self.current_vehicle: Vehicle | None = None
            self.used_vehicles: list[Vehicle] = []

        else:
            raise Exception('instance "' + instance_name + '" does not exist')

    def execute(self) -> None:
        # Mise en place du premier véhicule
        first_vehicle: Vehicle = Vehicle()
        self.current_vehicle = first_vehicle
        self.used_vehicles.append(first_vehicle)

        # Exemple d'utilisation des actions
        # (On fait un import local pour éviter les dépendances circulaires)
        from src.models.actions import ActionQueue, Move, Deliver
        aq: ActionQueue = ActionQueue(self, [
            Move(self, 1.0, 120),
            Deliver(self, 30)
        ])
        aq.execute()
        # TODO: algorithme principal

    def __initialize_visits(self) -> None:
        # Chargement des visites depuis le fichier CSV correspondant
        with open(self.files_paths[InstanceFile.VISITS], "r") as visits_csv_file:
            visits_csv_content = csv.DictReader(visits_csv_file, delimiter=',')
            # Pour chaque ligne du CSV, on crée une visite et on la met dans la liste des visites à effectuer
            for row in visits_csv_content:
                new_visit: Visit = Visit.from_csv_row(row)
                self.visits_to_do[new_visit.vi_id] = new_visit

    def __initialize_distances(self) -> None:
        with open(self.files_paths[InstanceFile.DISTANCES], "r") as distances_txt_file:
            self.distances = np.loadtxt(distances_txt_file).astype(float)

    def __initialize_times(self) -> None:
        with open(self.files_paths[InstanceFile.TIMES], "r") as times_txt_file:
            self.times = np.loadtxt(times_txt_file).astype(int)
