#!/usr/bin/env python
"""causal entropic forces using the weak law of large numbers"""
import math, sys, os
import matplotlib.pyplot as plt
import numpy as np

from monteCarloGaussianPaths import *

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'particleBox'))
from particleBox import *


# state variables
samples, steps = 400, 10

depth = tau / timeStep
variance = (kb * Tr * timeStep**2.0) / (4.0 * mass)

def force(pos):
    'calculate where the next step should be with mean of all samples'
    stdev = math.sqrt(variance / depth)
    config = configuration(dims, stdev, valid)
    ps = monteCarloGaussianPaths(pos, samples, config, depth)
    return [sum([float(p[i]) for p in ps]) / len(ps) for i in range(dims)]


def forcing(pos, steps):
    'return path taken by forcing of particle'
    path = []
    for j in range(steps):
        pos = force(np.array(pos))
        path.append(pos)
        print "moved", j, "steps, now at", pos
    return path



print "starting position", start
path = [start] + forcing(start, steps)
path = [[p[i] for p in path] for i in range(dims)]

plt.figure()
ax = plt.gca(aspect = 'equal')
ax.set_title("Particle in a 2 dimensional box")
ax.set_xlim(bounds[0][0], bounds[0][1])
ax.set_ylim(bounds[1][0], bounds[1][1])
ax.plot(path[0], path[1], linewidth=0.25, color='k')
plt.show()
