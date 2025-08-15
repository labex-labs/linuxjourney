# cp (copiar)

## Conteúdo da lição

Vamos começar a fazer algumas cópias desses arquivos. Assim como copiar e colar arquivos em outros sistemas operacionais, o shell nos oferece uma maneira ainda mais simples de fazer isso.

<pre> $ cp meuarquivolegal / home / pete / Documentos / documentoslegais </ pre>

meuarquivolegal é o arquivo que você deseja copiar e / home / pete / Documents / documentoslegais é onde você está copiando o arquivo.

Você pode copiar vários arquivos e diretórios, bem como usar curingas. Um caractere curinga é um caractere que pode ser substituído por uma seleção baseada em padrões, oferecendo mais flexibilidade para as pesquisas. Você pode usar caracteres curinga em todos os comandos para obter mais flexibilidade.

<ul>
<li> * o curinga dos curingas, é usado para representar todos os caracteres únicos ou qualquer sequência. </ li>
<li> usado para representar um caractere </ li>
<li> [] usado para representar qualquer caractere entre colchetes </ li>
</ ul>

<pre> $ cp * .jpg / home / pete / imagens </ pre>

Isso copiará todos os arquivos com a extensão .jpg em seu diretório atual para o diretório Pictures.

Um comando útil é usar o sinalizador -r, que copiará recursivamente os arquivos e diretórios dentro de um diretório.

Tente fazer um cp em um diretório que contenha alguns arquivos em seu diretório Documentos. Não funcionou, não é? Bem, isso porque você precisará copiar os arquivos e diretórios dentro também com o comando -r.

<pre> $ cp -r Abóbora / / home / pete / Documentos </ pre>

Note uma coisa, se você copiar um arquivo para um diretório que tenha o mesmo nome de arquivo, o arquivo será sobrescrito com o que você está copiando. Isso não é bom se você tiver um arquivo que não deseja ser substituído acidentalmente. Você pode usar o sinalizador -i (interativo) para avisar antes de sobrescrever um arquivo.

<pre> $ cp -i meuarquivolegal / home / pete / imagens </ pre>

## Exercício

Copie alguns arquivos, tenha cuidado para não sobrescrever nada importante.

## Questionário

Qual sinalizador você precisa especificar para copiar em um diretório?

## Resposta do Questionário

-r
