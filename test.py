__author__ = 'stephaniehippo'
import unittest
from HMM import HMM
from viterbi_matrix import Viterbi_Matrix
from posterior_probability import PosteriorProbability
from forward_probability import Forward_Matrix
from backward_probability import Backward_Matrix

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
        self.casino_forward = Forward_Matrix(casino_markov)


    def test_viterbi(self):
        self.casino.viterbi()
        solution_matrix = {'F': [0.25, 0.1125, 0.050625, 0.022781, 0.010252, 0.004613, 0.002076, 0.000934, 0.00042, 0.000189],
                'B': [0.375, 0.253125, 0.170859, 0.11533, 0.077848, 0.017516, 0.003941, 0.000887, 0.0002, 4.5e-05]}
        for coin in self.casino.hmm.states:
            for i in xrange(len(solution_matrix[coin])):
                assert round(self.casino.viterbi_matrix[coin][i][0], 6) == solution_matrix[coin][i]

    def test_viterbi_path(self):
        self.casino.viterbi()
        self.casino.calculate_viterbi_path()
        assert self.casino.viterbi_path == ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']

    def test_forward_matrix(self):
        self.casino_forward.calculate_forward_probabilities()
        solution_dict= {'F':[0.25, 0.13125, 0.07265625, 0.04236328125000001, 0.02586181640625001, 0.016385559082031258, 0.008474070739746098, 0.00408144184112549, 0.0019075661687850962, 0.0008794629798173909],
                        'B': [0.375, 0.27187500000000003, 0.19335937500000006, 0.13596679687500005, 0.09495483398437504, 0.022011383056640636, 0.005362200164794925, 0.0014183468055725106, 0.0004211640772819522, 0.00014245107160806665]}
        assert self.casino_forward.forward_matrix == solution_dict

    def test_prob_y(self):
        self.casino.viterbi()
        self.casino_forward.calculate_forward_probabilities()
        prob_y = 0
        for state in self.casino_forward.forward_matrix:
            prob_y += self.casino_forward.forward_matrix[state][-1]
        assert self.casino_forward.calculate_prob_y() == prob_y