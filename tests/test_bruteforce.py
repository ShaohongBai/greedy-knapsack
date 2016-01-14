import random
import unittest
import numpy as np
from knapsack_algorithm.tests.bank_cases \
    import ManualBank, SameGoldBank, SameValuesBank, SameWeightBank

####################
# Test cases that check that the brute force algorithm for the 0-1 knapsack problem works fine.
####################

method = 'bruteforce'

class TestManualCase(unittest.TestCase):
    """ When value and weight distribution is specified manually. """

    def test_1(self):
        values_bank = [60, 100, 120]
        weights_bank = [10, 20, 30]
        max_weight = 50
        bank = ManualBank()
        bank.setup(values_bank, weights_bank)
        values_solution = [100, 120]
        weights_solution = [20, 30]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_2(self):
        values_bank = [60, 100, 120]
        weights_bank = [10, 20, 30]
        max_weight = np.infty  # carry as much as you want
        bank = ManualBank()
        bank.setup(values_bank, weights_bank)
        values_solution = values_bank
        weights_solution = weights_bank
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_3(self):
        values_bank = [60, 100, 120, 100, 80]
        weights_bank = [10, 20, 30, 50, 80]
        max_weight = 60
        bank = ManualBank()
        bank.setup(values_bank, weights_bank)
        values_solution = [60, 100, 120]
        weights_solution = [10, 20, 30]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_4(self):
        values_bank = [60, 100, 120, 100, 80]
        weights_bank = [10, 20, 30, 50, 80]
        max_weight = 120
        bank = ManualBank()
        bank.setup(values_bank, weights_bank)
        values_solution = [60, 100, 120, 100]
        weights_solution = [10, 20, 30, 50]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_5(self):
        values_bank = [60, 100, 120, 100, 80]
        weights_bank = [10, 20, 30, 50, 80]
        max_weight = 200
        bank = ManualBank()
        bank.setup(values_bank, weights_bank)
        values_solution = [60, 100, 120, 100, 80]
        weights_solution = [10, 20, 30, 50, 80]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_6(self):
        values_bank = [10, 100, 120, 100, 80]
        weights_bank = [10, 20, 30, 50, 80]
        max_weight = 120
        bank = ManualBank()
        bank.setup(values_bank, weights_bank)
        values_solution = [10, 100, 120, 100]
        weights_solution = [10, 20, 30, 50]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))


class TestSameValuesCase(unittest.TestCase):
    """ When the values of all the pieces in the bank are equal (egalitarian bank). """

    def test_1(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = np.infty
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = bank.values
        weights_solution = bank.weights
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_2(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = 1
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = [100]
        weights_solution = [1]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_3(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = 3
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = [value, value]
        weights_solution = [1, 2]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_4(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = 7
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = [value, value, value]
        weights_solution = [1, 2, 4]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_5(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = 12
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = [value, value, value, value]
        weights_solution = [1, 2, 4, 5]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_6(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = 23
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = [value, value, value, value, value]
        weights_solution = [1, 2, 4, 5, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_7(self):
        value = 100
        purities = [100, 50, 25, 20, 10, 5]
        random.shuffle(purities)  # the order should not matter
        max_weight = 45
        bank = SameValuesBank()
        bank.setup(value=value, purities=purities)
        values_solution = [value, value, value, value, value, value]
        weights_solution = [1, 2, 4, 5, 10, 20]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))


class TestSameWeightCase(unittest.TestCase):
    """ When the weights of all the pieces in the bank are the same. """

    def test_1(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = np.infty
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = bank.values
        weights_solution = bank.weights
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_2(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 10
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120]
        weights_solution = [10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_3(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 20
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120, 100]
        weights_solution = [10, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_4(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 30
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120, 100, 90]
        weights_solution = [10, 10, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_5(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 41
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120, 100, 90, 80]
        weights_solution = [10, 10, 10, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_6(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 51
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120, 100, 90, 80, 70]
        weights_solution = [10, 10, 10, 10, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_7(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 61
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120, 100, 90, 80, 70, 60]
        weights_solution = [10, 10, 10, 10, 10, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_8(self):
        weight = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 72
        bank = SameWeightBank()
        bank.setup(weight=weight, values=values)
        values_solution = [120, 100, 90, 80, 70, 60, 50]
        weights_solution = [10, 10, 10, 10, 10, 10, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))


class TestSameGoldCase(unittest.TestCase):
    """ When the type of gold (ratio between value and weight) of the items is the same. """

    def test_1(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = np.infty
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = bank.values
        weights_solution = bank.weights
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_2(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 12
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = [120]
        weights_solution = [12]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_3(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 11
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = [60, 50]
        weights_solution = [6, 5]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        self.assertCountEqual(zip(values_robbed, weights_robbed),
                              zip(values_solution, weights_solution))

    def test_4(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 22
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = [120, 100]
        weights_solution = [12, 10]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        try:
            self.assertCountEqual(zip(values_robbed, weights_robbed),
                                  zip(values_solution, weights_solution))
        except AssertionError:
            # this assertion is because the optimal solution may not be unique, let's check at least optimality
            self.assertEqual(sum(weights_solution), sum(weights_robbed))

    def test_5(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 15
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = [80, 70]
        weights_solution = [8, 7]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        try:
            self.assertCountEqual(zip(values_robbed, weights_robbed),
                                  zip(values_solution, weights_solution))
        except AssertionError:
            # this assertion is because the optimal solution may not be unique, let's check at least optimality
            self.assertEqual(sum(weights_solution), sum(weights_robbed))

    def test_6(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 21
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = [80, 70, 60]
        weights_solution = [8, 7, 6]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        try:
            self.assertCountEqual(zip(values_robbed, weights_robbed),
                                  zip(values_solution, weights_solution))
        except AssertionError:
            # this assertion is because the optimal solution may not be unique, let's check at least optimality
            self.assertEqual(sum(weights_solution), sum(weights_robbed))

    def test_7(self):
        purity = 10
        values = [120, 100, 90, 80, 70, 60, 50]
        random.shuffle(values)  # the order should not matter
        max_weight = 19
        bank = SameGoldBank()
        bank.setup(purity=purity, values=values)
        values_solution = [100, 40, 50]
        weights_solution = [10, 4, 5]
        values_robbed, weights_robbed = bank.rob(max_weight=max_weight, knapsack_alg=method)
        try:
            self.assertCountEqual(zip(values_robbed, weights_robbed),
                                  zip(values_solution, weights_solution))
        except AssertionError:
            # this assertion is because the optimal solution may not be unique, let's check at least optimality
            self.assertEqual(sum(weights_solution), sum(weights_robbed))