import sys
from HMM import HMM

states = ('F','B')
observation = 'HHHHHTTTTT'

start_probability = {
    'F' : 0.5,
    'B' : 0.5
}

transition_probability = {
    'F' : {'F': 0.9, 'B': 0.1},
    'B': {'F' : 0.1, 'B': 0.9}
}

emission_probability = {
    'F' : {'H':0.5, 'T':0.5},
    'B' : {'H':0.75, 'T':0.75}
}

#Declare New HMM
markov = HMM(observation, states,start_probability,transition_probability,emission_probability)
#Run Viterbi
markov.viterbi()