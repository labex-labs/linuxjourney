---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "pt"
order_index: 9
title: "tail"
description: "Aprenda a visualizar o final de uma entrada e acompanhar arquivos conforme novos conteúdos são acrescentados."
meta_title: "tail - Text-Fu"
meta_description: "Aprenda a usar o comando tail do Linux para visualizar o final de arquivos e acompanhar logs em tempo real com as opções tail -f e tail -F."
meta_keywords: "comando tail, tail Linux, tail -f, visualizar logs, monitorar logs, tutorial Linux, Linux para iniciantes, monitoramento arquivos"
---

O comando `tail` exibe o final de um arquivo ou fluxo de entrada. Ele também pode permanecer ativo e mostrar dados acrescentados a um arquivo, o que é útil ao observar logs.

## Exibição das Dez Últimas Linhas

Sem uma opção de quantidade, `tail` mostra as 10 últimas linhas de cada arquivo indicado:

```bash
$ tail application.log
```

Se o arquivo tiver menos de 10 linhas, todas as linhas disponíveis serão mostradas. O arquivo em si não é alterado.

:::single-choice{#tail-default-lines}
O que `tail application.log` exibe por padrão?

::option[Até as 10 linhas iniciais do arquivo.]{#tail-first-ten explanation="O início de um arquivo é selecionado por `head`. `tail` trabalha a partir do final."}
::option[Todas as linhas acrescentadas depois que o comando é iniciado.]{#tail-follow-only explanation="O acompanhamento contínuo exige `-f` ou uma opção relacionada. `tail` sem opções mostra uma captura e termina."}
::option[Até as 10 linhas finais do arquivo.]{#tail-last-ten .correct explanation="Sem uma opção de quantidade, `tail` seleciona as dez últimas linhas, ou todas quando há menos."}
:::

## Escolha da Quantidade de Linhas ou Bytes

Use `-n NUMBER` para selecionar outra quantidade de linhas finais:

```bash
$ tail -n 20 application.log
```

Use `-c NUMBER` quando precisar dos bytes finais:

```bash
$ tail -c 100 payload.bin
```

O modo de bytes pode começar no meio de uma linha de texto ou de um caractere codificado; por isso, o modo de linhas costuma ser mais claro para textos.

:::single-choice{#tail-twenty-lines}
Qual comando exibe as 20 linhas finais de `application.log`?

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="A opção `-n` seleciona uma quantidade de linhas, e `tail` as obtém do final."}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="Esse comando seleciona 20 linhas do início, não do final."}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="A opção `-c` seleciona os 20 bytes finais, o que não equivale a 20 linhas."}
:::

## Início em uma Linha Específica

Uma quantidade com o prefixo `+` muda o significado: `tail -n +N` começa na linha N e mostra até o final.

```bash
$ tail -n +5 report.txt
```

Esse comando ignora as quatro primeiras linhas e começa na linha 5. Ele é útil para remover uma quantidade conhecida de linhas de cabeçalho de um fluxo.

:::single-choice{#tail-start-line-five}
Qual comando mostra `report.txt` a partir da linha 5?

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="A quantidade `+5` instrui `tail` a começar na linha 5 e continuar até o final."}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="Sem um sinal de adição, esse comando seleciona as cinco linhas finais, independentemente de seus números absolutos."}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="Essa não é a forma de início em uma linha de `tail`. Use `tail -n +5` para o intervalo solicitado."}
:::

## Acompanhamento de Dados Acrescentados

Com `-f`, `tail` mostra o final inicial e permanece ativo, exibindo os dados conforme são acrescentados:

```bash
$ tail -f application.log
```

Pressione `Ctrl+C` para interromper `tail` e retornar ao shell. Acompanhar um arquivo apenas exibe o conteúdo novo; isso não garante que o aplicativo produtor do log esteja saudável nem que todos os eventos relevantes usem esse arquivo.

:::single-choice{#tail-follow-file}
Qual comando mostra o final atual de `application.log` e continua aguardando conteúdo acrescentado?

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="A opção `-f` mantém `tail` ativo e exibe os dados acrescentados ao arquivo."}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="Esse comando inicialmente não mostra linhas e termina, pois nenhuma opção de acompanhamento foi fornecida."}
::option[`less application.log`]{#less-log explanation="`less` oferece paginação interativa, mas essa forma não permanece no modo de acompanhamento de `tail`."}
:::

## Acompanhamento de um Log Rotacionado pelo Nome

A rotação de logs pode renomear um arquivo antigo e criar um novo no caminho original. No GNU `tail`, `-F` equivale a acompanhar pelo nome e tentar novamente; assim, ele pode reabrir um arquivo substituído ou temporariamente ausente:

```bash
$ tail -F application.log
```

Use `-f` quando quiser acompanhar o arquivo atualmente aberto e `-F` quando for esperado que um log identificado pelo nome seja rotacionado. Esses são comportamentos do GNU; outras implementações podem ser diferentes.

:::single-choice{#tail-follow-rotated-name}
No GNU/Linux, qual opção é mais adequada para acompanhar `application.log` durante uma rotação comum por renomeação e recriação?

::option[`-n`]{#tail-rotation-lines explanation="A opção `-n` altera a quantidade de linhas exibidas. Ela não tenta novamente um caminho substituído."}
::option[`-c`]{#tail-rotation-bytes explanation="A opção `-c` altera a unidade de seleção para bytes. Ela não oferece acompanhamento consciente da rotação."}
::option[`-F`]{#tail-follow-name .correct explanation="`-F` do GNU acompanha pelo nome e tenta novamente, permitindo reabrir um log substituído ou temporariamente ausente."}
:::

Quando nenhum arquivo é indicado, `tail` lê stdin e pode selecionar o final da saída de um comando. Vários arquivos recebem cabeçalhos de identificação por padrão, como ocorre com `head`.

Para praticar a visualização e o acompanhamento do final dos arquivos, experimente estes laboratórios:

1. **[Comando tail do Linux: Exibição do Final de Arquivos](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** — Aprenda a usar `tail` para visualizar e monitorar o final de arquivos de texto, inclusive com `-f` para atualizações em tempo real.
2. **[Visualização de Arquivos de Log e Configuração no Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** — Pratique o uso de `tail`, junto com `cat` e `more`, para visualizar e percorrer logs e arquivos de configuração.
3. **[Detecção Rápida de Ameaças](https://labex.io/labs/linux-rapid-threat-detection-387930)** — Use `tail` para extrair e analisar rapidamente entradas recentes de logs em um cenário de segurança.

## Resumo

Agora você sabe inspecionar o final de arquivos e observar novos conteúdos acrescentados com `tail`.

1. Exiba as dez linhas finais por padrão.
2. Selecione explicitamente uma quantidade de linhas ou bytes.
3. Inicie a saída em uma linha numerada com `-n +N`.
4. Acompanhe conteúdo acrescentado com `-f` e pare com `Ctrl+C`.
5. Use `-F` do GNU quando um log identificado pelo nome puder ser rotacionado.
