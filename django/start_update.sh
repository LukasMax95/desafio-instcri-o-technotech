#!/bin/bash
# Script: start.sh
# =======================================================
python manage.py makemigrations --noinput
python manage.py migrate --noinput
# Define a porta inicial
PORTA=8000

# Loop para testar portas
while true; do
    echo "Tentando iniciar o servidor na porta $PORTA..."

    # Comando 'ss -ltn' verifica se a porta está em LISTEN.
    # Se o 'grep' encontrar a porta no output (retorna 0), significa que está ocupada.
    if ss -ltn | grep -q ":$PORTA\>"; then
        echo "A porta $PORTA está ocupada. Tentando a próxima porta..."
        # Incrementa a porta
        PORTA=$((PORTA + 1))
    else
        # Se o 'grep' não encontrar a porta (retorna diferente de 0), está livre.
        echo "Porta $PORTA está livre. Iniciando o servidor Django."
        break # Sai do loop
    fi
done

# Executa o Django com a porta livre encontrada
python manage.py runserver $PORTA
# =======================================================