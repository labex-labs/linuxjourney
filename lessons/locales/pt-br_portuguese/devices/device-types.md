# tipos de dispositivos

## Conteúdo da lição

Antes de conversarmos sobre como os dispositivos são gerenciados, vamos dar uma olhada em alguns dispositivos.

<pre> $ ls -l / dev
brw-rw ---- 1 disc root 8, 0 20 dez 20:13 sda
crw-rw-rw-  1 root root 1, 3 20 dez 20:13 null
srw-rw-rw-  1 root root 0    20 dez 20:13 log
prw-r - r-- 1 root root 0    20 dez 20:13 fdata
</ pre>

As colunas são as seguintes da esquerda para a direita:

<ul>
<li> Permissões </ li>
<li> Proprietário </ li>
<li> Grupo </ li>
<li> Número principal do dispositivo </ li>
<li> Número de dispositivo secundário </ li>
<li> Timestamp </ li>
<li> Nome do dispositivo </ li>
</ ul>

Lembre-se que no comando ls você pode ver o tipo de arquivo com o primeiro bit em cada linha. Arquivos de dispositivos são indicados como os seguintes:

<ul>
<li> c - caractere </ li>
<li> b - bloco </ li>
<li> p - pipe </ li>
<li> s - soquete </ li>
</ ul>

<b> Dispositivo de caracteres </ b>

Esses dispositivos transferem dados, mas um caractere por vez. Você verá muitos pseudo-dispositivos (/ dev / null) como dispositivos de caracteres, esses dispositivos não estão fisicamente conectados à máquina, mas permitem maior funcionalidade ao sistema operacional.

<b> Dispositivo de bloco </ b>

Esses dispositivos transferem dados, mas em grandes blocos de tamanho fixo. Você geralmente verá dispositivos que utilizam blocos de dados como dispositivos de bloco, como discos rígidos, sistemas de arquivos, etc.

<b> Dispositivo de pipe </ b>

Os chamados pipes permitem que dois ou mais processos se comuniquem entre si. Eles são semelhantes aos dispositivos de caractere, mas, em vez de ter saída enviada para um dispositivo, ele é enviado para outro processo.

<b> Dispositivo de soquete </ b>

Os dispositivos de soquete facilitam a comunicação entre os processos, semelhantes aos dispositivos de pipe, mas podem se comunicar com vários processos de uma só vez.

<b> Caracterização do dispositivo </ b>

Os dispositivos são caracterizados usando dois números, <b> número do dispositivo principal </ b> e <b> número menor do dispositivo </ b>. Você pode ver esses números no exemplo ls acima, eles são separados por uma vírgula. Por exemplo, digamos que um dispositivo tenha os números do dispositivo: <b> 8, 0 </ b>:

O número principal do dispositivo representa o driver de dispositivo usado, nesse caso 8, que geralmente é o maior número de dispositivos de bloco sd. O número menor informa ao kernel qual dispositivo exclusivo está nessa classe de driver, neste caso, 0 é usado para representar o primeiro dispositivo (a).

## Exercício

Olhe para o diretório / dev e descubra que tipos de dispositivos você pode ver.

## Questionário

Qual é o símbolo para dispositivos de caracteres no comando ls -l?

## Resposta do questionário

c