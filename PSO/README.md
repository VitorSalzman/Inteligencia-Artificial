# Inteligencia Artificial

#### <font color="green"> Membros </font><br>
Vitor Soares Salzman - 20161bsi0403 - vitor-salzman96@hotmail.com<br>
Luiz Antonio Roque Guzzo - 20151bsi0193 - luizguzzo@gmail.com<br>


## Relatório - Implementação do A*<br>

### Especificação<br>
Nesse relatório, vamos explicar o conceito do algoritmo de busca A*, bem como uma implementação detalhada, e seus resultados<br>

### Conceito<br>
Esse algoritmo é a combinação de aproximações heurísticas, como do algoritmo de busca em largura e do algoritmo de Dijkstra (1959). O algoritmo de Dijkstra basicamente visava solucionar os problemas de caminho mais curto.  A principal diferença entre ele e o algoritmo A* é a ausência de uma função heurística que facilite e diminua o número de nós expandidos, pois a cada passo o algoritmo de  Dijkstra verificaria os nós adjacentes para efetuar a avaliação, sem se importar com uma ordem ou priorização dos ramos, o que acontece no algoritmo A* devido a utilização da função heurística determinada pelo problema. Hoje em dia,  já existem muitas outras variantes do algoritmo A* proposto originalmente. Ele avalia os nós através da combinação de g(n) que é o custo para alcançar cada nó com a função h(n) que é o menor custo partindo da origem para se chegar ao destino, matematicamente dado na equação 1:<br>

<b> f(n) = g(n) + h(n) (1) </b><br>

Desse modo f(n) é, portanto, o custo estimado da solução de custo mais baixo passando por n. Esta técnica requer que a estimação do custo restante no próximo nó não seja nunca maior que o custo restante do nó anterior. Diferente do Dijkstra,  sob esta hipótese, sempre é possível encontrar a solução ótima com a busca A*.<br>

### Problema  <br>

O problema proposto é o caminho descrito na figura a seguir, onde um objeto precisa caminhar verticalmente/horizontalmente do ponto inicial, até o ponto final, sem que este colida com os obstáculos(em preto). O algoritmo deve ser capaz de definir o melhor caminho, de acordo com a heurística recebida.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/ProblemaProposto.PNG"> <br><br>

### Implementação<br>
O trecho a seguir, recebe parâmetros de linha e coluna e, de acordo com o estado representado, calcula os estados sucessores com peso 1 à frente.<br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/EncontraEstadosSucessores.PNG"> <br><br>

A função "verificaObstaculo" retorna <b>True</b>, caso as dimensões passadas por parâmetro sejam válidas(valor de linha e coluna devem pertencer ao tamanho da Matriz, além de não coincidirem com algum obstáculo). Caso contrário, retorna <b>False</b><br>

<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/EncontraEstadosSucessores.PNG"> <br><br>

Este trecho calcula o peso da distância de um estado, até o estado final, ou seja, o objetivo.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/CalculaDistanciaMeta.png"><br><br>

De acordo com a "margem"(estados que contornam o estado atual) e a heurística(h=f+g), calcula-se o estado mais promissor.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/EncontraEstadoPromissor.png"><br><br>

Esse loop controla todas as iterações do código. A cada tentativa de caminho, uma iteração é adicionada.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/Tentativas.png"><br><br>

O código completo encontra-se em https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/busca_a/busca_a.py. <br>

   

### Resultados<br>
O mapa do problema, apresenta uma matriz 10x10, representado por <b>zeros e um's</b>, sendo 0 como <b>estado livre</b>, e 1 como <b>Obstáculo</b>. A seguir, um teste realizado com a posição inicial de 0,0, e a posição final 8,8, tendo início em <b>S</b>, e fim em <b>E</b>.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/caminhoPadraoTracejado.png"><br><br>

Parametrizando o código, foi testado com a posição inicial em 0,9, e a final em 9,0:<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/caminhoParametrizadoTracejado.png"><br><br>

Testamos com dimensões que extrapolam o domínio do problema:<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/DimensoesIncorretas.png"><br><br>

Testamos, também, com dimensões que colidem com obstáculos no mapa:<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/Colisao.png"><br><br>

### Referências bibliográficas<br>
<li>http://pointclouds.org/documentation/tutorials/kdtree_search.php#kdtree-search</li><br>
<li>http://repositorio.roca.utfpr.edu.br/jspui/bitstream/1/10221/1/PG_COELE_2018_1_03.pdf</li><br>
<li>https://github.com/felipemartinsss/RepositorioIAsc/tree/master/Python/buscas</li><br>
