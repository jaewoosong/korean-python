# -*- coding: UTF-8 -*-

import unittest
import statistics
import 통계

class 수학시험(unittest.TestCase):

    def test_평균(self):
        자료1 = [10, 5, 1, 0]
        자료2 = [1.7, 2.3, -5, 132, 0.2]
        자료3 = []
        print(통계.평균(자료1))
        print(통계.평균(자료2))
        self.assertEqual(통계.평균(자료1), statistics.mean(자료1))
        self.assertEqual(통계.평균(자료2), statistics.mean(자료2))
        self.assertRaises(statistics.StatisticsError, lambda x: 통계.평균(x), 자료3)

if __name__ == '__main__':
    unittest.main()

