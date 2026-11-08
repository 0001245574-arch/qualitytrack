from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.models.entities import NCStatus, NCSeverity
class NCBase(BaseModel):
    title:str=Field(min_length=4,max_length=140); product:str=Field(min_length=2,max_length=120)
    production_line:str=Field(min_length=2,max_length=80); defect_type:str=Field(min_length=2,max_length=80)
    severity:NCSeverity=NCSeverity.MEDIA; status:NCStatus=NCStatus.ABERTA
    quantity:int=Field(ge=1,le=1000000); description:str=Field(min_length=8,max_length=3000)
    containment_action:str|None=Field(default=None,max_length=3000); corrective_action:str|None=Field(default=None,max_length=3000)
    responsible:str=Field(min_length=2,max_length=120); evidence_url:str|None=Field(default=None,max_length=500)
class NCCreate(NCBase): pass
class NCUpdate(BaseModel):
    title:str|None=Field(default=None,min_length=4,max_length=140); product:str|None=Field(default=None,min_length=2,max_length=120)
    production_line:str|None=Field(default=None,min_length=2,max_length=80); defect_type:str|None=Field(default=None,min_length=2,max_length=80)
    severity:NCSeverity|None=None; status:NCStatus|None=None; quantity:int|None=Field(default=None,ge=1,le=1000000)
    description:str|None=Field(default=None,min_length=8,max_length=3000); containment_action:str|None=Field(default=None,max_length=3000)
    corrective_action:str|None=Field(default=None,max_length=3000); responsible:str|None=Field(default=None,min_length=2,max_length=120)
    evidence_url:str|None=Field(default=None,max_length=500)
class NCRead(NCBase):
    id:int; code:str; created_at:datetime; updated_at:datetime
    model_config=ConfigDict(from_attributes=True)
class LoginInput(BaseModel): username:str; password:str
class Token(BaseModel): access_token:str; token_type:str="bearer"
