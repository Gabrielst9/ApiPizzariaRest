from pydantic import BaseModel


class Login(BaseModel):
    cpf: str
    senha: str