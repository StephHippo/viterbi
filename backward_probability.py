__author__ = 'stephaniehippo'

class Backward_Matrix:
    def __init__(self, hidden_markov_model):
        self.hmm = hidden_markov_model
        self.backward_matrix = {}

    def initialize_backward_matrix(self):
        for state in self.hmm.states:
            self.backward_matrix[state] = [0] * (len(self.hmm.observations))
            self.backward_matrix[state][-1] = 1

    def calculate_backward_probabilities(self):
        self.initialize_backward_matrix()
        for i in xrange(len(self.hmm.observations)-1):
            for state in self.hmm.states:
                for transition in self.hmm.transition_prob:
                    observation = self.hmm.observations[-(i+1)]
                    emission_prob = self.hmm.emission_prob[state][observation]
                    trans_prob = self.hmm.transition_prob[state][transition]
                    prev_prob = self.backward_matrix[transition][-i]
                    self.backward_matrix[transition][-(i+1)] += emission_prob * trans_prob * prev_prob
