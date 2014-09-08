'''
    Do some statistics of the clusters
'''

import numpy
from Modular import LIGAND2PROTEININFO, LIGAND_DISTANCE_MATRIX

def HistNumClusters(labels):
    pass

def MappedClusterStat():
    lig_clust_cri  = 0.95
    lig_distmatrix = numpy.load(LIGAND_DISTANCE_MATRIX)
    lig_cluster_labels = GetClusterAnnotate(lig_distmatrix, lig_clust_cri)
    lig_clusters   = GetClusterwithLabels(,labels)

