select LigandSuperRelationEJB.ligandId, MoadletEJB.protein from LigandSuperRelationEJB left join MoadletEJB on LigandSuperRelationEJB.moadlet = MoadletEJB.id;
