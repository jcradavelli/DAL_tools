#
#
#
import os

DRV_PATH = './'

def add_snippet(texto: str, tag: str, dicionario: dict):
    # Encontra a posição da tag no texto
    inicio_tag = texto.find(f"/*\nTAG: {tag}\n") # TODO: Add suport to space after /* and before/after {tag}
    if inicio_tag == -1:
        return None  # Tag não encontrada

    # Encontra a posição do fechamento da marcação
    fim_tag = texto.find("*/", inicio_tag)
    if fim_tag == -1:
        return None  # Marcação não fechada corretamente

    # Extrai o conteúdo entre a tag e o fechamento
    conteudo_model = texto[inicio_tag + len(f"/*\nTAG: {tag}\n"):fim_tag].strip() # TODO improove this... len(f"/*\nTAG: {tag}\n") looks bad

     # Remove a marcação "MODEL{" e a chave final
    if conteudo_model.startswith("MODEL{"):
        conteudo_model = conteudo_model[len("MODEL{"):].strip()
    if conteudo_model.endswith("}"):
        conteudo_model = conteudo_model[:-1].strip()

    for chave, valor in dicionario.items():
        conteudo_model = conteudo_model.replace('~'+chave+'~', valor) # Substituir as variaveis do snippet

    fim_tag = fim_tag+2
    return(texto[:fim_tag] + '\n' + conteudo_model + texto[fim_tag:])



def hDriver_new (name: str):

    # Prepara as variáveis a serem substituidas
    name = name.lower()
    NAME = name.upper()

    # Preenche o modelo do arquivo publico

    with open(f"{DRV_PATH}/Tools/hDriver_model.h", "r") as file:
        s_HdriverModel_h = file.read()
        s_HdriverModel_h = s_HdriverModel_h.replace('~name~', name)
        s_HdriverModel_h = s_HdriverModel_h.replace('~NAME~', NAME)
        file.close()

    # preenche o modelo do arquivo privado
    with open(f"{DRV_PATH}/Tools/hDriver_model.c", "r") as file:
        s_HdriverModel_c = file.read()
        s_HdriverModel_c = s_HdriverModel_c.replace('~name~', name)
        s_HdriverModel_c = s_HdriverModel_c.replace('~NAME~', NAME)
        file.close()

    # cria a pasta do driver
    if (os.path.isdir(f'{DRV_PATH}/HDRIVERS/{NAME}')):
        print("pasta já existe!")
    else:
        try:
            os.mkdir(f'{DRV_PATH}/HDRIVERS/{NAME}')
        except :
            print("Erro ao criar o diretório: " + f'{DRV_PATH}/HDRIVERS/{NAME}')

    # salva os arquivos criados
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.h', 'w') as f_hdrv_pub:
        f_hdrv_pub.write(s_HdriverModel_h)
        f_hdrv_pub.close()

    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.c', 'w') as f_hdrv_pri:
        f_hdrv_pri.write(s_HdriverModel_c)
        f_hdrv_pri.close()




