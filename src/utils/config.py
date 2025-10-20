MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Movimentar Estoque
6 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Produtos Abaixo do Mínimo
2 - Produtos por Categoria
3 - Movimentações por Período
4 - Posição Atual do Estoque
5 - Relatório de Produtos
6 - Relatório de Fornecedores
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - PRODUTOS
2 - CATEGORIAS
3 - FORNECEDORES
4 - LOCALIZAÇÕES
5 - MOVIMENTAÇÕES
0 - Voltar
"""

MENU_MOVIMENTACAO = """Movimentação de Estoque
1 - Registrar Entrada
2 - Registrar Saída
0 - Sair
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")