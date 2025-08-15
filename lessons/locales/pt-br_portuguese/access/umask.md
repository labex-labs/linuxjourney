# Umask

## Conteúdo da lição

Todo arquivo criado é fornecido com um conjunto padrão de permissões. Se você quiser alterar esse conjunto padrão de permissões, poderá fazê-lo com o comando umask. Este comando leva o conjunto de permissões de 3 bits que vemos em permissões numéricas.

Em vez de adicionar essas permissões, umask remove essas permissões.

<pre> $ umask 021 </ pre>

No exemplo acima, estamos afirmando que queremos que as permissões padrão de novos arquivos permitam que os usuários acessem tudo, mas, para grupos, queremos tirar sua permissão de gravação e, para outras pessoas, queremos tirar sua permissão executável. O padrão umask na maioria das distribuições é 022, significando todo o acesso do usuário, mas nenhum acesso de gravação para o grupo e outros usuários.

Quando você executar o comando umask, ele fornecerá esse conjunto padrão de permissões em qualquer novo arquivo que você fizer. No entanto, se você quiser persistir, terá que modificar seu arquivo de inicialização (.profile), mas discutiremos isso em uma lição posterior.

## Exercício

<ol>
<li> Crie um novo arquivo e observe suas permissões. </ li>
<li> Modifique o umask e crie outro novo arquivo. </ li>
<li> Verifique as permissões mais uma vez no novo arquivo, o que você espera ver? </ li>
<ol>

## Questionário

Qual comando é usado para alterar as permissões de arquivo padrão?

## Resposta do questionário

umask
