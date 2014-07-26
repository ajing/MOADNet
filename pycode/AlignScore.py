'''
   Reimplement sequence identity score, so I know every detail of what happen
   @Author:ajing
   @Date:7/24/2014
'''
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

import numpy as np

def alignScore(seq1, seq2):
    # blastp default option
    gap_open = -11
    gap_extend = -1
    alns = pairwise2.align.globalds(seq1, seq2, matlist.blosum62, gap_open, gap_extend)
    seq1_aln, seq2_aln, score, begin, end = alns[0]
    dismatch_num = seq1_aln.count("-") + seq2_aln.count("-")
    return (len(seq1_aln) - dismatch_num) * 1.0 / max( len(seq1), len(seq2) )

def alignScoreMatrix(seq_list):
    list_len = len(seq_list)
    simmatrix = np.zeros((list_len, list_len))
    for i in range(list_len - 1):
        for j in range(i, list_len):
            align_score = alignScore(seq_list[i], seq_list[j])
            simmatrix[i,j] = align_score
            simmatrix[j,i] = align_score
    return simmatrix

def getSequence(infile):
    pass


if __name__ == "__main__":
    print alignScore("ACG", "CG")
