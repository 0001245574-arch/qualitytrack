from types import SimpleNamespace
from unittest.mock import Mock
import pytest
from fastapi import HTTPException
from app.services.nc_service import NCService
from app.models.entities import NCStatus
def test_list_delegates():
 r=Mock();r.list.return_value=[];assert NCService(r).list("solda",None)==[];r.list.assert_called_once_with("solda",None)
def test_get_existing():
 item=object();r=Mock();r.get.return_value=item;assert NCService(r).get(3) is item
def test_get_missing_404():
 r=Mock();r.get.return_value=None
 with pytest.raises(HTTPException) as e: NCService(r).get(99)
 assert e.value.status_code==404
def test_dashboard_counts():
 r=Mock();r.list.return_value=[SimpleNamespace(status=NCStatus.ABERTA,severity=SimpleNamespace(value="Crítica")),SimpleNamespace(status=NCStatus.ENCERRADA,severity=SimpleNamespace(value="Baixa"))]
 d=NCService(r).dashboard();assert d["total"]==2 and d["abertas"]==1 and d["encerradas"]==1 and d["criticas"]==1 and d["taxa_encerramento"]==50.0
def test_delete_delegates():
 item=object();r=Mock();r.get.return_value=item;assert NCService(r).delete(1)["message"]=="Não-conformidade excluída";r.delete.assert_called_once_with(item)
