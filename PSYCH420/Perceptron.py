import numpy as np

tstpass = False
startwt = np.array([-0.6, -0.8])

Learning =[
    [np.array([0.15, 0.15]), 1],
    [np.array([0.25, 0.25]), 1],
    [np.array([0.35, 0.35]), 1],
    [np.array([0.45, 0.45]), 1],
    [np.array([0.55, 0.55]), 1],
    [np.array([-0.65, -0.65]), -1],
    [np.array([-0.75, -0.75]), -1],
    [np.array([-0.85, -0.85]), -1],
    [np.array([-0.95, -0.95]), -1],
    [np.array([-1.05, -1.05]), -1]

]

Testset = [
    [np.array([0.1, 0.1]), 1],
    [np.array([0.2, 0.2]), 1],
    [np.array([0.3, 0.3]), 1],
    [np.array([0.4, 0.4]), 1],
    [np.array([0.5, 0.5]), 1],
    [np.array([-0.6, -0.6]), -1],
    [np.array([-0.7, -0.7]), -1],
    [np.array([-0.8, -0.8]), -1],
    [np.array([-0.9, -0.9]), -1],
    [np.array([-1.0, -1.0]), -1]
]

def updWeight(i, wt, T=0, eta=0.5):
    clss = i[1]
    inpt = i[0]
    y = 1 if (inpt @ wt) >= T else -1
    error = clss - y
    wt = wt+eta*error*inpt
    print("input:", inpt, "target:", clss, "prediction:", y, "error:", error)
    print("updated weight:", wt)
    return(wt + eta*error*inpt)

def tstArray(set, wt):
    global tstpass
    tstcount = 0
    for i in set:
        if np.sign(i[0] @ wt) == i[1]:
            tstcount +=1
        print(np.sign(i[0] @ wt) == i[1])
    if tstcount >= len(set):
        print("Test passed")
        tstpass = True
    elif tstcount < len(set):
        print("Test failed")



def mainfunction(set, wt):
    runcount = 0
    while tstpass != True and runcount <100:
        for i in set:
            wt = updWeight(i, wt)
        tstArray(set, wt)
        runcount += 1


mainfunction(Learning, startwt)

tstArray(Learning, startwt)







