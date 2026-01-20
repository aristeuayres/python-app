FROM python:3.13-alpine

# Evita bytecode e buffer no stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Definir pasta de trabalho
WORKDIR /app

# Copiar dependências primeiro para aproveitar cache, codigo e app.py
COPY requirements.txt /app/requirements.txt 

#Copiar app.py
COPY app.py /app

# Instalar dependências (sem cache do pip)
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expor a porta que o Flask vai usar (opcional, docs)
EXPOSE 5000

# Usar forma JSON para repasse de sinais
CMD ["python", "/app/app.py"]



