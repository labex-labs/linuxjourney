---
index: 7
lang: "pt"
title: "Permissões de Processo"
meta_title: "Permissões de Processo - Permissões"
meta_description: "Aprenda sobre as permissões de processo do Linux, incluindo IDs de Usuário Real, Efetivo e Salvo. Entenda como os UIDs impactam a segurança e a execução de comandos. Comece a aprender hoje!"
meta_keywords: "permissões de processo Linux, UID Real, UID Efetivo, UID Salvo, segurança Linux, comando passwd, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Vamos abordar as permissões de processo por um momento. Lembra-se de como eu disse que, ao executar o comando `passwd` com o bit de permissão SUID ativado, você executaria o programa como root? Isso é verdade. No entanto, isso significa que, como você é temporariamente root, pode modificar as senhas de outros usuários? Não, felizmente não!

Isso ocorre devido aos muitos UIDs que o Linux implementa. Existem três UIDs associados a cada processo:

Quando você inicia um processo, ele é executado com as mesmas permissões do usuário ou grupo que o executou. Isso é conhecido como um **ID de usuário efetivo**. Este UID é usado para conceder direitos de acesso a um processo. Então, naturalmente, se Bob executasse o comando `touch`, o processo seria executado como ele, e quaisquer arquivos que ele criasse estariam sob sua propriedade.

Existe outro UID, chamado **ID de usuário real**. Este é o ID do usuário que iniciou o processo. Eles são usados para rastrear quem é o usuário que iniciou o processo.

Um último UID é o **ID de usuário salvo**. Isso permite que um processo alterne entre o UID efetivo e o UID real, e vice-versa. Isso é útil porque não queremos que nosso processo seja executado com privilégios elevados o tempo todo; é uma boa prática usar privilégios especiais em momentos específicos.

Agora vamos juntar tudo isso, olhando para o comando `passwd` mais uma vez.

Ao executar o comando `passwd`, seu UID efetivo é o seu ID de usuário; digamos que seja 500 por enquanto. Ah, mas espere, lembre-se de que o comando `passwd` tem a permissão SUID ativada. Então, quando você o executa, seu UID efetivo agora é 0 (0 é o UID de root). Agora este programa pode acessar arquivos como root.

Digamos que você sinta um pouco de poder e queira modificar a senha de Sally. Sally tem um UID de 600. Bem, você não terá sorte. Felizmente, o processo também tem seu UID real, neste caso 500. Ele sabe que seu UID é 500 e, portanto, você não pode modificar a senha do UID 600. (Isso, é claro, é sempre ignorado se você for um superusuário em uma máquina e puder controlar e mudar tudo).

Como você executou `passwd`, ele iniciará o processo usando seu UID real e salvará o UID do proprietário do arquivo (UID efetivo), para que você possa alternar entre os dois. Não há necessidade de modificar todos os arquivos com acesso root se não for necessário.

Na maioria das vezes, o UID real e o UID efetivo são os mesmos, mas em casos como o comando `passwd`, eles mudarão.

## Exercise

A prática leva à perfeição! Compreender os IDs de usuário e as permissões de processo é crucial para a segurança e administração do Linux. Aqui estão alguns laboratórios práticos para reforçar sua compreensão do gerenciamento de usuários e grupos, que forma a base de como os UIDs funcionam:

1. **[Permissões de Usuário, Grupo e Arquivo Linux](https://labex.io/pt/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprenda conceitos essenciais de gerenciamento de usuários e grupos Linux, incluindo criação e gerenciamento de usuários, exploração de associações de grupo, compreensão de permissões de arquivo e manipulação de propriedade de arquivo. Este laboratório oferece experiência prática na proteção de um ambiente Linux multiusuário.
2. **[Adicionar Novo Usuário e Grupo](https://labex.io/pt/labs/linux-add-new-user-and-group-17987)** - Neste desafio, você simulará a adição de novos membros da equipe a um ambiente de servidor, criando novas contas de usuário, configurando grupos personalizados e gerenciando associações de grupo. Isso testará suas habilidades em administração de usuários e grupos Linux, essencial para administradores de sistema e profissionais de DevOps.

Esses laboratórios o ajudarão a aplicar os conceitos de gerenciamento de usuários e grupos em cenários reais, construindo uma base sólida para entender como os UIDs controlam o acesso e as permissões no Linux.

## Quiz Question

Qual UID decide qual acesso conceder?

## Quiz Answer

effective
