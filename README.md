# Inteligencia-Artificial

Membros
Vitor Soares Salzman - 20161bsi0403
Luiz Antonio Roque Guzzo - 20151bsi0193


Relatório - Implementação do A*

Especificação
Nesse relatório, vamos explicar o conceito do algoritmo de busca A*, bem como uma implementação detalhada, e seus resultados
Conceito
Esse algoritmo é a combinação de aproximações heurísticas, como do algoritmo de busca em largura e do algoritmo de Dijkstra (1959). O algoritmo de Dijkstra basicamente visava solucionar os problemas de caminho mais curto.  A principal diferença entre ele e o algoritmo A* é a ausência de uma função heurística que facilite e diminua o número de nós expandidos, pois a cada passo o algoritmo de  Dijkstra verificaria os nós adjacentes para efetuar a avaliação, sem se importar com uma ordem ou priorização dos ramos, o que acontece no algoritmo A* devido a utilização da função heurística determinada pelo problema. Hoje em dia,  já existem muitas outras variantes do algoritmo A* proposto originalmente. Ele avalia os nós através da combinação de g(n) que é o custo para alcançar cada nó com a função h(n) que é o menor custo partindo da origem para se chegar ao destino, matematicamente dado na equação 1:
f(n) = g(n) + h(n) (1)
Desse modo f(n) é, portanto, o custo estimado da solução de custo mais baixo passando por n. Esta técnica requer que a estimação do custo restante no próximo nó não seja nunca maior que o custo restante do nó anterior. Diferente do Dijkstra,  sob esta hipótese, sempre é possível encontrar a solução ótima com a busca A*
Problema 
O problema proposto é o caminho descrito na figura a seguir, onde um objeto precisa caminhar verticalmente/horizontalmente do ponto inicial, até o ponto final, sem que este colida com os obstáculos(em preto). O algoritmo deve ser capaz de definir o melhor caminho, de acordo com a heurística recebida.

Implementação
O código completo encontra-se em https://github.com/VitorSalzman/Inteligencia-Artificial. 

Resultados

Referências bibliográficas
http://pointclouds.org/documentation/tutorials/kdtree_search.php#kdtree-search
http://repositorio.roca.utfpr.edu.br/jspui/bitstream/1/10221/1/PG_COELE_2018_1_03.pdf
https://github.com/felipemartinsss/RepositorioIAsc/tree/master/Python/buscas
