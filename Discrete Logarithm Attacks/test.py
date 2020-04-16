import unittest

from brute_force import brute
from bsgs import bsgs
from pohlig_hellman import pohlig_hellman
from pollard_rho import pollard_rho

class TestBrute(unittest.TestCase):
    def test_brute(self):
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        self.assertIn(brute(2, 1, 11), [0, 10])
        for i in range(1, 10):
            self.assertEqual(brute(2, two_powers[i], 11), i)
        
        three_powers = [1, 3, 9, 5, 4]
        self.assertIn(brute(3, 1, 11), [0, 10])
        for i in range(1, 5):
            self.assertEqual(brute(3, three_powers[i], 11), i)


class TestBSGS(unittest.TestCase):
    def test_bsgs(self):
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        self.assertIn(brute(2, 1, 11), [0, 10])
        for i in range(1, 10):
            self.assertEqual(bsgs(2, two_powers[i], 11), i)
        
        three_powers = [1, 3, 9, 5, 4]
        self.assertIn(bsgs(3, 1, 11), [0, 10])
        for i in range(1, 5):
            self.assertEqual(bsgs(3, three_powers[i], 11), i)

        p = 0xfffffed83c17 # 48 bit prime
        self.assertEqual(bsgs(5, 230152795807443, p), 123138732879379)


class TestPohligHellman(unittest.TestCase):
    def test_pohlig_hellman(self):
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        self.assertIn(pohlig_hellman(2, 1, 11, [2, 5], [1, 1]), [0, 10])
        for i in range(1, 10):
            self.assertEqual(pohlig_hellman(2, two_powers[i], 11, [2, 5], [1, 1], True), i)
        
        three_powers = [1, 3, 9, 5, 4]
        self.assertIn(pohlig_hellman(3, 1, 11, [2, 5], [1, 1]), [0, 10])
        for i in range(1, 5):
            self.assertEqual(pohlig_hellman(3, three_powers[i], 11, [2, 5], [1, 1], True) % 5, i)

        p = 0xfffffed83c17 # 48 bit prime
        self.assertEqual(pohlig_hellman(5, 230152795807443, p, \
                [2, 3, 7, 13, 47, 103, 107, 151], [1, 2, 1, 4, 1, 1, 1, 1], True), 123138732879379)

        self.assertEqual(pow(3, pohlig_hellman(3, 188, 257, [2], [8]), 257), 188)
        self.assertEqual(pow(3, pohlig_hellman(3, 46777, 65537, [2], [16]), 65537), 46777)


class TestPollardRho(unittest.TestCase):
    def test_pollard_rho(self):
        two_powers = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
        self.assertIn(pollard_rho(2, 1, 11, 10), [0, 10])
        for i in range(1, 10):
            self.assertEqual(pollard_rho(2, two_powers[i], 11, 10, verify=True), i)
        
        three_powers = [1, 3, 9, 5, 4]
        self.assertIn(pollard_rho(3, 1, 11, 5), [0, 10])
        for i in range(1, 5):
            self.assertEqual(pollard_rho(3, three_powers[i], 11, 5, verify=True) % 5, i)

        self.assertEqual(pollard_rho(2, 5, 1019, 1018, verify=True), 10)
        self.assertEqual(pollard_rho(2, 228, 383, 191, verify=True), 110)


if __name__ == "__main__":
    unittest.main()