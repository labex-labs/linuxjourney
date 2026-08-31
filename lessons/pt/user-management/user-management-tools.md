---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "pt"
order_index: 6
title: "Ferramentas de Gerenciamento de Usuários"
description: "Aprenda a criar, modificar, proteger, verificar e remover contas locais com opções explícitas."
meta_title: "Ferramentas de Gerenciamento de Usuários - Gerenciamento de Usuários"
meta_description: "Domine o gerenciamento de usuários Linux com ferramentas essenciais de linha de comando. Este guia aborda useradd, usermod, userdel e passwd para administrar contas locais com segurança."
meta_keywords: "gerenciamento de usuários Linux, ferramenta de linha de comando para gerenciar contas Linux, useradd, usermod, userdel, passwd, contas Linux, gerenciar usuários Linux"
---

As distribuições Linux normalmente oferecem ferramentas de contas do conjunto de utilitários shadow, mas os padrões e as interfaces de nível superior variam. Antes de alterar uma conta local, confirme que ela não é gerenciada centralmente, consulte o manual local do comando e mantenha um caminho de recuperação.

Os comandos desta lição alteram o estado de autenticação e propriedade. Pratique apenas em um ambiente descartável autorizado, nunca em um host de produção.

## Revisão dos Padrões de Criação de Contas

`useradd` cria uma conta local usando as opções do comando e os padrões do sistema. Inspecione os padrões compilados e configurados com:

```bash
$ useradd -D
```

Arquivos como `/etc/default/useradd`, `/etc/login.defs` e o conteúdo do diretório de modelos podem influenciar o comportamento, mas suas funções variam conforme a distribuição. Pode existir um comando `adduser` de nível superior, porém sua interface não é padronizada em todos os sistemas Linux.

## Criação Explícita de uma Conta Local

Em um ambiente controlado, especifique as propriedades importantes em vez de depender de padrões desconhecidos:

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` solicita a criação do diretório pessoal.
- `-s /bin/bash` escolhe o shell de login após confirmar que esse caminho é permitido e está instalado.
- `-c` fornece o campo GECOS/comentário.

A nova conta normalmente não consegue se autenticar com uma senha local válida até que uma seja definida, mas o estado inicial exato da senha e do bloqueio depende das ferramentas e políticas locais. Verifique os registros em vez de fazer suposições:

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home}
Qual opção de `useradd` solicita explicitamente a criação do diretório pessoal da nova conta?

::option[`-M`]{#user-tools-no-home-option explanation="A opção `-M` maiúscula instrui explicitamente as implementações comuns de `useradd` a não criar o diretório pessoal."}
::option[`-s`]{#user-tools-shell-option explanation="A opção `-s` escolhe um shell de login e não cria, por si só, um diretório pessoal."}
::option[`-m`]{#user-tools-home-option .correct explanation="A opção `-m` minúscula solicita que `useradd` crie e preencha o diretório pessoal de acordo com os padrões locais."}
:::

## Definição ou Alteração de uma Senha

Um usuário comum altera sua própria senha local interativamente com:

```bash
$ passwd
```

Um administrador autorizado pode definir a senha de outra conta local com:

```bash
$ sudo passwd bob
```

Digite senhas somente no prompt protegido, não em argumentos de comandos, no histórico do shell, nas anotações da lição nem em conversas. A política do PAM pode rejeitar senhas fracas ou reutilizadas. Contas gerenciadas por serviços de diretório podem exigir outra ferramenta.

:::single-choice{#user-tools-change-own-password}
Qual comando normalmente permite que o usuário atual altere sua própria senha por meio de um prompt interativo?

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` cria um registro de conta e não é o comando interativo comum para alterar senhas."}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` remove uma conta local e não tem relação com a alteração da senha do usuário solicitante."}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="Sem um nome de usuário como operando, `passwd` atua sobre a senha local do usuário solicitante conforme a política do PAM."}
:::

## Modificação das Propriedades e dos Grupos da Conta

`usermod` altera campos de contas locais. Alguns exemplos são:

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

Antes de mover o diretório pessoal, verifique o destino, a propriedade, o espaço disponível, os processos em execução, as montagens e os serviços. Para grupos suplementares, `-aG` significa acrescentar à lista atual. Usar `-G` sem `-a` substitui toda a lista de grupos suplementares e pode remover acessos inesperadamente.

As alterações de grupos normalmente afetam novas sessões de login, não os processos que já estão em execução com o conjunto antigo de credenciais.

