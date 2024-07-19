#
# - Driver Abstraction Layer Wizzard
#


import argparse

parser = argparse.ArgumentParser(
    description='''
    Wizzard para criar e alterar bibliotecas DAL - Driver Abstraction Layer
    ''',
    epilog='''
    DESCREVER

    - Essa ferramenta utiliza GIT para manter as alterações de usuário
    '''
    
    )


# parser.add_argument('-d',
#                     '--driver', 
#                     metavar='driver', 
#                     type=str, 
#                     nargs='+',
#                     help='nome(s) do(s) drivers(s) a ser(em) desenvolvidos(s)'
#                     )

# parser.add_argument('-p', 
#                     '--portlist', 
#                     metavar='PortList', 
#                     type=str, 
#                     nargs='+',
#                     help='nome(s) do(s) ports(s) a ser(em) desenvolvidos(s)'
#                     )

# parser.add_argument('-f', 
#                     '--function',
#                     metavar='function', 
#                     type=str, 
#                     nargs='+',
#                     help='nome(s) do(s) drivers(s) a ser(em) desenvolvidos(s)'
#                     )

# parser.add_argument('--function',
#                     metavar='PortList', 
#                     type=str, 
#                     nargs='+',
#                     help='nome(s) do(s) drivers(s) a ser(em) desenvolvidos(s)'
#                     )


# args = parser.parse_args()


print(f'''                                                        
  _____  _                __          ___                      _  
 |  __ \\| |        /\\     \\ \\        / (_)                    | | 
 | |  | | |       /  \\     \\ \\  /\\  / / _ __________ _ _ __ __| | 
 | |  | | |      / /\\ \\     \\ \\/  \\/ / | |_  |_  / _` | '__/ _` | 
 | |__| | |____ / ____ \\     \\  /\\  /  | |/ / / | (_| | | | (_| | 
 |_____/|______/_/    \\_\\     \\/  \\/   |_/___/___\\__,_|_|  \\__,_| 
        
------------------------------------------------------------------  
''')

import Tools.tools as tools

def add_function (driver:str = ' ', fnReturnType:str=' ', fnName:str = ' ', fnArgs:str = ' ', port:list[str] = [' ']):

    # captura apenas a primeira palavra de cada argumento
    driver          = driver.split()[0]
    fnReturnType    = driver.split()[0]
    fnName          = fnName.split()[0]
    fnArgs          = fnArgs.split(',')

    # captura as entradas do usuário (se necessário)
    if (driver == ' '):
        driver = str(input('Digite o nome do driver: '))
    
    if (fnName == ' '):
        fnName = str(input('Digite o nome da função: '))

    if (fnArgs.count() == 0):
        fnArgs = str(input('Digite os argumentos da função "<tipo> <nome>,": '))

    if (port.count() == 0):
        fnArgs = str(input('Digite os ports a serem incluidos: '))

    #TODO check if driver exists
    #TODO Valida os argumentos
    #TODO Cria a função

    tools.Driver_addFunction(driver, fnReturnType, fnName, fnArgs)


print("go")
parser.add_argument('-f',
                    '--add_function',
                    action='store_true'
                    )


args = parser.parse_args()

if(args.add_function == True):
    add_function()

