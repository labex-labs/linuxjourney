# dd

## Conteúdo da lição

A ferramenta dd é super útil para converter e copiar dados. Ele lê a entrada de um arquivo ou fluxo de dados e o grava em um arquivo ou fluxo de dados.

Considere o seguinte comando:

<pre> $ dd if = / home / pete / backup.img of = / dev / sdb bs = 1024 </ pre>

Este comando está copiando o conteúdo de backup.img para / dev / sdb. Ele copiará os dados em blocos de 1024 bytes até que não haja mais dados a serem copiados.

<ul>
<li> if = arquivo - Arquivo de entrada, lido de um arquivo em vez de uma entrada padrão </ li>
<li> of = arquivo - Arquivo de saída, gravar em um arquivo em vez de saída padrão </ li>
<li> bs = bytes - Tamanho do bloco, lê e grava esses muitos bytes de dados de cada vez. Você pode usar métricas de tamanhos diferentes indicando o tamanho com um k para kilobyte, m para megabyte, etc, então 1024 bytes é 1k </ li>
<li> count = número - Número de blocos a serem copiados. </ li>
</ ul>

Você verá alguns comandos dd que usam a opção count, geralmente com dd se você deseja copiar um arquivo que tenha 1 megabyte, você normalmente desejará ver esse arquivo como 1 megabyte quando ele estiver sendo copiado. Vamos dizer que você execute o seguinte comando:

<pre> $ dd if = / home / pete / backup.img of = / dev / sdb bs = count de 1M = 2 </ pre>

Nosso arquivo backup.img é 10M, no entanto, estamos dizendo neste comando para copiar mais de 1M 2 vezes, então apenas 2M está sendo copiado, deixando nossos dados copiados incompletos. A contagem pode ser útil em muitas situações, mas se você estiver copiando apenas dados, poderá omitir a contagem e até mesmo o bs. Se você realmente deseja otimizar suas transferências de dados, convém começar a usar essas opções.

O dd é extremamente poderoso, você pode usá-lo para fazer backups de qualquer coisa, incluindo unidades de disco inteiras, restaurando imagens de discos e muito mais. Tenha cuidado, essa ferramenta poderosa pode ter um preço se você não tiver certeza do que está fazendo.

## Exercício

Use o comando dd para fazer um backup de sua unidade e defina a saída para um arquivo .img.

## Questionário

Qual é a opção dd para tamanho de bloco?

## Resposta do questionário

bs
