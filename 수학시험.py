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

    def test_천장(self):
        입력 = [3.7, 2, 0, -4, -5.9]
        for x in 입력:
            값1 = math.ceil(x)
            값2 = 수학.천장(x)
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

