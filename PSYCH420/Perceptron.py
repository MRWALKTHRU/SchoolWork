import numpy as np

startwt = np.array([-0.6, 0.5])

# I can't find out how to make something that makes random coordinates + classes without manual input
# I have tried with a bunch of different things, but as long as they were separated by the line it worked
Learning = [
    [np.array([10, 3]), 1],
    [np.array([5, 3]), 1],
    [np.array([12, 5]), 1],
    [np.array([4, 0.45]), 1],
    [np.array([7, 0.55]), 1],
    [np.array([-0.65, -0.65]), -1],
    [np.array([-0.75, -0.75]), -1],
    [np.array([-0.85, -0.85]), -1],
    [np.array([-0.95, -0.95]), -1],
    [np.array([-1.05, -1.05]), -1]

]

Testset = [
    [np.array([0, 8]), 1],
    [np.array([6, 1]), 1],
    [np.array([7, 7]), 1],
    [np.array([0.4404594, 0.454305349]), 1],
    [np.array([0.50543543, 0.550345345]), 1],
    [np.array([-0.65345435, -0.64135]), -1],
    [np.array([-0.765342, -0.74135]), -1],
    [np.array([-0.845143, -0.854315]), -1],
    [np.array([-0.9531446, -0.954315]), -1],
    [np.array([-1.055431, -1.0541353]), -1]
]



def updWeight(i, wt, T=0, eta=0.5):
    ''' Takes a list of arrays containing coordinates and a class and a starting weight,
    updates the weight using the delta rule. Returns a new weight.
    Optionally can set a different threshold and eta value
    '''
    clss = i[1]  # Class = the second item
    inpt = i[0]  # input = the first item
    y = 1 if (inpt @ wt) >= T else -1 # y = 1 if dot product of coordinates and weight is above threshold
    error = clss - y
    wt = wt+eta*error*inpt # update weight
    print("input:", inpt, "target:", clss, "prediction:", y, "error:", error, "\n","-" *40)
    print("updated weight:", wt)
    return(wt)

def tstArray(set, wt):
    ''' Takes  a list of arrays containing coordinates and a class and a weight.
    Tests whether or not the weight is able to properly classify the coordinates into their proper class.
    Returns value and prints results.
    '''
    count = 0
    for i in set:
        if np.sign(i[0] @ wt) == i[1]: # check if the dot product of input and weight is of the same sign as the class
            count +=1
        print("Result of case", count, "perceptron accuracy is:", np.sign(i[0] @ wt) == i[1]
              , "\n","-" *40)
    if count >= len(set):  # if the count of good classifications is the same as the amount in the set, we passed
        print("Test passed")
        Pass = True
    elif count < len(set):
        print("Test failed")
    return Pass

def calTest(set, wt):  # same as test but doesn't print everything
    count = 0
    for i in set:
        if np.sign(i[0] @ wt) == i[1]:
            count +=1
    if count >= len(set):
        Pass = True
    elif count < len(set):
        Pass = False
    return Pass


def Calibration(set, wt, tries=100):
    ''' Takes a list of arrays containing coordinates and a class, a starting weight and a number of tries before quitting.
    Used to calibrate a new weight until it is able to classify the set properly.
    '''
    runcount = 1
    Pass = False
    while Pass == False and runcount < tries:  # keep going until we pass the test or run out of tries
        print("Calibration attempt #", runcount)
        for i in set:
            wt = updWeight(i, wt)
        Pass = calTest(set, wt)
        runcount += 1
    return wt  # update weight


final_weight = Calibration(Learning, startwt,)

tstArray(Testset, final_weight)











