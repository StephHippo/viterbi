__author__ = 'stephaniehippo'
from HMM import HMM

class Forward_Matrix:
    def __init__(self, hidden_markov_model):
        self.hmm = hidden_markov_model
        #one for every observation
        self.forward_matrix = {}

    def initialize_forward_matrix(self):
        for state in self.hmm.start_prob:
            self.forward_matrix[state] = [0] * (len(self.hmm.observations))
            self.forward_matrix[state][0] = self.hmm.start_prob[state]*self.hmm.emission_prob[state][self.hmm.observations[0]]

    def calculate_forward_probabilities(self):
        self.initialize_forward_matrix()
        #for every observation
        for i in xrange(len(self.hmm.observations)-1):
            #calculate for each state
            for state in self.hmm.states:
                for transition in self.hmm.transition_prob:
                    observation = self.hmm.observations[i+1]
                    emission_prob = self.hmm.emission_prob[state][observation]
                    trans_prob = self.hmm.transition_prob[state][transition]
                    prev_prob = self.forward_matrix[transition][i]
                    self.forward_matrix[transition][i+1] += emission_prob * trans_prob * prev_prob
        print self.forward_matrix