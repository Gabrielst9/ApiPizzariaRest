from pydantic import BaseModel

class ProdutoModel(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str = None
    foto: str
    valor_unitario: float
    