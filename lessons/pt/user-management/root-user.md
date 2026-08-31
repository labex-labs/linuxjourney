---
lesson_id: "root-user"
course_id: "user-management"
lang: "pt"
order_index: 2
title: "root"
description: "Aprenda como as políticas de su, sudo e sudoers fornecem acesso controlado a identidades privilegiadas."
meta_title: "root - Gerenciamento de Usuários"
meta_description: "Conheça a função do usuário root no Linux. Esta lição aborda as diferenças entre su e sudo para obter privilégios de superusuário e explica como o arquivo /etc/sudoers gerencia o acesso."
meta_keywords: "usuário root no Linux, usuário root Linux, su, sudo, sudoers, visudo, superusuário, gerenciamento de usuários, permissões Linux"
---

A conta tradicionalmente chamada `root` possui UID 0 e ampla autoridade em seu contexto de segurança. Use uma conta sem privilégios para o trabalho cotidiano e eleve seus privilégios apenas para uma finalidade administrativa específica que você compreenda.

## Início de um Shell como Outro Usuário com su

`su`, que significa substitute user, inicia um shell ou comando com a identidade de outra conta. Sem um nome de usuário, o destino padrão é root:

```bash
$ su
```

A autenticação é controlada pelo PAM e pela política local. Um sistema pode solicitar a senha da conta de destino, restringir quem pode usar `su` ou manter a senha do root bloqueada. Não presuma que conhecer uma senha seja a única condição.

O `su` simples altera a identidade, mas preserva uma parte maior do ambiente atual. `su - USER`, também escrito como `su --login USER`, inicia um shell no estilo de login e configura um ambiente mais próximo de um novo login para a conta de destino:

```bash
$ su - operator
```

Saia do subshell quando o trabalho específico da conta de destino estiver concluído.

