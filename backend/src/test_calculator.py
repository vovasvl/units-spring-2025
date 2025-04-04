import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(-1, -1), -2)
        self.assertEqual(self.calculator.addition(1 + 2j, 3 + 4j), (4 + 6j))
        self.assertEqual(self.calculator.addition(1 + 2j, -1 - 2j), 0)
        self.assertRaises(TypeError, self.calculator.addition, "1", 2)
        self.assertRaises(TypeError, self.calculator.addition, 1, "2")

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)
        self.assertEqual(self.calculator.multiplication(2, 0), 0)
        self.assertEqual(self.calculator.multiplication(1 + 2j, 3 + 4j), (-5 + 10j))
        self.assertEqual(self.calculator.multiplication(1 + 2j, 0), 0)
        self.assertRaises(TypeError, self.calculator.multiplication, "1", "2")

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(2, 3), -1)
        self.assertEqual(self.calculator.subtraction(1 + 2j, 3 + 4j), (-2 - 2j))
        self.assertEqual(self.calculator.subtraction(1 + 2j, 1 + 2j), 0)
        self.assertRaises(TypeError, self.calculator.subtraction, "1", 2)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, "2")

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(-6, 3), -2)
        self.assertEqual(self.calculator.division(6, -3), -2)
        self.assertEqual(self.calculator.division(-6, -3), 2)
        self.assertEqual(self.calculator.division(1 + 2j, 1 + 2j), (1 + 0j))
        self.assertEqual(self.calculator.division(1 + 2j, 1), (1 + 2j))
        self.assertIsNone(self.calculator.division(6, 0))
        self.assertRaises(TypeError, self.calculator.division, "1", 2)
        self.assertRaises(TypeError, self.calculator.division, 1, "2")

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(3), 3)
        self.assertEqual(self.calculator.absolute(-3), 3)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(3 + 4j), 5)
        self.assertEqual(self.calculator.absolute(-3 - 4j), 5)
        self.assertRaises(TypeError, self.calculator.absolute, "1")

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(2, -3), 0.125)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(0, 2), 0)
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(1 + 2j, 2), (-3 + 4j))
        self.assertEqual(self.calculator.degree(1 + 2j, 0), 1)
        self.assertEqual(self.calculator.degree(2, 1 + 2j), 0.36691394948660344 + 1.9660554808224875j)
        self.assertRaises(ZeroDivisionError, self.calculator.degree, 0, -1)
        self.assertRaises(TypeError, self.calculator.degree, "1", 2)
        self.assertRaises(TypeError, self.calculator.degree, 1, "2")

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(10), 2.30258509299404)
        self.assertAlmostEqual(self.calculator.ln(2.718281828459045), 1)
        self.assertAlmostEqual(self.calculator.ln(7.38905609893065), 2)
        self.assertAlmostEqual(self.calculator.ln(0.36787944117144), -1)
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(TypeError, self.calculator.ln, 1 + 1j)
        self.assertRaises(TypeError, self.calculator.ln, "1")

    def test_log(self):
        self.assertEqual(self.calculator.log(1, 10), 0)
        self.assertEqual(self.calculator.log(10, 10), 1)
        self.assertEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(0.01, 100), -1)
        self.assertAlmostEqual(self.calculator.log(7, 10), 0.84509804001425)
        self.assertAlmostEqual(self.calculator.log(7.38905609893065, 2.718281828459045), 2)
        self.assertRaises(ValueError, self.calculator.log, 1, -1)
        self.assertRaises(ValueError, self.calculator.log, -1, 1)
        self.assertRaises(ValueError, self.calculator.log, -1, 0)
        self.assertRaises(ValueError, self.calculator.log, -1, -1)
        self.assertRaises(ValueError, self.calculator.log, 0, 1)
        self.assertRaises(ValueError, self.calculator.log, 0, 0)
        self.assertRaises(ValueError, self.calculator.log, 0, -1)
        self.assertRaises(TypeError, self.calculator.log, 1 + 1j, 10)
        self.assertRaises(TypeError, self.calculator.log, "1", 2)
        self.assertRaises(TypeError, self.calculator.log, 1, "2")


    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(2), 1.41421356237309)
        self.assertAlmostEqual(self.calculator.sqrt(9.8596), 3.14)
        self.assertAlmostEqual(self.calculator.sqrt(-1), (6.123233995736766e-17+1j))
        self.assertAlmostEqual(self.calculator.sqrt(1 + 1j), 1.09868411346781 + 0.45508986056223j)
        self.assertAlmostEqual(self.calculator.sqrt(-1 - 1j), 0.45508986056223 - 1.09868411346781j)
        self.assertRaises(TypeError, self.calculator.sqrt, "1")

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertEqual(self.calculator.nth_root(0, 1), 0)
        self.assertAlmostEqual(self.calculator.nth_root(4, 0.5), 16)
        self.assertAlmostEqual(self.calculator.nth_root(0.5, 2), 0.70710678118654)
        self.assertAlmostEqual(self.calculator.nth_root(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(-1, 2), (6.123233995736766e-17+1j))
        self.assertAlmostEqual(self.calculator.nth_root(-1, -2), (6.123233995736766e-17-1j))
        self.assertAlmostEqual(self.calculator.nth_root(1 + 1j, 2), 1.09868411346781 + 0.45508986056223j)
        self.assertAlmostEqual(self.calculator.nth_root(-1 - 1j, 2), 0.45508986056223 - 1.09868411346781j)
        self.assertAlmostEqual(self.calculator.nth_root(2, -1 - 1j), 0.6650637002129894 + 0.24018799857404816j)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)
        self.assertRaises(TypeError, self.calculator.nth_root, "1", 2)
        self.assertRaises(TypeError, self.calculator.nth_root, 1, "2")
        


if __name__ == "__main__":
    unittest.main()
