import argparse

from brute_force import brute
from bsgs import bsgs
from pollard_rho import pollard_rho
from pohlig_hellman import pohlig_hellman


def check_positive(value):
    # Checks if the provided argument is positive integer
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("{} is an invalid positive int value".format(value))
    return ivalue

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--algo", type=str, default="BSGS",
                    choices=["Brute", "BSGS", "Pollard-rho", "Pohlig-Hellman"],
                    help="Algorithm to run to find the discrete log")
parser.add_argument("-g", type=check_positive, required=True)
parser.add_argument("-n", type=check_positive, required=True)
parser.add_argument("-y", type=check_positive, required=True)
parser.add_argument("-o", type=check_positive)
args = parser.parse_args()

# Some assertions to check input
assert args.g < args.n, "Generator {} must be smaller than n {}".format(args.g, args.n)
assert args.y < args.n, "y {} must be smaller than n {}".format(args.y, args.n)

# Run the corresponding algorithms
if args.algo == "Brute":
    x = brute(args.g, args.y, args.n)
elif args.algo == "BSGS":
    x = bsgs(args.g, args.y, args.n)
elif args.algo == "Pollard-rho":
    x = pollard_rho(args.g, args.y, args.n, args.o)
elif args.algo == "Pohlig-Hellman":
    x = pohlig_hellman(args.g, args.y, args.n)

# Print the computed answer
print("Answer")
print(x)