---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "pt"
order_index: 3
title: "cd (Mudar de Diretório)"
description: "Aprenda a usar cd com caminhos e atalhos para navegar pelo sistema de arquivos do Linux."
meta_title: "cd (Mudar de Diretório) - Linha de Comando"
meta_description: "Aprenda o comando cd do Linux com exemplos de caminhos absolutos e relativos, atalhos para o diretório pessoal, diretório pai e diretório anterior."
meta_keywords: "comando cd, comando cd Linux, mudar diretório, cd diretório pai, cd home, cd diretório anterior, caminho absoluto, caminho relativo"
---

Para navegar pelo sistema de arquivos do Linux, você usa caminhos que especificam seu destino. A principal ferramenta para isso é o comando `cd`, abreviação de change directory, ou mudar de diretório. Ele altera o diretório de trabalho atual do shell.

O destino deve ser um diretório, não um arquivo comum. Se o diretório não existir, se o nome estiver digitado incorretamente ou se você não tiver permissão para entrar nele, `cd` informará um erro em vez de mudar de localização.

A sintaxe básica é:

```bash
cd [DIRECTORY]
```

## Compreensão dos Caminhos

Há duas maneiras de especificar um caminho: absoluta e relativa.

- **Caminho absoluto**: o caminho completo a partir do diretório raiz (`/`). Por exemplo: `/home/pete/Desktop`.

- **Caminho relativo**: um caminho baseado em sua localização atual. Se você estiver em `/home/pete/Documents` e quiser acessar um subdiretório chamado `taxes`, poderá usar `taxes/`.

:::single-choice{#recognize-absolute-cd-path}
Qual afirmação descreve corretamente um caminho absoluto?

::option[Ele começa no diretório que o shell estiver usando no momento]{#begins-at-current-directory explanation="Um caminho que depende da localização atual do shell é relativo. Ele não começa necessariamente na raiz."}
::option[Ele contém apenas o nome do diretório final, sem os diretórios superiores]{#contains-final-name-only explanation="Um único nome de destino normalmente é interpretado em relação ao diretório atual. Um caminho absoluto inclui sua rota a partir de `/`."}
::option[Ele começa no diretório raiz, representado por `/`]{#begins-at-root .correct explanation="Um caminho absoluto começa na raiz do sistema de arquivos. A `/` inicial torna seu ponto de partida independente do diretório atual."}
:::

## Uso do Comando cd

Para mudar para um diretório específico usando um caminho absoluto, digite:

```bash
$ cd /home/pete/Pictures
```

Esse comando leva você diretamente ao diretório `Pictures`.

Confirme sua localização com `pwd`:

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory}
Qual comando confirma a localização atual do shell depois de `cd`?

::option[`cd`]{#cd-command explanation="`cd` muda o diretório atual, mas normalmente não exibe o caminho completo resultante. Use `pwd` para confirmá-lo."}
::option[`ls`]{#ls-command explanation="`ls` exibe o conteúdo do diretório. Ele ajuda a inspecionar uma localização, mas `pwd` informa qual é essa localização."}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` exibe o diretório de trabalho atual e permite verificar para onde `cd` levou o shell."}
:::

## Navegação para um Subdiretório

Se você já estiver em um diretório e quiser entrar em um de seus subdiretórios, use um caminho relativo. Por exemplo, se sua localização atual for `/home/pete/Pictures` e ela contiver uma pasta chamada `Hawaii`, você poderá entrar nela com:

```bash
$ cd Hawaii
```

Observe que usamos apenas o nome da pasta. Isso funciona porque já estávamos em seu diretório pai, `/home/pete/Pictures`.

## Atalhos Essenciais de Navegação

Navegar usando caminhos completos pode ser cansativo. Felizmente, o shell oferece vários atalhos que agilizam bastante a movimentação.

- `.` (diretório atual): representa o diretório em que você está.
- `..` (diretório pai): leva você um nível acima, ao diretório que contém o atual.
- `~` (diretório pessoal): é um atalho para seu diretório pessoal, como `/home/pete`.
- `-` (diretório anterior): leva você de volta ao último diretório em que esteve.

Você pode usar esses atalhos com `cd`:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory}
Partindo de `/home/pete/Pictures`, qual comando leva a `/home/pete`?

::option[`cd .`]{#cd-current explanation="`.` representa o diretório atual. Esse comando mantém o shell em `/home/pete/Pictures`."}
::option[`cd -`]{#cd-previous explanation="`-` retorna ao diretório de trabalho anterior, que não é necessariamente o pai. Use `..` quando o destino estiver um nível acima."}
::option[`cd ..`]{#cd-parent .correct explanation="`..` representa o pai do diretório atual. O pai de `Pictures` é `/home/pete`."}
:::

:::single-choice{#return-to-previous-directory}
Qual comando retorna ao diretório usado imediatamente antes do atual?

::option[`cd -`]{#previous-directory .correct explanation="`cd -` muda para o diretório de trabalho anterior, que pode estar em qualquer parte do sistema de arquivos."}
::option[`cd ..`]{#parent-directory explanation="`cd ..` leva ao diretório pai. O diretório pai e o anterior nem sempre são o mesmo local."}
::option[`cd ~`]{#home-directory explanation="`cd ~` leva ao seu diretório pessoal. Ele não acompanha o diretório visitado imediatamente antes."}
:::

Experimente esses atalhos para se tornar mais eficiente na linha de comando.

## Exemplos Práticos de cd

Vá para seu diretório pessoal:

```bash
$ cd
```

Executar `cd` sem um argumento de diretório também leva você ao diretório pessoal.

Suba dois níveis:

```bash
$ cd ../..
```

Entre em um diretório cujo nome contém espaços colocando-o entre aspas:

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces}
Qual comando trata `Vacation Photos` como um único nome de diretório?

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="Sem aspas, o shell fornece `Vacation` e `Photos` como argumentos separados, e não como um único nome de diretório."}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="Colocar a linha inteira entre aspas faz o shell tratá-la como um único nome de comando. O comando deve ficar fora das aspas do caminho."}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="As aspas agrupam as duas palavras em um único argumento de caminho para `cd`."}
:::

Volte ao diretório anterior:

```bash
$ cd -
/home/pete/Documents
```

Para reforçar sua compreensão sobre a navegação em diretórios no Linux, experimente estes laboratórios práticos:

1. **[Comando cd do Linux: Mudança de Diretórios](https://labex.io/labs/linux-linux-cd-command-directory-changing-209733)** — Aprenda a usar `cd` para navegar com eficiência pelo sistema de arquivos, incluindo diferentes técnicas para mudar de diretório, compreender caminhos e explorar a estrutura de arquivos.
2. **[Navegação em Diretórios no Linux](https://labex.io/labs/linux-directory-navigation-387844)** — Teste suas habilidades básicas na linha de comando navegando por diretórios com comandos essenciais.
3. **[Configuração da Estrutura de um Novo Projeto](https://labex.io/labs/linux-setting-up-a-new-project-structure-387859)** — Pratique o gerenciamento de diretórios criando uma estrutura de projeto específica e navegando por ela com comandos essenciais como `mkdir` e `cd`.

## Resumo

Agora você sabe usar `cd` para alternar entre diretórios com caminhos completos e atalhos do shell.

1. Diferencie caminhos absolutos de caminhos relativos.
2. Mude de diretório e verifique o resultado com `pwd`.
3. Navegue para os diretórios pai, pessoal e anterior.
4. Entre em diretórios cujos nomes contêm espaços.
5. Reconheça erros comuns de caminho e permissão.
