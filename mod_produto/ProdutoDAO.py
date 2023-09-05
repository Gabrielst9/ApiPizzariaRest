from fastapi import APIRouter

from mod_produto.Produto import ProdutoModel

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

@router.get("/produto/", tags=["Produto"])
def get_produto():
    return {"msg": "get todos executado"}, 200

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/produto/", tags=["Produto"])
def post_produto(p: ProdutoModel):
    return {"msg": "post executado", "nome": p.nome, "descricao": p.descricao, "valor Unitario": p.valor_unitario }, 200

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, p: ProdutoModel):
    return {"msg": "put executado", "id":id, "nome": p.nome, "descricao": p.descricao, "valor Unitario": p.valor_unitario }, 201

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201

