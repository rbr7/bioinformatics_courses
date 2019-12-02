
def mendelflaw(k,m,n):
    population = k+m+n

    dom = (k/population)
    hetdom = (m/population) * ((k)/(population - 1))
    hethet = (m/population) * ((m-1)/(population - 1)) * 0.75 #75% because breeding between het and het will 75% give dkminant phenotype
    hetrec = (m/population) * (n/(population - 1)) * 0.5 #50% because breeding between het and rec will 50 % give dominant phenotype
    het = hetdom+hethet+hetrec
    recdom = (n/population) * (k/(population - 1))
    rechet = (n/population) * ((m)/(population - 1)) * 0.5
    rec = recdom + rechet
    #no need to bother with rec rec as they will contribute 0% to dominant phentoype

    tot = dom + het + rec

    return print(tot)
mendelflaw(20,19,26)
