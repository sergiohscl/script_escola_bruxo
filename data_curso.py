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

# Função para inserir curso no banco de dados
cursor.execute("SELECT varinha FROM bruxo WHERE tipo='Aluno'")
bruxo_id = [row[0] for row in cursor.fetchall()]
for id in bruxo_id:
    conceito = random.randint(1, 10)
    cursor.execute(
        "SELECT varinha FROM bruxo WHERE tipo='Professor' order by rand() limit 1")  # noqa E501
    professor_data = cursor.fetchone()
    cursor.execute(
        "SELECT id FROM disciplina order by rand() limit 1")
    disciplina_data = cursor.fetchone()
    disciplina_id = disciplina_data[0]
    cursor.execute(
        "INSERT INTO curso (aluno_varinha, professor_varinha, disciplina_id, conceito) VALUES (%s, %s, %s, %s)", (id, professor_data, disciplina_id, conceito))  # noqa E501
    db.commit()

# Fechar a conexão com o banco de dados
db.close()
