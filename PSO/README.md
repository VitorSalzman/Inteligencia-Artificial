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
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/1_Formulas.png"> 
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/2_Fittness.png">
<br><br>


### Implementação<br>
O código foi subdividido em área global, estrutura de dados e funções gerais.<br>

A estrutura de dados <b>Particle</b>, armazena em seu interior, a posição X e Y da partícula(de imediato, é setado um valor aleatório dentro do escopo do trabalho), o valor e posição do pbest da partícula, e o vetor de velocidade. A função <b>move</b> desloca a partícula de acordo com o valor da velocidade.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/1_cod.PNG"> <br><br>

A função <b>fitness</b> calcula a função do escopo do problema, para os valores x e y.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/2_cod.PNG"> <br><br>

As funções <b>set_pbest e set_gbest</b> realizam o cálculo do pbest e gbest, de acordo com o andamento do algoritmo.<br> <img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/3_cod.PNG"> <br><br>

A função <b>move_particles</b> realiza o cálculo da velocidade, por partes, e no fim, chama a função da partícula, para movimentá-la(quando a velocidade ultrapassa o escopo definido(15% de 512), o valor é definido para o limite do escopo(77 ou -77).<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/4_cod.PNG"> <br><br>

O loop a seguir, é o loop principal, que só terminará a execução quando o número de interações definidas for atingida. Dentro do loop, o W é calculado a cada interação.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/5_cod.PNG"> <br><br>


O código completo encontra-se em https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/PSO/PSO.py. <br>

   

### Resultados<br>

Foram feitas 10 execuções do programa, para cada parâmetro utilizado, explicado a seguir:<br>
<li> 20 interações, com 50 partículas;</li>
<li> 20 interações, com 100 partículas;</li>
<li> 50 interações, com 50 partículas;</li>
<li> 50 interações, com 100 partículas;</li>
<li> 100 interações, com 50 partículas;</li>
<li> 100 interações, com 100 partículas;</li>

Para 20 interações, e 50 partículas, a média resultante foi: <b>-893,7514203188810</b>. Os detalhes estão na tabela a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/20_50.PNG"> <br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/graph_20_50.png"> <br>




Para 20 interações, e 100 partículas, a média resultante teve o <b> melhor resultado</b>, que foi: <b>-927,1075347559100</b>. Os detalhes estão na tabela a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/20_100.PNG"> <br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/graph_20_100.png"> <br><br>

Para 50 interações, e 50 partículas, a média resultante foi: <b>-786,5252680885200</b>. Os detalhes estão na tabela a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/50_50.PNG"> <br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/graph_50_50.png"> <br>

Para 50 interações, e 100 partículas, a média resultante teve o <b>pior resultado</b>, que foi: <b>-786,5254143025010</b>. Os detalhes estão na tabela a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/50_100.PNG"> <br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/graph_50_100.png"> <br>

Para 100 interações, e 50 partículas, a média resultante foi: <b>-891,7640119973470</b>. Os detalhes estão na tabela a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/100_50.PNG"> <br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/graph_100_50.png"> <br>

Para 100 interações, e 100 partículas, a média resultante foi: <b>-857,8876806216580</b>. Os detalhes estão na tabela a seguir.<br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/100_100.PNG"> <br><br>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/graph_100_100.png"> <br>

<b>Por fim, conclui-se que o algoritmo PSO, executado para vinte interações, produziu os melhores resultados(Sendo destes, obteve-se melhora ainda maior com 100 partículas), enquanto a execução do algoritmo para 50 interações, produziu os piores resultados(Sendo destes, obteve-se valores ainda menores com 100 partículas). Os resultados voltaram a crescer, com a execução em 100 interações.</b>
<img src="https://github.com/VitorSalzman/Inteligencia-Artificial/blob/master/PSO/Imagens/modelo_3d.jfif"> <br>





### Referências bibliográficas<br>
<li>http://pointclouds.org/documentation/tutorials/kdtree_search.php#kdtree-search</li><br>
<li>http://repositorio.roca.utfpr.edu.br/jspui/bitstream/1/10221/1/PG_COELE_2018_1_03.pdf</li><br>
<li>https://github.com/felipemartinsss/RepositorioIAsc/tree/master/Python/buscas</li><br>


Link do grafico 3D:
https://www.monroecc.edu/faculty/paulseeburger/calcnsf/CalcPlot3D/?type=z;z=-(y+47)sen(sqrt(abs((x)/(2)+y+47)))-x*sen(sqrt(abs(x-(y+47))));visible=true;umin=-512;umax=512;vmin=-512;vmax=512;grid=30;format=normal;alpha=-1;constcol=rgb(255,0,0);view=0;contourcolor=red;fixdomain=false&type=point;point=(512,404,-959);visible=true;color=rgb(255,0,0);size=4&type=point;point=(-457,-382,-786);visible=true;color=rgb(0,0,0);size=4&type=point;point=(283,-487,-718);visible=true;color=rgb(0,0,0);size=4&type=point;point=(347,499,-888);visible=true;color=rgb(0,0,0);size=4&type=point;point=(-465,385,-894);visible=true;color=rgb(0,0,0);size=4&type=point;point=(465,385,-894);visible=true;color=rgb(255,153,0);size=4&type=point;point=(-456,-382,-786);visible=true;color=rgb(0,0,0);size=4&type=point;point=(-456,382,-786);visible=true;color=rgb(0,0,0);size=4&type=window;hsrmode=0;nomidpts=false;anaglyph=-1;center=-3.4882998285241524,8.355103812971555,4.2454687115529115,1;focus=0,0,0,1;up=0.4540262477877348,-0.24563377062836095,0.856460283402963,1;transparent=true;alpha=140;twoviews=false;unlinkviews=false;axisextension=0.7;xaxislabel=x;yaxislabel=y;zaxislabel=z;edgeson=true;faceson=true;showbox=true;showaxes=true;showticks=true;perspective=true;centerxpercent=0.4596357371400438;centerypercent=0.439485627836611;rotationsteps=30;autospin=true;xygrid=false;yzgrid=false;xzgrid=false;gridsonbox=false;gridplanes=false;gridcolor=rgb(128,128,128);xmin=-512;xmax=512;ymin=-512;ymax=512;zmin=-512;zmax=512;xscale=256;yscale=256;zscale=256;zcmin=-1024;zcmax=1024;zoom=0.002328;xscalefactor=1;yscalefactor=1;zscalefactor=1
