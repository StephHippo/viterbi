import sys
from HMM import HMM
from viterbi_matrix import Viterbi_Matrix

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
print casino.viterbi_path

# states = ('H', 'F')
# observation = ["Normal", "Cold", "Dizzy"]
# start_probability = {
#     "H" : 0.6,
#     "F" : 0.4
# }
# transition_probability = {
#     "H" : {"H": 0.7, "F": 0.3},
#     "F" : {"H": 0.4, "F" : 0.6}
# }
# emission_probability = {
#     "H" : {"Dizzy": 0.1, "Cold": 0.4, "Normal": 0.5},
#     "F" : {"Dizzy": 0.6, "Cold": 0.3, "Normal": 0.1}
# }
#
# #Declare New HMM
# healthy_markov = HMM(observation, states,start_probability,transition_probability,emission_probability)
# #Run Viterbi
# healthy = Viterbi_Matrix(healthy_markov)
# healthy.viterbi()
# healthy.print_table()
# print healthy.probability_at_ith_observation(3,'F')
# print healthy.viterbi_path

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
# print rainy.viterbi_path
# rainy.backwards_probability()
# rainy.print_posterior_matrix()