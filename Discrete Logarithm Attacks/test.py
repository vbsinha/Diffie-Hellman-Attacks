import unittest

from brute_force import brute
from bsgs import bsgs
from pohlig_hellman import pohlig_hellman
from pollard_rho import pollard_rho

class TestBrute(unittest.TestCase):
    def test_brute(self):
        # Powers of 2 mod 11
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        for i in two_powers:
            self.assertEqual(pow(2, brute(2, i, 11), 11), i)
        
        # Powers of 3 mod 11
        three_powers = [1, 3, 9, 5, 4]
        for i in three_powers:
            self.assertEqual(pow(3, brute(3, i, 11), 11), i)


class TestBSGS(unittest.TestCase):
    def test_bsgs(self):
        # Powers of 2 mod 11
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        for i in two_powers:
            self.assertEqual(pow(2, bsgs(2, i, 11, verify=True), 11), i)
        
        # Powers of 3 mod 11
        three_powers = [1, 3, 9, 5, 4]
        for i in three_powers:
            self.assertEqual(pow(3, bsgs(3, i, 11, verify=True), 11), i)

        # This test takes a long time to run
        # Example adopted from https://github.com/ashutosh1206/Crypton/
        p = 0xfffffed83c17 # 48 bit prime
        # self.assertEqual(pow(5, bsgs(5, 230152795807443, p), p), 230152795807443)


class TestPohligHellman(unittest.TestCase):
    def test_pohlig_hellman(self):
        # Powers of 2 mod 11
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        for i in two_powers:
            self.assertEqual(pow(2, pohlig_hellman(2, i, 11, [2, 5], [1, 1], True), 11), i)
        
        # Powers of 3 mod 11
        three_powers = [1, 3, 9, 5, 4]
        for i in three_powers:
            self.assertEqual(pow(3, pohlig_hellman(3, i, 11, [2, 5], [1, 1], True), 11), i)

        p = 0xfffffed83c17 # 48 bit prime
        self.assertEqual(pow(5, pohlig_hellman(5, 230152795807443, p, \
                [2, 3, 7, 13, 47, 103, 107, 151], [1, 2, 1, 4, 1, 1, 1, 1], True), p), 230152795807443)

        self.assertEqual(pow(3, pohlig_hellman(3, 188, 257, [2], [8]), 257), 188)
        self.assertEqual(pow(3, pohlig_hellman(3, 46777, 65537, [2], [16]), 65537), 46777)


class TestPollardRho(unittest.TestCase):
    def test_pollard_rho(self):
        # Powers of 2 mod 11
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        for i in two_powers:
            self.assertEqual(pow(2, pollard_rho(2, i, 11, 10, verify=True), 11), i)
        
        # Powers of 3 mod 11
        three_powers = [1, 3, 9, 5, 4]
        for i in three_powers:
            self.assertEqual(pow(3, pollard_rho(3, i, 11, 5, verify=True), 11), i)

        self.assertEqual(pow(2, pollard_rho(2, 5, 1019, 1018, verify=True), 1019), 5)
        self.assertEqual(pow(2, pollard_rho(2, 228, 383, 191, verify=True), 383), 228)


if __name__ == "__main__":
    unittest.main()