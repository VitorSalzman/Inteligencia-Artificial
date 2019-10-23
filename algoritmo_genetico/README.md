# Inteligencia Artificial

#### <font color="green"> Membros </font><br>
Vitor Soares Salzman - 20161bsi0403 - vitor-salzman96@hotmail.com<br>
Luiz Antonio Roque Guzzo - 20151bsi0193 - luizguzzo@gmail.com<br>


## Relatório - Implementação do Algoritmo Genético<br>

### Especificação<br>
Nesse relatório, vamos explicar o conceito do algoritmo genético, bem como uma implementação detalhada, e seus resultados<br>

### Conceito<br>
O algoritmo genético está relacionado com um dos ramos de pesquisa emergente da Inteligência Artificial, a Computação Evolucionária(CE), que propõe um novo paradigma para solução de problemas inspirado na Seleção Natural, de Darwin.<br>
Criado em 1960 por John Holland, o algoritmo tinha o objetivo inicial de estudar os fenômenos relacionados à adaptação das espécies e da seleção natural que ocorre na natureza, propondo novas soluções para o conceito computacional. Os requisitos para execução desse algoritmo são resumidos nos passos a seguir:
<li>Inicialmente escolhe-se uma população inicial, normalmente formada por indivíduos criados aleatoriamente;</li><br>
<li>Avalia-se toda a população de indivíduos segundo algum critério, determinado por uma função que avalia a qualidade do indivíduo (função de aptidão ou"fitness");</li><br>
<li>Em seguida, através do operador de "seleção", escolhem-se os indivíduos demelhor valor (dado pela função de aptidão) como base para a criação de um novo conjunto de possíveis soluções, chamado de nova "geração";</li><br>
<li>Esta nova geração é obtida aplicando-se sobre os indivíduos selecionadosoperações que misturem suas características (chamadas "genes"), através dos operadores de "cruzamento" ("crossover") e "mutação";</li><br>
<li>Esta nova geração é obtida aplicando-se sobre os indivíduos selecionadosoperações que misturem suas características (chamadas "genes"), através dos operadores de "cruzamento" ("crossover") e "mutação";</li><br>
#######################PAREI AQUI
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
