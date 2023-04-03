import csv
import os.path
import numpy as np
import src.environment as env

from src.models.visit import Visit
from src.models.vehicle import Vehicle
from src.models.instance_file import InstanceFile

WAREHOUSE_POSITION: int = 0


class Instance:
    distances: list[list[float]] = []
    times: list[list[int]] = []
    visits: dict[int, Visit] = {}

    def __init__(self, instance_name: str):
        self.__initialize_files(instance_name)

        # Initialisation des visites
        self.__initialize_visits()

        # Initialisation des données de véhicule
        Vehicle.initialize(self.files_paths[InstanceFile.VEHICLE])

        # Initialisation de la matrice des distances (en kilomètres)
        self.__initialize_distances()

        # Initialisation de la matrice des temps de trajet (en secondes)
        self.__initialize_times()

    # Exécution de l'algorithme principal
    def execute(self) -> None:
        # On crée un nouveau véhicule
        current_vehicle: Vehicle = Vehicle()
        used_vehicles: list[Vehicle] = [current_vehicle]
        # On ne charge PAS le véhicule (on le fait avant le départ du pilote du véhicule).
        # Tant qu'il y a des visites à effectuer...
        while len(self.visits_to_do) > 0:
            # La prochaine visite à effectuer est la première de la liste
            next_visit: int = self.visits_to_do[0]
            # Si le véhicule peut se déplacer, livrer puis rentrer
            if current_vehicle.can_move_and_deliver(next_visit, self.visits[next_visit].demand):
                # Se déplacer puis livrer
                current_vehicle.move_to(next_visit)
                current_vehicle.deliver(self.visits[next_visit].demand)
                # On enlève la visite de la liste des visites à effectuer
                self.visits_to_do.remove(next_visit)
            else:
                # Rentrer au dépôt
                current_vehicle.move_to(WAREHOUSE_POSITION)
                # Si le véhicule a besoin d'être rechargé
                if current_vehicle.needs_recharge():
                    # Recharger le véhicule
                    current_vehicle.recharge()
                current_vehicle.fill()
                # Si le véhicule peut se déplacer, livrer puis rentrer
                if current_vehicle.can_move_and_deliver(next_visit, self.visits[next_visit].demand):
                    # Se déplacer puis livrer
                    current_vehicle.move_to(next_visit)
                    current_vehicle.deliver(self.visits[next_visit].demand)
                    # On enlève la visite de la liste des visites à effectuer
                    self.visits_to_do.remove(next_visit)
                else:
                    # On change de véhicule
                    current_vehicle = Vehicle()
                    used_vehicles.append(current_vehicle)
        # Rentrer pour terminer la journée
        current_vehicle.move_to(0)

        for vehicle in used_vehicles:
            print("%s" % ",".join(vehicle.history))

    def __initialize_files(self, instance_name: str) -> None:
        self.instance_dir = os.path.join(env.ROOT_DIR, 'data', 'instances', instance_name)
        # Vérification de l'existence du dossier de l'instance
        if os.path.isdir(self.instance_dir):
            self.files_paths: dict[InstanceFile, str] = {}  # Chemins pour les fichiers d'instance
            # Vérification de l'existence de tous les fichiers d'instance
            for instance_file in InstanceFile:
                filename: str = instance_file.value
                filepath: str = os.path.join(self.instance_dir, filename)
                if os.path.isfile(filepath):
                    self.files_paths[instance_file] = filepath
                else:
                    raise Exception('instance "' + instance_name + '" is missing file "' + filename + '"')
        else:
            raise Exception('instance "' + instance_name + '" does not exist')

    def __initialize_visits(self) -> None:
        # Chargement des visites depuis le fichier CSV correspondant
        with open(self.files_paths[InstanceFile.VISITS], "r") as visits_csv_file:
            visits_csv_content = csv.DictReader(visits_csv_file, delimiter=',')
            # Pour chaque ligne du CSV, on crée une visite et on la met dans la liste des visites à effectuer
            for row in visits_csv_content:
                new_visit: Visit = Visit.from_csv_row(row)
                Instance.visits[new_visit.vi_id] = new_visit
        self.visits_to_do: list[int] = [visit_id for visit_id in self.visits]
        self.visits_to_do.remove(WAREHOUSE_POSITION)

    def __initialize_distances(self) -> None:
        with open(self.files_paths[InstanceFile.DISTANCES], "r") as distances_txt_file:
            Instance.distances = np.loadtxt(distances_txt_file).astype(float)

    def __initialize_times(self) -> None:
        with open(self.files_paths[InstanceFile.TIMES], "r") as times_txt_file:
            Instance.times = np.loadtxt(times_txt_file).astype(int)
