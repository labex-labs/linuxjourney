# Permissões de propriedade

## Conteúdo da lição

Além de modificar as permissões nos arquivos, você também pode modificar o grupo e a propriedade do usuário do arquivo também.

<b> Modifique a propriedade do usuário </ b>

<pre> $ sudo chown patty meuarquivo </ pre>

Este comando irá definir o dono do meuarquivo para o patty.

<b> Modifique a propriedade do grupo </ b>

<pre> $ sudo chgrp whales meuarquivo </ pre>

Este comando irá definir o grupo de meuarquivo para whales.

<b> Modifique a propriedade do usuário e do grupo ao mesmo tempo </ b>
Se você adicionar dois pontos e um nome de grupo após o usuário, poderá definir o usuário e o grupo ao mesmo tempo.

<pre> $ sudo chown patty: whales meuarquivo </ pre>

## Exercício

Modifique o grupo e usuário de alguns arquivos de teste. Depois, dê uma olhada nas permissões com ls -l.

## Questionário

Qual comando você usa para alterar as propriedades do usuário?

## Resposta do questionário

chown
