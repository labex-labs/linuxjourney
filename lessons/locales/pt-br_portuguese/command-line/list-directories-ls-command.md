# ls (listar diretórios)

## Conteúdo da lição

Agora que sabemos como navegar pelo sistema, como descobrimos o que está disponível para nós? Agora é como se estivéssemos nos movendo no escuro. Bem, podemos usar o maravilhoso comando ls para listar o conteúdo do diretório. O comando ls listará diretórios e arquivos no diretório atual por padrão, no entanto, você pode especificar qual caminho você deseja listar os diretórios.

<pre> $ ls
$ ls / home / pete </ pre>

O ls é uma ferramenta bastante útil, ele também mostra informações detalhadas sobre os arquivos e diretórios que você está vendo.

Observe também que nem todos os arquivos em um diretório estarão visíveis. Nomes de arquivo que começam com. estão ocultos, você pode visualizá-los com o comando ls e passar o sinalizador -a para ele (um para todos).

<pre> $ ls -a </ pre>

Há também um sinalizador ls mais útil, -l por exemplo, ele mostra uma lista detalhada de arquivos em um formato longo. Ele mostrará informações detalhadas, começando pela esquerda: permissões de arquivos, número de links, nome do proprietário, grupo de proprietários, tamanho do arquivo, data e hora da última modificação e nome do arquivo / diretório.

<pre> $ ls -l </ pre>

<pre> pete @ icebox: ~ $ ls -l
total de 80
drwxr-x --- 7 pete penguingroup 4096 20 de novembro às 16:37 Desktop
drwxr-x --- 2 pete penguingroup 4096 Oct 19 10:46 Documentos
drwxr-x --- 4 pete penguingroup 4096 Nov 20 09:30 Downloads
drwxr-x --- 2 pete penguingroup 4096 7 de outubro 13:13 Música
drwxr-x --- 2 pete penguingroup 4096 Set 21 14:02 Fotos
drwxr-x --- 2 pete penguingroup 4096 Jul 27 12:41 Public
drwxr-x --- 2 pete penguingroup 4096 Jul 27 12:41 Templates
drwxr-x --- 2 pete penguingroup 4096 Jul 27 12:41 Vídeos </ pre>

Comandos têm coisas chamadas flags (ou argumentos ou opções, como você quiser chamá-lo) para adicionar mais funcionalidade. Veja como nós adicionamos -a e -l, bem, você pode adicionar os dois juntos com -la. A ordem dos sinalizadores determina em qual ordem ele entra, na maioria das vezes isso não importa, portanto você também pode fazer ls -al e ainda funcionaria.

<pre> $ ls -la </ pre>

## Exercício

Execute ls com diferentes flags e veja a saída que você recebe.

## Questionário

Qual comando você usaria para ver arquivos ocultos?

## Resposta do questionário

ls -a
