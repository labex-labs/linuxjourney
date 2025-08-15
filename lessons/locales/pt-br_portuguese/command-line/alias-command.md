# alias

## Conteúdo da lição

Às vezes, os comandos de digitação podem ficar realmente repetitivos ou, se você precisar digitar um longo comando várias vezes, é melhor ter um alias que possa ser usado para isso. Para criar um alias para um comando, basta especificar um nome de alias e configurá-lo para o comando.

<pre> $ alias foobar = 'ls -la' </ pre>

Agora, em vez de digitar ls -la, você pode digitar foobar e ele executará esse comando, algo muito interessante. Lembre-se de que esse comando não salvará seu alias após a reinicialização, portanto, você precisará adicionar um alias permanente em:

<pre> ~ / .bashrc </ pre>

ou arquivos semelhantes, se você quiser que ele persista após a reinicialização.

Você pode remover aliases com o comando unalias:

<pre> $ unalias foobar </ pre>

## Exercício

Crie um par de aliases e remova-os.

## Questionário

Qual comando é usado para criar um alias?

## Resposta do Questionário

alias
