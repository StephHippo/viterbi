import numpy

class Viterbi_Matrix:
    def __init__(self,hidden_markov_model):
        self.hmm = hidden_markov_model
        self.matrix = numpy.zeros((len(self.hmm.emission_prob),len(self.hmm.observations)))

    def viterbi(self):
        #For Every Observations



