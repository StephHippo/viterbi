from HMM import HMM
from operator import itemgetter

class Viterbi_Matrix:
    def __init__(self,hidden_markov_model):
        self.hmm = hidden_markov_model
        self.viterbi_matrix = {}
        self.viterbi_path = [None] * len(self.hmm.observations)

    def viterbi(self):
        #initialize start probabilities in first column
        self.__initialize_matrix()
        for i in xrange(len(self.hmm.observations)-1):
            top_state = None
            highest_prob = 0
            for transition in self.hmm.transition_prob:
                max = 0
                candidate_state = None
                for state in self.hmm.states:
                    prev_prob = self.viterbi_matrix[state][i][0]
                    trans_prob = self.hmm.transition_prob[state][transition]
                    observe = self.hmm.observations[i+1]
                    emis_prob = self.hmm.emission_prob[transition][observe]
                    candidate = prev_prob * trans_prob * emis_prob
                    #The max candidate should be stored for back-tracing.
                    if candidate > max:
                        max = candidate
                        candidate_state = state
                self.viterbi_matrix[transition][i+1] = (max, candidate_state)

    def __initialize_matrix(self):
        start = None
        for state in self.hmm.start_prob:
            self.viterbi_matrix[state] = [None] * (len(self.hmm.observations))
            self.viterbi_matrix[state][0] = (self.hmm.start_prob[state] * self.hmm.emission_prob[state][self.hmm.observations[0]], "S")
            if self.viterbi_matrix[state][0] > start:
                start = state
        self.viterbi_path[0]=start

    def __validate_matrix_filled(self):
        for key in self.viterbi_matrix:
            for value in self.viterbi_matrix[key]:
                if value == None:
                    raise "Matrix needs filled out. Run Viterbi first"

    def print_table(self):
        self.__validate_matrix_filled()
        table = ""
        header = "\t"
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
                body += "|"
                body += str(round(self.viterbi_matrix[state][observation][0],6))
            body += "\n"
        table += body
        print table

    def calculate_viterbi_path(self):
        prev_state=None
        prob=0
        #initial prev_state
        for state in self.hmm.states:
            if self.viterbi_matrix[state][-1][0] > prob:
                prob = self.viterbi_matrix[state][-1][0]
                prev_state = self.viterbi_matrix[state][-1][1]
        #find a state for every observation
        for i in xrange(len(self.hmm.observations)):
            #For each location, grab the previous state
            self.viterbi_path[-(i+1)] = prev_state
            prev_state = self.viterbi_matrix[prev_state][-(i+1)][1]
