# Setuid

## Conteúdo da lição

Existem muitos casos em que usuários normais precisam de acesso elevado para fazer coisas. O administrador do sistema nem sempre pode estar lá para inserir uma senha de root toda vez que um usuário precisar acessar um arquivo protegido, portanto, há bits de permissão de arquivo especiais para permitir esse comportamento. A ID de usuário definida (SUID) permite que um usuário execute um programa como o proprietário do arquivo de programa, e não como ele mesmo.

Vamos ver um exemplo:

Vamos dizer que eu quero mudar minha senha, simples né? Eu apenas uso o comando passwd:

<pre> $ passwd </ pre>

O que o comando de senha está fazendo? Está modificando alguns arquivos, mas o mais importante é modificar o arquivo / etc / shadow. Vamos dar uma olhada nesse arquivo por um segundo:

<pre> $ ls -l / etc / shadow

-rw-r ----- 1 shadow root 1134 1 de dezembro 11:45 / etc / shadow
</ pre>

Ahh! Espere um minuto, esse arquivo é de propriedade do root? Como é possível que consigamos modificar um arquivo de propriedade do root?

Vamos ver outro conjunto de permissões, desta vez do comando que executamos:

<pre> $ ls -l / usr / bin / passwd

-rwsr-xr-x 1 root root 47032 1 de dezembro 11:45 / usr / bin / passwd
</ pre>

Você notará um novo bit de permissão aqui <b> s </ b>. Esse bit de permissão é o SUID, quando um arquivo tem essa permissão definida, ele permite que os usuários que iniciaram o programa obtenham a permissão do proprietário do arquivo, bem como a permissão de execução, neste caso, root. Então, essencialmente, enquanto um usuário está executando o comando passwd, eles estão sendo executados como root.

É por isso que somos capazes de acessar um arquivo protegido como / etc / shadow quando executamos o comando passwd. Agora, se você remover esse bit, verá que não poderá modificar o / etc / shadow e, portanto, alterar sua senha.

<b> Modificando o SUID </ b>

Assim como as permissões regulares, existem duas maneiras de modificar as permissões do SUID.

<i> Forma simbólica: </ i>
<pre> $ sudo chmod u + s meuarquivo </ pre>

<i> Forma numérica: </ i>
<pre> sudo chmod 4755 meuarquivo </ pre>

Como você pode ver, o SUID é denotado por um 4 e pré-anexado ao conjunto de permissões. Você pode ver o SUID indicado como <b> S </ b>, isso significa que ele ainda faz a mesma coisa, mas não tem permissões de execução.

## Exercício

Olhe para a permissão do / etc / passwd em detalhes, você percebe mais alguma coisa? Arquivos com SUID habilitado também são facilmente distinguíveis.

## Questionário

Qual número representa o SUID?

## Resposta do questionário

4
