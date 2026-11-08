from datetime import datetime,timezone
from fastapi import HTTPException
from app.models.entities import NonConformity,NCStatus
class NCService:
    def __init__(self,repository): self.repository=repository
    def list(self,search=None,status=None): return self.repository.list(search,status)
    def get(self,nc_id):
        item=self.repository.get(nc_id)
        if not item: raise HTTPException(404,"Não-conformidade não encontrada")
        return item
    def create(self,data):
        values=data.model_dump(); values["code"]=f"NC-{datetime.now(timezone.utc):%y%m%d%H%M%S%f}"
        return self.repository.create(NonConformity(**values))
    def update(self,nc_id,data):
        item=self.get(nc_id); values=data.model_dump(exclude_unset=True)
        if item.status==NCStatus.ENCERRADA and values.get("status") not in (None,NCStatus.ENCERRADA): raise HTTPException(409,"Ocorrência encerrada não pode ser reaberta por edição")
        for key,value in values.items(): setattr(item,key,value)
        return self.repository.save(item)
    def delete(self,nc_id): self.repository.delete(self.get(nc_id));return {"message":"Não-conformidade excluída"}
    def dashboard(self):
        items=self.repository.list(); closed=sum(x.status==NCStatus.ENCERRADA for x in items)
        return {"total":len(items),"abertas":sum(x.status==NCStatus.ABERTA for x in items),"em_tratamento":sum(x.status==NCStatus.EM_TRATAMENTO for x in items),"aguardando_validacao":sum(x.status==NCStatus.AGUARDANDO_VALIDACAO for x in items),"encerradas":closed,"criticas":sum(x.severity.value=="Crítica" for x in items),"taxa_encerramento":round(closed/len(items)*100,1) if items else 0}
