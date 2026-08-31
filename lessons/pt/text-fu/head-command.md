---
lesson_id: "head-command"
course_id: "text-fu"
lang: "pt"
order_index: 8
title: "head"
description: "Aprenda a exibir uma quantidade controlada de linhas ou bytes do início de uma entrada."
meta_title: "head - Text-Fu"
meta_description: "Aprenda a usar o comando head do Linux para visualizar o início de um arquivo e controlar a quantidade de linhas ou bytes mostrados."
meta_keywords: "comando head, head Linux, visualizar início arquivo, tutorial Linux, comandos Linux, Linux para iniciantes, head -n, arquivos texto, linha de comando"
---

O comando `head` exibe o início de um arquivo ou fluxo de entrada. Ele é útil para verificar cabeçalhos, visualizar dados estruturados ou obter uma amostra da saída sem mostrar tudo.

## Exibição das Dez Primeiras Linhas

Sem uma opção de quantidade, `head` mostra as 10 primeiras linhas de cada arquivo indicado:

```bash
$ head events.log
```

O arquivo não é modificado. Se tiver menos de 10 linhas, todas as linhas disponíveis serão mostradas.

:::single-choice{#head-default-lines}
O que `head events.log` mostra por padrão?

::option[As 10 últimas linhas, ou todas as linhas se o arquivo for menor.]{#head-last-ten explanation="Exibir o final da entrada é a função de `tail`. `head` seleciona a partir do início."}
::option[As 10 primeiras linhas, ou todas as linhas se o arquivo for menor.]{#head-first-ten .correct explanation="Sem uma opção de quantidade, `head` seleciona até as dez primeiras linhas da entrada."}
::option[Apenas a primeira linha, independentemente do tamanho do arquivo.]{#head-first-one explanation="Uma linha exige uma quantidade explícita, como `-n 1`; a quantidade padrão é dez."}
:::

## Escolha da Quantidade de Linhas

Use `-n NUMBER` para escolher quantas linhas mostrar:

```bash
$ head -n 15 events.log
```

O GNU `head` também aceita a forma compacta `-15`, mas `-n 15` deixa mais claro o significado da opção.

:::single-choice{#head-five-lines}
Qual comando exibe as cinco primeiras linhas de `report.txt`?

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="A opção `-c` conta bytes, não linhas; portanto, ela pode parar no meio da primeira linha."}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="A opção `-n` seleciona uma quantidade de linhas, e `5` solicita as cinco primeiras."}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="Esse comando exibe as cinco linhas finais do arquivo, não o início."}
:::

## Escolha da Quantidade de Bytes

Use `-c NUMBER` quando precisar de bytes, não de linhas completas:

```bash
$ head -c 20 archive.bin
```

Esse comando mostra os 20 primeiros bytes. A saída pode terminar no meio de uma linha de texto ou, em um texto multibyte, no meio de um caractere codificado. Use o modo de linhas para visualizações comuns de texto.

:::single-choice{#head-first-bytes}
Qual comando grava os 100 primeiros bytes de `payload.bin` em stdout?

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="A opção `-c` seleciona uma quantidade de bytes; portanto, são solicitados os primeiros 100 bytes disponíveis."}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="A opção `-n` conta linhas, não bytes. Ela pode produzir muito mais ou muito menos que 100 bytes."}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="Esse comando seleciona a posição 100 de cada linha, não os 100 primeiros bytes da entrada inteira."}
:::

## Leitura de stdin e de Vários Arquivos

Quando nenhum arquivo é fornecido, `head` lê stdin:

```bash
$ generate-report | head -n 5
```

Quando vários arquivos são indicados, `head` normalmente acrescenta um cabeçalho que identifica a saída de cada um:

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

Use `-q` para suprimir esses cabeçalhos ou `-v` para mostrar um cabeçalho até mesmo para um único arquivo.

:::single-choice{#head-pipeline-preview}
Em `generate-report | head -n 5`, o que `head` lê?

::option[Stdout de `generate-report` por meio de stdin.]{#head-pipe-input .correct explanation="O pipe conecta stdout do produtor a stdin de `head`, da qual são selecionadas as cinco primeiras linhas."}
::option[Os cinco primeiros nomes de arquivos do diretório atual.]{#head-directory-names explanation="Nenhum comando de listagem de diretório está envolvido. `head` recebe um fluxo pelo pipeline."}
::option[Cinco bytes de um arquivo chamado `generate-report`.]{#head-producer-file explanation="O lado esquerdo é executado como comando, e `-n` conta linhas, não bytes."}
:::

:::single-choice{#head-suppress-filename-headers}
Qual opção suprime os cabeçalhos com nomes de arquivos quando `head` lê vários arquivos?

::option[`-v`]{#head-verbose explanation="A opção `-v` solicita cabeçalhos mesmo quando há apenas um arquivo, o oposto da supressão."}
::option[`-c`]{#head-byte-option explanation="A opção `-c` altera a unidade de seleção para bytes. Ela não controla os cabeçalhos com nomes."}
::option[`-q`]{#head-quiet .correct explanation="A opção `-q`, ou quiet, impede que `head` mostre rótulos de cabeçalhos para cada arquivo."}
:::

Para praticar a visualização do início dos arquivos, experimente estes laboratórios:

1. **[Comando head do Linux: Exibição do Início de Arquivos](https://labex.io/labs/linux-linux-head-command-file-beginning-display-214302)** — Aprenda a usar `head` para exibir as linhas iniciais de arquivos de texto e alterar a quantidade de linhas.
2. **[Visualização de Arquivos de Log e Configuração no Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** — Pratique habilidades para visualizar e percorrer arquivos de texto, inclusive logs e configurações do sistema, que frequentemente exigem comandos como `head`.
3. **[Detecção Rápida de Ameaças](https://labex.io/labs/linux-rapid-threat-detection-387930)** — Aplique seu conhecimento de `head` e `tail` para extrair e analisar rapidamente entradas de logs em um cenário de segurança.

## Resumo

Agora você sabe visualizar o início de arquivos e saídas de comandos com `head`.

1. Use a visualização padrão das dez primeiras linhas.
2. Selecione uma quantidade de linhas com `-n`.
3. Selecione uma quantidade de bytes com `-c` quando apropriado.
4. Leia stdin em um pipeline.
5. Controle os cabeçalhos ao exibir vários arquivos.
