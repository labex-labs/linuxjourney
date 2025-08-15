# find

## Conteúdo da lição

Com todos esses arquivos que temos no sistema, pode ser um pouco complicado tentar encontrar um específico. Bem, há um comando que podemos usar para isso, find!

<pre> $ find / home -name filhotes.jpg </ pre>

Com o find, você precisará especificar o diretório que pesquisará e o que está procurando. Nesse caso, estamos tentando encontrar um arquivo com o nome de filhotes.jpg.

Você pode especificar o tipo de arquivo que você está tentando encontrar.

<pre> $ find / home -tipo d -name MinhaPasta </ pre>

Você pode ver que eu defini o tipo de arquivo que estou tentando encontrar como (d) para o diretório e ainda estou pesquisando pelo nome de MinhaPasta.

Uma coisa legal de se notar é que o find não para no diretório que você está pesquisando, ele irá procurar dentro de subdiretórios que o diretório possa ter também.

## Exercício

<ol>
<li> Encontre um arquivo do diretório root que tenha a palavra net nele. </ li>
</ ol>

## Questionário

Qual opção devo especificar para encontrar se quero pesquisar por nome?

## Resposta do questionário

-name
