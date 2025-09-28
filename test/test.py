from difflib import restore

from pydantic import BaseModel

from src.main import *
from unittest.mock import patch



#http://127.0.0.1:8000/
def test_root():
    assert root() == {"message": "Hello World"}

#http://127.0.0.1:8000/teste1
def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()

    assert funcaoteste() == {"teste": True, "num_aleatorio": 12345}

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="curso 1", ativo=False)
    assert estudante_teste == test_create_estudante()

def test_update_estudante_negativo():
    assert not update_estudante(-5)


def updtate_studante(param):
    pass


def test_update_estudante_positivo():
    assert updtate_studante(10)


def update_estudante(param):
    pass


def test_delete_estudante_negativo():
    assert not update_estudante(-5)


def test_delete_estudante_positivo():
    assert update_estudante(5)


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

