---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "pt"
order_index: 14
title: "uniq (Único)"
description: "Aprenda a agrupar, contar ou filtrar grupos adjacentes de linhas iguais com uniq."
meta_title: "uniq (Único) - Text-Fu"
meta_description: "Explore o comando uniq do Linux para filtrar linhas duplicadas adjacentes. Aprenda as opções -c, -u e -d e sua combinação com sort."
meta_keywords: "comando uniq, uniq Linux, remover duplicatas, sort uniq, processamento texto, limpeza dados, tutorial Linux"
---

O comando `uniq` compara cada linha de entrada com a linha anterior. Ele pode agrupar, contar ou selecionar grupos adjacentes de linhas iguais, mas não pesquisa o arquivo inteiro por duplicatas separadas.

## Agrupamento de Linhas Duplicadas Adjacentes

Suponha que `reading.txt` contenha valores agrupados:

```plaintext
book
book
paper
paper
article
article
magazine
```

Execute `uniq` sem opção de filtro para mostrar uma linha representativa de cada grupo adjacente:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

O arquivo de entrada permanece inalterado, pois o resultado vai para stdout.

:::single-choice{#uniq-collapse-adjacent}
O que `uniq reading.txt` faz por padrão?

::option[Ordena o arquivo inteiro e remove todos os valores repetidos.]{#uniq-auto-sort explanation="`uniq` preserva a ordem da entrada e não a ordena. Cópias separadas permanecem em grupos diferentes."}
::option[Mostra uma linha de cada grupo adjacente de linhas iguais.]{#uniq-one-per-group .correct explanation="Por padrão, `uniq` agrupa linhas iguais consecutivas em uma única linha de saída."}
::option[Exclui as linhas duplicadas diretamente de `reading.txt`.]{#uniq-edit-file explanation="O comando grava o texto filtrado em stdout por padrão e não edita o arquivo de entrada."}
:::

## Contagem de Grupos Adjacentes

Use `-c` para prefixar cada grupo de saída com sua quantidade de linhas consecutivas:

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Essas quantidades representam o tamanho de cada sequência, não os totais globais, a menos que todas as linhas iguais tenham sido agrupadas primeiro.

:::single-choice{#uniq-count-groups}
O que a contagem de `uniq -c` representa?

::option[A quantidade de caracteres de cada linha de entrada.]{#uniq-character-count explanation="Contar caracteres não é a finalidade de `uniq -c`; ferramentas como `wc` calculam totais de caracteres e bytes."}
::option[A quantidade de linhas iguais consecutivas em cada grupo.]{#uniq-consecutive-count .correct explanation="`-c` prefixa cada grupo adjacente condensado com a quantidade de linhas que ele continha."}
::option[A quantidade total de linhas correspondentes em qualquer parte do arquivo.]{#uniq-global-count explanation="Linhas iguais separadas formam grupos distintos, a menos que os dados sejam ordenados ou agrupados primeiro."}
:::

## Seleção de Grupos Únicos ou Repetidos

Use `-u` para mostrar apenas os grupos que contêm exatamente uma linha:

```bash
$ uniq -u reading.txt
magazine
```

Use `-d` para mostrar uma linha representativa de cada grupo adjacente que contém mais de uma:

```bash
$ uniq -d reading.txt
book
paper
article
```

O GNU `uniq -D` mostra todas as linhas dos grupos repetidos, enquanto `-d` minúsculo mostra o valor de cada grupo uma vez.

:::single-choice{#uniq-only-singletons}
Qual comando mostra apenas os grupos adjacentes que ocorrem exatamente uma vez?

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="Essa forma mostra todos os grupos com uma contagem, incluindo repetidos e únicos."}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="`-d` minúsculo mostra uma linha de cada grupo repetido, a seleção oposta."}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="A opção `-u` seleciona grupos cuja sequência adjacente possui exatamente uma linha."}
:::

:::single-choice{#uniq-one-per-duplicate-group}
Qual comando mostra uma linha de cada grupo adjacente que aparece mais de uma vez?

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="A opção `-d` seleciona grupos adjacentes repetidos e emite uma linha representativa de cada um."}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="`-D` maiúsculo do GNU mostra todas as linhas pertencentes aos grupos repetidos, não apenas uma representante."}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="A opção `-u` seleciona grupos únicos, não os repetidos."}
:::

## Agrupamento de Duplicatas Separadas

Se linhas iguais estiverem separadas, elas formarão grupos diferentes:

```plaintext
book
paper
book
paper
article
magazine
article
```

Executar `uniq` nesse arquivo produz um resultado que pode surpreender:

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

Nenhuma linha é agrupada porque os valores vizinhos são diferentes. Ordene primeiro quando a mudança de ordem for aceitável e você quiser reunir linhas completas iguais:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Use um locale e uma política de comparação consistentes nas duas etapas. `sort -u reading.txt` também pode ordenar e preservar uma linha para cada chave igual em um único comando.

:::single-choice{#uniq-separated-duplicates}
Linhas iguais estão espalhadas por `reading.txt`, e a ordem da saída pode mudar. Qual pipeline produz uma cópia ordenada de cada linha completa distinta?

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="A ordenação agrupa linhas completas iguais, e `uniq` reduz cada grupo adjacente a uma única linha."}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="`uniq` é executado antes que linhas iguais separadas se tornem adjacentes; por isso, a ordenação posterior ainda pode deixar duplicatas."}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="Essa forma conta os grupos adjacentes existentes e limita a saída. Ela não agrupa globalmente duplicatas separadas."}
:::

`uniq` lê stdin quando nenhum arquivo de entrada é indicado, motivo pelo qual se encaixa naturalmente depois de `sort`. Opções GNU como `-i` podem ignorar maiúsculas e minúsculas, enquanto `-f`, `-s` e `-w` podem ignorar ou limitar regiões de comparação; use-as apenas quando a igualdade deva ser definida por parte de cada linha.

Para praticar o agrupamento, a contagem e a filtragem de duplicatas, experimente estes laboratórios:

1. **[Comando uniq do Linux: Filtragem de Duplicatas](https://labex.io/labs/linux-linux-uniq-command-duplicate-filtering-219199)** — Aprenda a combinar `uniq` com `sort` para identificar, filtrar e analisar linhas duplicadas.
2. **[Comando sort do Linux: Ordenação de Texto](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** — Pratique a organização de linhas com `sort`, uma etapa importante antes do uso eficaz de `uniq`.
3. **[Contagem e Ordenação de Palavras](https://labex.io/labs/linux-word-count-and-sorting-388125)** — Aprenda as ferramentas essenciais de processamento de texto do Linux `wc` (contagem de palavras) e `sort` neste desafio prático. Aprenda a contar linhas, palavras e caracteres, encontrar padrões frequentes e ordenar dados com eficiência em várias tarefas de análise de texto.

## Resumo

Agora você sabe analisar grupos adjacentes de linhas iguais com `uniq`.

1. Agrupe cada grupo adjacente duplicado em uma linha.
2. Conte ocorrências consecutivas com `-c`.
3. Selecione grupos únicos com `-u`.
4. Selecione grupos repetidos com `-d` ou `-D` do GNU.
5. Ordene primeiro quando duplicatas separadas precisarem ser agrupadas.
