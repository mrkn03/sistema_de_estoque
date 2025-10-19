from model.movimentacoes import Movimentacao
from conexion.oracle_queries import OracleQueries
from datetime import datetime

class Controller_Movimentacao:
    def __init__(self):
        pass

    def registrar_entrada(self) -> Movimentacao:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo = oracle.sqlToDataFrame("select nvl(max(codigo), 0) + 1 as codigo from movimentacoes")["codigo"].values[0]
        codigo_produto = int(input("Código do Produto: "))
        quantidade = float(input("Quantidade: "))
        cnpj_fornecedor = input("CNPJ do Fornecedor: ")
        numero_nota = input("Número da Nota: ")
        motivo = input("Motivo: ")
        
        oracle.write(f"""insert into movimentacoes values 
                    ({codigo}, {codigo_produto}, 'E', {quantidade}, 
                    TO_DATE('{datetime.now().strftime("%d/%m/%Y")}', 'DD/MM/YYYY'),
                    '{cnpj_fornecedor}', '{motivo}', '{numero_nota}')""")
        
        oracle.write(f"""update produtos set 
                    quantidade_atual = quantidade_atual + {quantidade},
                    data_ultima_movimentacao = TO_DATE('{datetime.now().strftime("%d/%m/%Y")}', 'DD/MM/YYYY')
                    where codigo = {codigo_produto}""")
        
        df_movimentacao = oracle.sqlToDataFrame(f"select * from movimentacoes where codigo = {codigo}")
        nova_movimentacao = Movimentacao(df_movimentacao.codigo.values[0], 
                                       df_movimentacao.codigo_produto.values[0],
                                       df_movimentacao.tipo.values[0],
                                       df_movimentacao.quantidade.values[0],
                                       df_movimentacao.data.values[0],
                                       df_movimentacao.cnpj_fornecedor.values[0],
                                       df_movimentacao.motivo.values[0],
                                       df_movimentacao.numero_nota.values[0])
        print(nova_movimentacao.to_string())
        return nova_movimentacao

    def registrar_saida(self) -> Movimentacao:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo = oracle.sqlToDataFrame("select nvl(max(codigo), 0) + 1 as codigo from movimentacoes")["codigo"].values[0]
        codigo_produto = int(input("Código do Produto: "))
        quantidade = float(input("Quantidade: "))
        motivo = input("Motivo: ")
        
        # Verificar se há quantidade suficiente
        qtd_atual = oracle.sqlToDataFrame(f"select quantidade_atual from produtos where codigo = {codigo_produto}")["quantidade_atual"].values[0]
        if qtd_atual < quantidade:
            print(f"Quantidade insuficiente. Disponível: {qtd_atual}")
            return None
        
        oracle.write(f"""insert into movimentacoes values 
                    ({codigo}, {codigo_produto}, 'S', {quantidade}, 
                    TO_DATE('{datetime.now().strftime("%d/%m/%Y")}', 'DD/MM/YYYY'),
                    NULL, '{motivo}', NULL)""")
        
        oracle.write(f"""update produtos set 
                    quantidade_atual = quantidade_atual - {quantidade},
                    data_ultima_movimentacao = TO_DATE('{datetime.now().strftime("%d/%m/%Y")}', 'DD/MM/YYYY')
                    where codigo = {codigo_produto}""")
        
        df_movimentacao = oracle.sqlToDataFrame(f"select * from movimentacoes where codigo = {codigo}")
        nova_movimentacao = Movimentacao(df_movimentacao.codigo.values[0], 
                                       df_movimentacao.codigo_produto.values[0],
                                       df_movimentacao.tipo.values[0],
                                       df_movimentacao.quantidade.values[0],
                                       df_movimentacao.data.values[0],
                                       df_movimentacao.cnpj_fornecedor.values[0],
                                       df_movimentacao.motivo.values[0],
                                       df_movimentacao.numero_nota.values[0])
        print(nova_movimentacao.to_string())
        return nova_movimentacao