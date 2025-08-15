# mv (mover)

## Conteúdo da lição

Usado para mover arquivos e também renomeá-los. Bastante semelhante ao comando cp em termos de sinalizadores e funcionalidade.

Você pode renomear arquivos assim:

<pre> $ mv arquivoAntigo arquivoNovo </ pre>

Ou você pode realmente mover um arquivo para um diretório diferente:

<pre> $ mv arquivo2 / home / pete / Documents </ pre>

E mova mais de um arquivo:

<pre> $ mv arquivo_1 arquivo_2 / algumdiretorio </ pre>

Você pode renomear diretórios também:

<pre> $ mv diretorio1 diretorio2 </ pre>

Como o cp, se você usar mv em um arquivo ou diretório, ele irá sobrescrever qualquer coisa no mesmo diretório. Então você pode usar o sinalizador -i para avisar antes de sobrescrever qualquer coisa.

<pre> mv -i diretorio1 diretorio2 </ pre>

Digamos que você queira copiar um arquivo para substituir o anterior. Você também pode fazer um backup desse arquivo e ele apenas renomeará a versão antiga com um ~.

<pre> $ mv -b diretorio1 diretorio2 </ pre>

## Exercício

Renomeie um arquivo e mova esse arquivo para um diretório diferente.

## Questionário

Como você renomeia um arquivo chamado gato para cachorro?

## Resposta do questionário

mv gato cachorro
