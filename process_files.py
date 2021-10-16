import os
import subprocess

pentaho_loc = 'C:/Program Files (x86)/Pentaho/data-integration/'
file_path = os.path.abspath('./files/extracted/')
transform_path = os.path.abspath('./pentaho/')
#files = os.listdir(file_path)

#for file in files:
#    fullpath = file_path + "/" + file
#    command = '"' + pentaho_loc + 'pan.bat" /file:"' + transform_path + '/{0}.ktr" ' + '"/param:filepath=' + fullpath + '"'

def run_transform(file):
    fullpath = file_path + "/" + file
    command = '"' + pentaho_loc + 'pan.bat" /file:"' + transform_path + '/{0}.ktr" ' + '"/param:filepath=' + fullpath + '"'
    if file.find('dados_abertos_cnpj_empresa_') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('empresa'))
    
    elif file.find('dados_abertos_cnpj_estabelecimento_') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('estabelecimento'))

    elif file.find('dados_abertos_cnpj_socio_') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('socio'))

    elif file.find('informacoes_sobre_o_simples_nacional-mei') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('simples'))

    elif file.find('tabela_de_atributo_municipio') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('municipio'))

    elif file.find('tabela_de_atributo_natureza_juridica') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('natureza_juridica'))
                
    elif file.find('tabela_de_atributo_pais') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('pais'))

    elif file.find('tabela_de_atributo_qualificacao_dos_socios') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('qualificacao_socio'))

    elif file.find('tabela_de_motivo_da_situacao_cadastral') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('situacao_cadastral'))

    elif file.find('tabela_de_atributo_cnae') >= 0:
        print("Transforming " + file)
        subprocess.run(command.format('cnae'))
    
    else:
        print("No transformation for file " + file)


def run_dw_transform(sync_date):
    command = '"' + pentaho_loc + 'pan.bat" /file:"' + transform_path + '/{0}.ktr" ' + '"/param:sync_date=' + sync_date + '"'
    subprocess.run(command.format('staging_production'))
