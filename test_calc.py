'''
@Author: your name
@Date: 2020-06-19 20:56:34
@LastEditTime: 2020-06-19 20:58:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \demo_calc\test_calc.py
'''
import unittest
from calc import neuron


class Tests(unittest.TestCase):
    def test_neuron(self):
        self.assertEqual(neuron(1, 2, 3), 5)
        self.assertEqual(neuron(1, -2, 1), 0)
        self.assertEqual(neuron(3, -1, 1), 0)


if __name__ == '__main__':
    unittest.main()
