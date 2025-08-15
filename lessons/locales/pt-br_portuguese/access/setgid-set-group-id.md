# Setgid

## Conteúdo da lição

Semelhante ao bit de permissão set ID do usuário, há um bit de permissão set group ID (SGID). Esse bit permite que um programa seja executado como se fosse um membro desse grupo.

Vamos ver um exemplo:

<pre> $ ls -l / usr / bin / wall
-rwxr-sr-x 1 raiz tty 19024 14 de dezembro às 11:45 / usr / bin / wall
</ pre>

Podemos ver agora que o bit de permissão está no conjunto de permissões do grupo.

<b> Modificando o SGID </ b>

<pre> $ sudo chmod g + s meuarquivo
$ sudo chmod 2555 meuarquivo
</ pre>

A representação numérica para o SGID é 2.

## Exercício

Nenhum exercício para esta lição.

## Questionário

Qual número representa o SGID?

## Resposta do questionário

2
