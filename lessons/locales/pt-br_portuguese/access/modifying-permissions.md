# Modifying Permissions

## Lesson Content

Alterar permissões pode ser feito facilmente com o comando <b> chmod </ b>. 

Primeiro, escolha o conjunto de permissões que você deseja alterar, usuário, grupo ou outro. Você pode adicionar ou remover permissões com <b> + </ b> ou <b> - </ b>, vamos ver alguns exemplos.

<b>Adicionando bit de permissão em um arquivo</b>
<pre>$ chmod u+x meuarquivo</pre>

O comando acima é assim: altere a permissão em meuarquivo adicionando um bit de permissão executável no conjunto de usuários. Então agora o usuário tem permissão executável neste arquivo!

<b>Removendo bit de permissão em um arquivo</b>
<pre>$ chmod u-x meuarquivo</pre>

<b>Adicionando vários bits de permissão em um arquivo</b>
<pre>$ chmod ug+w</pre>

Existe outra maneira de alterar as permissões usando o formato numérico. Esse método permite que você altere as permissões de uma só vez. Em vez de usar r, w ou x para representar permissões, você usará uma representação numérica para um único conjunto de permissões. Portanto, não há necessidade de especificar o grupo com g ou o usuário com u.

The numerical representations are seen below:

<ul>
<li>4: permissão de leitura</li>
<li>2: permissão de gravação</li>
<li>1: permissão de execução</li>
</ul>

Vamos ver um exemplo:

<pre> $ chmod 755 meuarquivo </ pre>

Você consegue adivinhar quais permissões estamos dando a este arquivo? Vamos dividir isso, então agora 755 cobre as permissões para todos os grupos. O primeiro número (7) representa as permissões do usuário, o segundo número (5) representa as permissões do grupo e o último 5 representa outras permissões.

Espere um minuto, 7 e 5 não foram listados acima, de onde estamos pegando esses números? Lembre-se de que estamos combinando todas as permissões em um único número agora, então você terá alguma matemática envolvida.

7 = 4 + 2 + 1, então 7 são as permissões do usuário e tem permissões de leitura, gravação e execução

5 = 4 + 1, o grupo tem permissões de leitura e execução

5 = 4 +1 e todos os outros usuários têm permissões de leitura e execução

De qualquer modo, você poderia potencialmente expor um arquivo confidencial para todos modificarem, no entanto, muitas vezes você deseja legitimamente alterar as permissões, apenas tome cuidado ao usar o comando chmod.

## Exercício

Altere algumas permissões básicas do arquivo de texto e veja os bits mudando conforme você faz um ls -l.

## Questionátio

Qual número representa a permissão de leitura ao usar o formato numérico?

## Resposta do questionário

4
