CREATE DATABASE MundoDosQuadrinhos;
USE MundoDosQuadrinhos;

-- Tabela de Editoras para evitar repetição
CREATE TABLE Editoras (
    id_editora INT PRIMARY KEY AUTO_INCREMENT,
    nome_editora VARCHAR(100) NOT NULL
);

-- Tabela Principal de Séries
CREATE TABLE Series (
    id_serie INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    id_editora INT,
    num_volumes INT,
    vendas_milhoes DECIMAL(10, 2),
    ano_inicio INT,
    FOREIGN KEY (id_editora) REFERENCES Editoras(id_editora)
);