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

# Função para inserir disciplina no banco de dados


def insert_disciplina(num_escolas):
    for _ in range(num_escolas):
        nome = fake.unique.first_name()
        ementa = fake.sentence()
        data = fake.date_of_birth(minimum_age=5, maximum_age=50)
        cursor.execute(
            "INSERT INTO disciplina (nome, ementa, data) VALUES (%s, %s, %s)", (nome, ementa, data))  # noqa E501
        db.commit()


# Inserir disciplina
insert_disciplina(25)

# Fechar a conexão com o banco de dados
db.close()
