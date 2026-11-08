from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.config import settings
from app.database.session import Base,engine,get_db
from app.models import NonConformity
from app.controllers.nc_controller import router as nc_router
from app.controllers.auth_controller import router as auth_router
from app.core.security import get_current_user
from app.services.nc_service import NCService
from app.repositories.nc_repository import NCRepository
Base.metadata.create_all(bind=engine)
app=FastAPI(title="QualityTrack API",description="Gestão de inspeção de qualidade e não-conformidades industriais",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=settings.allowed_origins,allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",allow_credentials=True,allow_methods=["GET","POST","PUT","DELETE","OPTIONS"],allow_headers=["Authorization","Content-Type"])
app.include_router(auth_router);app.include_router(nc_router)
@app.get("/")
def home(): return {"sistema":"QualityTrack","mensagem":"API funcionando","versao":"1.0.0"}
@app.get("/health")
def health(): return {"status":"online"}
@app.get("/api/dashboard",tags=["Indicadores"])
def dashboard(db:Session=Depends(get_db),user:str=Depends(get_current_user)): return NCService(NCRepository(db)).dashboard()
@app.exception_handler(Exception)
async def unexpected_error_handler(request,exc): return JSONResponse(status_code=500,content={"detail":"Erro interno. Consulte os registros do servidor."})
