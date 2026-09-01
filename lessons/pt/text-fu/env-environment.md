---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "pt"
order_index: 5
title: "env (Ambiente)"
description: "Aprenda como o Bash expande, exporta, inspeciona e substitui temporariamente variáveis de ambiente."
meta_title: "env (Ambiente) - Text-Fu"
meta_description: "Explore o comando env no Linux. Aprenda a visualizar e usar variáveis de ambiente como PATH, HOME e USER e entenda a herança entre processos."
meta_keywords: "env, env Linux, comando env Linux, variáveis de ambiente, variável PATH, variáveis shell, HOME, USER"
---

Todo processo possui um ambiente: uma coleção de cadeias de nome e valor herdadas de seu processo pai. Os shells usam variáveis de ambiente para transmitir aos programas iniciados configurações como idioma e caminhos de pesquisa de executáveis.

## Expansão dos Valores das Variáveis no Bash

O Bash expande `$NAME` ou `${NAME}` para o valor de uma variável antes de executar um comando. Coloque a expansão entre aspas para preservar o valor como um único argumento:

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

Algumas variáveis de ambiente comuns são:

- `HOME`: caminho do diretório pessoal do usuário atual.
- `USER`: nome de usuário fornecido pelo ambiente de login em muitos sistemas.
- `PWD`: diretório de trabalho atual do shell.
- `PATH`: diretórios pesquisados em busca de nomes de comandos.

Os valores dependem do ambiente do processo atual; eles não são constantes universais. Uma variável não definida se expande para uma cadeia vazia, a menos que um comportamento mais rigoroso do shell esteja ativado.

:::single-choice{#env-print-home-value} Qual comando do Bash mostra o valor de `HOME`, preservando-o como um único argumento?

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="Aspas simples impedem a expansão de parâmetros; portanto, esse comando mostra os caracteres literais `$HOME`."}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="O Bash expande `$HOME` dentro de aspas duplas, e `printf` recebe o valor completo como um único argumento."}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="Sem um cifrão ou a sintaxe de parâmetro, `HOME` é um texto comum, não uma expansão de variável."}
:::

## Inspeção do Ambiente Atual

Execute `env` sem operandos para mostrar o ambiente herdado pelo processo `env`:

```bash
$ env
```

A saída contém registros `NAME=value`, por exemplo:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Variáveis de ambiente podem conter credenciais, tokens, caminhos internos ou outros dados confidenciais. Não cole a saída completa de `env` em relatórios públicos ou logs sem revisá-la e ocultar os segredos.

