from __future__ import division

import random
import time
import timeit

import numpy as np
def np_bdays(persons=23, samples=1000):

    count = 0
    for i in range(samples):
        x = np.random.randint(0,365, persons)
        if len(np.unique(x)) < len(x):
            count += 1
    prob = count / samples
    return prob

def no_np_bdays(persons=23, samples=1000):

    count = 0
    for i in range(samples):
        bdays = [random.randint(0, 365) for i in range(persons)]
        if len(set(bdays)) < len(bdays):
            count += 1
    prob = count / samples
    return prob

print timeit.timeit('no_np_bdays(23, 50000)', 'from __main__ import no_np_bdays', number=10)
print timeit.timeit('np_bdays(23, 50000)', 'from __main__ import np_bdays', number=10)


probs = []
for i in range(2,51):
    probs.append(np_bdays(i, 2000))

print probs

# Let's go ahead and plot this

import matplotlib.pyplot as plt

plt.plot(probs)
plt.ylabel('Probabilities')
plt.show()
