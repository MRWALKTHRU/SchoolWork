# make 2-d input that are square and size "n"
# store them
# compute the weight matrix with the given formula
# program an asynchronous updating rule that runs until it stabilises
# do the same with at least one corrupted pattern

"""
Name: Jules Gravestock
Assignment: Hopfield Network

Assignment Instructions:

Generate Random Size and Number of Patterns
Function to make random patterns
Function to Make Weight Matrix for a set of Generated Patterns
Function to Loop Asyncrhonously Through all the Elements of a Pattern Until Output is Stable
A Function to Visualize the Output
Make a corrupted input and test if it still works

Program Instructions:
-
"""

import numpy as np
import random as r
import matplotlib.pyplot as p


def rand_ns(n1=5, n2=10,s1=2,s2=5):
    """ returns a number between a range, as well as a size between another range in a list"""
    number = r.randint(n1,n2)
    size = r.randint(s1,s2)
    return [number, size]


def genPat(s, getPrint=False):
    """ Generates an array of size s*s """
    count = 0
    pattern = np.zeros(s*s)
    for i, value in enumerate(pattern):
        value = 1 if r.randint(1, 100) > 50 else -1
        pattern[i] = value
    pattern = pattern.reshape(s, s)
    print(pattern) if getPrint is True else None
    return pattern

def getPats(n, s, getPrint=False):
    """ generates n arrays of s*s size"""
    patterns_l = []
    while True:
        patterns_l.append(genPat(s))
        if len(patterns_l) == n: break
    print(patterns_l) if getPrint is True else None
    patterns_l = np.array(patterns_l)
    return patterns_l

def weights_calc(patterns, getPrint=False):
    """ calculates the matrix weight using the Hebbian formula"""
    patterns = [p.flatten() for p in patterns]
    wt = np.zeros((patterns[0].size, patterns[0].size))
    for p in patterns:
        wt = wt + np.outer(p,p)
    np.fill_diagonal(wt, 0)
    print(wt) if getPrint is True else None
    return wt

def asyncLoop(pattern, weight, max=500): # Despite trying, I could not find a functioning novel way to do this
    input = pattern
    while True:
        rows, cols = input.shape
        rows = list(range(rows))
        cols = list(range(cols))
        r.shuffle(rows) # makes it asycnhronous
        r.shuffle(cols)
        test = input
        for row in rows:
            for col in cols:
                input[row][col] = 1 if ((np.reshape(input, (1, input.size))
                                         @ weight[row]) * input[row][col]) > 0 else -1
        if np.array_equal(test, input): break
    return pattern


def hopPlot(ins,outs, title=""):
    r = len(ins)
    c = 3
    p.title(title)
    pltcntr = 1
    for i in range(r):
        p.subplot(r,3,pltcntr)
        p.imshow(ins[i])
        p.subplot(r,3,(pltcntr+1))
        p.imshow(outs[i])
        p.subplot(r,3,(pltcntr+2))
        p.imshow(ins[i]-outs[i])
        pltcntr = pltcntr+3
    return(p)

def corrupter(pattern, getPrint=False):
    """ flips 2 bits in every pattern array"""
    cPats = []
    if getPrint is True:
        print(f"The original pattern is : \n {pattern[0]}")
    shape = pattern[0].shape[0]
    for p in pattern:
        pat = p.flatten()
        c = r.randrange(0, p.size)
        pat[c] = 1 if pat[c] == -1 else -1
        pat[c // 2] = 1 if pat[c // 2] == -1 else -1
        pat = np.reshape(p, (shape, shape))
        cPats.append(pat)
    if getPrint is True:
        print(f"the corrupted pattern is: \n {pattern[0]}")
    return cPats


ns = rand_ns()
Pats = getPats(ns[0], ns[1])
Wt = weights_calc(Pats)
outputs = []
for i in Pats:
    out = asyncLoop(i,Wt)
    outputs.append(out)

Plot = hopPlot(Pats, outputs, "Original Plot")
Plot.show()

cPats = corrupter(Pats)
cOuts = []
for c in cPats:
    out = asyncLoop(c, Wt)
    cOuts.append(out)

cPlot = hopPlot(cPats,cOuts, "Corrupted Plot")
cPlot.show()
