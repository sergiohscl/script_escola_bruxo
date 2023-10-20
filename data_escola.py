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

# Função para inserir escolas no banco de dados


def insert_escolas(num_escolas):
    for _ in range(num_escolas):
        nome = fake.unique.first_name()
        data_fundacao = fake.date_of_birth(minimum_age=50, maximum_age=200)
        fundador = fake.name()
        cursor.execute(
            "INSERT INTO escola (nome, data_fundacao, fundador) VALUES (%s, %s, %s)", (nome, data_fundacao, fundador))  # noqa E501
        db.commit()


# Inserir escolas
insert_escolas(10)

# Fechar a conexão com o banco de dados
db.close()
