---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "pt"
order_index: 5
title: "/etc/group"
description: "Aprenda como os registros de grupos locais mapeiam nomes para GIDs e listam membros suplementares."
meta_title: "/etc/group - Gerenciamento de Usuários"
meta_description: "Conheça o arquivo /etc/group no Linux para entender o gerenciamento de grupos. Aprenda a visualizar dados de grupos e interpretar sua estrutura, incluindo GID e listas de usuários."
meta_keywords: "/etc/group, /etc/group Linux, arquivo /etc/group no Linux, cat /etc/group, gerenciamento de grupos, GID, permissões Linux, grupos Linux"
---

`/etc/group` armazena registros de grupos locais. Ele mapeia nomes de grupos para GIDs numéricos e lista membros explícitos, oferecendo suporte ao controle de acesso compartilhado por várias contas.

## Grupos Locais e Grupos Resolvidos

O arquivo é apenas uma das possíveis fontes de grupos. O NSS pode resolver grupos a partir de arquivos locais, serviços de diretório ou outros bancos de dados configurados. Exiba os registros locais com:

```bash
$ cat /etc/group
```

Consulte o banco de dados de grupos resolvido com `getent`:

```bash
$ getent group
$ getent group developers
```

As listas de grupos podem revelar nomes internos de contas e funções, portanto revise a saída antes de compartilhá-la.

