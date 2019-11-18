# Inteligência Artificial

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
<li>Esta nova geração é obtida aplicando-se sobre os indivíduos selecionados, operações que misturem suas características (chamadas "genes"), através dos operadores de "cruzamento" ("crossover") e "mutação".</li><br>






### Problema  <br>

O problema proposto é a minimização da função abaixo.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/Funcao_Aptidao.PNG"> <br>
A função citada gera um gráfico, que contém alguns mínimos locais, que estarão visíveis na solução. Mas o resultado esperado de um bom algoritmo que resolva tal problema é próximo de <b>-16.7</b>. <br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/grafico_aptidao.PNG"> <br><br>

### Implementação<br>


A aptidão, informada na fórmula citada anteriormente, é calculada no trecho de código abaixo.<br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_aptidao.PNG"> <br><br>

Para representar os cromossomos, a seguinte estrutura de dados foi codificada, guardando um vetor de bits, o valor normalizado e a aptidão.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_cromossomo.PNG"> <br><br>

Para transformar o vetor de bits em um valor normalizado, é necessário o processamento a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_normaliza.PNG"><br><br>

O modo de seleção escolhido para o trabalho foi o Torneio, representado a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_torneio.PNG"><br><br>

Para o crossover, foi definido a porcentagem de <b>80%</b>, o que melhorou consideravelmente o desempenho do código.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_crossOver.PNG"><br><br>

A porcentagem de mutação escolhida foi de <b>1%</b>. Outras porcentagens foram testadas, mas não influenciaram positivamente no desempenho do código.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_mutacao.PNG"><br><br>

Ao realizar as mutações, o melhor cromossomo pai é escolhido para permanecer nas interações. Este substitui o pior cromossomo filho.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/1_elite.PNG"><br><br>

O código completo encontra-se em https://github.com/VitorSalzman/Inteligencia-Artificial/tree/master/algoritmo_genetico/ag. <br>
<br>

Em outra etapa, foram implementados alterações na estrutura do código, a fim de comparação e nova análise. as alterações foram as seguintes:<br>

<li><b>Estrutura do cromossomo:</b></li>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/ag_real_cromossomo.png"><br><br>
<li><b> Estrutura do Crossover</b>, seguindo a fórmula:<br>
   <h4>c= p1 - beta(p2 - p1),</h4><br>
   onde beta=~U(-alfa,1+alfa), U representa uma distribuição uniforme, e alfa=0,5.
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/ag_real_crossover.png"><br>
   <li><b> Estrutura do Crossover</br>, seguindo a fórmula descrita a seguir:</li>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/ag_real_mutation_formula.png"><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/ag_real_mutation.png"><br><br>

O código completo do algoritmo genético com <b>números reais</b> encontra-se em https://github.com/VitorSalzman/Inteligencia-Artificial/tree/master/algoritmo_genetico/ag. <br>
<br>

### Resultados<br>
A cada execução, o código gera uma tabela em csv, que contém os dados de 10 interações, com 10 gerações, e outra tabela(no mesmo arquivo csv) que contém os dados de 10 interações, com 20 gerações. <br>

A seguir está a tabela dos dados referentes a 10 interações com 10 gerações, do código do algoritmo genético com bits na estrutura do cromossomo. A média geral foi de <b>-16,7050761119737</b>.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/print_tab_10_10.png"><br>


Para essa execução, também há um gráfico que mostra a média das execuções, e também a melhor interação. Nota-se que a melhor interação iniciou em um valor acima de -12, até ultrapassar e normalizar na média.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/Grafico_10_10.PNG"><br><br>

Para essa execução, também há um gráfico que mostra a média das execuções, e também a melhor interação do código do algoritmo genético com valores reais na estrutura do cromossomo. A média geral foi de <b>-14,3527508470154</b>.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/tabela_agreal_10_10.png"><br><br>


Na mesma execução, há a tabela que contém os dados referentes a 10 interações com 20 gerações. A média geral foi de <b>-16,850059495935</b>.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/print_tab_10_20.png"><br>

Para essa execução, também há um gráfico que mostra a média das execuções, e também a melhor interação. Nota-se que a melhor interação iniciou em um valor acima de -8, até ultrapassar e normalizar na média.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/Grafico_10_20.pi"><br><br>

Para essa execução, também há um gráfico que mostra a média das execuções, e também a melhor interação do código do algoritmo genético com valores reais na estrutura do cromossomo. A média geral foi de <b>-16,6427465387627</b>. 
<br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/algoritmo_genetico/imagens/tabela_agreal_10_20.png"><br><br>

<b>Por fim, concluímos que a taxa de crossover de 80% melhorou o desempenho do código em até 25%.</b>

### Referências bibliográficas<br>
<li>http://conteudo.icmc.usp.br/pessoas/andre/research/genetic/</li><br>
<li>http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0103-17592008000300006</li><br>
<li>https://github.com/felipemartinsss/RepositorioIAsc/tree/master/Python/buscas</li><br>