def lDriver_new (name: str, portname: str):
    # Prepara as variáveis a serem substituidas
    name = name.lower()
    NAME = name.upper()
    portname = portname.lower()
    PORTNAME = portname.upper()

    # Preenche o modelo do arquivo publico

    with open(f"{DRV_PATH}/Tools/lDriver_model.h", "r") as file:
        s_LdriverModel_h = file.read()
        s_LdriverModel_h = s_LdriverModel_h.replace('~name~', name)
        s_LdriverModel_h = s_LdriverModel_h.replace('~NAME~', NAME)
        s_LdriverModel_h = s_LdriverModel_h.replace('~portname~', portname)
        s_LdriverModel_h = s_LdriverModel_h.replace('~PORTNAME~', PORTNAME)
        file.close()

    # preenche o modelo do arquivo privado
    with open(f"{DRV_PATH}/Tools/lDriver_model.c", "r") as file:
        s_LdriverModel_c = file.read()
        s_LdriverModel_c = s_LdriverModel_c.replace('~name~', name)
        s_LdriverModel_c = s_LdriverModel_c.replace('~NAME~', NAME)
        s_LdriverModel_c = s_LdriverModel_c.replace('~portname~', portname)
        s_LdriverModel_c = s_LdriverModel_c.replace('~PORTNAME~', PORTNAME)
        file.close()

    # cria a pasta do driver
    if (os.path.isdir(f'{DRV_PATH}/LDRIVERS/{PORTNAME}')):
        print("pasta já existe!")
    else:
        try:
            os.mkdir(f'{DRV_PATH}/LDRIVERS/{PORTNAME}')
        except :
            print("Erro ao criar o diretório: " + f'{DRV_PATH}/LDRIVERS/{PORTNAME}')

    if (os.path.isdir(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}')):
        print("pasta já existe!")
    else:
        try:
            os.mkdir(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}')
        except :
            print("Erro ao criar o diretório: " + f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}')


    # salva os arquivos criados
    with open(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}/ldrv_{name}.h', 'w') as f_hdrv_pub:
        f_hdrv_pub.write(s_LdriverModel_h)
        f_hdrv_pub.close()

    with open(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}/ldrv_{name}.c', 'w') as f_hdrv_pri:
        f_hdrv_pri.write(s_LdriverModel_c)
        f_hdrv_pri.close()

    # Add snippets to hDriver

    dicionario = {
        "PORTNAME" : PORTNAME
    }


    # - arquivo publico ------------------------------------------------------
    s_HdriverModel_h = ''
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.h', 'r') as f_hdrv_pub:
        s_HdriverModel_h = f_hdrv_pub.read()
        f_hdrv_pub.close()


    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'lDriversUseDefines', dicionario)
    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'lDriversHfiles', dicionario)
    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'lDriversList', dicionario)
    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'lDriverInitArgs', dicionario)

    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.h', 'w') as f_hdrv_pub:
        #save file
        f_hdrv_pub.write(s_HdriverModel_h)
        f_hdrv_pub.close()

    # - arquivo privado -------------------------------------------------------
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.c', 'r') as f_hdrv_pri:
        s_HdriverModel_c = f_hdrv_pri.read()
        f_hdrv_pri.close()

    s_HdriverModel_c = add_snippet(s_HdriverModel_c, 'lDriversCfiles', dicionario)
    s_HdriverModel_c = add_snippet(s_HdriverModel_c, 'portInitRoutine', dicionario)

    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.c', 'w') as f_hdrv_pri:
        # save file
        f_hdrv_pri.write(s_HdriverModel_c)
        f_hdrv_pri.close()


def Driver_new (name: str, portnames: list[str]):
    hDriver_new(name)
    for portname in portnames:
        lDriver_new(name, portname)

def get_all_subdirectories(directory_path:str):

    if (directory_path.endswith('/') == False):
        directory_path = directory_path + '/'

    all_subdirs = [x[0].replace(directory_path,'') for x in os.walk(directory_path)]
    return all_subdirs[1:]  # Exclude the root directory itself

def lDriver_addFunction (name:str, portname:str, dicionario: dict):

    name = name.lower()
    NAME = name.upper()
    portname = portname.lower()
    PORTNAME = portname.upper()

    # ================================================================================
    # Drivers baixos

    # Abre os arquivos ---------------------------------------------------------------

    # Arquivo privado

    with open(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}/ldrv_{name}.c', 'r') as f_ldrv_pri:
        s_LdriverModel_c = f_ldrv_pri.read()
        f_ldrv_pri.close()

    # Arquivo publico
    with open(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}/ldrv_{name}.h', 'r') as f_ldrv_pub:
        s_LdriverModel_h = f_ldrv_pub.read()
        f_ldrv_pub.close()

    # Insere os snippets ------------------------------------------------------------

    # arquivo privado
    s_LdriverModel_c = add_snippet(s_LdriverModel_c, 'lDrvFunctionsPrototypes', dicionario)
    s_LdriverModel_c = add_snippet(s_LdriverModel_c, 'lDrvPortInitialization', dicionario)
    s_LdriverModel_c = add_snippet(s_LdriverModel_c, 'ldrvPublicFunctions', dicionario)

    # arquivo publico
    # NONE YET

    # Salva os arquivos ------------------------------------------------------------

    # Arquivo privado
    with open(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}/ldrv_{name}.c', 'w') as f_ldrv_pri:
        # save file
        f_ldrv_pri.write(s_LdriverModel_c)
        f_ldrv_pri.close()

    # Arquivo publico
    with open(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}/ldrv_{name}.h', 'w') as f_ldrv_pub:
        #save file
        f_ldrv_pub.write(s_LdriverModel_h)
        f_ldrv_pub.close()

    return