:::single-choice{#group-query-resolved-database} Qual comando consulta o banco de dados de grupos resolvido pelo NSS?

::option[`getent group`]{#group-getent-all .correct explanation="`getent` consulta as fontes do NSS configuradas para os registros de grupos."}
::option[`cat /etc/group`]{#group-cat-local explanation="Esse comando lê apenas o arquivo de grupos local e pode omitir grupos fornecidos por outras fontes."}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` espera nomes de usuários e informa associações; ele não trata o caminho do banco de dados local como uma consulta ao NSS."}
:::

## Leitura dos Quatro Campos

Um registro local possui quatro campos separados por dois-pontos:

```text
developers:x:1500:alice,bob
```

1. **Nome do grupo**: `developers`.
2. **Campo de senha**: Normalmente `x`, `*` ou outro marcador; os dados protegidos da senha do grupo podem ser armazenados em `/etc/gshadow`.
3. **GID**: A identidade numérica do grupo, `1500` neste caso.
4. **Lista de membros**: Nomes dos membros explícitos separados por vírgulas, `alice` e `bob` neste caso.

As senhas de grupos são um recurso legado usado por ferramentas como `newgrp` em algumas configurações. Elas não são o mecanismo normal para conceder autorização sudo e não devem ser introduzidas por meio de edições manuais dos campos.

:::single-choice{#group-gid-field} Em `developers:x:1500:alice,bob`, qual campo contém o GID?

::option[O segundo campo, `x`]{#group-second-password explanation="O campo 2 é o marcador de senha do grupo, não a identidade numérica."}
::option[O quarto campo, `alice,bob`]{#group-fourth-members explanation="O campo 4 lista os nomes dos membros explícitos, não o GID."}
::option[O terceiro campo, `1500`]{#group-third-gid .correct explanation="O terceiro campo separado por dois-pontos é o ID numérico do grupo."}
:::

:::single-choice{#group-explicit-member-field} Como os nomes dos membros explícitos são representados em um registro de grupo local?

::option[Como uma lista separada por vírgulas no campo 4.]{#group-members-field-four .correct explanation="O campo final contém os nomes dos membros suplementares explícitos separados por vírgulas."}
::option[Como uma lista separada por espaços no campo 2.]{#group-members-field-two explanation="O campo 2 é reservado para dados relacionados à senha ou para um marcador, não para a lista de membros."}
::option[Como UIDs numéricos incorporados ao nome do grupo.]{#group-members-in-name explanation="O nome do grupo e os nomes dos membros ficam em campos separados; as entradas comuns de membros são nomes de login, não dígitos de UID incorporados."}
:::

## Consideração da Associação ao Grupo Primário

A lista de membros em `/etc/group` normalmente não repete os usuários cujo registro passwd indica esse GID como grupo primário. Portanto, um usuário pode pertencer ao grupo mesmo que seu nome não apareça no campo 4.

Por exemplo, se o registro passwd de Alice tiver 1500 como GID primário, ela pertence a `developers` mesmo que o registro local do grupo termine com um campo de membros vazio:

```text
developers:x:1500:
```

É por isso que analisar somente o campo 4 produz uma visão incompleta das associações.

:::single-choice{#group-primary-membership-visibility} O registro passwd de Alice usa o GID 1500 como GID primário, mas seu nome não aparece no campo 4 do grupo 1500. Ela pertence a esse grupo?

::option[Não, toda associação deve aparecer no campo 4 de `/etc/group`.]{#group-field-four-only explanation="Isso ignora a associação pelo GID primário e resultaria em uma contagem incompleta dos membros do grupo."}
::option[Sim, a associação primária vem do campo GID do registro passwd.]{#group-primary-from-passwd .correct explanation="A lista explícita do arquivo de grupos serve principalmente para associações suplementares; a associação primária é registrada com a conta."}
::option[Somente se o campo de senha do grupo contiver seu nome de usuário.]{#group-password-member explanation="O campo de senha não tem relação com a declaração da associação primária."}
:::

## Inspeção dos Grupos de um Usuário

Use `id USER` ou `groups USER` para obter a visão de uma conta resolvida:

```bash
$ id alice
$ groups alice
```

Para o processo atual, `id` sem argumentos informa os grupos efetivamente presentes em suas credenciais. Uma associação suplementar recém-configurada normalmente não aparece em uma sessão de login já em execução; inicie uma nova sessão autenticada ou use um mecanismo configurado deliberadamente, como `newgrp`, quando for apropriado.

:::single-choice{#group-current-process-credentials} Qual comando informa o UID, o GID primário e os grupos suplementares do processo atual?

::option[`id`]{#group-current-id .correct explanation="Sem um usuário como operando, `id` informa as credenciais de identidade do processo atual."}
::option[`cat /etc/group`]{#group-current-cat explanation="O arquivo local lista registros, mas não mostra quais grupos resolvidos estão ativos no processo atual."}
::option[`getent passwd`]{#group-current-passwd explanation="Esse comando consulta registros de contas e não informa especificamente a lista de grupos suplementares do processo atual."}
:::

## Alteração Segura dos Grupos Locais

Use ferramentas como `groupadd`, `groupmod`, `groupdel`, `gpasswd` e `usermod` em vez de editar registros com um editor de uso geral. Tenha atenção especial a:

- `usermod -aG GROUP USER`, que acrescenta uma associação suplementar.
- `usermod -G ...`, que substitui a lista de grupos suplementares quando `-a` é omitido.

Se o reparo manual do banco de dados local for inevitável, use `vigr` para o bloqueio e `grpck` para a validação. Mantenha um caminho de recuperação antes de realizar alterações remotas de identidade.

Para praticar o gerenciamento de grupos locais em um ambiente controlado, experimente estes laboratórios práticos:

1. **[Gerenciamento de Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** — Pratique todo o ciclo de administração de usuários, desde a criação e proteção de novas contas até sua modificação e exclusão.
2. **[Gerenciamento de Grupos Linux com groupadd, usermod e groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** — Adquira experiência prática com os principais utilitários de linha de comando para administração de grupos, incluindo `groupadd`, `usermod` e `groupdel`.
3. **[Adição de Novo Usuário e Grupo](https://labex.io/labs/linux-add-new-user-and-group-17987)** — Simule a inclusão de novos membros de uma equipe em um servidor, criando contas de usuário, configurando grupos personalizados e gerenciando associações.

## Resumo

Agora você sabe interpretar registros de grupos locais e resolver associações completas com mais precisão.

1. Consulte as fontes de grupos configuradas com `getent group`.
2. Leia os quatro campos do grupo separados por dois-pontos.
3. Localize o GID numérico e a lista de membros explícitos.
4. Inclua a associação primária obtida dos registros passwd.
5. Inspecione as credenciais ativas antes de confiar em uma associação alterada.
