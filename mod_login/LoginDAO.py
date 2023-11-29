from fastapi import APIRouter, Depends
from mod_funcionario.FuncionarioModel import FuncionarioDB
from mod_login.Login import Login
import security
import db


router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])


@router.post("/login/", tags=["Login"])
def post_usuario(login: Login):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == login.cpf, FuncionarioDB.senha == login.senha).one()       
        return dados, 200
    except Exception as ex:
        return {"erro": str(ex)}, 400
    finally:
        session.close()