import re
def separar_tipos_e_nomes(argumentos_c):
    # Divide a string de entrada em argumentos individuais
    argumentos = re.split(r',\s*', argumentos_c)

    nomes = ''
    for arg in argumentos:
        # Separa o tipo e o nome usando espaços
        partes = arg.split()
        if len(partes) >= 2:
            nomes = nomes + ', ' + partes[-1]

    return nomes


def Driver_addFunction (name:str, returnType:str, fnName:str, fnArgsWithTypes:str = '' ):

    name = name.lower()
    NAME = name.upper()

    args = separar_tipos_e_nomes(fnArgsWithTypes)
    # ================================================================================
    # Valida os argumentos e retornos
    # TODO

    # ================================================================================
    # Drivers altos

    # Abre os arquivos ---------------------------------------------------------------

    # Arquivo privado
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.c', 'r') as f_hdrv_pri:
        s_HdriverModel_c = f_hdrv_pri.read()
        f_hdrv_pri.close()

    # Arquivo publico
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.h', 'r') as f_hdrv_pub:
        s_HdriverModel_h = f_hdrv_pub.read()
        f_hdrv_pub.close()

    # Insere os snippets ------------------------------------------------------------

    dicionario = {
        'name' : name,
        'fnName' : fnName,
        'argsWithTipes' : fnArgsWithTypes,
        'args' : args,
        'returnType' : returnType,
    }

    # arquivo privado
    s_HdriverModel_c = add_snippet(s_HdriverModel_c, 'hdrvPublicFunctions', dicionario)

    # arquivo publico
    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'FunctionTypes', dicionario)
    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'FunctionList', dicionario)
    s_HdriverModel_h = add_snippet(s_HdriverModel_h, 'hDrvFunctionsPrototypes', dicionario)

    # Salva os arquivos ------------------------------------------------------------

    # Arquivo privado
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.c', 'w') as f_hdrv_pri:
        # save file
        f_hdrv_pri.write(s_HdriverModel_c)
        f_hdrv_pri.close()

    # Arquivo publico
    with open(f'{DRV_PATH}/HDRIVERS/{NAME}/hdrv_{name}.h', 'w') as f_hdrv_pub:
        #save file
        f_hdrv_pub.write(s_HdriverModel_h)
        f_hdrv_pub.close()

    # - Drivers baixos, todos
    PORTNAMES = get_all_subdirectories(f'{DRV_PATH}/LDRIVERS/')
    for PORTNAME in PORTNAMES:
        if (os.path.isdir(f'{DRV_PATH}/LDRIVERS/{PORTNAME}/{NAME}')):
            lDriver_addFunction(name, PORTNAME, dicionario)

    return




import subprocess