:::single-choice{#root-su-login-shell}
Qual comando solicita um shell no estilo de login como o usuário `operator`?

::option[`su - operator`]{#root-su-login-operator .correct explanation="O hífen solicita o comportamento de shell de login e um ambiente orientado ao destino para `operator`."}
::option[`su operator`]{#root-su-preserve-environment explanation="Esse comando muda para a identidade de destino, mas não solicita a inicialização completa no estilo de login apresentada aqui."}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` lista os comandos permitidos pela política; ele não inicia o shell de login solicitado."}
:::

## Execução de um Comando Específico com sudo

`sudo COMMAND` solicita autorização da política para executar um comando como um usuário de destino, normalmente root por padrão. Use `-u USER` para solicitar outro destino:

```bash
$ sudo -u postgres id
```

Isso não significa que a solicitação será permitida. A política do sudo controla o usuário solicitante, o host, a identidade de destino, o comando e outras condições. Dependendo da configuração, a autenticação pode usar a senha do usuário solicitante, outro mecanismo ou não apresentar nenhuma solicitação.

Quando for viável, prefira um único comando administrativo de escopo restrito a um shell privilegiado de longa duração. O escopo menor reduz a probabilidade de comandos acidentais serem executados com autoridade elevada.

:::single-choice{#root-sudo-target-user}
O que `sudo -u postgres id` solicita?

::option[Renomear permanentemente a conta atual como `postgres`.]{#root-sudo-rename explanation="`sudo` executa um comando com as credenciais de destino; ele não renomeia os registros de contas."}
::option[Executar `id` com `postgres` como usuário de destino, sujeito à política.]{#root-sudo-postgres-id .correct explanation="A opção `-u` seleciona a identidade de destino, enquanto a política do sudoers decide se a solicitação é permitida."}
::option[Listar todos os usuários cujo UID seja maior que o do usuário atual.]{#root-sudo-list-uids explanation="O comando `id` informa a identidade de seu processo; essa sintaxe não enumera os UIDs das contas."}
:::

## Como Evitar Shells Privilegiados Persistentes

Comandos como `su -`, `sudo -s` ou `sudo -i` podem criar um shell privilegiado quando a política permite. Todos os comandos posteriores nesse shell podem ter impacto elevado até que você saia dele. Erros em caminhos, scripts não revisados e expansões do shell tornam-se mais perigosos.

O comportamento de auditoria depende da configuração. `sudo` normalmente registra as invocações, mas o registro da inicialização de um único shell não fornece automaticamente um histórico completo de todos os comandos digitados dentro dele. O histórico do shell, a auditoria do sistema e o registro de E/S do sudo são mecanismos distintos, cada um com suas próprias políticas.

:::single-choice{#root-persistent-shell-risk}
Por que um shell root de longa duração é mais arriscado do que elevar um comando compreendido por vez?

::option[Shells root excluem automaticamente todos os comandos de todos os sistemas de auditoria.]{#root-shell-no-audit explanation="O registro varia conforme a configuração; é incorreto afirmar que todos os registros de auditoria são apagados automaticamente."}
::option[O shell desabilita nomes de caminhos do sistema de arquivos com mais de um componente.]{#root-shell-path-limit explanation="Os privilégios não impõem essa restrição aos caminhos; a preocupação é a autoridade aplicada às operações comuns."}
::option[Os comandos posteriores podem manter um impacto elevado até que o shell seja encerrado.]{#root-shell-elevated-scope .correct explanation="Uma identidade privilegiada persistente amplia o intervalo em que um erro de digitação ou comando não confiável pode modificar recursos protegidos."}
:::

## Revisão da Autorização do sudo

Execute `sudo -l` para listar o que a conta atual pode solicitar segundo a política ativa:

```bash
$ sudo -l
```

Revise os caminhos dos comandos, os usuários de destino permitidos e as restrições de argumentos. Uma regra aparentemente ampla não deve ser tratada como permissão para realizar trabalhos não relacionados.

:::single-choice{#root-list-sudo-rules}
Qual comando lista os privilégios sudo disponíveis para o usuário solicitante atual?

::option[`sudo -i`]{#root-sudo-login explanation="Esse comando solicita um shell no estilo de login para o destino e pode ampliar o escopo dos privilégios; não é uma listagem de política somente para leitura."}
::option[`sudo -l`]{#root-sudo-list .correct explanation="A opção `-l` minúscula solicita que o sudo liste os comandos permitidos pela política atual."}
::option[`su -l`]{#root-su-login-default explanation="Esse comando invoca o comportamento de shell de login para `su`, em vez de listar a autorização do sudo."}
:::

## Edição Segura da Política do sudoers

A política padrão do sudo normalmente lê `/etc/sudoers` e pode incluir arquivos em `/etc/sudoers.d/`. Outras fontes de política são possíveis. A sintaxe controla muito mais do que uma simples lista de usuários e grupos.

Use `visudo` para alterar a política, pois ele bloqueia o arquivo e valida a sintaxe antes da instalação:

```bash
$ sudo visudo
```

Para um arquivo complementar, especifique seu caminho exato:

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

Não edite sudoers com um redirecionamento comum nem por meio de um fluxo de edição sem validação. Um erro de sintaxe ou permissão pode remover o acesso administrativo. Mantenha outro caminho de recuperação verificado disponível ao alterar a autorização remotamente.

:::single-choice{#root-edit-sudoers-safely}
Qual ferramenta deve ser usada para editar e verificar a sintaxe da política principal do sudoers?

::option[`cat`]{#root-cat-sudoers explanation="`cat` pode exibir texto legível, mas não edita, bloqueia nem valida a sintaxe do sudoers com segurança."}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` oferece o bloqueio e a validação de sintaxe desenvolvidos para alterações na política do sudoers."}
::option[`echo` com `>`]{#root-echo-sudoers explanation="O redirecionamento do shell pode truncar a política imediatamente e não oferece validação da sintaxe do sudoers."}
:::

Para praticar a administração delegada em um ambiente controlado, experimente este laboratório prático:

1. **[Configuração de Contas de Usuário e Privilégios sudo no Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** — Pratique a aplicação de políticas de senha, o bloqueio e desbloqueio de contas de usuário, a proteção da conta root e a concessão de permissões administrativas, assuntos diretamente relacionados ao gerenciamento do acesso de superusuário.

## Resumo

Agora você sabe distinguir a troca de identidade da delegação de comandos controlada por política.

1. Use `su - USER` somente quando quiser um shell de login para o destino.
2. Solicite um destino específico ao sudo com `-u USER`.
3. Minimize o tempo gasto em um shell privilegiado.
4. Revise as regras efetivas do sudo com `sudo -l`.
5. Edite a política do sudoers somente por meio de `visudo`.
