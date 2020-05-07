from brute_force import brute
from bsgs import bsgs
from functools import reduce
from mathlib import mod_inverse, chinese_remainder
from operator import mul


def pohlig_hellman(g: int, y: int, n: int, factors: [int], powers: [int], verify: bool = False) -> int:
    """ 
    Solves Discrete Log using Pohlig Hellman. Works best when factors of n-1 are small

    This algorithm only works when g^(n-1) = 1, which will hold true if g is a generator or if n is prime.
    Expects factorization of n-1 in factors and powers.
    n-1 = prod_{i} factors[i] ** powers[i]

    :param g: g of g^x = y (mod n). g > 1.
    :param y: y of g^x = y (mod n). Positive integer.
    :param n: n of g^x = y (mod n). n > 1.
    :param factors: Prime factors of n-1.
    :param powers: Exponent of each factor in the prime factorization of n-1.
    :param verify: Does some checks if input is appropriate when True
    :returns: x
    """

    assert pow(g, n-1, n) == 1, "Pohlig Hellman only works for g and n such that g^(n-1) = 1 (mod n)"

    # Compute the values (factors[i]^powers[i]) for each i
    mods = [pow(factor, power) for (factor, power) in zip(factors, powers)]

    if verify:
        assert n-1 == reduce(mul, mods), "Improper factors passed to pohlig_hellman"

    # Compute x (mod (factors[i]^powers[i])) for each i
    x_is = [__pohlig_hellman_helper(g, y, n, factor, power, verify) for (factor, power) in zip(factors, powers)]

    # Get x (mod n-1) using the Chinese remainder theorem
    return chinese_remainder(x_is, mods)
    

def __pohlig_hellman_helper(g: int, y: int, n: int, p: int, e: int, verify: bool = False) -> int:
    """
    Computes x mod (p^e) where g^x = y (mod n) and 
    e is the highest non-zero exponent of p such that p^e | n-1
    
    :param g: g of g^x = y (mod n). g > 1.
    :param y: y of g^x = y (mod n). Positive integer.
    :param n: n of g^x = y (mod n). n > 1.
    :param p: Prime integer p
    :param e: Positive integer e such that p^e | n-1 and p^(e+1) does not divide n-1
    :param verify: Verifies that p^e | n-1 if True
    :returns: x mod (p^e)
    """
    if verify:
        assert (n-1) % pow(p, e) == 0, "Inappropriate input to __pohlig_hellman_helper"

    # x that will eventually contain the answer
    x = 0
    # Precompute usefull value: g^((n-1)/p) (mod n)
    gamma = pow(g, (n-1)//p, n)

    # Stores p^j, j starting at 0 and increasing with loop iterations
    p_power_j = 1

    # Let x = sum_{0 <= i < e} x_0*p^i + c*p^e
    # Each iteration of loop computes x_j and builds up the answer x accordingly
    for j in range(e):
        # This makes h = g ^ (x_i * ((n-1)/p)) (mod n)
        # h = pow(y, (n-1)//pow(p, (j+1)), n)
        h = pow(y, (n-1)//(p_power_j * p), n)
        # h is the x_jth power of gamma
        # Now we find x_j again using Discrete Log algorithm
        # When p > 2 we use BSGS when p = 2 we use Brute
        # BSGS takes sqrt(p) time and Brute takes O(1) time as x_j in that case is 0/1.
        if p > 2:
            # We know that x_j < p so we restrict BSGS to only search till p
            x_j = bsgs(gamma, h, n, p)
        else:
            x_j = brute(gamma, h, n)

        if x_j < 0:
            print("Either there is no solution x or Pohlig Hellman algorithm fails on this instance")
            exit()

        # Update x by adding x_j * (p^j)
        curr_exp = p_power_j * x_j
        x += curr_exp

        # This is equivalent to removing g^(x_j * (p^j)) from y
        # So in the next step smallest power of p in x would be (j+1) 
        y = (y * mod_inverse(pow(g, curr_exp, n), n)) % n
        p_power_j *= p

    return x