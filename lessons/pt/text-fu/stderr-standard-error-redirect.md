---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "pt"
order_index: 3
title: "stderr (Erro Padrão)"
description: "Aprenda a redirecionar o erro padrão separadamente ou combiná-lo com a saída padrão no Bash."
meta_title: "stderr (Erro Padrão) - Text-Fu"
meta_description: "Aprenda a gerenciar o erro padrão no Linux. Conheça o descritor 2 e redirecione stderr para um arquivo ou /dev/null usando 2>, 2>&1 e &>."
meta_keywords: "stderr, erro padrão Linux, descritor stderr, arquivo stderr, redirecionar stderr, 2>, 2>&1, &>, /dev/null, tratamento de erros Bash"
---

Os programas normalmente gravam resultados comuns na saída padrão e diagnósticos em um fluxo separado chamado erro padrão, ou **stderr**. Manter os fluxos separados permite salvar dados úteis sem misturar mensagens de erro.

## Separação dos Resultados Comuns e dos Erros

Considere um comando cujo caminho não existe:

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

O operador `>` redireciona apenas stdout. O diagnóstico é gravado em stderr, que continua conectada ao terminal. Enquanto isso, o shell cria ou trunca `peanuts.txt` para stdout, mesmo que `ls` não produza um resultado comum.

Os fluxos padrão usam convencionalmente estes descritores de arquivo:

- `0`: stdin (entrada padrão)
- `1`: stdout (saída padrão)
- `2`: stderr (erro padrão)

:::single-choice{#stderr-not-in-stdout-file}
Por que o erro de `ls /missing > results.txt` normalmente permanece no terminal?

::option[`>` redireciona stdout, enquanto o diagnóstico é gravado em stderr.]{#stderr-separate-stream .correct explanation="Um `>` simples altera apenas o descritor de arquivo 1. O descritor 2 mantém seu destino atual no terminal."}
::option[`ls` espera o arquivo ser fechado antes de mostrar qualquer erro.]{#stderr-waits-for-close explanation="A questão não é o momento da saída. As mensagens comuns e de diagnóstico usam fluxos diferentes."}
::option[`results.txt` pode armazenar texto comum, mas não diagnósticos.]{#stderr-file-capability explanation="Um arquivo comum pode armazenar qualquer um dos fluxos. A linha de comando simplesmente não redirecionou stderr para ele."}
:::

## Redirecionamento de stderr com 2>

Coloque o descritor de arquivo `2` antes de `>` para redirecionar stderr:

```bash
$ ls /fake/directory 2> errors.txt
```

O shell cria ou trunca `errors.txt` e o conecta ao descritor 2. Stdout mantém seu destino anterior. Use `2>> errors.txt` quando a saída de erro deva ser acrescentada.

:::single-choice{#stderr-to-error-file}
Qual comando substitui `errors.log` pelos diagnósticos de `find /restricted`, mantendo stdout em seu destino atual?

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="Um `>` simples redireciona o descritor 1; portanto, ele captura resultados comuns, não especificamente os diagnósticos."}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="O operador de menor fornece o arquivo como stdin. Ele não captura nenhum dos fluxos de saída."}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="O `2` inicial seleciona stderr, e `>` cria ou trunca o destino desse fluxo."}
:::

## Combinação de stdout e stderr

Para colocar os dois fluxos de saída em um arquivo, primeiro redirecione stdout e depois duplique stderr para o destino atual de stdout:

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

Os redirecionamentos são processados da esquerda para a direita:

1. `> combined.txt` conecta stdout ao arquivo.
2. `2>&1` conecta stderr ao destino para o qual stdout aponta naquele momento.

Inverter a ordem muda o resultado:

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

Aqui, stderr primeiro duplica o destino original de stdout no terminal. Depois, stdout muda para `regular.txt`; assim, os dois fluxos terminam em lugares diferentes.

:::single-choice{#stderr-combine-order}
Qual redirecionamento do Bash envia stdout e stderr de `command` para `all.log`?

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="Essa forma primeiro conecta stderr ao destino antigo de stdout e depois redireciona somente stdout para o arquivo. Os fluxos terminam separados."}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="Essa forma envia stderr para `all.log`, mas descarta stdout. Ela não combina os dois fluxos no arquivo."}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="Stdout vai primeiro para o arquivo, e stderr então duplica esse destino atual de stdout."}
:::

O Bash também oferece `&>` como uma sintaxe mais curta para substituir um arquivo com os dois fluxos:

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

Use `&>>` para acrescentar os dois fluxos no Bash. É útil reconhecer a forma explícita `> file 2>&1`, pois ela também aparece em scripts e documentações do shell.

:::single-choice{#stderr-bash-short-form}
Qual comando do Bash acrescenta stdout e stderr de `build` a `build.log`?

::option[`build &> build.log`]{#replace-both-build explanation="`&>` do Bash redireciona os dois fluxos, mas substitui um arquivo existente em vez de acrescentar a ele."}
::option[`build 2>> build.log`]{#append-errors-build explanation="Essa forma acrescenta apenas stderr. Stdout mantém seu destino anterior."}
::option[`build &>> build.log`]{#append-both-build .correct explanation="No Bash, `&>>` acrescenta os descritores de arquivo 1 e 2 ao mesmo destino."}
:::

## Descarte Consciente de um Fluxo

`/dev/null` é um dispositivo especial que descarta os dados gravados nele. Redirecione stderr para ele apenas quando tiver determinado que os diagnósticos são esperados e desnecessários:

```bash
$ ls /fake/directory 2> /dev/null
```

Isso não faz o comando ter sucesso nem altera seu status de saída; apenas oculta o fluxo de diagnóstico. Durante uma investigação, preserve ou exiba stderr em vez de descartar as informações necessárias.

:::single-choice{#stderr-dev-null-effect}
O que `check-data 2> /dev/null` altera?

::option[Descarta stdout e transforma todos os erros em sucesso.]{#discard-stdout-success explanation="O descritor 2 é stderr, não stdout, e o redirecionamento não reescreve o status de saída do programa."}
::option[Descarta stderr, mas não força um status de saída bem-sucedido.]{#discard-stderr-only .correct explanation="O redirecionamento muda o destino dos diagnósticos. O programa continua determinando seu próprio status de sucesso ou falha."}
::option[Salva stderr em um arquivo oculto chamado `/dev/null`.]{#save-dev-null explanation="`/dev/null` descarta os dados gravados; ele não é um arquivo de armazenamento para recuperação posterior."}
:::

Para praticar o gerenciamento dos três fluxos padrão, experimente este laboratório:

1. **[Redirecionamento de Entrada e Saída no Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** — Neste laboratório, você aprenderá a redirecionar entrada e saída no shell do Linux. Você praticará o controle do fluxo de dados dos comandos manipulando a saída padrão (stdout), o erro padrão (stderr) e a entrada padrão (stdin) com operadores como `>`, `>>`, `2>` e o comando `tee`.

## Resumo

Agora você sabe manter os diagnósticos separados ou combiná-los com a saída comum dos comandos.

1. Reconheça stderr como o descritor de arquivo 2.
2. Substitua ou acrescente a um log de erros com `2>` ou `2>>`.
3. Aplique vários redirecionamentos da esquerda para a direita.
4. Combine os dois fluxos de saída com uma sintaxe consciente.
5. Descarte diagnósticos somente quando sua perda for aceitável.
