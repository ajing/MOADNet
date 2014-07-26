'''
    Mapping from protein to ligand or from ligand to protein
'''

from sklearn.cluster import DBSCAN
import numpy

from Modular import LIGAND2PROTEININFO

def GetClusterAnnotate(distance_matrix, cluster_cri):
    min_distance = 1 - cluster_cri
    db = DBSCAN(eps=min_distance, min_samples=1, metric="precomputed").fit(D)
    return db.labels_

def HistNumClusters(labels):
    pass


if __name__ == "__main__":
    pro_dict, lig_dict = ProteinLigandDict(LIGAND2PROTEININFO)

