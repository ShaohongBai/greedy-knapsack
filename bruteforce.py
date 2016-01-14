import itertools

def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    https://docs.python.org/2/library/itertools.html#recipes
    """
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r)
                                         for r in range(len(s)+1))

def knapsack(v, w, W):
    """
    Solve the 0-1 knapsack problem by brute force.

    This guarantees an optimal solution, but its computation is O(2^n).

    The terminology (analogy) used will be the following: there is a burglary of a bank,
    and the burglar has to decide which pieces of gold (with different value and weight)
    to take with him, but he can only carry up to W in weight.

    :param v:      List of values of every piece.
    :param w:      List of weights of every piece.
    :param W:      Maximum weight.
    :return:       A tuple of 2 lists: 1 with the values of the elements chosen, and another list with its weights.

    PRECONDITIONS:
     - Weights are strictly positive (> 0)
     - v and w have the same length
    """

    # elements in the knapsack (the order must be consequent)
    v_in_knapsack = []
    w_in_knapsack = []

    # current total value of all the elements put in the knapsack so far
    total_value_in_knapsack = 0

    # each item will consist on (value, weight)
    items = zip(v, w)

    for subset in powerset(items):
        v_this_subset = [item[0] for item in subset]
        total_value_this_subset = sum(v_this_subset)
        w_this_subset = [item[1] for item in subset]
        total_weight_this_subset = sum(w_this_subset)
        if total_weight_this_subset <= W and total_value_this_subset > total_value_in_knapsack:
            v_in_knapsack = v_this_subset
            w_in_knapsack = w_this_subset
            total_value_in_knapsack = total_value_this_subset

    return v_in_knapsack, w_in_knapsack