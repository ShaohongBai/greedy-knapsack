def unzip(iterable):
    return zip(*iterable)

def knapsack(v, w, W):
    """
    Solve the 0-1 knapsack problem using a greedy approach.

    The terminology (analogy) used will be the following: there is a burglary of a bank,
    and the burglar has to decide which pieces of gold (with different value and weight)
    to take with him, but he can only carry up to W in weight.

    A greedy burglar would do the following: look for the "purest" (most dense)
    gold piece, and if he can carry it, put it in the knapsack.
    Repeat this procedure with the remaining pieces.
    This is what this method implements.
    This method is greedy because the thief is taking the step that maximizes
    a profit function (value/weight in this case) at every step.
    Obviously, this does not guarantee to obtain the maximum profit,
    but the burglar was in a rush and only had polynomial time to rob the bank.

    :param v:      List of values of every piece.
    :param w:      List of weights of every piece.
    :param W:      Maximum weight.
    :return:       A tuple of 2 lists: 1 with the values of the elements chosen,
                   and another list with its weights.

    PRECONDITIONS:
     - Weights are strictly positive (> 0)
     - v and w have the same length
    """

    # elements in the knapsack (the order must be consequent)
    v_in_knapsack = []
    w_in_knapsack = []

    # current weight of all the elements put in the knapsack so far
    weight_in_knapsack = 0

    # sort elements by purity in descendant order
    v_sorted, w_sorted = unzip(sorted(zip(v, w), key=lambda x: x[0]/x[1], reverse=True))

    for v_i, w_i in zip(v_sorted, w_sorted):
        if w_i + weight_in_knapsack <= W:  # if I can carry it,
            v_in_knapsack.append(v_i)
            w_in_knapsack.append(w_i)
            weight_in_knapsack += w_i

    return v_in_knapsack, w_in_knapsack