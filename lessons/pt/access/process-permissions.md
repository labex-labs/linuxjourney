---
lang: "pt"
title: "Permissões de Processo"
description: "Aprenda sobre as permissões de processo do Linux, incluindo IDs de Usuário Real, Efetivo e Salvo. Entenda como os UIDs impactam a segurança e a execução de comandos. Comece a aprender hoje!"
keywords: "permissões de processo Linux, UID Real, UID Efetivo, UID Salvo, segurança Linux, comando passwd, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Vamos abordar um pouco as permissões de processo. Lembra que eu disse que quando você executa o comando `passwd` com o bit de permissão SUID habilitado, você executará o programa como root? Isso é verdade. No entanto, isso significa que, como você é temporariamente root, pode modificar as senhas de outros usuários? Não, felizmente não!

Isso ocorre por causa dos muitos UIDs que o Linux implementa. Existem três UIDs associados a cada processo:

Quando você inicia um processo, ele é executado com as mesmas permissões do usuário ou grupo que o executou. Isso é conhecido como um **ID de usuário efetivo**. Este UID é usado para conceder direitos de acesso a um processo. Então, naturalmente, se Bob executasse o comando `touch`, o processo seria executado como ele, e quaisquer arquivos que ele criasse estariam sob sua propriedade.

Existe outro UID, chamado **ID de usuário real**. Este é o ID do usuário que iniciou o processo. Eles são usados para rastrear quem é o usuário que iniciou o processo.

Um último UID é o **ID de usuário salvo**. Isso permite que um processo alterne entre o UID efetivo e o UID real, e vice-versa. Isso é útil porque não queremos que nosso processo seja executado com privilégios elevados o tempo todo; é uma boa prática usar privilégios especiais em momentos específicos.

Agora vamos juntar tudo isso, olhando o comando `passwd` mais uma vez.

Ao executar o comando `passwd`, seu UID efetivo é o seu ID de usuário; digamos que seja 500 por enquanto. Ah, mas espere, lembre-se que o comando `passwd` tem a permissão SUID habilitada. Então, quando você o executa, seu UID efetivo agora é 0 (0 é o UID do root). Agora este programa pode acessar arquivos como root.

Digamos que você sinta um pouco de poder e queira modificar a senha de Sally. Sally tem um UID de 600. Bem, você não terá sorte. Felizmente, o processo também tem seu UID real, neste caso 500. Ele sabe que seu UID é 500 e, portanto, você não pode modificar a senha do UID 600. (Isso, é claro, é sempre ignorado se você for um superusuário em uma máquina e puder controlar e alterar tudo).

Como você executou `passwd`, ele iniciará o processo usando seu UID real e salvará o UID do proprietário do arquivo (UID efetivo), para que você possa alternar entre os dois. Não há necessidade de modificar todos os arquivos com acesso root se não for necessário.

Na maioria das vezes, o UID real e o UID efetivo são os mesmos, mas em casos como o comando `passwd`, eles mudarão.

## Exercise

Não discutimos processos ainda, mas ainda podemos observar essa mudança acontecendo em tempo real:

1. Open one terminal window and run the command: `watch -n 1 "ps aux | grep passwd"`. This will watch for the `passwd` process.
2. Open a second terminal window and run: `passwd`.
3. Look at the first terminal window; you'll see a process come up for `passwd`. The first column in the process table is the effective user ID. Lo and behold, it's the root user!

## Quiz Question

Qual UID decide qual acesso conceder?

## Quiz Answer

effective
