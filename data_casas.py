from faker import Faker
# import random
import pymysql
from os import environ

# Conectar ao banco de dados
db = pymysql.connect(
    host=environ["DB_LOCALHOST"],
    user=environ["DB_USER"],
    password=environ["DB_PASSWORD"],
    database=environ["DB_DATABASE"],
)
cursor = db.cursor()

# Inicializar o Faker
fake = Faker()


# Função para inserir casas no banco de dados


def insert_casas(num_casas):
    cursor.execute("SELECT id FROM escola")
    escola_id = [row[0] for row in cursor.fetchall()]
    for id in escola_id:
        for _ in range(num_casas):
            nome = fake.unique.first_name()
            mascote = fake.unique.first_name()
            cursor.execute(
                f"INSERT INTO casa (nome, mascote, escola_id) VALUES ('{nome}', '{mascote}', '{id}')")  # noqa E501
            db.commit()


# Inserir casa
insert_casas(10)


# Fechar a conexão com o banco de dados
db.close()
