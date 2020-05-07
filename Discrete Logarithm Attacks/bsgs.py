from math import ceil, sqrt
from mathlib import is_prime

def bsgs(g, y, p, max_power=None, verify: bool = False):
    """
    Baby-Step Giant-Step algorithm to solve Discrete Log Problem

    :param g: g of g^x = y (mod n). g > 0.
    :param y: y of g^x = y (mod n). Non-negative integer.
    :param p: p of g^x = y (mod p). Prime number.
    :param max_power: restricts the search of x between [1, max_power). Useful for Pohling_Hellman
    :param verify: Checks if p is prime when True
    :returns: x of g^x = y (mod n). If not found returns -1.
    """

    if verify:
        assert is_prime(p), "Pollard-rho works for prime p"
    else:
        print("BSGS running assuming passed n is prime. If not, answer may be wrong.")

    # If the search space is not restricted, set max_power to be n
    # and compute m accordingly
    if max_power == None:
        max_power = p
    m = ceil(sqrt(max_power))

    # This dictionary will store pre-computed g^j
    table = dict()

    # Loop to calculate all g^j and fill the table
    g_raised_to_j = 1
    for j in range(0, m):
        table[g_raised_to_j] = j
        g_raised_to_j = (g_raised_to_j * g) % p
    
    # Now we have to compute g^(-im)
    # To do so first we compute g^(-m) and then just keep raising its power in the loop
    g_raised_to_minus_m = pow(g, p-(m+1), p)
    # temp will store g^x * g^(-im)
    temp = y
    for i in range(0, m):
        # If temp is found then return the solution
        if temp in table:
            return (i * m) + table[temp]
        # Update temp
        temp = (temp * g_raised_to_minus_m) % p

    # No x found
    return -1