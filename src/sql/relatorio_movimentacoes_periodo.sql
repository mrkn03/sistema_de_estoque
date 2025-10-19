select m.data as "Data"
     , p.descricao_produto as "Produto"
     , m.tipo as "Tipo"
     , m.quantidade as "Quantidade"
     , f.nome_fantasia as "Fornecedor"
     , m.motivo as "Motivo"
     , m.numero_nota as "Nota"
  from movimentacoes m
     , produtos p
     , fornecedores f
 where m.codigo_produto = p.codigo
   and m.cnpj_fornecedor = f.cnpj (+)
   and m.data between to_date('&data_inicial', 'DD/MM/YYYY')
                  and to_date('&data_final', 'DD/MM/YYYY')
 order by m.data desc;