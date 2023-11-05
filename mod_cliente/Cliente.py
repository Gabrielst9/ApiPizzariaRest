import datetime
from pydantic import BaseModel

class ClienteModel(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str = None
    telefone: str = None
    compra_fiado: int = None
    dia_fiado: str = None  
    senha: str = None
