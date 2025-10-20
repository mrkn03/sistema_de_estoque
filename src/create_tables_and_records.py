from conexion.oracle_queries import OracleQueries

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)            

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Successfully executed")

def drop_tables():
    oracle = OracleQueries(can_write=True)
    oracle.connect()
    
    tables = ["MOVIMENTACOES", "PRODUTOS", "CATEGORIAS", "LOCALIZACOES", "FORNECEDORES"]
    
    for table in tables:
        try:
            oracle.executeDDL(f"DROP TABLE LABDATABASE.{table}")
            print(f"Tabela {table} removida com sucesso!")
        except Exception as e:
            if "ORA-00942" in str(e):  # Tabela não existe
                print(f"Tabela {table} não existia.")
            else:
                print(f"Erro ao remover tabela {table}: {str(e)}")

def run():
    # Remover tabelas existentes
    print("Removendo tabelas existentes...")
    drop_tables()
    print("Processo de remoção concluído!")
    
    # Criar tabelas
    print("Criando tabelas...")
    
    # Criar tabela de Fornecedores (deve ser primeira pois outras dependem dela)
    with open("../sql/create_tables_fornecedores.sql") as f:
        query_create = f.read()
        create_tables(query=query_create)
    print("Tabela de Fornecedores criada!")
    
    # Criar tabela de Categorias
    with open("../sql/create_tables_categorias.sql") as f:
        query_create = f.read()
        create_tables(query=query_create)
    print("Tabela de Categorias criada!")

    # Criar tabela de Localizações
    with open("../sql/create_tables_localizacoes.sql") as f:
        query_create = f.read()
        create_tables(query=query_create)
    print("Tabela de Localizações criada!")

    # Criar tabela de Produtos
    with open("../sql/create_tables_produtos.sql") as f:
        query_create = f.read()
        create_tables(query=query_create)
    print("Tabela de Produtos criada!")

    # Criar tabela de Movimentações
    with open("../sql/create_tables_movimentacoes.sql") as f:
        query_create = f.read()
        create_tables(query=query_create)
    print("Tabela de Movimentações criada!")

    print("Todas as tabelas foram criadas com sucesso!")

    # Inserir dados de exemplo
    print("Inserindo dados de exemplo...")
    with open("../sql/inserting_samples_records.sql") as f:
        query_generate_records = f.read()
        generate_records(query=query_generate_records)
    print("Dados de exemplo inseridos com sucesso!")

if __name__ == '__main__':
    run()