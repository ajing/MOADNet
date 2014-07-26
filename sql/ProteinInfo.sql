select ProteinEJB.*, MoadletEJB.pdbFile from MoadletEJB left join ProteinEJB on ProteinEJB.id=MoadletEJB.protein where ProteinEJB.name is not null;
