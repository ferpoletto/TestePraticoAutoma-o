# ==== SCHEMA: Criação do banco e tabelas ====
 
CREATE_DATABASE_AND_TABLES = """
CREATE DATABASE IF NOT EXISTS automacao_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE automacao_db;
 
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    status ENUM('ativo', 'inativo') DEFAULT 'ativo',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
 
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
 
CREATE TABLE IF NOT EXISTS pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    status ENUM('pendente', 'concluido', 'cancelado') DEFAULT 'pendente',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
"""
 
# ==== USUÁRIOS ====
 
GET_USUARIO_POR_EMAIL = "SELECT * FROM usuarios WHERE email = %s"
GET_USUARIOS_ATIVOS = "SELECT * FROM usuarios WHERE status = 'ativo'"
 
INSERT_USUARIO = """
INSERT INTO usuarios (nome, email, status)
VALUES (%s, %s, %s)
"""
 
UPDATE_STATUS_USUARIO = """
UPDATE usuarios
SET status = %s
WHERE email = %s
"""
 
DELETE_USUARIO_POR_EMAIL = "DELETE FROM usuarios WHERE email = %s"
 
TRUNCATE_USUARIOS = "TRUNCATE TABLE usuarios"
 
# ==== PRODUTOS ====
 
GET_PRODUTO_POR_ID = "SELECT * FROM produtos WHERE id = %s"
 
INSERT_PRODUTO = """
INSERT INTO produtos (nome, preco, estoque)
VALUES (%s, %s, %s)
"""
 
UPDATE_ESTOQUE_PRODUTO = """
UPDATE produtos
SET estoque = %s
WHERE id = %s
"""
 
DELETE_PRODUTO = "DELETE FROM produtos WHERE id = %s"
 
TRUNCATE_PRODUTOS = "TRUNCATE TABLE produtos"
 
# ==== PEDIDOS ====
 
GET_PEDIDO_POR_ID = "SELECT * FROM pedidos WHERE id = %s"
 
INSERT_PEDIDO = """
INSERT INTO pedidos (usuario_id, total, status)
VALUES (%s, %s, %s)
"""
 
UPDATE_STATUS_PEDIDO = """
UPDATE pedidos
SET status = %s
WHERE id = %s
"""
 
DELETE_PEDIDO = "DELETE FROM pedidos WHERE id = %s"
 
TRUNCATE_PEDIDOS = "TRUNCATE TABLE pedidos"