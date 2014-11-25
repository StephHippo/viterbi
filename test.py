__author__ = 'stephaniehippo'
import unittest
from HMM import HMM
from viterbi_matrix import Viterbi_Matrix

class TestViterbi(unittest.TestCase):

    def setUp(self):
        coins = ('F','B')
        flips = ['H','H','H','H','H','T','T','T','T','T']

        coin_start_probability = {
            'F' : 0.5,
            'B' : 0.5
        }

        dealer_switch_probability = {
            'F' : {'F': 0.9, 'B': 0.1},
            'B': {'F' : 0.1, 'B': 0.9}
        }

        flip_probability = {
            'F' : {'H':0.5, 'T':0.5},
            'B' : {'H':0.75, 'T':0.25}
        }
        casino_markov = HMM(flips,coins,coin_start_probability,dealer_switch_probability,flip_probability)
        self.casino = Viterbi_Matrix(casino_markov)

    def test_viterbi(self):
        self.casino.viterbi()
        solution_matrix = [[0.25, 0.1125, 0.050625, 0.022781, 0.010252, 0.004613, 0.002076, 0.000934, 0.00042, 0.000189],
                [0.375, 0.253125, 0.170859, 0.11533, 0.077848, 0.017516, 0.003941, 0.000887, 0.0002, 4.5e-05]]
        assert self.casino.viterbi_matrix() == solution_matrix

    def test_viterbi_path(self):
        assert self.casino.viterbi_path == ['B','B','B','B','B','B','B','B','B','B']

