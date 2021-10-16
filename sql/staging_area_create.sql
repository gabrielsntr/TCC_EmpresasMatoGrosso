create database if not exists cnpj_staging_area CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI;
use cnpj_staging_area;

create table empresa (
    cnpj_basico_int int,
	cnpj_basico varchar(8),
    razao_social varchar(255),
    id_natureza_juridica smallint,
    qualificacao_responsavel smallint,
    capital_social DECIMAL(15,2) default 0,
    porte tinyint,
    ente_responsavel varchar(255),
    cpf varchar(15)
);

create table estabelecimento (
    cnpj_basico_int int,
	cnpj_basico varchar(8),
    cnpj_ordem varchar(4),
    cnpj_dv varchar(2),
    id_matriz_filial tinyint,
    nome_fantasia VARCHAR(255),
    id_situacao_cadastral smallint,
    data_situacao_cadastral date,
    id_motivo_situacao_cadastral smallint,
    nome_cidade_exterior varchar(50),
    id_pais smallint,
    data_inicio_atividade date,
    id_cnae int,
    is_cnae_primario varchar(1),
    tipo_logradouro varchar(20),
    logradouro varchar(100),
    numero varchar(15),
    complemento varchar(255),
    bairro varchar(50),
    cep varchar(10),
    uf varchar(2),
    id_municipio int,
    telefone_1 varchar(15),
    telefone_2 varchar(15),
    email varchar(100),
    situacao_especial varchar(100),
    data_situacao_especial date
    );
    
create table dados_simples (
    cnpj_basico_int int,
	cnpj_basico varchar(8),
    opcao_simples varchar(1),
    data_opcao_simples date,
    data_exclusao_simples date,
    opcao_mei varchar(1),
    data_opcao_mei date,
    data_exclusao_mei date
    );

create table socio (
    cnpj_basico_int int,
	cnpj_basico varchar(8),
    identificador_socio tinyint,
    nome_socio varchar(255),
    cnpj_cpf_socio varchar(20),
    id_qualificacao_socio smallint,
    data_entrada_sociedade date,
    id_pais smallint,
    cpf_representante_legal varchar(15),
    nome_representante_legal varchar(255),
    id_qualificacao_representante_legal smallint,
    id_faixa_taria smallint
);

create table pais (
	id smallint,
	nome varchar(50)
);

create table municipio (
	id smallint,
	nome varchar(50)
);

create table qualificacao_socio (
	id smallint,
	nome varchar(100)
);

create table natureza_juridica (
	id smallint,
	nome varchar(100)
);

create table cnae (
	id int,
	nome varchar(150)
);

create table situacao_cadastral (
	id smallint,
	nome varchar(100)
);

CREATE TABLE sync_dates (
	data_dados DATE,
	data_update DATETIME DEFAULT NOW()
);

CREATE INDEX cnpj_int ON dados_simples (cnpj_basico_int);
CREATE INDEX cnpj_int ON empresa (cnpj_basico_int);
CREATE INDEX cnpj_int ON estabelecimento (cnpj_basico_int);
CREATE INDEX cnpj_int ON socio (cnpj_basico_int);