def saveUserData ():
    # check if git exists
    proc = subprocess.Popen(["git", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err != b'':
        print(err)
        print ('ABORT')
        exit(1)
    # check if is a git repository
    if os.path.isdir('.git') == False :
        print ('Not a git repository')
        print ('ABORT')
        exit(1)
    # checkout to branch - generate
    proc = subprocess.Popen(["git", "checkout", "Generate"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if 'error' in err.decode() :
        print(err)
        print ('ABORT')
        exit(1)


def registerChanges (msg :str):
    # add files to stage
    proc = subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err != b'':
        print(err)
        print ('ABORT')
        exit(1)
    # commit files
    proc = subprocess.Popen(["git", "commit", '-m', '\"'+msg+'\"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err != b'':
        print(err)
        print ('ABORT')
        exit(1)


def restoreUserData ():
    # checkout to branch - User
    proc = subprocess.Popen(["git", "checkout", "User"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if 'error' in err.decode() :
        print(err)
        print ('ABORT')
        exit(1)
    # merge changes
    proc = subprocess.Popen(["git", "merge", "Generate"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err != b'':
        print(err)
        print ('ABORT')
        exit(1)



import shutil



# Serão utilizados dois branches de edição:
#   1. User
#   2. Generated
# Será utilizado o branch master para o release dos drivers
#
# O script roda no breanch 'Generated' e o usuário realiza as suas alterações no branch 'User'
# Se o script tiver que gerar novamente:
# 1. O código corrente no branch user deve ser commitado
# 2. Faz-se o checkout para o branch 'Generated'
# 3. Realizam-se as modificações
# 4. Adiciona e commita as novas alterações
# 5. Faz-se o checkout para o branch 'User'
# 6. Faze-se o merge 'git merge Generated'
if __name__ == "__main__":

    saveUserData()
    
    # cria a pasta do driver
    if (os.path.isdir(f'{DRV_PATH}/LDRIVERS')):
        print("pasta já existe!")
        print("Apagando o conteudo da pasta...")
        shutil.rmtree(f'{DRV_PATH}/LDRIVERS')
    try:
        os.mkdir(f'{DRV_PATH}/LDRIVERS')
    except :
        print("Erro ao criar o diretório: " + f'{DRV_PATH}/LDRIVERS')
    

    if (os.path.isdir(f'{DRV_PATH}/HDRIVERS')):
        print("pasta já existe!")
        print("Apagando o conteudo da pasta...")
        shutil.rmtree(f'{DRV_PATH}/HDRIVERS')
    try:
        os.mkdir(f'{DRV_PATH}/HDRIVERS')
    except :
        print("Erro ao criar o diretório: " + f'{DRV_PATH}/HDRIVERS')



    # ====================================================================
    # Driver para acesso a servomotores
    Driver_new('servomotor', ['sg90'])
    Driver_addFunction('servomotor', 'void', 'set_angle', 'int angle')
    Driver_addFunction('servomotor', 'int', 'get_angle')
    Driver_addFunction('servomotor', 'void', 'release')

    # ====================================================================
    # Driver para acesso a geração de sinais PWM
    Driver_new('pwm', ['esp32'])
    Driver_addFunction('pwm', 'void', 'set_duty', 'int duty')

    # ====================================================================
    # Driver para comunicação serial
    Driver_new('serial', ['esp32'])
    Driver_addFunction('serial', 'void', 'write', 'uint8_t *data, size_t length')
    Driver_addFunction('serial', 'void', 'add_callback_OnReceive', 'onReceive_callback_t px_function')

    # ====================================================================
    # Driver para log de mensagens
    Driver_new('log', ['esp32'])
    Driver_addFunction('log', 'void', 'msg_debug', 'const char* msg')
    Driver_addFunction('log', 'void', 'msg_info', 'const char* msg')
    Driver_addFunction('log', 'void', 'msg_warning', 'const char* msg')
    Driver_addFunction('log', 'void', 'msg_error', 'const char* msg')
    Driver_addFunction('log', 'void', 'int_debug', 'const char* msg')
    Driver_addFunction('log', 'void', 'int_info', 'const char* msg')
    Driver_addFunction('log', 'void', 'int_warning', 'const char* msg')
    Driver_addFunction('log', 'void', 'int_error', 'const char* msg')
    Driver_addFunction('log', 'void', 'set_level', 'hDrv_log_level_t level')
    Driver_addFunction('log', 'hDrv_log_level_t', 'get_levet')

    # ====================================================================
    # Driver para execução de loop PID
    Driver_new('pid', ['pid_float'])
    Driver_addFunction('pid', 'float', 'compute', 'float input')
    Driver_addFunction('pid', 'float', 'get_lastOutput')
    Driver_addFunction('pid', 'void', 'set_input', 'float input')
    Driver_addFunction('pid', 'void', 'set_kp', 'float kp')
    Driver_addFunction('pid', 'void', 'set_ki', 'float ki')
    Driver_addFunction('pid', 'void', 'set_kd', 'float kd')
    Driver_addFunction('pid', 'void', 'pause')
    Driver_addFunction('pid', 'void', 'resume')

    registerChanges("Gerado")
    restoreUserData()

    print ('Pronto!')
