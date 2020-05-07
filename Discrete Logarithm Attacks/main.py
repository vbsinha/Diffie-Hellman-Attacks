import argparse

from brute_force import brute
from bsgs import bsgs
from pohlig_hellman import pohlig_hellman
from pollard_rho import pollard_rho


# The equation under consideration is g^x = y (mod n)
# We assume g > 0, y > 0 and n > 1. Other cases are trivial / not-interesting.

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--algo", type=str, default="BSGS",
                    choices=["Brute", "BSGS", "Pollard-rho", "Pohlig-Hellman"],
                    help="Algorithm to run to find the discrete log")
parser.add_argument("-g", type=int, required=True)
parser.add_argument("-n", type=int, required=True)
parser.add_argument("-y", type=int, required=True)
parser.add_argument("-o", type=int) # Only required for Pollard-rho
parser.add_argument("--factors", nargs='+', type=int) # Only required for Pohlig-Hellman
parser.add_argument("--powers", nargs='+', type=int) # Only required for Pohlig-Hellman
parser.add_argument("-v", action='store_true')
args = parser.parse_args()

# Some simplifications and assertions
args.g %= args.n
args.y %= args.n

assert args.n > 1, "n {} must be greater than 1".format(args.n)
assert args.g > 0, "g {} must be greater than 0".format(args.g)
assert args.y > 0, "y {} must be greater than 0".format(args.y)
if args.o is not None:
    assert args.o > 0, "o {} must be greater than 0".format(args.o)

# Run the corresponding algorithms
if args.algo == "Brute":
    x = brute(args.g, args.y, args.n)
elif args.algo == "BSGS":
    x = bsgs(args.g, args.y, args.n, verify=args.v)
elif args.algo == "Pollard-rho":
    x = pollard_rho(args.g, args.y, args.n, args.o, verify=args.v)
elif args.algo == "Pohlig-Hellman":
    assert args.factors is not None, "-factors is a compulsary argument for Pohlig-Hellman"
    assert args.powers is not None, "-powers is a compulsary argument for Pohlig-Hellman"
    x = pohlig_hellman(args.g, args.y, args.n, args.factors, args.powers, verify=args.v)

# Print the computed answer
print("Answer")
print(x)