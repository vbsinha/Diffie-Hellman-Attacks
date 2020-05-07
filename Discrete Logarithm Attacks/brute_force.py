def brute(g, y, n):
    """
    Brute Force to solve Discrete Log

    :param g: g of g^x = y (mod n). g > 0.
    :param y: y of g^x = y (mod n). Non-negative integer.
    :param n: n of g^x = y (mod n). n > 1.
    :returns: x of g^x = y (mod n). If not found returns -1.
    """
    # Iterate over all g^i and see if any one matches
    # Start with i = 0
    g_raised_to_i = 1
    for i in range(0, n-1):
        # If matched we have found x
        if g_raised_to_i == y:
            return i
        g_raised_to_i = (g_raised_to_i * g) % n
    return -1