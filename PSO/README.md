# Inteligencia Artificial

#### <font color="green"> Membros </font><br>
Vitor Soares Salzman - 20161bsi0403 - vitor-salzman96@hotmail.com<br>
Luiz Antonio Roque Guzzo - 20151bsi0193 - luizguzzo@gmail.com<br>


## Relatório - Implementação do PSO<br>

### Especificação<br>
Nesse relatório, vamos explicar o conceito do algoritmo de otimização por enxame de partículas, o PSO, bem como uma implementação detalhada, e seus resultados<br>

### Conceito<br>
A otimização por enxame de partículas é outro algoritmo que foi criado com base em comportamentos da natureza. Esse algoritmo é baseado em uma estratégia inspirada no voo dos pássaros e movimento de cardumes de peixes. Permite a otimização global de uma função, utilizando um chamado "enxame de partículas". A movimentação dessas partículas é feito dentro do escopo do problema. Dentro de sua estratégia, as "N" partículas se movimentam da seguinte forma: <br>
<li> Cada partícula é um ponto mapeado, pertencente ao escopo do caso; </li>
<li> Cada partícula representa uma solução potencial; </li>
<li> De forma a obedecer uma função objetivo, e a uma velocidade calculada.</li><br>
As fórmulas para a velocidade e o deslocamento são as seguintes: (inserir link da imagem)<br>



### Problema  <br>

O problema proposto é a otimização por enxame de partículas, de uma função fitness, descrita a seguir, como a função Eggholder, que é uma função clássica na condução de testes para otimização de funções.<br>
(inserir a imagem 2 aqui) <br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/imagens/ProblemaProposto.PNG"> <br><br>

### Implementação<br>
Foram feitas 10 execuções do programa, para cada parâmetro utilizado, explicado a seguir:<br>
<li> 20 interações, com 50 partículas;</li>
<li> 20 interações, com 100 partículas;</li>
<li> 50 interações, com 50 partículas;</li>
<li> 50 interações, com 100 partículas;</li>
<li> 100 interações, com 50 partículas;</li>
<li> 100 interações, com 100 partículas;</li>

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
