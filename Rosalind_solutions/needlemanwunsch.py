#!/usr/bin/env python
import sys


def nwalign(x, y):

    seq1 = ''
    with open(x, 'r') as x:
        for i in x:
            if not i[0] == ">":
                seq1 += i.rstrip()
    seq2 = ''
    with open(y, 'r') as y:
        for i in y:
            if not i[0] == ">":
                seq2 += i.rstrip()
    match = +1
    gap = -1
    mismatch = -1
    D = []
    for i in range(len(seq1)+1):
        D.append([0]*(len(seq2)+1))

    for i in range(len(seq1)+1):
        D[i][0] = i*gap
    for j in range(len(seq2)+1):
        D[0][j] = j*gap

    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            H = D[i][j-1] + gap
            V = D[i-1][j] + gap
            if seq1[i-1] == seq2[j-1]:
                Di = D[i-1][j-1] + match
            else:
                Di = D[i-1][j-1] + mismatch
            D[i][j] = max(H, V, Di)

    a, b = len(seq1), len(seq2)
    s1 = ''
    s2 = ''

    while a > 0 and b > 0:
        up = D[a-1][b]
        diag = D[a-1][b-1]
        left = D[a][b-1]

        if D[a][b] == diag + match and seq1[a-1] == seq2[b-1]:
            s1 += (seq1[a-1])
            s2 += (seq2[b-1])
            a -= 1
            b -= 1

        elif D[a][b] == diag + mismatch and seq1[a-1] != seq2[b-1]:
            s1 += (seq1[a-1])
            s2 += (seq2[b-1])
            a -= 1
            b -= 1

        elif D[a][b] == up + gap:
            s2 += ("-")
            s1 += (seq1[a-1])

            a -= 1

            # print(s1)
            # print(s2)

            # print(s1)
            # print(s2)

        elif D[a][b] == left + gap:
            s1 += ("-")
            s2 += (seq2[b-1])

            b -= 1

        else:

            raise ValueError()

        # D[len(seq1)][len(seq2)-1]

    while a > 0:
        s1 += (seq1[a-1])
        s2 += ("-")
        a = a-1
    while b > 0:
        s1 += ("-")
        s2 += (seq2[b-1])
        b = b-1

    s1 = s1[::-1]
    s2 = s2[::-1]

    s3 = ''
    for i, j in zip(s1, s2):
        if i == j:
            s3 += "|"
        else:
            s3 += " "
    print("{}".format(s1))
    print(s3)
    print(s2)
    print("Alignment score: {}".format(D[len(seq1)][len(seq2)]))


nwalign(sys.argv[1], sys.argv[2])
