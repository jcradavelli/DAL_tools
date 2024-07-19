#
# - Generic code recype interpreter
#


import argparse

parser = argparse.ArgumentParser(
    description='''
    Compila um arquivo em linguagem GCR - Generic code recipe
    ''',
    epilog='''
    Esse script tem o objetivo de substituir 
    '''
    
    )


parser.add_argument('Snippets', 
                    metavar='Snippets', 
                    type=str, 
                    nargs='+',
                    help='nome(s) do(s) snippets(s) a ser(em) processados(s)'
                    )

parser.add_argument(
                    '-f',
                    '--files', 
                    type=str, 
                    nargs='+',
                    help='Arquivos a serem compilados'
                    )

parser.add_argument(
                    '-t',
                    '--tags', 
                    type=str, 
                    nargs='+',
                    help='Tags a serem substituidas'
                    )

parser.add_argument(
                    '-v',
                    '--values', 
                    type=str, 
                    nargs='+',
                    help='Valores a serem substituidos'
                    )

parser.add_argument(
                    'out', 
                    type=str, 
                    nargs='+',
                    help='Arquivos de saída'
                    )

args = parser.parse_args()


print('Arquivos compilados: ',args.files)
print('Snippets processados: ', args.Snippets)
print('Tags informadas: ', args.tags)
print('Valores informados: ', args.values)
print('Arquivos de saida: ', args.out)
