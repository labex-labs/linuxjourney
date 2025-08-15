# cd ("Change Directory" alterar diretório)

## Conteúdo da lição

Agora que você sabe onde está, vamos ver se podemos nos movimentar um pouco no sistema de arquivos. Lembre-se de que precisamos navegar no nosso caminho usando caminhos. Existem duas maneiras diferentes de especificar um caminho, com caminhos absolutos e relativos.

<ul>
<li> Caminho absoluto: esse é o caminho do diretório root. A raiz é o chefe. O diretório root é comumente mostrado como uma barra. Toda vez que seu caminho começa com /, significa que você está iniciando a partir do diretório root. Por exemplo, / home / pete / Desktop. </ li>

<li> Caminho relativo: este é o caminho de onde você está atualmente no sistema de arquivos. Se eu estava em location / home / pete / Documents e queria chegar a um diretório dentro de Documents chamado impostos, eu não tenho que especificar o caminho inteiro do root como / home / pete / Documents / taxes, eu posso ir impostos / em vez disso. </ li>
</ ul>

Agora que você sabe como os caminhos funcionam, só precisamos de algo para nos ajudar a mudar para o diretório que queremos. Felizmente, temos cd ou “alterar diretório” para fazer isso.

<pre> $ cd / home / pete / Pictures </ pre>

Então agora mudei a localização do meu diretório para / home / pete / Pictures.

Agora a partir deste diretório eu tenho uma pasta chamada Hawaii, eu posso navegar para essa pasta com:

<pre> $ cd Hawaii </ pre>

Perceba como acabei de usar o nome da pasta? É porque eu já estava em / home / pete / Pictures.

Pode ficar bastante cansativo navegar com caminhos absolutos e relativos o tempo todo, felizmente, existem alguns atalhos para ajudá-lo.

<ul>
<li> (diretório atual). Este é o diretório em que você está atualmente. </ li>
<li> .. (diretório anterior). Leva você ao diretório acima do seu atual. </ li>
<li> ~ (diretório inicial). Este diretório é padronizado para o seu "diretório home". Tal como / home / pete. </ li>
<li> - (diretório anterior). Isso levará você ao diretório anterior em que você estava. </ li>
</ ul>

<pre> $ cd.
$ cd ..
$ cd ~
$ cd -
</ pre>
Dê uma chance a eles!

## Exercício

<ol>
<li> Execute o comando cd sem sinalizadores, para onde você leva? </ li>
</ ol>

## Questionário

Se você estiver em / home / pete / Pictures e quiser acessar / home / pete, qual seria um bom atalho para usar?

## Resposta do questionário

cd ..