:::single-choice{#user-tools-append-group}
Qual comando adiciona `bob` ao grupo suplementar `developers` sem substituir suas outras associações suplementares?

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="Sem `-a`, `-G` substitui a lista de grupos suplementares e pode remover associações existentes."}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="A opção `-a` acrescenta o grupo indicado por `-G`, preservando as outras associações suplementares."}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` remove a definição de um grupo e não acrescenta a associação de um usuário."}
:::

## Bloqueio de uma Senha Local

Um administrador pode bloquear o hash da senha local com `passwd -l USER` e inspecionar seu estado com `passwd -S USER`. O desbloqueio é realizado com `passwd -u USER` somente após verificar por que o bloqueio existe e se ainda há um hash válido.

O bloqueio de uma senha não necessariamente impede chaves SSH, tokens, tarefas agendadas, processos já em execução nem a autenticação específica de serviços. Para desabilitar uma conta de forma abrangente, defina a ameaça e os caminhos de acesso e aplique uma política coordenada, que pode incluir a expiração da conta, o shell de login, o acesso a serviços, chaves e o encerramento de sessões.

:::single-choice{#user-tools-password-lock-scope}
O que `passwd -l bob` bloqueia principalmente?

::option[Todos os caminhos possíveis de autenticação e execução para a conta.]{#user-tools-lock-everything explanation="Chaves, tokens, tarefas, serviços e sessões existentes podem exigir controles separados."}
::option[Todos os arquivos que atualmente pertencem ao UID de Bob.]{#user-tools-lock-files explanation="O estado da senha não altera a propriedade do sistema de arquivos nem torna automaticamente inacessíveis os dados pertencentes à conta."}
::option[O hash da senha Unix local usado pela autenticação por senha.]{#user-tools-lock-local-password .correct explanation="O comando adiciona um prefixo ao hash da senha local ou o desabilita de outra forma, impedindo a verificação normal por esse caminho."}
:::

## Remoção Deliberada de uma Conta Local

`userdel bob` sem opções remove os registros da conta local, mas normalmente mantém o diretório pessoal. `userdel -r bob` também tenta remover o diretório pessoal e a caixa de correio, tornando-se uma operação destrutiva.

Antes de qualquer remoção:

1. Confirme a conta exata com `getent passwd bob` e `id bob`.
2. Identifique processos em execução, tarefas agendadas, serviços, chaves e acessos delegados.
3. Faça um inventário dos arquivos pertencentes ao UID nos sistemas de arquivos pretendidos.
4. Decida se os dados devem ser transferidos, arquivados, mantidos ou excluídos com segurança.
5. Confirme que o UID não será reatribuído enquanto ainda houver arquivos órfãos.

`userdel -r` não garante a remoção de arquivos fora dos locais configurados para o diretório pessoal e a caixa de correio. A exclusão da conta também pode deixar propriedades numéricas em arquivos, permissões de bancos de dados, identidades de aplicações e registros em diretórios remotos.

:::single-choice{#user-tools-userdel-r-scope}
Que remoção adicional o comando comum `userdel -r bob` solicita em comparação com `userdel bob` sem opções?

::option[Todos os arquivos com o UID de Bob em todos os sistemas de arquivos montados.]{#user-tools-delete-all-owned explanation="A ferramenta não localiza e apaga de forma universal todos os arquivos pertencentes ao UID em todo o armazenamento."}
::option[Todas as contas remotas cujo nome de usuário também seja `bob`.]{#user-tools-delete-remote explanation="`userdel` atua nos bancos de dados de contas locais aplicáveis e não exclui identidades não relacionadas de serviços de diretório."}
::option[O diretório pessoal e a caixa de correio local de Bob, além dos registros da conta.]{#user-tools-delete-home-mail .correct explanation="A opção de remoção recursiva da conta atua sobre o diretório pessoal e a caixa de correio configurados, mas não sobre todos os objetos que possam pertencer a Bob em outros locais."}
:::

Para praticar o ciclo de vida das contas em um ambiente isolado, experimente estes laboratórios práticos:

1. **[Gerenciamento de Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** — Pratique todo o ciclo de administração de usuários, desde a criação e proteção de novas contas até sua modificação e exclusão.
2. **[Gerenciamento de Grupos Linux com groupadd, usermod e groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** — Adquira experiência prática com os principais utilitários de linha de comando para administração de grupos, incluindo a adição, a modificação e a exclusão de grupos.
3. **[Configuração de Contas de Usuário e Privilégios sudo no Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** — Aprenda técnicas essenciais de gerenciamento de contas de usuário e privilégios sudo para aumentar a segurança de um sistema Linux.

## Resumo

Agora você sabe gerenciar contas locais com escopo explícito e verificação.

1. Revise os padrões de `useradd` antes da criação.
2. Solicite explicitamente as configurações de diretório pessoal, shell e metadados.
3. Altere senhas somente por meio de prompts protegidos.
4. Acrescente grupos suplementares sem substituir a lista existente.
5. Faça um inventário das dependências da identidade antes de uma remoção destrutiva.
