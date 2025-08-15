# rm (remover)

## Conteúdo da lição

Agora eu acho que temos muitos arquivos, vamos remover alguns. Para remover arquivos, você pode usar o comando rm. O comando rm (remove) é usado para excluir arquivos e diretórios.

<pre> $ rm arquivo1 </ pre>

Tome cuidado ao usar rm, não há lixeira mágica de onde você pode pescar arquivos removidos. Uma vez que eles se forem, eles se foram para sempre, então tenha cuidado.

Felizmente, existem algumas medidas de segurança postas em prática. Por isso, a pessoa comum não pode remover apenas um monte de arquivos importantes. Os arquivos protegidos contra gravação solicitarão sua confirmação antes de excluí-los. Se um diretório estiver protegido contra gravação, ele também não será facilmente removido.

Agora, se você não se preocupa com nada disso, pode remover um monte de arquivos.

<pre> $ rm -f arquivo1 </ pre>

-f (ou força a opção) diz ao rm para remover todos os arquivos, estejam eles protegidos contra gravação ou não, sem avisar o usuário (contanto que você tenha as permissões apropriadas).

<pre> $ rm -i arquivo </ pre>

Adicionar o sinalizador -i como muitos dos outros comandos, lhe dará um aviso se você deseja realmente remover os arquivos ou diretórios.

<pre> $ rm -r diretorio </ pre>

Você não pode simplesmente criar um diretório por padrão, mas precisará adicionar o sinalizador -r (recursivo) para remover todos os arquivos e subdiretórios que ele possa ter.

Você pode remover um diretório com o comando rmdir.

<pre> diretorio $ rmdir </ pre>

## Exercício

<ol>
<li> Crie um arquivo chamado -arquivo (não esqueça o traço!). </ li>
<li> Remover esse arquivo. </ li>
</ ol>

## Questionário

Como você remove um arquivo chamado meuarquivo?

## Resposta do questionário

rm meuarquivo