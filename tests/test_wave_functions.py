import unittest
from interference_package import I1, I2, psi, Is, c1, z, l

class TestWaveFunctions(unittest.TestCase):

    def test_I1_positive(self):
        result = I1(0, 30*l, c1)
        self.assertGreaterEqual(result, 0)

    def test_Is_positive(self):
        result = Is(0, 30*l, c1)
        self.assertGreaterEqual(result, 0)

    def test_psi_real(self):
        result = psi(0, 30*l, c1)
        self.assertIsInstance(result, complex)

if __name__ == '__main__':
    unittest.main()
