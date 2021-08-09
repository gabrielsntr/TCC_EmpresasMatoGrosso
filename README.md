# TCC_EmpresasMatoGrosso

Projeto desenvolvido como requisito para graduação no curso de Sistemas de Informação da Universidade do Estado de Mato Grosso (UNEMAT). Este projeto está sendo desenvolvido sob orientação do Prof. Me. Francisco Sanches Banhos Filho.

O objetivo deste projeto é desenvolver dashboards interativos para visualização de dados utilizando mapas de calor. Para isso, será utilizado ferramentas e ténicas de ciência de dados. O repositório de dados escolhido é a base pública de CNPJ disponibilizada pela Receita Federal do Brasil. Os dados podem ser encontrados no seguinte endereço:

https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj

O primeiro passo será o download dos dados utilizando Python e bibliotecas de Web Scraping. O script main.py foi desenvolvido para realizar essa tarefa. Para a execução do script é necessário:

* Python 3

Os seguintes módulos também são necessários e obteníveis através do pip:

`pip install requests, wget, bs4`


Ao executar o script, será criada uma pasta chamada files, onde serão salvos os arquivos comprimidos. Após o término do download, eles serão extraídos para uma pasta extracted. 
