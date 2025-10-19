class Movimentacao:
    def __init__(self,
                 codigo:int=None,
                 codigo_produto:int=None,
                 tipo:str=None,
                 quantidade:float=0,
                 data:str=None,
                 cnpj_fornecedor:str=None,
                 motivo:str=None,
                 numero_nota:str=None
                 ):
        self.codigo = codigo
        self.codigo_produto = codigo_produto
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data
        self.cnpj_fornecedor = cnpj_fornecedor
        self.motivo = motivo
        self.numero_nota = numero_nota

    def to_string(self) -> str:
        return f"Código: {self.codigo} | Produto: {self.codigo_produto} | Tipo: {self.tipo} | Qtd: {self.quantidade}"