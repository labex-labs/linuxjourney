---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "pt"
order_index: 1
title: "Usuários e Grupos"
description: "Aprenda como o Linux identifica usuários e grupos e como as credenciais dos processos afetam as decisões de acesso."
meta_title: "Usuários e Grupos - Gerenciamento de Usuários"
meta_description: "Entenda usuários e grupos no Linux, UIDs, GIDs, o superusuário root, credenciais de processos e o uso de sudo para privilégios elevados."
meta_keywords: "usuários e grupos Linux, fundamentos Linux, sudo, usuário root, UID, GID, gerenciamento usuários, tutorial Linux"
---

O Linux usa identidades de usuários e grupos para rotular processos, definir a propriedade de objetos do sistema de arquivos e tomar decisões de controle de acesso. Os nomes legíveis ajudam os administradores, enquanto o kernel trabalha principalmente com identificadores numéricos e credenciais de processos.

## Identificação de Usuários com UIDs

Cada conta possui um identificador numérico de usuário, ou **UID**. Os nomes são mapeados para UIDs pelos bancos de dados de contas do sistema. Os arquivos armazenam a propriedade numericamente, embora as ferramentas normalmente mostrem o nome correspondente.

Execute `id` para inspecionar as informações de identidade do processo atual:

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

Os valores variam conforme o sistema. Contas humanas de login geralmente possuem diretórios pessoais como `/home/alice`, mas uma conta pode usar outro caminho ou não ter um diretório pessoal comum. Contas de serviço frequentemente existem para executar software com uma identidade limitada, não para permitir login interativo.

