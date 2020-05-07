# [Diffie-Hellman-Attacks](https://github.com/vbsinha/Diffie-Hellman-Attacks/)

Implementation of the following algorithms used to attack Discrete Logarithm Problems (which in turn drives Diffie-Hellman Cryptosystem):
* Brute Force
* Baby-step Giant-step
* Pollard’s ρ algorithm
* Pohlig-Hellman algorithm 

A description of these algorithms have been provided in [algorithms.pdf](https://github.com/vbsinha/Diffie-Hellman-Attacks/blob/master/algorithms.pdf)

### Prerequisites
* Python 3.7

## Running the code

The program computes the discrete log. Given g, y and n it computes x such that g^x = y (mod n).

To run any of the code first change directories to Discrete Logarithm Attacks
```bash
cd Discrete\ Logarithm\ Attacks/
```

The code only works for 0 < g < n, 1 < n and 0 < y < n (which are the usual limits).

To brute force find x use (for eg. with n = 97, g = 3, y = 18),
```bash
python main.py --algo Brute -n 97 -g 3 -y 18
```
This returns answer 45 as expected. If no solution x exists, the returned answer is -1, as for the follwoing case:
```bash
python main.py --algo Brute -n 11 -g 3 -y 6
```

Similarly to run BSGS change --algo to BSGS:
```bash
python main.py --algo BSGS -n 97 -g 3 -y 18
```
BSGS and Pollard's rho algorithm work only for prime n. They might result incorrect results for composite n. To make them check if n is prime before running the algorithm pass -v (this might blow the running time for large n and should be avoided):
```bash
python main.py --algo BSGS -n 97 -g 3 -y 18 -v
```

To run Pollard's rho algorithm use
```bash
python main.py --algo Pollard-rho -n 11 -g 3 -y 9 -o 5 -v
```
-o argument provides the order of g mod n. If -o is not provided, the answer returned might not be the smallest x satisfying the equation. For eg.
```bash
python main.py --algo Pollard-rho -n 11 -g 3 -y 4 -v
```
returns 9, which is a correct answer, but not the smallest correct answer, 4.

To run Pohlig Hellman algorithm the prime factorization of n-1 must be passed in the form of two list, factors and powers such that prod_i factors[i]^powers[i] = n-1. Also the algorithm only works g^(n-1) (mod n) = 1. As 10 = 2 x 5, we can run,
```bash
python main.py --algo Pohlig-Hellman -n 11 -g 3 -y 4 --factors 2 5 --powers 1 1 -v
``` 

To run the tests
```bash
python -m unittest test
```

## License
This code is provided using the [MIT License](LICENSE).

---
This project was a part of the course INF 385T: Applied Encryption, offered in Spring 2020 at University of Texas at Austin.