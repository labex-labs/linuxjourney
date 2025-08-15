# Permissões de arquivos

## Conteúdo da lição

Como aprendemos anteriormente, os arquivos têm diferentes permissões ou modos de arquivo. Vamos ver um exemplo:

<pre>$ ls -l Desktop/
drwxr-xr-x 2 pete linux 4096 Dec 1 11:45 .
</pre>

Existem quatro partes para as permissões de um arquivo. A primeira parte é o tipo de arquivo, que é denotado pelo primeiro caractere nas permissões, no nosso caso, já que estamos vendo um diretório que mostra <b>d</b> para o tipo de arquivo. Mais comumente você verá um <b>-</b> para um arquivo comum. 

As próximas três partes do modo de arquivo são as permissões reais. As permissões são agrupadas em 3 bits cada. Os primeiros 3 bits são permissões de usuário, depois permissões de grupo e outras permissões. Eu adicionei o pipe para facilitar a diferenciação.

<pre>d | rwx | r-x | r-x </pre>

Cada caractere representa uma permissão diferente: 
<ul>
<li>r: leitura</li>
<li>w: escrita</li>
<li>x: execução (basicamente um programa executável)</li>
<li>-: vazio</li>
</ul>

Então, no exemplo acima, vemos que o usuário pete tem permissão de leitura, escrita e executar no arquivo. O grupo linux tem permissões de leitura e execução. E finalmente, os outros usuários (todos os outros) têm permissões de leitura e execução.

## Exercício

Use o comando ls -l em vários arquivos e recite suas permissões, usuário e grupo. 

## Questinário

Que bit de permissão é usado para executável? 

## Resposta do questionário

x
