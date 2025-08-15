# O bit persistente

## Conteúdo da lição

Um último bit de permissão especial que eu quero falar é o bit persistente.

Este bit de permissão, "persiste em um arquivo / diretório", significa que somente o proprietário ou o usuário root pode excluir ou modificar o arquivo. Isso é muito útil para diretórios compartilhados. Dê uma olhada no exemplo abaixo:

<pre> $ ls -ld / tmp
drwxrwxrwxt 6 root 4096 Dez 15 11:45 / tmp
</ pre>

Você verá um bit de permissão especial no final aqui <b> t </ b>, isso significa que todos podem adicionar arquivos, gravar arquivos, modificar arquivos no diretório / tmp, mas somente o root pode excluir o diretório / tmp.

<b> Modifique o bit persistente </ b>

<pre> $ sudo chmod + t meudiretorio

$ sudo chmod 1755 meudiretorio </ pre>

A representação numérica para o bit persistente é <b> 1 </ b>

## Exercício

Quais outros arquivos e diretórios você acha que têm um bit persistente ativado?

## Questionário

Qual símbolo representa o bit persistente?

## Resposta do questionário

t
