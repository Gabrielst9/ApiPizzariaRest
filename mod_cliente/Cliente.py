from pydantic import BaseModel

class ClienteModel(BaseModel):
    id_cliente: int = None
    nome: str = None
    cpf: str = None
    telefone: str = None
    compra_fiado: int
    dia_fiado: int
    senha: str = None