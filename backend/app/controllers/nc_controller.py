from fastapi import APIRouter,Depends,Query
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.nc_repository import NCRepository
from app.services.nc_service import NCService
from app.schemas.non_conformity import NCCreate,NCUpdate,NCRead
from app.core.security import get_current_user
router=APIRouter(prefix="/api/non-conformities",tags=["Não-conformidades"])
def svc(db): return NCService(NCRepository(db))
@router.get("",response_model=list[NCRead])
def list_ncs(search:str|None=Query(default=None,max_length=120),status:str|None=None,db:Session=Depends(get_db),user:str=Depends(get_current_user)): return svc(db).list(search,status)
@router.post("",response_model=NCRead,status_code=201)
def create_nc(payload:NCCreate,db:Session=Depends(get_db),user:str=Depends(get_current_user)): return svc(db).create(payload)
@router.get("/{nc_id}",response_model=NCRead)
def get_nc(nc_id:int,db:Session=Depends(get_db),user:str=Depends(get_current_user)): return svc(db).get(nc_id)
@router.put("/{nc_id}",response_model=NCRead)
def update_nc(nc_id:int,payload:NCUpdate,db:Session=Depends(get_db),user:str=Depends(get_current_user)): return svc(db).update(nc_id,payload)
@router.delete("/{nc_id}")
def delete_nc(nc_id:int,db:Session=Depends(get_db),user:str=Depends(get_current_user)): return svc(db).delete(nc_id)
