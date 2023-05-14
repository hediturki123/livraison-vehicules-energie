import unittest

from src.models.heuristics import SwapHeuristic


class TestSwapHeuristic(unittest.TestCase):
    def setUp(self) -> None:
        self.visits: list[int] = [1, 2, 3]

    def test_it_should_swap_visits_from_the_start_to_the_middle(self):
        result: list[int] = SwapHeuristic.swap_visits(0, 1, self.visits)
        self.assertEqual([2, 1, 3], result)

    def test_it_should_swap_visits_from_the_start_to_the_end(self):
        result: list[int] = SwapHeuristic.swap_visits(0, 2, self.visits)
        self.assertEqual([3, 2, 1], result)

    def test_it_should_swap_visits_from_the_end_to_the_start(self):
        result: list[int] = SwapHeuristic.swap_visits(2, 0, self.visits)
        self.assertEqual([3, 2, 1], result)

    def test_it_should_swap_visits_from_the_end_to_the_middle(self):
        result: list[int] = SwapHeuristic.swap_visits(2, 1, self.visits)
        self.assertEqual([1, 3, 2], result)

    def test_it_should_swap_visits_from_the_middle_to_the_end(self):
        result: list[int] = SwapHeuristic.swap_visits(1, 2, self.visits)
        self.assertEqual([1, 3, 2], result)

    def test_it_should_swap_visits_from_the_middle_to_the_start(self):
        result: list[int] = SwapHeuristic.swap_visits(1, 0, self.visits)
        self.assertEqual([2, 1, 3], result)

    def test_it_should_not_change_the_visits(self):
        result: list[int] = SwapHeuristic.swap_visits(0, 0, self.visits)
        self.assertEqual([1, 2, 3], result)

    def test_it_should_raise_index_error_when_no_visit(self):
        self.assertRaises(IndexError, SwapHeuristic.swap_visits, 1, 2, [])

    def test_it_should_raise_index_error_when_source_index_out_of_range(self):
        self.assertRaises(IndexError, SwapHeuristic.swap_visits, 4, 2, self.visits)

    def test_it_should_raise_index_error_when_target_index_out_of_range(self):
        self.assertRaises(IndexError, SwapHeuristic.swap_visits, 0, 21, self.visits)


if __name__ == '__main__':
    unittest.main()
