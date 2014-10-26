from HMM import HMM

class Viterbi_Matrix:
    def __init__(self,hidden_markov_model):
        self.hmm = hidden_markov_model
        self.matrix = {}

    def viterbi(self):
        #initialize start probabilities in first column
        self.__initialize_matrix()
        for i in xrange(len(self.hmm.observations)-1):
            for transition in self.hmm.transition_prob:
                max = 0
                for state in self.hmm.states:
                    # for emission in self.hmm.emission_prob[state]:
                    prev_prob = self.matrix[state][i]
                    trans_prob = self.hmm.transition_prob[state][transition]
                    observe = self.hmm.observations[i+1]
                    emis_prob = self.hmm.emission_prob[transition][observe]
                    candidate = prev_prob * trans_prob * emis_prob
                    if candidate > max:
                        max = candidate
                self.matrix[transition][i+1] = max

    def __initialize_matrix(self):
        for state in self.hmm.start_prob:
            self.matrix[state] = [None] * (len(self.hmm.observations))
            self.matrix[state][0] = self.hmm.start_prob[state] * self.hmm.emission_prob[state][self.hmm.observations[0]]

    def __validate_matrix_filled(self):
        for key in self.matrix:
            for value in self.matrix[key]:
                if value == None:
                    raise "Matrix needs filled out. Run Viterbi first"

    def print_table(self):
        self.__validate_matrix_filled()
        table = ""
        header = "\t\t"
        for observation in self.hmm.observations:
            header += "\t|"
            header += observation
            header += "\t"
        table+=header+"\n"
        body = ""
        for state in self.hmm.states:
            body += "\t|"
            body += state
            body += "\t"
            for observation in xrange(len(self.hmm.observations)):
                body += "\t|"
                body += str(round(self.matrix[state][observation],4))
            body += "\n"
        table += body
        print table


    def probability_at_ith_observation(self, i, state):
        self.__validate_matrix_filled()
        return self.matrix[state][i-1]