select LigandSuperRelationEJB.ligandId, MoadletEJB.protein as proteinId from LigandSuperRelationEJB left join MoadletEJB on LigandSuperRelationEJB.moadlet = MoadletEJB.id;
