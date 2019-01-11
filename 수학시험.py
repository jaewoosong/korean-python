import unittest
import math
import 수학

class 수학시험(unittest.TestCase):

    def test_천장(self):
        print('천장 함수 시험')
        입력 = [3.7, 2, 0, -4, -5.9]
        for x in 입력:
            값1 = math.ceil(x)
            값2 = 수학.천장(x)
            self.assertEqual(값1, 값2)

if __name__ == '__main__':
    unittest.main()

