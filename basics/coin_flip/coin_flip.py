import random
import matplotlib.pyplot as plt

def coin_flip(min, max):
    ratios =[]
    x = range(min, max+1)
    for number_flips in x:
        numHeads = 0
        for n in range(number_flips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = number_flips - numHeads
        ratios.append(numHeads/float(numTails))
    
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of flips')
    plt.ylabel('Heads/Tails')
    plt.plot(x,ratios)
    plt.hlines(1,0,x[-1],linestyles='dashed',colors='y')
    plt.show()