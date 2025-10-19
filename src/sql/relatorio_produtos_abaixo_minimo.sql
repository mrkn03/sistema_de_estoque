select p.codigo as "Código"
     , p.descricao_produto as "Produto"
     , p.quantidade_atual as "Qtd Atual"
     , p.quantidade_minima as "Qtd Mínima"
     , c.nome as "Categoria"
     , l.nome as "Localização"
  from produtos p
     , categorias c
     , localizacoes l
 where p.codigo_categoria = c.codigo
   and p.codigo_localizacao = l.codigo
   and p.quantidade_atual <= p.quantidade_minima
 order by p.quantidade_atual;