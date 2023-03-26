import configparser as ini

vehicle_ini_section: str = 'Vehicle'


class Vehicle:
    __id: int = -1
    max_dist: float
    total_capacity: int
    start_time: int
    end_time: int
    start_position: (float, float)

    def __init__(self):
        Vehicle.__id += 1
        self.ve_id: int = Vehicle.__id
        self.dist: float = Vehicle.max_dist
        self.used_capacity: int = 0
        self.remaining_time: int = Vehicle.end_time - Vehicle.start_time
        self.position: (float, float) = Vehicle.start_position

    @staticmethod
    def initialize(ini_path: str, start_position: (float, float)):
        # Lecture des données de base du véhicule depuis le fichier .ini
        ini_parser = ini.ConfigParser()
        ini_parser.read(ini_path)

        # Vérification de la validité du fichier chargé
        if not ini_parser.has_section(vehicle_ini_section):
            raise Exception('invalid ini file for vehicle (missing Vehicle section)')
        vehicle_ini = ini_parser[vehicle_ini_section]

        # Chargement de la distance maximale (en km)
        max_dist_key: str = 'max_dist'
        if max_dist_key in vehicle_ini:
            Vehicle.max_dist = float(vehicle_ini.get(max_dist_key))
        else:
            raise Exception('invalid ini file for vehicle (missing "max_dist" key)')

        # Chargement de la capacité (sans unité)
        capacity_key: str = 'capacity'
        if capacity_key in vehicle_ini:
            Vehicle.total_capacity = vehicle_ini.get(capacity_key)
        else:
            raise Exception('invalid ini file for vehicle (missing "capacity" key)')

        # Chargement de l'heure de départ (en secondes)
        start_time_key: str = "start_time"
        if start_time_key in vehicle_ini:
            [hours, minutes] = vehicle_ini.get(start_time_key).split(':')
            start_time = int(hours) * 3600 + int(minutes) * 60
            Vehicle.start_time = start_time
        else:
            raise Exception('invalid ini file for vehicle (missing "start_time" key)')

        # Chargement de l'heure d'arrivée (en secondes)
        end_time_key: str = "end_time"
        if end_time_key in vehicle_ini:
            [hours, minutes] = vehicle_ini.get(end_time_key).split(':')
            end_time = int(hours) * 3600 + int(minutes) * 60
            Vehicle.end_time = end_time
        else:
            raise Exception('invalid ini file for vehicle (missing "end_time" key)')

        # Affectation de la position de départ
        Vehicle.start_position = start_position
