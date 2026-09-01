---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "pt"
order_index: 15
title: "wc e nl"
description: "Aprenda a contar linhas, palavras, bytes ou caracteres com wc e numerar linhas com nl."
meta_title: "wc e nl - Text-Fu"
meta_description: "Domine os comandos wc e nl no Linux. Aprenda a contar palavras, linhas, bytes e caracteres e a acrescentar números às linhas sem editar o arquivo."
meta_keywords: "comando wc, comando nl, contagem palavras Linux, contar palavras arquivo Linux, números linhas Linux, análise arquivos, processamento texto Linux"
---

O comando `wc` conta propriedades de fluxos de texto, enquanto `nl` grava a entrada com números de linha gerados. Os dois leem arquivos ou stdin e enviam seus resultados a stdout.

## Leitura da Saída Padrão de wc

Sem uma opção de contagem, `wc` mostra a quantidade de caracteres de nova linha, palavras e bytes, seguida do nome do arquivo quando um foi fornecido:

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

Da esquerda para a direita:

1. `2` caracteres de nova linha, informados como linhas.
2. `3` palavras delimitadas por espaços em branco.
3. `15` bytes neste exemplo ASCII.

Uma linha final de texto sem uma nova linha de terminação não é contada por `wc -l`, pois essa opção conta caracteres de nova linha, não linhas percebidas visualmente.

:::single-choice{#wc-default-columns} Na saída padrão de `wc file.txt`, o que os três primeiros números representam?

::option[Linhas, palavras e bytes, nessa ordem.]{#wc-lines-words-bytes .correct explanation="A saída padrão de `wc` informa a quantidade de novas linhas, palavras e bytes antes do nome do arquivo."}
::option[Bytes, palavras e linhas, nessa ordem.]{#wc-bytes-words-lines explanation="Essas são as mesmas medidas na ordem errada. A quantidade de linhas aparece primeiro."}
::option[Arquivos, caracteres e parágrafos, nessa ordem.]{#wc-files-characters-paragraphs explanation="As colunas padrão não contam arquivos nem parágrafos, e a terceira medida padrão é a quantidade de bytes."}
:::

## Solicitação de uma Única Contagem

Selecione apenas a medida necessária:

- `-l`: conta caracteres de nova linha.
- `-w`: conta palavras.
- `-c`: conta bytes.
- `-m`: conta caracteres de acordo com o locale atual.

Por exemplo:

```bash
$ wc -w colors.txt
3 colors.txt
```

As quantidades de bytes e caracteres são iguais em textos ASCII, mas podem ser diferentes em codificações multibyte como UTF-8. Quando stdin é usada sem um operando de nome de arquivo, `wc` normalmente omite o rótulo do nome:

```bash
$ printf 'one two\n' | wc -w
2
```

:::single-choice{#wc-word-count-only} Qual comando informa apenas a quantidade de palavras de `essay.txt`?

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="A opção `-l` informa caracteres de nova linha, não palavras."}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="A opção `-w` seleciona a medida de contagem de palavras."}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="A opção `-c` informa bytes, não palavras delimitadas por espaços em branco."}
:::

:::single-choice{#wc-characters-not-bytes} Qual opção solicita que `wc` conte caracteres, não bytes, no locale atual?

::option[`-m`]{#wc-character-option .correct explanation="A opção `-m` informa caracteres, que podem diferir de bytes em textos multibyte."}
::option[`-c`]{#wc-byte-option explanation="A opção `-c` informa bytes. Um caractere pode ocupar vários bytes em codificações como UTF-8."}
::option[`-w`]{#wc-word-option explanation="A opção `-w` conta palavras, não caracteres ou bytes."}
:::

Quando vários arquivos são indicados, `wc` mostra um resultado para cada um e uma linha `total`. O GNU `wc -L` informa a largura máxima de exibição de uma linha da entrada.

## Numeração de Linhas Não Vazias com nl

Por padrão, `nl` numera as linhas não vazias do corpo lógico da entrada. Suponha que `notes.txt` contenha uma segunda linha vazia:

```text
alpha

beta
```

A linha vazia é preservada, mas não recebe um número:

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl` grava uma saída numerada; ele não modifica `notes.txt`.

:::single-choice{#nl-default-blank-lines} Como `nl notes.txt` trata as linhas vazias do corpo por padrão?

::option[Omite completamente cada linha vazia da saída.]{#nl-omit-blank explanation="A linha vazia permanece na saída, mas não recebe um número por padrão."}
::option[Preserva-as sem números de linha.]{#nl-preserve-unnumbered .correct explanation="O estilo padrão do corpo numera linhas não vazias e mantém as linhas vazias sem numeração."}
::option[Numera-as na mesma sequência das linhas não vazias.]{#nl-number-blank-default explanation="Numerar todas as linhas do corpo exige outro estilo, como `-ba`."}
:::

## Numeração de Todas as Linhas

Use `-ba` para selecionar o estilo de corpo `a`, que numera todas as linhas:

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

Outras opções controlam a formatação. Por exemplo, `-w 3` define a largura do campo numérico, e `-s ': '` muda o separador depois do número.

:::single-choice{#nl-number-all-lines} Qual comando numera todas as linhas do corpo de `notes.txt`, inclusive as vazias?

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="Essa forma muda a largura do campo numérico, mas mantém a regra padrão de numerar somente linhas não vazias."}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="A opção `-b` escolhe o estilo do corpo, e o estilo `a` numera todas as linhas."}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="Esse comando mostra uma contagem de caracteres de nova linha e não reproduz o arquivo com números."}
:::

Para praticar a contagem e a numeração de textos, experimente estes laboratórios:

1. **[Comando wc do Linux: Contagem de Texto](https://labex.io/labs/linux-linux-wc-command-text-counting-219200)** — Pratique a contagem de palavras, linhas e caracteres em arquivos de texto com `wc`.
2. **[Comando nl do Linux: Numeração de Linhas](https://labex.io/labs/linux-linux-nl-command-line-numbering-210988)** — Aprenda a numerar as linhas dos arquivos com `nl`.
3. **[Contagem e Ordenação de Palavras](https://labex.io/labs/linux-word-count-and-sorting-388125)** — Aplique `wc` para contar linhas, palavras e caracteres e combine-o com ordenação em análises práticas.

## Resumo

Agora você sabe medir fluxos de texto e acrescentar números de linha visíveis sem editar a origem.

1. Interprete as colunas padrão de linhas, palavras e bytes de `wc`.
2. Selecione uma contagem com `-l`, `-w`, `-c` ou `-m`.
3. Diferencie a quantidade de bytes da quantidade de caracteres.
4. Numere linhas não vazias com o comportamento padrão de `nl`.
5. Numere também as linhas vazias com `nl -ba`.
