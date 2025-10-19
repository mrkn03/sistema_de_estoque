select p.codigo as "Código"
     , p.descricao_produto as "Produto"
     , c.nome as "Categoria"
     , l.nome as "Localização"
     , p.quantidade_atual as "Qtd Atual"
     , p.quantidade_minima as "Qtd Mínima"
     , p.quantidade_maxima as "Qtd Máxima"
     , p.preco_custo as "Preço Custo"
     , p.preco_venda as "Preço Venda"
     , p.data_ultima_movimentacao as "Última Movimentação"
  from produtos p
     , categorias c
     , localizacoes l
 where p.codigo_categoria = c.codigo
   and p.codigo_localizacao = l.codigo
 order by p.descricao_produto;