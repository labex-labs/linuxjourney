# Permissões de processos

## Conteúdo da lição

Vamos nos concentrar em algumas permissões de processo, lembre-se de como eu disse que quando você executa o comando passwd com o bit de permissão SUID ativado, você executará o programa como root? Isso é verdade, no entanto, isso significa que você está temporariamente como root, você pode modificar senhas de outros usuários? Não, felizmente não!

Isso é por causa dos muitos UIDs que o Linux implementa. Existem três UIDS associadas a cada processo:

Quando você inicia um processo, ele é executado com as mesmas permissões que o usuário ou grupo que o executou, isso é conhecido como um <b> ID de usuário efetivo </ b>. Este UID é usado para conceder direitos de acesso a um processo. Então, naturalmente, se Bob executasse o comando touch, o processo seria executado como ele e quaisquer arquivos que ele criasse seriam de sua propriedade.

Existe outro UID, chamado de <b> ID do usuário real </ b>, este é o ID do usuário que iniciou o processo. Eles são usados para rastrear quem é o usuário que iniciou o processo.

Um último UID é o <b> ID do usuário salvo </ b>, isso permite que um processo alterne entre o UID efetivo e o UID real, e vice-versa. Isso é útil porque não queremos que nosso processo seja executado com privilégios elevados o tempo todo, é uma boa prática usar privilégios especiais em momentos específicos.

Agora vamos juntar tudo isso olhando o comando passwd mais uma vez.

Ao executar o comando passwd, seu UID efetivo é seu ID de usuário, digamos 500 por enquanto. Ah, mas espere, lembre-se que o comando passwd tem a permissão SUID habilitada. Então, quando você executá-lo, o seu UID efetivo é agora 0 (0 é o UID do root). Agora este programa pode acessar arquivos como root.

Digamos que você tenha um pouco de poder e queira modificar a senha de Sally, Sally tem um UID de 600. Bem, você estará sem sorte, felizmente o processo também tem seu UID real neste caso 500. Ele sabe que o seu O UID é 500 e, portanto, você não pode modificar a senha do UID de 600. (Isso, obviamente, sempre é ignorado se você for um superusuário em uma máquina e puder controlar e alterar tudo).

Desde que você executou o passwd, ele iniciará o processo usando seu UID real e salvará o UID do proprietário do arquivo (UID efetivo), para que você possa alternar entre os dois. Não há necessidade de modificar todos os arquivos com acesso root, se não for necessário.

Na maioria das vezes, o UID real e o UID efetivo são os mesmos, mas em casos como o comando passwd, eles serão alterados.

## Exercício

Ainda não discutimos processos, ainda podemos observar essa mudança em tempo real:

<ol>
<li> Abra uma janela de terminal e execute o comando: <b> watch -n 1 "ps aux | grep passwd" </ b>. Isto irá observar o processo de passwd. </ li>
<li> Abra uma segunda janela de terminal e execute: <b> passwd </ b> </ li>
<li> Olhe para a primeira janela do terminal, você verá um processo para passwd. A primeira coluna na tabela de processos é o ID do usuário efetivo, e eis que é o usuário root! </ li>
</ ol>

## Questionário

Qual UID decide qual acesso conceder?

## Resposta do questionário

eficaz
