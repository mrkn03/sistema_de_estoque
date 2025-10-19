select c.nome as "Categoria"
     , p.codigo as "Código"
     , p.descricao_produto as "Produto"
     , p.quantidade_atual as "Qtd Atual"
     , l.nome as "Localização"
  from produtos p
     , categorias c
     , localizacoes l
 where p.codigo_categoria = c.codigo
   and p.codigo_localizacao = l.codigo
 order by c.nome, p.descricao_produto;