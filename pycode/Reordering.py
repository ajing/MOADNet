'''
    Reordering the ligand similarity matrix with ligand_standalizesmile.txt_new
'''

ORDERING_FILE = "../Data/ligand_standalizesmile.txt_new"
UNORDERDMATRIX_FILE = "../Data/similarityMatrix_moadligand_unorder.npy"
ORDERDMATRIX_FILE = "../Data/similarityMatrix_moadligand_order.npy"

import numpy as np
np.set_printoptions(threshold=np.nan)

def GetOrdering(orderfile):
    firstcol = []
    for line in open(orderfile):
        content = line.strip().split()
        firstcol.append(int(content[0]))
    firstcol_sorted = sorted(firstcol)
    #ordering = [firstcol_sorted.index(each) for each in firstcol]
    ordering = sorted(range(len(firstcol)), key=lambda k: firstcol[k])
    return ordering

def ReorderMatrix(dm_file, ordering):
    oldmatrix = np.load(dm_file)
    newmatrix = oldmatrix[:, ordering][ordering]
    np.save(ORDERDMATRIX_FILE, newmatrix)

if __name__ == "__main__":
    ordering = GetOrdering(ORDERING_FILE)
    ReorderMatrix(UNORDERDMATRIX_FILE, ordering)
