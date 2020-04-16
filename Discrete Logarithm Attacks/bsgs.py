from math import ceil, sqrt

def bsgs(g, y, n, max_power=None):
    """
    Baby_step Giant-Step algorithm to solve Discrete Log Problem

    :param g: g of g^x = y (mod n). g > 1.
    :param y: y of g^x = y (mod n). Positive integer.
    :param n: n of g^x = y (mod n). n > 1.
    :param max_power: restricts the search of x between [1, max_power). Useful for Pohling_Hellman
    :returns: x of g^x = y (mod n). If not found returns a TODO.
    """

    # If the search space is not restricted, set max_power to be n
    # and compute m accordingly
    if max_power == None:
        max_power = n
    m = ceil(sqrt(max_power))

    # This dictionary will store pre-computed g^j
    table = dict()

    # Loop to calculate all g^j and fill the table
    g_raised_to_j = 1
    for j in range(0, m):
        table[g_raised_to_j] = j
        g_raised_to_j = (g_raised_to_j * g) % n
    
    # Now we have to compute g^(-im)
    # To do so first we compute g^(-m) and then just keep raising its power in the loop
    g_raised_to_minus_m = pow(g, n-(m+1), n)
    # temp will store g^x * g^(-im)
    temp = y
    for i in range(0, m):
        # If temp is found then return the solution
        if temp in table:
            return (i * m) + table[temp]
        # Update temp
        temp = (temp * g_raised_to_minus_m) % n

    # No x found
    return -1