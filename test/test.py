import pytest
from unittest.mock import patch
from pydantic import BaseModel
from src.main import root, funcaoteste

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="curso 1", ativo=False)
    assert estudante_teste.name == "Fulano"
    assert estudante_teste.curso == "curso 1"
    assert not estudante_teste.ativo

def test_update_estudante_negativo():
    param = -5
    assert param < 0

def test_update_estudante_positivo():
    param = 10
    assert param > 0