:::single-choice{#env-list-exported-values} Qual comando mostra o ambiente visível para um processo recém-iniciado?

::option[`env`]{#env-print-all .correct explanation="Sem um comando ou atribuições, `env` mostra o ambiente de nomes e valores recebido."}
::option[`alias`]{#env-alias-list explanation="`alias` lista definições de aliases, que fazem parte do estado do shell, não dos registros de ambiente exportados."}
::option[`history`]{#env-history-list explanation="`history` exibe as linhas de comando lembradas pelo shell. Ele não enumera variáveis exportadas."}
:::

## Localização de Comandos por meio de PATH

`PATH` é uma lista de diretórios separados por dois-pontos que o Bash pesquisa quando um nome de comando não contém uma barra:

```bash
$ printf '%s\n' "$PATH"
```

A ordem importa: o Bash usa o primeiro comando adequado que encontra conforme suas regras de resolução. Use `type -a NAME` para inspecionar como o shell atual resolve um nome.

Para acrescentar `/opt/coolapp/bin` ao início no shell atual e em seus futuros filhos, preservando o caminho de pesquisa existente:

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

Não substitua acidentalmente `PATH` apenas pelo novo diretório nem acrescente diretórios graváveis não confiáveis. Qualquer um desses erros pode impedir a localização de comandos normais ou fazer um executável inesperado ser executado.

:::single-choice{#env-prepend-path-directory} Qual comando acrescenta `/opt/coolapp/bin` antes do `PATH` existente para o processo Bash atual e seus futuros filhos?

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="Essa forma descarta todos os diretórios de pesquisa existentes, dificultando a localização de comandos comuns."}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="Essa forma acrescenta o novo diretório ao início, preserva o valor anterior e exporta o resultado para processos filhos."}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="Aspas simples preservam o texto literal `$PATH`, e a atribuição não é exportada para futuros processos filhos."}
:::

## Exportação de uma Variável para Processos Filhos

Variáveis do Bash não fazem parte automaticamente do ambiente fornecido aos processos filhos. Marque um nome para exportação com `export`:

```bash
$ export TEST=test
```

O processo Bash atual agora possui uma variável chamada `TEST`, e os comandos que ele inicia herdam `TEST=test`. Um processo filho não pode usar esse mecanismo para alterar o ambiente de seu pai.

```bash
$ printenv TEST
test
```

A atribuição normalmente dura até que você a remova ou o shell seja encerrado. Ela não modifica um ambiente de todo o sistema.

:::single-choice{#env-export-inheritance} Qual é o principal efeito de `export TEST=test` no Bash?

::option[Ele grava `TEST` na configuração do sistema de todos os usuários.]{#env-system-wide explanation="A atribuição afeta o shell atual e a herança por seus filhos, não todos os usuários nem todo o sistema operacional."}
::option[Ele marca `TEST=test` para herança por futuros processos filhos.]{#env-child-inheritance .correct explanation="`export` acrescenta a variável do shell ao ambiente que o Bash fornece aos comandos iniciados."}
::option[Ele altera o ambiente de processos que já estão em execução.]{#env-existing-processes explanation="Processos existentes mantêm seus próprios ambientes. A exportação afeta os processos iniciados posteriormente."}
:::

## Definição de um Valor para um Único Comando

Coloque atribuições antes de um comando para fornecer valores apenas ao ambiente desse comando:

```bash
$ LANG=C sort names.txt
```

O valor de `LANG` no shell atual não é alterado permanentemente. O utilitário `env` oferece outra forma explícita:

```bash
$ env LANG=C sort names.txt
```

Use `env -i COMMAND` para iniciar um comando com um ambiente inicialmente vazio e depois acrescente as atribuições necessárias. Muitos programas dependem de valores do ambiente; portanto, use essa opção conscientemente.

:::single-choice{#env-one-command-value} Qual comando executa `sort names.txt` com `LANG=C` sem alterar permanentemente `LANG` no shell atual?

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` acrescenta a atribuição ao ambiente do comando iniciado, enquanto o shell pai mantém seu valor anterior."}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="Essa forma exporta `LANG=C` no shell atual e o mantém alterado depois que `sort` termina."}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="Essa forma começa com um ambiente vazio, mas não define o valor `LANG=C` solicitado."}
:::

## Carregamento de Valores Pessoais em Sessões Futuras

Para recriar uma variável exportada em futuras sessões interativas do Bash, coloque uma linha `export` adequada no arquivo de inicialização realmente lido por essas sessões, normalmente `~/.bashrc` para o Bash interativo não iniciado como login:

```bash
export TEST=test
```

O Zsh normalmente usa `~/.zshrc`, enquanto o Fish usa uma sintaxe e configuração diferentes. Shells de login e não interativos podem ler outros arquivos; por isso, identifique o shell e o tipo de sessão em vez de presumir que um único arquivo configura todos os processos.

Para praticar a herança do ambiente e a configuração do shell, experimente estes laboratórios:

1. **[Gerenciamento do Ambiente e da Configuração do Shell no Linux](https://labex.io/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** — Pratique a criação e o gerenciamento de variáveis locais e de ambiente, entenda a herança e torne configurações persistentes modificando `.bashrc`.
2. **[Variáveis de Ambiente no Linux](https://labex.io/labs/linux-environment-variables-in-linux-385274)** — Aprenda o conceito e o uso das variáveis de ambiente, como criá-las, modificá-las e gerenciá-las e seu papel na configuração do sistema.

## Resumo

Agora você sabe inspecionar e controlar o ambiente transmitido pelo Bash aos processos filhos.

1. Expanda valores de variáveis usando aspas conscientemente.
2. Revise os valores exportados sem expor segredos.
3. Preserve e ordene os diretórios de comandos em `PATH`.
4. Exporte uma variável do shell para futuros processos filhos.
5. Substitua um valor para um único comando sem alterar o shell pai.
