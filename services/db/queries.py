# ==== SCHEMA: Criação do banco e tabelas ====

CREATE_DATABASE = """
CREATE DATABASE IF NOT EXISTS banco_teste_automacao;
USE banco_teste_automacao;
"""

CREATE_TABLES_USUARIOS = """ 
CREATE TABLE IF NOT EXISTS usuarios (
    id VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    username VARCHAR(50),
    senha VARCHAR(50)
);
"""

CREATE_TABLES_PEDIDOS = """ 
CREATE TABLE IF NOT EXISTS pedidos (
    numero_pedido VARCHAR(50) PRIMARY KEY,
    usuario_id VARCHAR(20),
    codigo_rastreamento VARCHAR(100),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
"""

CREATE_TABLE_PRODUTOS = """
CREATE TABLE IF NOT EXISTS produtos (
    id INT(11) NOT NULL AUTO_INCREMENT,
    nome_produto VARCHAR(45) DEFAULT NULL,
    personalizacao VARCHAR(45) DEFAULT NULL,
    display VARCHAR(600) DEFAULT NULL,
    resolucao_display VARCHAR(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
    tamanho_display VARCHAR(45) DEFAULT NULL,
    memoria VARCHAR(45) DEFAULT NULL,
    sistema_operacional VARCHAR(45) DEFAULT NULL,
    processador VARCHAR(255) DEFAULT NULL,
    touchscreen VARCHAR(45) DEFAULT NULL,
    peso VARCHAR(45) DEFAULT NULL,
    cor VARCHAR(45) DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""

# ==== USUÁRIOS ====

GET_USUARIO_POR_ID = "SELECT * FROM usuarios WHERE id = %s"

INSERT_USUARIO = """
INSERT INTO usuarios (nome, email, username, senha)
VALUES (%s, %s, %s, %s)
"""

UPDATE_STATUS_USUARIO = """
UPDATE usuarios
SET status = %s
WHERE id = %s
"""

DELETE_USUARIO_POR_ID = "DELETE FROM usuarios WHERE id = %s"

# ==== PRODUTOS ====

GET_PRODUTO_POR_ID = "SELECT * FROM produtos WHERE id = %s"

INSERT_PRODUTOS_MASSA_TESTE = """
INSERT INTO produtos (
    nome_produto, personalizacao, display, resolucao_display, tamanho_display,
    memoria, sistema_operacional, processador, touchscreen, peso, cor
) VALUES (
    "HP PAVILION 15Z TOUCH LAPTOP", "Simplicity", "15.6-inch diagonal Full HD WLED-backlit Display (1920x1080) Touchscreen",
    "1920x1080", "15.6", "16GB DDR3 - 2 DIMM", "Windows 10", "AMD Quad-Core A10-8700P Processor + AMD Radeon(TM)",
    "Yes", "4.62 lbs", "Silver"
);
"""

# ==== PEDIDOS ====

GET_PEDIDO_POR_ID = "SELECT * FROM pedidos WHERE numero_pedido = %s"
