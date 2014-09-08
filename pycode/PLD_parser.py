## This is for parsing of PLD
## Date: 5/7/12
## Author: ajing

import os

class PLD_parser:
    def __init__(self, threshold,workdir = '/users/ajing/PLD_MOADNet/Binning/'):
        self.work_dir = workdir
        self.blast_list_dir = os.path.join(self.work_dir, 'CurrentRun/blastlist')
        self.threshold = threshold
        self.protein_center = self.out_parser()

    def fancy_parser(self,threshold = None):
        if threshold is None:
            threshold = self.threshold
        filename = str(threshold) + 'ec-subbins.fancy.out'
        fancy_dir = os.path.join(self.blast_list_dir, 'scale2/'+filename)
	## the core for fancy.out file parser
        n = -1
        n_old = None
        p_cluster = dict()
        header_flag = 0
        for line in open(fancy_dir):
            ## ignore the header
            ## protein family number
            content = line.strip().split('\t')
    	    if line.startswith('EC: '):
                header_flag = 1
                n = n + 1
            elif n != n_old and header_flag:
                n_old = n
                p_cluster[n] = [content[0]]
            elif n == n_old and header_flag:
                p_cluster[n].append(content[0])
        p_cluster_refine = dict()
        for key in p_cluster.keys():
            if len(p_cluster[key])>1:
                p_cluster_refine[p_cluster[key][0]] = p_cluster[key][1:]
            else:
                p_cluster_refine[p_cluster[key][0]] = []
        #print p_cluster_refine
        return p_cluster_refine

    def out_parser(self,threshold = None):
        if threshold is None:
            threshold = self.threshold
        filename = str(threshold) + 'ec-subbins.out'
        out_dir = os.path.join(self.blast_list_dir, 'scale2/'+filename)
        protein_center = []
        for line in open(out_dir):
            protein_center.append(line.strip())
        return protein_center

if __name__ == "__main__":
    parser = PLD_parser(95)
    cluster = parser.fancy_parser()
    print cluster
    print cluster['0116']
    print len(cluster.keys())
    print len(sum(cluster.values(),[]))
