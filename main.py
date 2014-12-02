import sys
from HMM import HMM
from forward_probability import Forward_Matrix
from backward_probability import Backward_Matrix
from viterbi_matrix import Viterbi_Matrix
from posterior_probability import PosteriorProbability

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
#Run Viterbi
casino = Viterbi_Matrix(casino_markov)
casino.viterbi()
casino.print_table()
print "Viterbi Path:"
casino.calculate_viterbi_path()
print casino.viterbi_path
print "========================"
print "Forward Matrix:"
casino_forward = Forward_Matrix(casino_markov)
casino_forward.calculate_forward_probabilities()
print casino_forward.forward_matrix['F']
print casino_forward.forward_matrix['B']
print casino_forward.calculate_prob_y()
print "Backward Matrix:"
casino_backward = Backward_Matrix(casino_markov)
casino_backward.calculate_backward_probabilities()
print casino_backward.backward_matrix['F']
print casino_backward.backward_matrix['B']
print "Posterior Probability:"
casino_posterior = PosteriorProbability(casino_markov)
print casino_posterior.calculate_posterior_probability(7, 'B')




# states = ('R', 'D') #Raining and Dry
# observation = ["U", "U", "N", "U", "U"]
# start_probability = {
#     "R": .5,
#     "D": .5
# }
# transition_probability = {
#     "R": {"R": .7, "D": .3},
#     "D": {"R": .3, "D": .7}
# }
# emission_probability = {
#     "R": {"U": .9, "N": .1},
#     "D": {"U": .2, "N": .8}
# }
# rainy_markov = HMM(observation, states,start_probability,transition_probability,emission_probability)
# rainy = Viterbi_Matrix(rainy_markov)
# rainy.viterbi()
# rainy.print_table()
# rainy_forward = Forward_Matrix(rainy_markov)
# rainy_forward.calculate_forward_probabilities()
# rainy_backward = Backward_Matrix(rainy_markov)
# rainy_backward.calculate_backward_probabilities()