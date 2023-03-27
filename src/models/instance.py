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
            self.visits: dict[int, Visit] = {}
            self.__initialize_visits()
            self.visits_to_do: list[int] = [visit_id for visit_id in self.visits]
            self.visits_to_do.remove(0)

            # Initialisation du dépôt
            self.warehouse: Visit = self.visits[0]

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

    # Exécution de l'algorithme principal
    def execute(self) -> None:
        # Tant qu'il y a des visites à effectuer...
        while len(self.visits_to_do) > 0:
            # On crée un nouveau véhicule
            self.current_vehicle = Vehicle(self.distances, self.times)
            self.used_vehicles.append(self.current_vehicle)
            # On charge le véhicule
            self.current_vehicle.fill()
            # Tant que la journée n'est pas finie (moins le temps pour rentrer)...
            while self.current_vehicle.remaining_time - self.times[self.current_vehicle.position][0] > 0:
                # On s'arrête si le véhicule ne peut plus faire de visite
                if len(self.visits_to_do) <= 0:
                    break
                # La prochaine visite à effectuer est la première de la liste
                next_visit: int = self.visits_to_do[0]
                # Si le véhicule peut se déplacer, livrer puis rentrer
                if self.current_vehicle.can_move_to(next_visit):  # FIXME: manque conditions "livrer" et "rentrer"
                    # Se déplacer puis livrer
                    self.current_vehicle.move_to(next_visit)
                    self.current_vehicle.deliver(self.visits[next_visit].demand)
                    # On enlève la visite de la liste des visites à effectuer
                    self.visits_to_do.remove(next_visit)
                else:
                    # Rentrer puis recharger
                    self.current_vehicle.move_to(0)
                    self.current_vehicle.recharge()
            # Rentrer pour terminer la journée
            self.current_vehicle.move_to(0)

    def __initialize_visits(self) -> None:
        # Chargement des visites depuis le fichier CSV correspondant
        with open(self.files_paths[InstanceFile.VISITS], "r") as visits_csv_file:
            visits_csv_content = csv.DictReader(visits_csv_file, delimiter=',')
            # Pour chaque ligne du CSV, on crée une visite et on la met dans la liste des visites à effectuer
            for row in visits_csv_content:
                new_visit: Visit = Visit.from_csv_row(row)
                self.visits[new_visit.vi_id] = new_visit

    def __initialize_distances(self) -> None:
        with open(self.files_paths[InstanceFile.DISTANCES], "r") as distances_txt_file:
            self.distances = np.loadtxt(distances_txt_file).astype(float)

    def __initialize_times(self) -> None:
        with open(self.files_paths[InstanceFile.TIMES], "r") as times_txt_file:
            self.times = np.loadtxt(times_txt_file).astype(int)
