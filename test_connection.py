import psycopg
import time  # Importando o módulo time

try:
    conn = psycopg.connect(
        dbname="robot",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )
    time.sleep(2)  # Pausa de 2 segundos antes de imprimir
    print("Conexão realizada com sucesso!")
    time.sleep(2)
    conn.close()
except psycopg.Error as e:
    print(f"Erro: {e}")
