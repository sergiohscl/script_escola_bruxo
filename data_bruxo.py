from faker import Faker
import random
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

# Função para inserir bruxos no banco de dados


def insert_bruxos(num_bruxos, professores):
    for _ in range(num_bruxos):
        nome = fake.first_name()
        data_nascimento = fake.date_of_birth(minimum_age=11, maximum_age=100)
        tipo = "Aluno" if random.choice([True, False]) else "Professor"
        animal = fake.word() if tipo == "Aluno" else None
        cursor.execute(
            "SELECT id, escola_id FROM casa order by rand() limit 1")
        casa_data = cursor.fetchone()
        print(casa_data)
        casa_id = casa_data[0]
        escola_id = casa_data[1]
        casa_responsavel = professores if tipo == "Professor" else None
        casa_monitor = None if tipo == "Professor" else casa_id
        cursor.execute("INSERT INTO bruxo (nome, data_nascimento, tipo, animal, escola_id, mora_casa_id, casa_responsavel, casa_monitor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",  # noqa E501
                       (nome, data_nascimento, tipo, animal, escola_id, casa_id, casa_responsavel, casa_monitor))  # noqa E501
        db.commit()


# Inserir bruxos
professores = random.randint(1, 50)
insert_bruxos(4999, professores)


# Fechar a conexão com o banco de dados
db.close()
