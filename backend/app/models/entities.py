from datetime import datetime, timezone
from sqlalchemy import String, Integer, Text, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum
from app.database.session import Base
class NCStatus(str, enum.Enum):
    ABERTA="Aberta"; EM_TRATAMENTO="Em tratamento"; AGUARDANDO_VALIDACAO="Aguardando validação"; ENCERRADA="Encerrada"
class NCSeverity(str, enum.Enum):
    BAIXA="Baixa"; MEDIA="Média"; ALTA="Alta"; CRITICA="Crítica"
class NonConformity(Base):
    __tablename__="non_conformities"
    id: Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    code: Mapped[str]=mapped_column(String(24),unique=True,index=True)
    title: Mapped[str]=mapped_column(String(140),nullable=False)
    product: Mapped[str]=mapped_column(String(120),nullable=False)
    production_line: Mapped[str]=mapped_column(String(80),nullable=False)
    defect_type: Mapped[str]=mapped_column(String(80),nullable=False)
    severity: Mapped[NCSeverity]=mapped_column(Enum(NCSeverity),default=NCSeverity.MEDIA)
    status: Mapped[NCStatus]=mapped_column(Enum(NCStatus),default=NCStatus.ABERTA)
    quantity: Mapped[int]=mapped_column(Integer,default=1)
    description: Mapped[str]=mapped_column(Text,nullable=False)
    containment_action: Mapped[str|None]=mapped_column(Text,nullable=True)
    corrective_action: Mapped[str|None]=mapped_column(Text,nullable=True)
    responsible: Mapped[str]=mapped_column(String(120),nullable=False)
    evidence_url: Mapped[str|None]=mapped_column(String(500),nullable=True)
    created_at: Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(timezone.utc))
    updated_at: Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))
