import unittest

from src.models import Context, Vehicle, ContextFile
from src.models.vehicle import DELIVERY_CONST_DURATION


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.context = Context(
            instance_name='mock_instance',
            vehicle_charge_speed="medium",
            vehicle_charge_threshold=0.20,
            keep_first_solution=True,
            verbose=False
        )
        self.vehicle = Vehicle(self.context)

    def test_it_should_start_at_the_warehouse(self):
        self.assertEqual(0, self.vehicle.position)

    def test_it_should_start_with_maximal_distance_remaining(self):
        # Distance maximale définie à 150 dans l'instance 'mock_instance'.
        self.assertEqual(150, self.vehicle.remaining_dist)

    def test_it_should_start_with_zero_distance_driven(self):
        self.assertEqual(0, self.vehicle.total_driven_dist)

    def test_it_should_start_with_full_remaining_time(self):
        # Il y a 43200 secondes entre 7:00 et 19:00 (voir l'instance 'mock_instance').
        self.assertEqual(43200, self.vehicle.remaining_time)

    def test_it_should_start_with_fully_filled_load(self):
        # Le chargement max est de 100 sacs (voir l'instance 'mock_instance').
        self.assertEqual(100, self.vehicle.used_capacity)

    def test_it_should_start_with_no_history(self):
        self.assertEqual([], self.vehicle.history)

    def test_it_should_not_start_with_empty_distances(self):
        self.assertNotEqual([], self.vehicle.distances)

    def test_it_should_not_start_with_empty_times(self):
        self.assertNotEqual([], self.vehicle.times)

    def test_it_should_update_remaining_distance_when_moving(self):
        self.vehicle.remaining_dist = 100
        self.vehicle.move_to(1)  # La visite 1 est à une distance de 2.685 (voir l'instance 'mock_instance').
        self.assertEqual(97.315, self.vehicle.remaining_dist)

    def test_it_should_update_remaining_time_when_moving(self):
        self.vehicle.remaining_time = 600
        self.vehicle.move_to(3)  # Il y a 305 secondes pour aller du dépôt à la visite 3 (voir l'instance 'mock_instance').
        self.assertEqual(295, self.vehicle.remaining_time)

    def test_it_should_update_total_driven_distance_when_moving(self):
        self.vehicle.total_driven_dist = 0
        self.vehicle.move_to(5)  # La visite 5 est une distance de 4.888 (voir l'instance 'mock_instance').
        self.assertEqual(4.888, self.vehicle.total_driven_dist)

    def test_it_should_update_position_when_moving(self):
        self.vehicle.position = 7
        self.vehicle.move_to(4)
        self.assertEqual(4, self.vehicle.position)

    def test_it_should_not_update_position_when_moving_to_actual_position(self):
        self.vehicle.position = 12
        self.vehicle.move_to(12)
        self.assertEqual(12, self.vehicle.position)

    def test_it_should_not_update_remaining_time_when_moving_to_actual_position(self):
        self.vehicle.position = 11
        self.vehicle.remaining_time = 100
        self.vehicle.move_to(11)
        self.assertEqual(100, self.vehicle.remaining_time)

    def test_it_should_not_update_total_driven_distance_when_moving_to_actual_position(self):
        self.vehicle.position = 13
        self.vehicle.total_driven_dist = 5.432
        self.vehicle.move_to(13)
        self.assertEqual(5.432, self.vehicle.total_driven_dist)

    def test_it_should_not_update_remaining_distance_when_moving_to_actual_position(self):
        self.vehicle.position = 99
        self.vehicle.remaining_dist = 47
        self.vehicle.move_to(99)
        self.assertEqual(47, self.vehicle.remaining_dist)

    def test_it_should_update_history_when_moving(self):
        self.vehicle.move_to(1)
        self.assertEqual(['1'], self.vehicle.history)
        self.vehicle.move_to(5)
        self.assertEqual(['1', '5'], self.vehicle.history)

    def test_it_should_update_history_when_charging(self):
        self.vehicle.recharge()
        self.assertEqual(['C'], self.vehicle.history)

    def test_it_should_update_history_when_filling(self):
        self.vehicle.fill()
        self.assertEqual(['R'], self.vehicle.history)

    def test_it_should_not_update_history_when_going_back_to_warehouse(self):
        self.vehicle.move_to(1)
        self.vehicle.move_to(2)
        self.vehicle.move_to(0)
        self.assertEqual(['1', '2'], self.vehicle.history)

    def test_it_can_not_deliver_in_warehouse(self):
        self.assertEqual(False, self.vehicle.can_deliver(0))

    def test_it_can_not_deliver_when_not_enough_capacity(self):
        self.vehicle.used_capacity = 0
        self.vehicle.move_to(1)
        self.assertEqual(False, self.vehicle.can_deliver(1))

    def test_it_can_not_deliver_when_not_enough_time(self):
        self.vehicle.move_to(1)
        self.vehicle.remaining_time = 0
        self.assertEqual(False, self.vehicle.can_deliver(1))

    def test_it_should_not_deliver_when_it_can_not_deliver(self):
        self.vehicle.remaining_time = 0
        self.assertRaises(Exception, self.vehicle.deliver, 1)

    def test_it_should_update_capacity_when_delivering(self):
        self.vehicle.move_to(1)
        self.vehicle.used_capacity = 100
        self.vehicle.deliver(1)
        self.assertEqual(99, self.vehicle.used_capacity)

    def test_it_should_update_remaining_time_when_delivering(self):
        self.vehicle.move_to(1)
        self.vehicle.remaining_time = 1200
        self.vehicle.deliver(1)
        self.assertEqual(1200 - (DELIVERY_CONST_DURATION + 10), self.vehicle.remaining_time)

    def test_it_should_need_recharge_when_under_threshold(self):
        # Le seuil simulé est de 20%.
        self.vehicle.remaining_dist = 19
        self.vehicle.max_dist = 100
        self.assertEqual(True, self.vehicle.needs_recharge())

    def test_it_should_not_need_recharge_when_above_threshold(self):
        # Le seuil simulé est de 20%.
        self.vehicle.remaining_dist = 21
        self.vehicle.max_dist = 100
        self.assertEqual(False, self.vehicle.needs_recharge())

    def test_it_should_use_time_recharging(self):
        self.vehicle.charge_duration = 60
        self.vehicle.remaining_time = 120
        self.vehicle.recharge()
        self.assertEqual(60, self.vehicle.remaining_time)

    def test_it_should_reset_vehicle_distance_when_recharging(self):
        Vehicle.max_dist = 123
        self.vehicle.remaining_dist = 0
        self.vehicle.recharge()
        self.assertEqual(123, self.vehicle.remaining_dist)
