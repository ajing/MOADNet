'''
    Parse info file
'''

from Modular import LIGANDINFO, PROTEININFO, LIGAND2PROTEININFO

from collections import defaultdict
import csv

class AllInfo:
    def __init__(self):
        self._liginfo = LIGANDINFO
        self._proinfo = PROTEININFO
        self._mapinfo = LIGAND2PROTEININFO
        self._prodict, self._ligdict = self.getProteinLigandDict(self._mapinfo)
        self._proinfodict = self.getInfoDict(self._proinfo)
        self._liginfodict = self.getInfoDict(self._liginfo)

    def getMappedLigand(self, pid):
        return self._prodict[pid]

    def getMappedProtein(self, lid):
        return self._ligdict[lid]

    def getProteinInfo(self, pid):
        return self._proinfodict[pid]

    def getLigandInfo(self, lid):
        return self._liginfodict[lid]

    def getProteinLigandDict(self, infile):
        lig_dict = defaultdict(list)
        pro_dict = defaultdict(list)
        with open(infile) as f:
            first_line = f.readline()
        content = first_line.strip().split("\t")
        lig_index = content.index("ligandId")
        pro_index = content.index("proteinId")
        with open(infile) as f:
            for line in f:
                content = line.strip().split("\t")
                if not content[pro_index] in lig_dict[content[lig_index]]:
                    lig_dict[content[lig_index]].append(content[pro_index])
                if not content[lig_index] in pro_dict[content[pro_index]]:
                    pro_dict[content[pro_index]].append(content[lig_index])
        return pro_dict, lig_dict

    def getInfoDict(self, infile):
        info_csv = csv.DictReader(open(infile), delimiter="\t")
        info_dict = dict()
        for each in info_csv:
            info_dict[each["id"]] = each
        return info_dict

if __name__ == "__main__":
    info = AllInfo()
    print info.getMappedLigand("1")
    print info.getMappedProtein("1")
    print info.getProteinInfo("1")
