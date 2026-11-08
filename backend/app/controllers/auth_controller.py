from fastapi import APIRouter,HTTPException
from app.schemas.non_conformity import LoginInput,Token
from app.core.security import create_access_token,verify_password,hash_password
router=APIRouter(prefix="/api/auth",tags=["Autenticação"])
DEMO_USERNAME="admin"; DEMO_PASSWORD_HASH=hash_password("Quality@123")
@router.post("/login",response_model=Token)
def login(payload:LoginInput):
    if payload.username!=DEMO_USERNAME or not verify_password(payload.password,DEMO_PASSWORD_HASH): raise HTTPException(401,"Usuário ou senha incorretos")
    return Token(access_token=create_access_token(payload.username))
