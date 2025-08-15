# pwd (Imprimir diretório de trabalho)

## Conteúdo da lição

Tudo no Linux é um arquivo, à medida que você se aprofunda no Linux, você entenderá isso, mas, por enquanto, lembre-se disso. Todo arquivo é organizado em uma árvore de diretórios hierárquica. O primeiro diretório no sistema de arquivos é adequadamente chamado de diretório root (ou diretório raiz). O diretório root tem muitas pastas e arquivos onde você pode armazenar mais pastas e arquivos, etc. Aqui está um exemplo de como a árvore de diretórios se parece:

<pre>/
|-- bin
|   |-- arquivo1
|   |-- arquivo2
|-- etc
|   |-- arquivo3
|   `-- diretorio1
|       |-- arquivo4
|       `-- arquivo5
|-- home
|-- var
</pre>

A localização desses arquivos e diretórios é chamada de caminhos. Se você tivesse uma pasta chamada home com uma pasta dentro dela chamada pete e outra pasta naquela pasta chamada Movies, o caminho seria assim: / home / pete / Movies, bem simples, né?

A navegação do sistema de arquivos, assim como na vida real, é útil se você souber onde está e para onde está indo. Para ver onde você está, você pode usar o comando pwd, esse comando significa "imprimir diretório de trabalho" e mostra apenas em qual diretório você está, observe o caminho derivado do diretório root.

<pre> $ pwd </ pre>

Onde está voce? Onde estou? Faz um teste.

## Exercício

Nenhum exercício para esta lição.

## Questionário

Como faria para encontrar em qual diretório você está atualmente?

## Resposta do questionário

pwd