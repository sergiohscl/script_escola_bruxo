CREATE TABLE IF NOT EXISTS escola (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL UNIQUE,
  data_fundacao DATE NOT NULL,
  fundador VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS casa (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL UNIQUE,
  mascote VARCHAR(255) NOT NULL UNIQUE,
  escola_id INT NOT NULL,
  FOREIGN KEY (escola_id) REFERENCES escola (id) ON DELETE CASCADE,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS bruxo (
  varinha INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  data_nascimento DATE NOT NULL,
  tipo VARCHAR(255) NOT NULL,
  animal VARCHAR(255),
  escola_id INT,
  mora_casa_id INT,
  casa_responsavel INT,
  casa_monitor INT,
  FOREIGN KEY (escola_id) REFERENCES escola (id),
  FOREIGN KEY (casa_responsavel) REFERENCES casa (id),
  FOREIGN KEY (casa_monitor) REFERENCES casa (id),
  PRIMARY KEY (varinha)
);

CREATE TABLE IF NOT EXISTS quadribol(
  id_jogo INT NOT NULL AUTO_INCREMENT,
  oponente_1 INT NOT NULL,
  oponente_2 INT NOT NULL,
  pontos_oponente_1 INT NOT NULL DEFAULT 0,
  pontos_oponente_2 INT NOT NULL DEFAULT 0,
  FOREIGN KEY (oponente_1) REFERENCES casa (id),
  FOREIGN KEY (oponente_2) REFERENCES casa (id),
  PRIMARY KEY (id_jogo)  
);

CREATE TABLE IF NOT EXISTS torneio_tribruxo(
 id INT NOT NULL AUTO_INCREMENT,
 escola_1 INT NOT NULL,
 escola_2 INT NOT NULL,
 responsavel_escola_1 INT NOT NULL,
 responsavel_escola_2 INT NOT NULL,
 ponto_escola_1 INT NOT NULL DEFAULT 0,
 ponto_escola_2 INT NOT NULL DEFAULT 0,
 FOREIGN KEY (escola_1) REFERENCES escola (id),
 FOREIGN KEY (escola_2) REFERENCES escola (id),
 FOREIGN KEY (responsavel_escola_1) REFERENCES bruxo (varinha),
 FOREIGN KEY (responsavel_escola_2) REFERENCES bruxo (varinha),
 PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS disciplina (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  ementa VARCHAR(255) NOT NULL,
  data DATE NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS curso (
  id INT NOT NULL AUTO_INCREMENT,
  aluno_varinha INT,
  professor_varinha INT,
  disciplina_id INT NOT NULL,
  conceito INT NOT NULL,
  FOREIGN KEY (aluno_varinha) REFERENCES bruxo (varinha),
  FOREIGN KEY (professor_varinha) REFERENCES bruxo (varinha),
  FOREIGN KEY (disciplina_id) REFERENCES disciplina (id) ON DELETE CASCADE,
  PRIMARY KEY (id)
);