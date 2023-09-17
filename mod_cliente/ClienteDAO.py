from fastapi import APIRouter

from mod_cliente.Cliente import ClienteModel

#importacao da depencia da security
from fastapi import Depends
import security

# import da persistência
import db
from mod_cliente.ClienteModel import ClienteDB

router = APIRouter()

# dependências de forma global
router = APIRouter( dependencies=[Depends(security.verify_token), Depends(security.verify_key)] )

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE
#--------------------------------------------------------------------
#GET
@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(ClienteDB).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
#--------------------------------------------------------------------
#GET
@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).all()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
#--------------------------------------------------------------------
#POST
@router.post("/cliente/", tags=["Cliente"])
def post_cliente(corpo: ClienteModel):
    try:
        session = db.Session()
        dados = ClienteDB(None, corpo.nome,
                            corpo.cpf, corpo.telefone, corpo.compra_fiado, corpo.dia_fiado, corpo.senha)

        session.add(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
#--------------------------------------------------------------------
@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, corpo: ClienteModel):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(
        ClienteDB.id_cliente == id).one()
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf            
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.compra_fiado = corpo.compra_fiado
        dados.dia_fiado = corpo.dia_fiado
        
        session.add(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
#--------------------------------------------------------------------
#DELETE

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    try:
        session = db.Session()
        dados = session.query(ClienteDB).filter(ClienteDB.id_cliente == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_cliente}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()
#--------------------------------------------------------------------