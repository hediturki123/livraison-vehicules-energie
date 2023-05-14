import unittest

from src.models.heuristics import TripletShiftHeuristic


class TestTripletShiftHeuristic(unittest.TestCase):
    def setUp(self) -> None:
        self.visits: list[int] = [1, 2, 3, 4, 5]

    def test_it_should_shift_visits(self):
        result: list[int] = TripletShiftHeuristic.shift_visits(0, self.visits)
        self.assertEqual([4, 1, 2, 3, 5], result)

    def test_it_should_shift_visits_2(self):
        result: list[int] = TripletShiftHeuristic.shift_visits(1, self.visits)
        self.assertEqual([1, 5, 2, 3, 4], result)

    def test_it_should_shift_visits_at_the_start(self):
        result: list[int] = TripletShiftHeuristic.shift_visits(2, self.visits)
        self.assertEqual([5, 2, 1, 3, 4], result)

    def test_it_should_shift_visits_with_modulo(self):
        result: list[int] = TripletShiftHeuristic.shift_visits(10, self.visits)
        self.assertEqual([4, 1, 2, 3, 5], result)


if __name__ == '__main__':
    unittest.main()
