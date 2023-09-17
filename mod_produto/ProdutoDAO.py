from fastapi import APIRouter

from mod_produto.Produto import ProdutoModel

#importacao da depencia da security
from fastapi import Depends
import security

# import da persistência
import db
from mod_produto.ProdutoModel import ProdutoDB

router = APIRouter()

# Criar as rotas/endpoints: GET, POST, PUT, DELETE

# dependências de forma global
router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] )

# --------------------------------------------------------------------
@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

# --------------------------------------------------------------------


@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ProdutoDB).filter(
            ProdutoDB.id_produto == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

# --------------------------------------------------------------------


@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: ProdutoModel):
    try:
        session = db.Session()
        dados = ProdutoDB(None, corpo.nome, corpo.descricao, 
                          corpo.foto, corpo.valor_unitario)
        session.add(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
# --------------------------------------------------------------------
@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, corpo: ProdutoModel):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(
        ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        dados.valor_unitario = corpo.valor_unitario

        session.add(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
# --------------------------------------------------------------------


@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_produto}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
# --------------------------------------------------------------------
