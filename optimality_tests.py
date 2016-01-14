import random
import matplotlib.pyplot as plt
import numpy as np
from knapsack_algorithm import bruteforce
from knapsack_algorithm import greedy

####################
# This class measures the optimality of the greedy algorithm of a very diverse type of inputs.
####################

class OptimalityTests:
    """ Measures the optimality of the greedy algorithm for a bunch of inputs. """

    def __init__(self):
        self.min_n_elems = 1
        self.max_n_elems = 22

    def run(self):
        self.test_manual_1()
        self.test_manual_2()
        # self.test_manual_3_same_weight()
        # self.test_manual_4_same_value()
        # self.test_same_gold()
        # self.test_same_values()
        # self.test_same_weight()

    def test_manual_1(self):

        print("_______Test 1_______")

        values = [120, 100, 50, 60, 120, 40, 80]
        weights = [6, 2, 10, 1, 5, 4, 8]

        for W in range(1, sum(weights) + 1):
            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])

            optimality = greedy_value / optimum_value

            print("W={W} \t (gred/opt)=({gred}/{opt}) \t optimality={optimality}".
                  format(W=W, optimality=optimality, gred=greedy_value, opt=optimum_value))

    def test_manual_2(self):

        print("_______Test 2_______")

        values = [140, 120, 100, 80, 60, 40, 20]
        weights = [10, 6, 2, 5, 3, 4, 1]

        for W in range(1, sum(weights) + 1):
            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])

            optimality = greedy_value / optimum_value

            print("W={W} \t (gred/opt)=({gred}/{opt}) \t optimality={optimality}".
                  format(W=W, optimality=optimality, gred=greedy_value, opt=optimum_value))

    def test_manual_3_same_weight(self):

        print("_______Test 3: same weight_______")

        values = [29, 28, 21, 17, 16, 13, 12, 10]
        weights = [2] * len(values)

        for W in range(2, sum(weights) + 1):
            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])

            optimality = greedy_value / optimum_value

            print("W={W} \t (gred/opt)=({gred}/{opt}) \t optimality={optimality}".
                  format(W=W, optimality=optimality, gred=greedy_value, opt=optimum_value))

    def test_manual_4_same_value(self):

        print("_______Test 4: same value _______")

        values = [10, 10, 10, 10, 10, 10, 10]
        weights = [2, 8, 4, 10, 15, 3, 6]

        for W in range(2, sum(weights) + 1):
            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])

            optimality = greedy_value / optimum_value

            print("W={W} \t (gred/opt)=({gred}/{opt}) \t optimality={optimality}".
                  format(W=W, optimality=optimality, gred=greedy_value, opt=optimum_value))

    def test_same_gold(self):

        print("_____Test Same Gold_____")

        # constant purity, and the values form a uniform random distribution
        purity = 10
        max_val = 1000

        for n_elems in range(self.min_n_elems, self.max_n_elems + 1):
            values = [random.randrange(start=1, stop=max_val) for _ in range(n_elems)]
            # print("values={values}".format(values=values))
            weights = list(np.array(values) / purity)
            # print("weights={weights}".format(weights=weights))
            W = np.sum(weights) / 2

            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])
            if greedy_value == 0 and optimum_value == 0:
                continue
            optimality = greedy_value / optimum_value

            print("n_elems={n_elems} \t\t optimality={optimality} \t\t ({gred}/{opt})".format(n_elems=n_elems,
                                                                                              optimality=optimality,
                                                                                              gred=greedy_value,
                                                                                              opt=optimum_value))

    def test_same_values(self):

        print("_____Test Same Values_____")

        # constant value, and the purities form a uniform random distribution
        value = 10
        max_weight = 100

        for n_elems in range(self.min_n_elems, self.max_n_elems + 1):
            # values = [np.random.exponential() for _ in range(n_elems)]
            weights = [random.randrange(start=1, stop=max_weight) for _ in range(n_elems)]
            # print("values={values}".format(values=values))
            values = [value] * n_elems
            # print("weights={weights}".format(weights=weights))
            W = np.sum(weights) / 3

            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])
            if greedy_value == 0 and optimum_value == 0:
                continue
            optimality = greedy_value / optimum_value

            print("n_elems={n_elems} \t\t (gred/opt)=({gred}/{opt}) \t\t optimality={optimality}".
                  format(n_elems=n_elems, optimality=optimality, gred=greedy_value, opt=optimum_value))

    def test_same_weight(self):

        print("_____Test Same Weight_____")

        # constant weight, and the values form a uniform random distribution
        weight = 31

        max_value = 100

        for n_elems in range(self.min_n_elems, self.max_n_elems + 1):
            values = [random.randrange(start=1, stop=max_value) for _ in range(n_elems)]
            # print("values={values}".format(values=values))
            weights = [weight] * n_elems
            # print("weights={weights}".format(weights=weights))
            W = np.sum(weights) / 2

            optimum_value = sum(bruteforce.knapsack(values, weights, W)[0])
            greedy_value = sum(greedy.knapsack(values, weights, W)[0])
            if greedy_value == 0 and optimum_value == 0:
                continue
            optimality = greedy_value / optimum_value

            print("n_elems={n_elems} \t\t optimality={optimality}\t\t ({gred}/{opt})".format(n_elems=n_elems,
                                                                                             optimality=optimality,
                                                                                             gred=greedy_value,
                                                                                             opt=optimum_value))
if __name__ == "__main__":
    OptimalityTests().run()
