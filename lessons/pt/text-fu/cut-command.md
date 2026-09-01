---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "pt"
order_index: 6
title: "cut"
description: "Aprenda a selecionar posições de caracteres ou campos delimitados de cada linha com cut."
meta_title: "cut - Text-Fu"
meta_description: "Aprenda a usar o comando cut do Linux para extrair trechos específicos de texto por posição de caractere ou campo, inclusive com delimitadores personalizados."
meta_keywords: "comando cut, processamento de texto Linux, extrair texto, cut f, campos cut, tutorial Linux, exemplos cut, delimitadores"
---

O comando `cut` seleciona posições de caracteres ou campos especificados em cada linha da entrada. Ele funciona melhor com textos de estrutura consistente cujos delimitadores e posições de campos são conhecidos.

Crie um pequeno arquivo separado por tabulações para os exemplos. `printf` interpreta `\t` como uma tabulação literal e `\n` como uma nova linha:

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## Seleção de Posições de Caracteres

Use `-c LIST` para selecionar posições de cada linha. As posições começam em 1:

```bash
$ cut -c 1 team.tsv
n
a
b
```

A lista pode conter posições individuais e intervalos:

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

Espaços, tabulações e sinais de pontuação também ocupam posições. `cut` processa cada linha independentemente.

:::single-choice{#cut-first-character} Qual comando mostra o primeiro caractere de cada linha de `names.txt`?

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="A opção `-c` seleciona posições de caracteres, e a posição 1 é o primeiro caractere de cada linha."}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="A opção `-f` seleciona o primeiro campo delimitado por tabulação, que pode conter mais de um caractere."}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="A opção `-d` especifica um delimitador de campos e deve ser combinada com a seleção de campos. Ela não seleciona uma posição de caractere."}
:::

## Seleção de Campos Delimitados por Tabulação

Use `-f LIST` para selecionar campos. O delimitador padrão é uma tabulação:

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

Assim como na seleção de caracteres, uma lista pode incluir valores como `1`, `1,3`, `2-4`, `-3` ou `2-`.

:::single-choice{#cut-second-tab-field} Qual comando mostra o segundo campo delimitado por tabulação de cada linha de `team.tsv`?

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="Esse comando seleciona a segunda posição de caractere de cada linha, não o segundo campo separado por tabulação."}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="Sem `-d`, o modo de campos usa a tabulação como delimitador, e `-f 2` seleciona o segundo campo."}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="Esse comando tenta usar `2` como delimitador, mas não fornece uma lista de campos. Ele não seleciona o campo 2."}
:::

## Escolha de um Delimitador Personalizado

Use `-d CHARACTER` com `-f` quando os campos utilizarem outro delimitador. Este exemplo cria dados separados por ponto e vírgula:

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

O delimitador dessa forma é um único caractere. Coloque `;` entre aspas, pois um ponto e vírgula sem aspas possui significado de controle no shell.

:::single-choice{#cut-semicolon-role-field} Qual comando mostra o segundo campo delimitado por ponto e vírgula de `team.txt`?

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="Esse comando seleciona campos separados por dois-pontos, mas o arquivo usa ponto e vírgula."}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="O ponto e vírgula entre aspas define o delimitador, e `-f 2` seleciona o segundo campo de cada linha."}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="Essa forma mistura a seleção de caracteres com um argumento de campo inválido. O delimitador deve vir depois de `-d`, e o número do campo depois de `-f`."}
:::

## Tratamento de Linhas sem o Delimitador

No modo de campos, `cut` normalmente mostra uma linha inalterada quando ela não contém o delimitador. Acrescente `-s` para suprimir essas linhas:

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

Isso não valida um arquivo CSV genérico. CSV pode conter delimitadores entre aspas, novas linhas incorporadas e regras de escape que uma divisão por um único caractere não compreende; use uma ferramenta compatível com CSV para esses dados.

:::single-choice{#cut-suppress-undelimited} O que `-s` faz em `cut -d ':' -f 1`?

::option[Classifica os campos selecionados antes de mostrá-los.]{#cut-s-sort explanation="`cut` não classifica a entrada, e `-s` não tem relação com a ordenação."}
::option[Trata delimitadores consecutivos como um único separador.]{#cut-s-squeeze explanation="`cut` não usa `-s` para agrupar delimitadores. Campos vazios continuam sendo posições significativas."}
::option[Suprime as linhas que não contêm o delimitador selecionado.]{#cut-s-suppress .correct explanation="No modo de campos, `-s` impede que as linhas sem delimitador sejam mostradas inalteradas."}
:::

## Leitura de stdin

Quando nenhum arquivo é indicado, ou quando `-` é usado como operando de entrada, `cut` lê stdin. Isso o torna uma etapa natural de um pipeline:

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input} Em `generate-data | cut -d ':' -f 1`, de onde `cut` lê sua entrada?

::option[De stdout de `generate-data` por meio do pipe.]{#cut-pipe-stdin .correct explanation="O pipe conecta stdout do produtor a stdin de `cut`, e nenhum arquivo de entrada separado foi indicado."}
::option[De um arquivo cujo nome literal é `generate-data`.]{#cut-pipe-file explanation="`generate-data` é executado como o comando à esquerda do pipeline. Ele não é fornecido a `cut` como nome de arquivo."}
::option[Do fluxo de erro padrão de `cut`.]{#cut-pipe-stderr explanation="Um pipe comum alimenta a entrada padrão com stdout do comando anterior, não com stderr de `cut`."}
:::

Para praticar a seleção por posição e campo, experimente estes laboratórios:

1. **[Comando cut do Linux: Recorte de Texto](https://labex.io/labs/linux-linux-cut-command-text-cutting-219187)** — Este laboratório oferece uma introdução prática e direta ao comando `cut`, permitindo que você pratique a extração de colunas ou campos específicos de arquivos de texto, exatamente como apresentado na lição.
2. **[Controle de Sequência e Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** — Aumente sua eficiência na linha de comando aprendendo a controlar sequências de execução de comandos, usar pipelines e aproveitar ferramentas avançadas de processamento de texto como `cut`, `grep`, `wc`, `sort` e `uniq`.

## Resumo

Agora você sabe selecionar posições previsíveis de textos orientados por linhas com `cut`.

1. Selecione posições ou intervalos de caracteres.
2. Extraia campos delimitados por tabulação com `-f`.
3. Forneça um delimitador de um caractere com `-d`.
4. Suprima linhas sem delimitador quando apropriado.
5. Leia texto estruturado de arquivos ou stdin.
