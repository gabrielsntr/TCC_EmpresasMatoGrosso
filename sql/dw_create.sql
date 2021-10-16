create database if not exists cnpj_dw CHARACTER SET utf8 COLLATE UTF8_GENERAL_CI;
use cnpj_dw;

create table fact_estabelecimento (
    cnpj_basico_int int,
	cnpj_basico varchar(8),
    cnpj_ordem varchar(4),
    cnpj_dv varchar(2),
    id_matriz_filial tinyint,
    nome_fantasia VARCHAR(255),
    id_situacao_cadastral smallint,
    data_situacao_cadastral date,
    id_motivo_situacao_cadastral smallint,
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
	id_pais smallint,
    telefone_1 varchar(15),
    telefone_2 varchar(15),
    email varchar(100),
    situacao_especial varchar(100),
    data_situacao_especial date   
);


create table fact_socio (
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


create table dim_empresa (
    cnpj_basico_int int,
    cnpj_basico varchar(8),
    razao_social varchar(255),
    id_natureza_juridica smallint,
    natureza_juridica varchar(100),
    id_qualificacao_responsavel smallint,
    qualificacao_responsavel varchar(100),
    capital_social DECIMAL(15,2) default 0,
    id_porte tinyint,
    porte varchar(30),
    ente_responsavel varchar(255),
    cpf varchar(15),
    opcao_simples varchar(1) default 'N',
	data_opcao_simples DATE default null, 
	data_exclusao_simples DATE default null, 
    opcao_mei varchar(1) default 'N',
	data_opcao_mei DATE default null,
	data_exclusao_mei DATE default null
);


create table dim_municipio (
	id smallint,
	nome varchar(50)
);

create table dim_cnae (
	id int,
	nome varchar(150)
);

create table dim_motivo_situacao_cadastral (
	id smallint,
	nome varchar(100)
);

create table dim_situacao_cadastral (
	id smallint,
	nome varchar(20)
);

create table dim_matriz_filial (
	id tinyint,
	nome varchar(15)
);

create table dim_faixa_etaria (
	id tinyint,
	nome varchar(15)
);

create table dim_pais (
	id smallint,
	nome varchar(50)
);

create table dim_id_socio (
	id smallint,
	nome varchar(30)
);

create table dim_qualificacao_socio (
	id smallint,
	nome varchar(100)
);

CREATE TABLE sync_dates (
	data_dados DATE,
	data_update DATETIME DEFAULT NOW()
);

CREATE INDEX cnpj_int ON dim_empresa (cnpj_basico_int);
CREATE INDEX cnpj_int ON fact_estabelecimento (cnpj_basico_int);
CREATE INDEX cnpj_int ON fact_socio (cnpj_basico_int);