:::single-choice{#users-uid-purpose} Qual identificador o kernel usa principalmente para representar uma identidade de usuário?

::option[Um caminho de diretório pessoal]{#users-home-path explanation="Um caminho pessoal é uma configuração da conta e pode variar ou estar ausente; ele não é o identificador de usuário do kernel."}
::option[Um UID numérico]{#users-numeric-uid .correct explanation="Os bancos de contas mapeiam nomes para UIDs numéricos, usados nas credenciais dos processos e nos registros de propriedade."}
::option[Um número de janela do terminal]{#users-terminal-number explanation="Dispositivos e sessões de terminal são conceitos separados das identidades numéricas de usuário."}
:::

## Organização do Acesso com Grupos

Um grupo possui um identificador numérico, ou **GID**. Uma conta normalmente tem um grupo primário e pode pertencer a grupos suplementares. A associação a grupos permite conceder acesso a um conjunto de usuários sem atribuir permissões individualmente a cada conta.

Inspecione as associações com:

```bash
$ id alice
$ groups alice
```

Esses comandos informam dados de identidade configurados ou resolvidos. Serviços de diretório e caches podem participar; por isso, ler diretamente `/etc/group` nem sempre mostra o quadro completo das associações efetivas.

:::single-choice{#users-primary-supplementary-groups} Como uma conta Linux normalmente pode participar de grupos?

::option[Ela pode pertencer a exatamente um grupo durante toda a sua existência.]{#users-single-group explanation="Os processos Linux podem carregar um grupo primário e uma lista de grupos suplementares."}
::option[Ela pertence a todos os grupos cujos arquivos consegue ler.]{#users-readable-groups explanation="A leitura de arquivos segue permissões e credenciais; ela não cria automaticamente uma associação a grupos."}
::option[Ela possui um grupo primário e pode ter grupos suplementares.]{#users-group-memberships .correct explanation="O GID primário faz parte do registro da conta, enquanto associações suplementares fornecem identidades de grupo adicionais."}
:::

## Compreensão das Credenciais dos Processos

Um processo possui credenciais como UIDs e GIDs reais e efetivos, além de grupos suplementares. As credenciais efetivas são centrais para muitas verificações de permissão. Um processo iniciado por um usuário geralmente herda as credenciais do pai, mas mecanismos controlados podem alterá-las.

Isso é mais preciso que dizer que um processo sempre é executado apenas “como o usuário que o iniciou”. Executáveis set-user-ID, gerenciadores de serviços, contêineres, namespaces e chamadas de sistema que alteram privilégios podem afetar as identidades visíveis ou efetivas em determinado contexto.

:::single-choice{#users-process-access-identity} Quais informações são normalmente consideradas quando o kernel verifica um processo segundo as permissões de um arquivo?

::option[O UID efetivo, o GID efetivo e os grupos suplementares do processo.]{#users-effective-credentials .correct explanation="Essas credenciais são comparadas aos dados de propriedade e permissão nas verificações discricionárias comuns."}
::option[O tema de cores do terminal que iniciou o processo.]{#users-terminal-theme explanation="Preferências de exibição não participam das verificações de permissões do sistema de arquivos."}
::option[A quantidade de letras do nome da conta.]{#users-username-length explanation="O kernel trabalha com credenciais numéricas; o tamanho do nome de usuário não concede acesso."}
:::

## Reconhecimento da Identidade Root

A conta tradicionalmente chamada `root` possui UID 0. O UID 0 recebe tratamento especial de muitos mecanismos de permissão do Linux e carrega amplo poder administrativo. O Linux moderno também pode dividir privilégios por capabilities, namespaces, controles de acesso obrigatórios e confinamento de serviços; portanto, “poder ilimitado em todos os contextos” é uma simplificação excessiva.

O trabalho cotidiano deve usar uma conta sem privilégios. A autoridade administrativa aumenta o impacto de erros de caminho, comandos não confiáveis e software comprometido.

:::single-choice{#users-root-uid} Qual UID numérico identifica tradicionalmente a conta root?

::option[`0`]{#users-uid-zero .correct explanation="Sistemas Linux e semelhantes ao Unix tradicionalmente reservam o UID 0 para a identidade de superusuário."}
::option[`1000`]{#users-uid-thousand explanation="Muitas distribuições atribuem um valor próximo de 1000 à primeira conta humana comum, mas esse não é o UID de root."}
::option[`1`]{#users-uid-one explanation="O UID 1 pode pertencer a uma conta de sistema e não é a identidade tradicional de superusuário."}
:::

## Uso de sudo sob uma Política

`sudo` pergunta à política configurada se o usuário chamador pode executar um comando como uma identidade de destino. O destino padrão costuma ser root, mas uma política ou `-u USER` pode escolher outra conta. As solicitações de autenticação e o registro também dependem da configuração.

Liste os comandos que a conta atual tem permissão para executar:

```bash
$ sudo -l
```

Use um comando administrativo permitido somente quando a tarefa exigir e você compreender seus efeitos. Não use `sudo` apenas para silenciar um erro de permissão nem exiba bancos de hashes de senhas, como `/etc/shadow`, como exercício casual.

:::single-choice{#users-sudo-policy} O que `sudo` faz antes de executar um comando solicitado?

::option[Consulta a política configurada para autorizar o uso da identidade de destino solicitada.]{#users-sudo-policy-check .correct explanation="`sudo` autoriza segundo a política e estabelece as credenciais de destino configuradas quando permitido."}
::option[Sempre concede a todos os usuários locais acesso root irrestrito.]{#users-sudo-always-root explanation="A autorização é controlada por política; usuários ou comandos negados não recebem acesso root geral."}
::option[Altera permanentemente o UID da conta chamadora para 0.]{#users-sudo-permanent-uid explanation="`sudo` executa um comando com credenciais de destino; ele não reescreve permanentemente a identidade da conta chamadora."}
:::

Para praticar a administração de contas e grupos em um ambiente controlado, experimente estes laboratórios:

1. **[Gerenciamento de Contas Linux com useradd, usermod e userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** — Pratique todo o ciclo de administração de usuários, da criação e proteção à modificação e remoção.
2. **[Gerenciamento de Grupos Linux com groupadd, usermod e groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** — Obtenha experiência prática com os principais utilitários de linha de comando para administrar grupos, inclusive a criação de grupos, a modificação das associações de usuários e a remoção de grupos.
3. **[Configuração de Contas e Privilégios sudo no Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** — Aprenda técnicas essenciais para gerenciar contas de usuários e privilégios `sudo`, inclusive a concessão de permissões administrativas, a fim de melhorar a segurança de um sistema Linux.

## Resumo

Agora você sabe descrever como o Linux representa identidades e delega comandos administrativos.

1. Identifique contas por UID e grupos por GID.
2. Diferencie associações a grupos primários e suplementares.
3. Relacione as credenciais dos processos às verificações de acesso.
4. Reconheça o UID 0 como a identidade root tradicional.
5. Trate `sudo` como uma ferramenta de delegação controlada por política.
