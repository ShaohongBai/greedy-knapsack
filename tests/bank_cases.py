import numpy as np
from ..greedy import knapsack as greedy_knapsack
from ..bruteforce import knapsack as bruteforce_knapsack

####################
# Classes to test the Knapsack problem for a variety of input types:
#  very large inputs, already sorted inputs, inversely sorted...
# The terminology (analogy) used will be the following: there is a burglary in a bank, and the burglar has to decide
# which pieces of gold (with different value and weight) to take with him, but he can only carry up to W in weight.
# Each class corresponds to a different case with a different distribution of values and weights
# (different banks have different pieces of gold).
####################

class BaseBank:
    """
    Base class for BankCases.
    Classes that inherit from this class provide BankCases with different distribution of pieces.
    This class should not be used directly.
    """

    def __init__(self):
        self.values = []
        self.weights = []

    def rob(self, max_weight, knapsack_alg):
        if knapsack_alg == 'greedy':
            return greedy_knapsack(v=self.values, w=self.weights, W=max_weight)
        elif knapsack_alg == 'bruteforce':
            return bruteforce_knapsack(v=self.values, w=self.weights, W=max_weight)
        else:
            raise NotImplementedError()
            # raise NotImplementedError("Only 'greedy' and 'dynamic' algorithms are implemented")

class ManualBank(BaseBank):
    """ Values and weights are manually specified. """

    def setup(self, values, weights):
        self.values = values
        self.weights = weights

class SameGoldBank(BaseBank):
    """
    The purity of all the gold pieces are the same. They only have one kind of gold.
    But they might have different values. Weights adapt accordingly.
    """

    def setup(self, purity, values):
        self.values = values
        self.weights = np.array(values)/purity

class SameValuesBank(BaseBank):
    """
    The values of all the pieces in the bank are equal (egalitarian bank).
    But they might have different purities. Weights adapt accordingly.
    """
    def setup(self, value, purities):
        self.values = value * np.ones_like(purities)
        self.weights = self.values / np.array(purities)

class SameWeightBank(BaseBank):
    """
    The weights of all the pieces in the bank are equal.
    But they might have different values.
    """
    def setup(self, weight, values):
        self.weights = weight * np.ones_like(values)
        self.values = values