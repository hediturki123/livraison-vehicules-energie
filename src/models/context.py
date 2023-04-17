import csv
import os.path
import numpy as np
import src.environment as env

from src.models.context_file import ContextFile

WAREHOUSE_POSITION: int = 0


# Contexte de l'instance choisie comportant les distances, les temps, les visites, etc.
class Context:
    def __init__(self, instance_name: str):
        self.__initialize_files(instance_name)

        # Initialisation des visites
        self.__initialize_visits()

        # Initialisation des données de véhicule
        from src.models.vehicle import Vehicle
        Vehicle.initialize(self.files_paths[ContextFile.VEHICLE])

        # Initialisation de la matrice des distances (en kilomètres)
        self.__initialize_distances()

        # Initialisation de la matrice des temps de trajet (en secondes)
        self.__initialize_times()

    def __initialize_files(self, instance_name: str) -> None:
        self.instance_dir = os.path.join(env.ROOT_DIR, 'data', 'instances', instance_name)
        # Vérification de l'existence du dossier de l'instance
        if os.path.isdir(self.instance_dir):
            self.files_paths: dict[ContextFile, str] = {}  # Chemins pour les fichiers d'instance
            # Vérification de l'existence de tous les fichiers d'instance
            for instance_file in ContextFile:
                filename: str = instance_file.value
                filepath: str = os.path.join(self.instance_dir, filename)
                if os.path.isfile(filepath):
                    self.files_paths[instance_file] = filepath
                else:
                    raise Exception('instance "' + instance_name + '" is missing file "' + filename + '"')
        else:
            raise Exception('instance "' + instance_name + '" does not exist')

    def __initialize_visits(self) -> None:
        from src.models.visit import Visit
        self.visits: dict[int, Visit] = {}
        # Chargement des visites depuis le fichier CSV correspondant
        with open(self.files_paths[ContextFile.VISITS], "r") as visits_csv_file:
            visits_csv_content = csv.DictReader(visits_csv_file, delimiter=',')
            # Pour chaque ligne du CSV, on crée une visite et on la met dans la liste des visites à effectuer
            for row in visits_csv_content:
                new_visit: Visit = Visit.from_csv_row(row)
                self.visits[new_visit.vi_id] = new_visit

    def __initialize_distances(self) -> None:
        self.distances: list[list[float]] = []
        with open(self.files_paths[ContextFile.DISTANCES], "r") as distances_txt_file:
            # noinspection PyTypeChecker
            self.distances = np.loadtxt(distances_txt_file).astype(float)

    def __initialize_times(self) -> None:
        self.times: list[list[int]] = []
        with open(self.files_paths[ContextFile.TIMES], "r") as times_txt_file:
            # noinspection PyTypeChecker
            self.times = np.loadtxt(times_txt_file).astype(int)