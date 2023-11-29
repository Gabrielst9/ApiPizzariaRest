from fastapi import FastAPI
from settings import HOST, PORT, RELOAD

# import das classes com as rotas/endpoints
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO
from mod_login import LoginDAO

app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)
app.include_router(LoginDAO.router)

#cria, caso não existam, as tabelas de todos os modelos importados
import db
db.criaTabelas()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('apiPizzaria:app', host=HOST, port=int(PORT), reload=RELOAD) # type: ignore

# rota padrão
@app.get("/")
def root():
    return {"detail":"API Pastelaria", "Swagger UI": "http://127.0.0.1:8000/docs", "ReDoc": "http://127.0.0.1:8000/redoc" }