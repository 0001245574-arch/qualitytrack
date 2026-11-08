import base64,hashlib,hmac,json,time,secrets
from fastapi import HTTPException,Header
from app.core.config import settings
def hash_password(password:str,salt:bytes|None=None)->str:
    salt=salt or secrets.token_bytes(16); digest=hashlib.pbkdf2_hmac("sha256",password.encode(),salt,180000)
    return base64.b64encode(salt+digest).decode()
def verify_password(password:str,encoded:str)->bool:
    raw=base64.b64decode(encoded); return hmac.compare_digest(hash_password(password,raw[:16]),encoded)
def create_access_token(subject:str)->str:
    enc=lambda b:base64.urlsafe_b64encode(b).decode().rstrip("=")
    head=enc(json.dumps({"alg":"HS256","typ":"JWT"}).encode()); payload=enc(json.dumps({"sub":subject,"exp":int(time.time())+settings.access_token_minutes*60}).encode())
    sig=enc(hmac.new(settings.secret_key.encode(),f"{head}.{payload}".encode(),hashlib.sha256).digest())
    return f"{head}.{payload}.{sig}"
def get_current_user(authorization:str|None=Header(default=None)):
    if not authorization or not authorization.lower().startswith("bearer "): raise HTTPException(401,"Autenticação necessária")
    try:
        head,payload,sig=authorization.split(" ",1)[1].split("."); expected=base64.urlsafe_b64encode(hmac.new(settings.secret_key.encode(),f"{head}.{payload}".encode(),hashlib.sha256).digest()).decode().rstrip("=")
        if not hmac.compare_digest(sig,expected): raise ValueError()
        data=json.loads(base64.urlsafe_b64decode(payload+"="*(-len(payload)%4)))
        if data["exp"]<time.time(): raise ValueError()
        return data["sub"]
    except Exception: raise HTTPException(401,"Token inválido ou expirado")
