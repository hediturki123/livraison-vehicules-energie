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

    def __init__(self):
        Vehicle.__id += 1
        self.ve_id: int = Vehicle.__id
        self.dist: float = Vehicle.max_dist
        self.used_capacity: int = 0
        self.remaining_time: int = Vehicle.end_time - Vehicle.start_time
        self.position: int = 0

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

    # Méthode pour vérifier que le véhicule peut se déplacer de <distance> km pendant <duration> secondes.
    def can_move(self, distance: float, duration: float) -> bool:
        return self.dist >= distance and self.remaining_time >= duration

    # Méthode pour déplacer le véhicule à la position <position> sur <distance> km pendant <duration> secondes.
    def move_to(self, new_position: int, distance: float, duration: int):
        if self.can_move(distance, duration):
            self.position = new_position
            self.dist -= distance
            self.remaining_time -= duration
        else:
            raise Exception("vehicle %d can't move to position %d (too far or too long)" % (self.ve_id, new_position))

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

    # Méthode pour vérifier que le véhicule peut charger <freight> sacs à son bord.
    def can_load(self, freight: int) -> bool:
        return all([
            self.position == 0,
            self.total_capacity - self.used_capacity >= freight,
            self.remaining_time >= LOADING_CONST_DURATION
        ])

    # Méthode pour mettre un chargement de <freight> sacs dans le véhicule.
    def load(self, freight: int):
        if self.can_load(freight):
            self.used_capacity += freight
            self.remaining_time -= LOADING_CONST_DURATION
        else:
            raise Exception(
                "vehicle %d can't load freight (%d required ; %d available)" %
                (self.ve_id, freight, self.total_capacity - self.used_capacity)
            )

    # Méthode pour remplir entièrement le véhicule de sacs.
    def fill(self):
        freight: int = self.total_capacity - self.used_capacity
        if freight > 0:
            self.load(freight)

    # Méthode pour recharger la batterie du véhicule (i.e. remettre sa distance disponible au max).
    def recharge(self):
        self.remaining_time -= self.charge_duration
        self.dist = Vehicle.max_dist

    # Méthode pour calculer la durée d'une livraison.
    @staticmethod
    def __get_delivery_duration(amount: int) -> int:
        return DELIVERY_CONST_DURATION + amount * 10
