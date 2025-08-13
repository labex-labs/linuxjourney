# Permissão de Arquivos

## Conteúdo da Lição: 

Como aprendemos anteriormente, os arquivos têm diferentes permissões ou modos de arquivo. Vamos ver um exemplo:



<pre>$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
</pre>

Existem quatro partes para as permissões de um arquivo. A primeira parte é o tipo de arquivo, que é indicado pelo primeiro caractere nas permissões, no nosso caso, já que estamos vendo um diretório que mostra d para o tipo de arquivo. Mais comumente você verá um - para um arquivo regular. 

As próximas três partes do modo de arquivo são as permissões reais. As permissões são agrupadas em 3 bits cada. Os primeiros 3 bits são permissões de usuário, depois permissões de grupo e outras permissões. Eu adicionei o pipe para facilitar a diferenciação.


<pre>d | rwx | r-x | r-x </pre>

Each character represent a different permission: 
<ul>
<li>r: legível</li>
<li>w: gravável</li>
<li>x: executável (basicamente um programa executável)</li>
<li>-: Vazio</li>
</ul>

Portanto, no exemplo acima, vemos que o usuário pete leu, escreveu e executou permissões no arquivo. O grupo pingüins leu e executou permissões. E finalmente, os outros usuários (todos os outros) têm permissões de leitura e execução. 

## Exercise

Use o comando ls -l em vários arquivos e recite suas permissões, usuário e grupo.
 

## Quiz Question

Que bit de permissão é usado para executável?

## Quiz Answer

x
