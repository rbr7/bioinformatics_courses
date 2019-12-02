
import sys

Genome = sys.argv[1]

def Skew(Genome):
    
    skew = [0]

    for i in range(0, len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

def minimum_skew(Genome):
    skew = Skew(Genome)
    minimum = min(skew)
    return [i for i, val in enumerate(skew) if val == minimum]

