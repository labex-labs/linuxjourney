---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "pt"
order_index: 4
title: "pipe e tee"
description: "Aprenda como pipelines conectam comandos e como tee salva um fluxo enquanto o encaminha."
meta_title: "pipe e tee - Text-Fu"
meta_description: "Explore pipe e tee no Linux. Aprenda a encadear comandos, redirecionar dados, exibir a saída na tela e salvá-la em um arquivo ao mesmo tempo."
meta_keywords: "pipe e tee Linux, pipe para tee, pipe Linux, comando tee, stdout, stdin, redirecionamento linha de comando, tutorial Linux"
---

Pipelines conectam pequenos comandos para que os dados fluam entre eles sem um arquivo intermediário. O comando `tee` pode copiar parte desse fluxo para um arquivo enquanto continua a encaminhá-lo.

## Conexão de Comandos com |

Suponha que uma listagem de diretório seja longa demais para ler de uma vez:

```bash
$ ls -la /etc
```

Coloque o operador de pipe, `|`, entre os comandos para conectar stdout do comando à esquerda a stdin do comando à direita:

```bash
$ ls -la /etc | less
```

O shell inicia os comandos do pipeline e organiza a conexão do fluxo. Os comandos podem trabalhar simultaneamente: `less` pode começar a ler antes que `ls` produza toda a listagem.

:::single-choice{#pipe-stream-connection}
Em `ls -la /etc | less`, quais fluxos `|` conecta por padrão?

::option[stdin de `ls` a stdout de `less`.]{#pipe-reversed-streams explanation="Essa resposta inverte o produtor e o consumidor. Os dados fluem da saída do comando à esquerda para a entrada do comando à direita."}
::option[stderr de `ls` aos dois fluxos de `less`.]{#pipe-stderr-both explanation="Um pipe simples não conecta stderr do comando à esquerda nem se dirige aos dois fluxos do comando à direita."}
::option[stdout de `ls` a stdin de `less`.]{#pipe-stdout-stdin .correct explanation="Um pipeline padrão conecta o descritor de arquivo 1 do comando à esquerda ao descritor 0 do comando à direita."}
:::

## Manutenção de stderr Separada

Um `|` simples transporta apenas stdout. Stderr do comando à esquerda mantém seu destino anterior, geralmente o terminal:

```bash
$ find /etc -name "*.conf" | less
```

Os caminhos correspondentes passam pelo pipe, enquanto os diagnósticos de permissão ainda podem aparecer diretamente no terminal. Redirecione stderr separadamente quando precisar de outro comportamento:

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr}
Em `find /etc -name "*.conf" | less`, para onde stderr de `find` normalmente vai quando não há outro redirecionamento?

::option[Para `less` pelo mesmo pipe de stdout.]{#pipe-errors-to-less explanation="O pipe comum conecta apenas stdout. Stderr não é combinada automaticamente com ela."}
::option[Para um arquivo chamado `stderr` no diretório atual.]{#pipe-errors-to-file explanation="Não há redirecionamento para um arquivo de erros; portanto, o shell não cria esse arquivo."}
::option[Para seu destino atual, geralmente o terminal.]{#pipe-errors-terminal .correct explanation="Como o descritor 2 permanece inalterado, os diagnósticos normalmente continuam conectados ao terminal."}
:::

## Cópia de um Fluxo com tee

`tee` lê stdin, grava uma cópia em cada arquivo indicado e também envia os mesmos dados a stdout:

```bash
$ ls | tee listing.txt
```

Aqui, `listing.txt` recebe a listagem e stdout de `tee` continua conectada ao terminal. Por padrão, `tee` cria ou trunca o arquivo indicado, assim como `>`.

:::single-choice{#tee-display-and-save}
Qual comando exibe a saída de `generate-report` e também substitui `report.txt` pela mesma saída?

::option[`generate-report > report.txt`]{#redirect-report-only explanation="Um redirecionamento simples grava o arquivo, mas não mantém uma cópia fluindo para o terminal."}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` copia stdin para `report.txt` e para stdout, que permanece conectada ao terminal neste pipeline."}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="Essa forma trata `generate-report` como nome de destino e tenta executar `report.txt` como comando. O produtor deve ficar à esquerda."}
:::

Use `-a` quando o conteúdo deva ser acrescentado ao arquivo em vez de substituí-lo:

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log}
Qual comando exibe a data atual e a acrescenta a `activity.log`?

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="A opção `-a` faz `tee` acrescentar ao arquivo enquanto continua copiando a entrada para stdout."}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="Sem `-a`, `tee` substitui o arquivo existente em vez de preservar suas entradas anteriores."}
::option[`date > activity.log`]{#redirect-replace-activity explanation="Essa forma substitui o arquivo e não envia uma cópia ao terminal. Ela não atende aos requisitos de acréscimo e exibição."}
:::

## Salvamento de um Resultado Intermediário

Coloque `tee` no meio de um pipeline para salvar um fluxo intermediário e continuar seu processamento:

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

Esse pipeline:

1. Produz a listagem longa completa.
2. Salva o fluxo completo em `etc-listing.txt`.
3. Envia o mesmo fluxo a `grep`, que mostra apenas as linhas que contêm `conf`.

O arquivo contém os dados anteriores ao filtro de `grep`. Se quiser salvar apenas as linhas filtradas, coloque `tee` depois de `grep`.

:::single-choice{#tee-before-filter-result}
O que `all.txt` contém depois que `produce | tee all.txt | grep error` termina com sucesso?

::option[Apenas as linhas correspondentes em `grep`.]{#tee-filtered-only explanation="`tee` é executado antes de `grep`; portanto, ele grava a entrada não filtrada, não o conjunto de correspondências posterior."}
::option[Apenas stderr de `produce`.]{#tee-producer-stderr explanation="Um pipe simples transporta stdout de `produce`. Stderr não é a entrada de `tee`."}
::option[Toda a stdout produzida antes da filtragem.]{#tee-complete-intermediate .correct explanation="`tee` salva cada byte recebido e depois envia o mesmo fluxo a `grep` para filtragem."}
:::

Para praticar pipelines e cópias de fluxos, experimente estes laboratórios:

1. **[Redirecionamento de Entrada e Saída no Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** — Pratique o controle do fluxo de dados dos comandos manipulando a saída padrão (stdout), o erro padrão (stderr) e a entrada padrão (stdin) com operadores como `>`, `>>`, `2>` e o comando `tee`.
2. **[Controle de Sequência e Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** — Aprenda a controlar sequências de comandos, usar pipelines e aproveitar ferramentas de texto como `cut`, `grep`, `wc`, `sort` e `uniq`.
3. **[Redirecionamento de Fluxos de Dados](https://labex.io/labs/linux-data-stream-redirection-17995)** — Aprenda a arte do redirecionamento de fluxos no Linux, incluindo a manipulação dos fluxos de entrada, saída e erro padrão, a combinação de saídas e o uso de `/dev/null`.

## Resumo

Agora você sabe conectar comandos e preservar pontos escolhidos em um fluxo de dados.

1. Encaminhe stdout de um comando para stdin de outro.
2. Redirecione stderr separadamente quando necessário.
3. Copie a entrada para um arquivo e para stdout com `tee`.
4. Acrescente com `tee -a` em vez de substituir o arquivo.
5. Posicione `tee` antes ou depois de um filtro conscientemente.
