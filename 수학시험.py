# -*- coding: UTF-8 -*-

import unittest
import math
import 수학

class 수학시험(unittest.TestCase):

    def test_바닥(self):
        입력 = [3.7, 2, 0, -4, -5.9]
        for x in 입력:
            값1 = math.floor(x)
            값2 = 수학.바닥(x)
            self.assertEqual(값1, 값2)

    def test_절댓값(self):
        입력 = [3.7, 2, 0, -4, -5.9]
        for x in 입력:
            값1 = math.fabs(x)
            값2 = 수학.절댓값(x)
            self.assertEqual(값1, 값2)

    def test_사인(self):
        입력 = [0, 1.2, 0.5*수학.파이, 4, 5.78, 2*수학.파이, 2*수학.파이, 1002]
        for x in 입력:
            값1 = math.sin(x)
            값2 = 수학.사인(x)
            self.assertAlmostEqual(값1, 값2, places=5)

    def test_천장(self):
        입력 = [3.7, 2, 0, -4, -5.9]
        for x in 입력:
            값1 = math.ceil(x)
            값2 = 수학.천장(x)
            self.assertEqual(값1, 값2)

    def test_최대공약수(self):
        입력 = [(36, 24), (78696, 19332), (0, 756), (-3, 0), (-12, -294)]
        for (ㄱ, ㄴ) in 입력:
            값1 = math.gcd(ㄱ, ㄴ)
            값2 = 수학.최대공약수(ㄱ, ㄴ)
            self.assertEqual(값1, 값2)

    def test_팩토리얼(self):
        입력1 = [10, 5, 1, 0]
        입력2 = [-2, 3.7 -5.9]
        for x in 입력1:
            값1 = math.factorial(x)
            값2 = 수학.팩토리얼(x)
            self.assertEqual(값1, 값2)
        for x in 입력2:
            self.assertRaises(ValueError, lambda x: 수학.팩토리얼(x), x)

if __name__ == '__main__':
    unittest.main()

