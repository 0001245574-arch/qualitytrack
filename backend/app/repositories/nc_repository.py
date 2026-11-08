from sqlalchemy.orm import Session
from sqlalchemy import select,func,or_
from app.models.entities import NonConformity
class NCRepository:
    def __init__(self,db:Session): self.db=db
    def list(self,search=None,status=None):
        stmt=select(NonConformity).order_by(NonConformity.created_at.desc())
        if search:
            term=f"%{search.strip()}%"; stmt=stmt.where(or_(NonConformity.code.ilike(term),NonConformity.title.ilike(term),NonConformity.product.ilike(term),NonConformity.defect_type.ilike(term)))
        if status: stmt=stmt.where(NonConformity.status==status)
        return list(self.db.scalars(stmt).all())
    def get(self,nc_id): return self.db.get(NonConformity,nc_id)
    def create(self,item): self.db.add(item);self.db.commit();self.db.refresh(item);return item
    def save(self,item): self.db.commit();self.db.refresh(item);return item
    def delete(self,item): self.db.delete(item);self.db.commit()
