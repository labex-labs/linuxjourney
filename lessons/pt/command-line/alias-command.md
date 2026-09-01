---
lesson_id: "alias-command"
course_id: "command-line"
lang: "pt"
order_index: 18
title: "alias"
description: "Aprenda a criar, inspecionar, persistir, ignorar e remover aliases de comandos no Bash."
meta_title: "alias - Linha de Comando"
meta_description: "Aprenda o comando alias do Linux com exemplos para criar aliases temporários, salvá-los em .bashrc, listá-los e removê-los com unalias."
meta_keywords: "comando alias Linux, comando alias, alias Bash, alias .bashrc, comando unalias, atalho de comando Linux, alias shell"
---

Um alias instrui um shell interativo a substituir uma palavra de comando por outra sequência antes de executar a linha. Isso pode abreviar um comando frequente ou fornecer um conjunto preferido de opções.

## Criação de um Alias no Shell Atual

No Bash, defina um alias com `alias NAME='REPLACEMENT'`. Não coloque espaços ao redor do sinal de igualdade:

```bash
$ alias ll='ls -la'
```

Depois dessa definição, inserir `ll` como comando o expande para `ls -la`. As aspas mantêm a substituição agrupada durante a definição do alias.

Aliases são mais adequados para substituições simples do prefixo de um comando. Use uma função do shell quando precisar processar argumentos de maneira mais estruturada.

:::single-choice{#define-ll-alias} Qual comando do Bash define `ll` como um alias de `ls -la` no shell atual?

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="Os espaços ao redor de `=` dividem a definição em palavras separadas; assim, o Bash não recebe uma atribuição de alias válida."}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="Essa forma usa `NAME=REPLACEMENT` e coloca entre aspas a substituição que contém um espaço."}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` remove nomes de aliases existentes. Ele não cria uma substituição."}
:::

## Carregamento de um Alias em Sessões Futuras do Bash

Um alias definido no prompt pertence ao shell atual e desaparece quando ele é encerrado. Sessões interativas não iniciadas como login do Bash normalmente leem `~/.bashrc`; por isso, esse arquivo é o local habitual para aliases pessoais do Bash:

```bash
alias ll='ls -la'
```

Depois de editar o arquivo, inicie uma nova sessão interativa do Bash ou recarregue-o no shell atual:

```bash
$ source ~/.bashrc
```

O comportamento de inicialização pode variar conforme o shell, o modo de login e a configuração da distribuição. Um usuário do Zsh, por exemplo, normalmente usaria a configuração do Zsh, não o `.bashrc` do Bash.

:::single-choice{#persist-bash-alias} Onde um alias pessoal normalmente deve ser definido para que futuras sessões interativas não iniciadas como login do Bash o carreguem?

::option[No arquivo `~/.bashrc` do usuário.]{#bashrc-alias .correct explanation="O Bash interativo não iniciado como login normalmente lê `~/.bashrc`, tornando-o o local convencional para aliases pessoais."}
::option[No arquivo executável usado pelo comando que recebe o alias.]{#edit-executable explanation="Alterar um executável instalado não tem relação com a expansão de aliases e pode danificar arquivos gerenciados do sistema."}
::option[No histórico de rolagem do terminal atual.]{#terminal-scrollback explanation="O histórico de rolagem apenas registra o texto exibido. O Bash não o executa como configuração de inicialização."}
:::

## Inspeção de Aliases e da Resolução de Nomes

Execute `alias` sem argumentos para listar os aliases do shell atual:

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Use `type NAME` para inspecionar como o Bash resolve um nome específico:

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias} Qual comando mostra se o Bash atualmente resolve `ll` como alias, função, comando interno ou executável?

::option[`file ll`]{#file-ll explanation="`file` classifica um caminho no sistema de arquivos. Um alias existe no estado do shell e não precisa corresponder a um arquivo chamado `ll`."}
::option[`type ll`]{#type-ll .correct explanation="O comando interno `type` informa como a sessão atual do Bash resolve o nome `ll`."}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` consulta descrições de páginas de manual. Aliases pessoais normalmente não possuem uma entrada nesse banco de dados."}
:::

## Como Ignorar e Remover um Alias

Para ignorar um alias em uma única linha, coloque uma barra invertida antes do nome do comando ou use-o depois do comando interno `command` do Bash:

```bash
$ \ls
$ command ls
```

Isso é útil quando você precisa do comportamento normal do comando subjacente. Mantenha os aliases curtos e previsíveis e evite ocultar comportamentos surpreendentes ou destrutivos por trás de nomes conhecidos.

:::single-choice{#bypass-ls-alias} A sessão atual do Bash possui um alias chamado `ls`. Qual comando ignora esse alias em uma invocação?

::option[`alias ls`]{#show-ls-alias explanation="Esse comando mostra a definição do alias `ls`. Ele não invoca o comando subjacente."}
::option[`command ls`]{#command-ls .correct explanation="Como `command` é a palavra de comando, o Bash não expande o `ls` seguinte como alias e aplica a resolução normal."}
::option[`source ls`]{#source-ls explanation="`source` lê um arquivo como código do shell atual. Ele não é uma forma segura nem apropriada de ignorar um alias."}
:::

Remova um alias do shell atual com `unalias`:

```bash
$ unalias ll
```

Se a definição continuar em `~/.bashrc`, um shell futuro poderá recriá-la. Remova ou altere também essa linha de configuração quando quiser excluir o alias permanentemente.

:::single-choice{#remove-current-alias} Qual comando remove o alias `ll` da sessão atual do Bash?

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` exclui o alias indicado da tabela de aliases do shell atual."}
::option[`alias ll=''`]{#empty-ll explanation="Esse comando substitui o alias por uma expansão vazia, em vez de remover sua definição."}
::option[`command ll`]{#command-ll explanation="`command` pode ignorar a expansão do alias nessa linha, mas não o exclui do estado do shell."}
:::

## Resumo

Agora você sabe personalizar o Bash com aliases simples e inspecionáveis.

1. Defina um alias temporário com as aspas corretas.
2. Carregue aliases pessoais de `~/.bashrc` em sessões futuras.
3. Inspecione aliases e a resolução de comandos.
4. Ignore um alias em uma única invocação.
5. Remova as definições ativa e salva quando necessário.
