#!/usr/bin/env python3
#Smith-Waterman (SW) algorithm
#standard imports
import sys

def get_alignment_seqs()-> list:
    """ method to read sequences for alignment and return processed reads
    :return: list of sequence 1 nucleotides, list of sequence 2 nucleotides
    """
    seq_1file = sys.argv[1]
    seq_2file = sys.argv[2]
    sequences = list()
    for seq in [seq_1file, seq_2file]:
        with open(seq, 'r') as fh:
            seq_fa = fh.readlines()
        if seq_fa[0].startswith('>'):
            seq_fa = [x.rstrip() for x in seq_fa[1:]]
        elif seq_fa[0][0].upper() in ['A','T','G','C']:
            seq_fa = [x.rstrip() for x in seq_fa]
        sequences.append(seq_fa)
    return list(''.join(sequences[0])), list(''.join(sequences[1]))

def generate_base_matrix(seq_1: list, seq_2: list)-> list:
    """ method to generate empty matrix initialised with zeros
    :param seq_1: processed read sequence 1 from first fasta file
    :param seq_2: processed read sequence 2 from second fasta file
    :return: base matrix initialised with zeros, updated seq 1, seq 2
    """
    seq_1 = ['D',''] + seq_1
    seq_2 = ['D',''] + seq_2
    base = [[0 for i in range(len(seq_2))] for j in range(len(seq_1))]
    base[0] = seq_2
    for i in range(len(base)):
        base[i][0] = seq_1[i]
    return base, seq_1, seq_2

def generate_scoring_matrix(base_matrx: list, row: int, col: int, seq_1: list, seq_2: list):
    """ method to fill base matrix and create scoring matrix for alignment
    :param base_matrx: matrix initialised with zeros
    :param row: row identifier to start scoring with
    :param col: column identifier to start scoring with
    :param seq_1: processed read seq 1
    :param seq_2: processed read seq 2
    :return: scoring matrix with alignment scores filled
    """
    score = {'match': 3, 'mismatch': -3, 'gap': -2}
    if col >= len(seq_2):
        return generate_scoring_matrix(base_matrx, row + 1, 1, seq_1, seq_2)

    if row >= len(seq_1):
        return base_matrx

    if 1 in [row, col]:
        base_matrx[row][col] = [0 if row == col else max(base_matrx[row][col - 1]+score['gap'],0) if row == 1 else max(base_matrx[row - 1][col]+score['gap'],0)][0]
    else:
        base_matrx[row][col] = [max(base_matrx[row][col - 1]+score['gap'],base_matrx[row - 1][col - 1]+score['match'],base_matrx[row - 1][col]+score['gap'],0) if seq_1[row] == seq_2[col] else max(base_matrx[row][col - 1]+score['gap'],base_matrx[row - 1][col - 1]+score['mismatch'],base_matrx[row - 1][col]+score['gap'],0)][0]
    return generate_scoring_matrix(base_matrx, row, col+1, seq_1, seq_2)

def max_value_cell(matrx: list, seq_1: list, seq_2: list):
    """ method to find cell with maximum score
    :param matrx: scoring matrix with alignments
    :param seq_1: processed read sequence 1
    :param seq_2: processed read sequence 2
    :return: x coordinate, y coordinate of cell with max value
    """
    max_val = 0
    for i in range(1, len(seq_1)):
        for j in range(1, len(seq_2)):
            if matrx[i][j] > max_val:
                max_val = matrx[i][j]
                id_x, id_y = i, j
    return id_x, id_y

def compute_backtracking(matrx: list, row: int, col: int, result: dict, seq_1: list, seq_2: list):
    """ method to find the optimal global alignment sequence and score
    :param matrx: scoring matirx with alignments completed
    :param row: row identifier to start global alignment match from
    :param col: column identifier for same
    :param result: dictionary to capture alignments and scores
    :return: result dictionary with alignments and scores
    """
    if matrx[row][col] == 0:
        return result
    mark = {0: '*', 1: '-', 2: '-'}
    if seq_1[row] == seq_2[col]:
        result['alignment'] = result['alignment'] + [(seq_1[row], '|', seq_2[col])]
    else:
        cells = [(row - 1, col - 1), (row - 1, col), (row, col - 1)]
        num = [matrx[i[0]][i[1]] for i in cells]
        val = max(num)
        idx = num.index(val)
        result['alignment'] = result['alignment'] + [([seq_1[row] if idx in [0, 1] else mark[idx]][0],mark[idx],[seq_2[col] if idx in [0, 2] else mark[idx]][0])]
        row, col = cells[idx]
        return compute_backtracking(matrx, row, col, result, seq_1, seq_2)

    return compute_backtracking(matrx, row-1, col-1, result, seq_1, seq_2)

def display_results(results: dict):
    """ method to print results of alignment to stdout
    :param results: dictionary with mapped results and scores
    :return: None
    """
    res = results['alignment'][::-1]
    print(''.join([x[0] for x in res]))
    symbol = [x[1].replace('-',' ') if '-' in x[1] else x[1] for x in res]
    print(''.join(symbol))
    print(''.join([x[2] for x in res]))
    print("Alignment score: ",sum([3 if x == '|' else -2 if x == ' ' else -3 for x in symbol]))
    return

if __name__ == '__main__':
    #a common construct to organise your project you will find in multiple python programs to call each function one by one
    x, y = get_alignment_seqs()
    matrx, x, y = generate_base_matrix(seq_1=x, seq_2=y)
    score_matrx = generate_scoring_matrix(base_matrx=matrx, row=1, col=1, seq_1=x, seq_2=y)
    idx, idy = max_value_cell(matrx=score_matrx, seq_1=x, seq_2=y)
    result = compute_backtracking(matrx=score_matrx, row=idx, col=idy, result={'alignment': []}, seq_1=x, seq_2=y)
    display_results(results=result)
    sys.exit()