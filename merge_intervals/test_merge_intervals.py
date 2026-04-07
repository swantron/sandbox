import unittest

from merge_intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_empty(self) -> None:
        self.assertEqual(self.solution.merge([]), [])

    def test_single_interval(self) -> None:
        self.assertEqual(self.solution.merge([[1, 3]]), [[1, 3]])

    def test_no_overlap(self) -> None:
        self.assertEqual(
            self.solution.merge([[1, 2], [4, 5], [7, 8]]),
            [[1, 2], [4, 5], [7, 8]],
        )

    def test_overlapping_merged(self) -> None:
        self.assertEqual(
            self.solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )

    def test_unsorted_input(self) -> None:
        self.assertEqual(
            self.solution.merge([[2, 6], [1, 3]]),
            [[1, 6]],
        )

    def test_touching_endpoints_merge(self) -> None:
        self.assertEqual(
            self.solution.merge([[1, 4], [4, 5]]),
            [[1, 5]],
        )


if __name__ == "__main__":
    unittest.main()
