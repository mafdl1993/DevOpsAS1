# Use uma versão mais recente do Python
FROM python:3.9

# Defina o diretório de trabalho
WORKDIR /usr/src/app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para dentro do container
COPY . .

# Exponha a porta que o Uvicorn vai rodar
EXPOSE 80

# Comando para rodar a aplicação FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
