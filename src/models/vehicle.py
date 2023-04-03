import configparser as ini

VEHICLE_INI_SECTION: str = 'Vehicle'
DELIVERY_CONST_DURATION: int = 300
LOADING_CONST_DURATION: int = 600


class Vehicle:
    __id: int = -1
    max_dist: float
    total_capacity: int
    start_time: int
    end_time: int
    charge_duration: int = 10800  # TODO: Prendre en compte la vitesse de charge.

    def __init__(self, distances: list[list[float]], times: list[list[int]]):
        Vehicle.__id += 1
        self.ve_id: int = Vehicle.__id
        self.dist: float = Vehicle.max_dist
        self.used_capacity: int = Vehicle.total_capacity
        self.remaining_time: int = Vehicle.end_time - Vehicle.start_time
        self.position: int = 0
        self.history: list[str] = []
        self.distances = distances
        self.times = times

    @staticmethod
    def initialize(ini_path: str):
        # Lecture des données de base du véhicule depuis le fichier .ini
        ini_parser = ini.ConfigParser()
        ini_parser.read(ini_path)

        # Vérification de la validité du fichier chargé
        if not ini_parser.has_section(VEHICLE_INI_SECTION):
            raise Exception('invalid ini file for vehicle (missing Vehicle section)')
        vehicle_ini = ini_parser[VEHICLE_INI_SECTION]

        # Chargement de la distance maximale (en km)
        max_dist_key: str = 'max_dist'
        if max_dist_key in vehicle_ini:
            Vehicle.max_dist = float(vehicle_ini.get(max_dist_key))
        else:
            raise Exception('invalid ini file for vehicle (missing "max_dist" key)')

        # Chargement de la capacité (sans unité)
        capacity_key: str = 'capacity'
        if capacity_key in vehicle_ini:
            Vehicle.total_capacity = int(vehicle_ini.get(capacity_key))
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

    def can_move_and_deliver(self, position: int, demand: int) -> bool:
        if position == 0:
            return True
        return all([
            self.dist >= self.distances[self.position][position] + self.distances[position][0],
            self.remaining_time >= self.times[self.position][position]
            + self.times[position][0] + self.__get_delivery_duration(demand),
            self.used_capacity >= demand
        ])

    # Méthode pour déplacer le véhicule à la position <position> sur <distance> km pendant <duration> secondes.
    def move_to(self, new_position: int):
        if new_position != self.position:
            self.dist -= self.distances[self.position][new_position]
            self.remaining_time -= self.times[self.position][new_position]
            self.position = new_position
            if new_position != 0:
                self.history.append("%d" % new_position)

    # Méthode pour vérifier si le véhicule peut effectuer une livraison (i.e. s'il a assez de chargement).
    def can_deliver(self, demand: int) -> bool:
        return all([
            self.position != 0,
            self.used_capacity >= demand,
            self.remaining_time >= self.__get_delivery_duration(demand)
        ])

    # Méthode pour effectuer une livraison (i.e. vider le chargement du véhicule).
    def deliver(self, amount: int):
        if self.can_deliver(amount):
            self.used_capacity -= amount
            self.remaining_time -= self.__get_delivery_duration(amount)
        else:
            raise Exception(
                "vehicle %d can't make delivery (%d required ; %d available)" %
                (self.ve_id, amount, self.used_capacity)
            )

    # Méthode pour remplir entièrement le véhicule de sacs.
    def fill(self) -> None:
        self.used_capacity = Vehicle.total_capacity
        self.remaining_time -= LOADING_CONST_DURATION
        self.history.append("R")

    # Méthode pour déterminer si le véhicule a besoin d'être rechargé ou non.
    def needs_recharge(self) -> bool:
        return self.dist / self.max_dist < 0.20

    # Méthode pour recharger la batterie du véhicule (i.e. remettre sa distance disponible au max).
    def recharge(self):
        self.remaining_time -= self.charge_duration
        self.dist = Vehicle.max_dist
        self.history.append("C")

    # Méthode pour calculer la durée d'une livraison.
    @staticmethod
    def __get_delivery_duration(amount: int) -> int:
        return DELIVERY_CONST_DURATION + amount * 10
