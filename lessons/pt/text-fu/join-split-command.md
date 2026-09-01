---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "pt"
order_index: 11
title: "join e split"
description: "Aprenda a unir dois arquivos de texto ordenados por uma chave e dividir um arquivo em partes nomeadas."
meta_title: "join e split - Text-Fu"
meta_description: "Aprenda a usar join e split no Linux para combinar arquivos por campos comuns e dividir arquivos grandes em partes menores."
meta_keywords: "unir arquivos Linux, comando join Linux, comando split Linux, manipulação arquivos, linha de comando, processamento texto"
---

Os comandos `join` e `split` resolvem problemas diferentes de processamento de arquivos. `join` combina registros relacionados de duas entradas de texto ordenadas, enquanto `split` divide uma entrada em uma sequência de arquivos menores.

## União de Dois Arquivos pelo Primeiro Campo

Por padrão, `join` compara o primeiro campo separado por espaços em exatamente dois arquivos de entrada. Considere estes arquivos já ordenados:

`people.txt`:

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`:

```text
1 Doe
2 Doe
3 Sue
```

Una os registros cujos campos-chave são iguais:

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

A saída contém uma vez a chave compartilhada, seguida dos campos restantes do primeiro e do segundo arquivo. `join` processa dois arquivos de cada vez; ele não aceita três operandos comuns como uma união relacional de três vias.

:::single-choice{#join-default-key} Sem opções de campo, quais registros `join first.txt second.txt` combina?

::option[Linhas cujos primeiros campos separados por espaços são iguais.]{#join-first-fields .correct explanation="O comportamento padrão de `join` compara o campo 1 de cada uma das duas entradas ordenadas."}
::option[Linhas que ocupam o mesmo número físico nos arquivos.]{#join-line-numbers explanation="A correspondência se baseia nos valores dos campos-chave, não apenas nas posições dos registros."}
::option[Todas as linhas do primeiro arquivo com todas as linhas do segundo.]{#join-all-pairs explanation="`join` emite registros para chaves correspondentes, não um produto cartesiano irrestrito de todas as linhas."}
:::

## Ordenação das Chaves de União

Cada entrada precisa estar ordenada por seu campo de união com regras de comparação compatíveis. Para o campo 1 padrão, prepare cópias com `sort -k 1,1`:

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

Usar o mesmo locale na ordenação e na união mantém as regras de comparação consistentes. Não redirecione a saída de `sort` para seu próprio caminho de entrada, pois o shell truncaria esse arquivo primeiro.

:::single-choice{#join-sort-requirement} Que preparação `join` normalmente exige para uma correspondência confiável?

::option[Os dois arquivos precisam conter exatamente a mesma quantidade de linhas físicas.]{#join-equal-line-count explanation="As entradas podem ter tamanhos diferentes. As correspondências de chaves, não a quantidade igual de linhas, determinam a saída."}
::option[Os nomes dos dois arquivos precisam ficar lado a lado em ordem alfabética.]{#join-filename-order explanation="As chaves do conteúdo precisam estar ordenadas; a relação lexical entre os nomes dos arquivos é irrelevante."}
::option[Os dois arquivos precisam estar ordenados por seus campos de união com uma ordem compatível.]{#join-sorted-keys .correct explanation="`join` avança por chaves ordenadas; portanto, cada entrada deve usar uma ordem compatível com a comparação realizada."}
:::

## Seleção de Outros Campos de União

Use `-1 FIELD` para a chave do primeiro arquivo e `-2 FIELD` para a chave do segundo. Suponha que a primeira entrada contenha:

```text
John 1
Jane 2
Mary 3
```

A segunda contém:

```text
1 Doe
2 Doe
3 Sue
```

Depois de ordenar o primeiro arquivo pelo campo 2 e o segundo pelo campo 1, execute:

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Use `-t CHARACTER` quando um único caractere não vazio, como `:`, separar os campos. Opções como `-a 1` ou `-a 2` podem incluir linhas sem pares de uma das entradas; por padrão, a saída contém apenas chaves correspondentes.

:::single-choice{#join-different-fields} Quais opções unem o campo 2 do primeiro arquivo ao campo 1 do segundo?

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="Essa forma seleciona o campo 1 da primeira entrada e o campo 2 da segunda, o inverso do mapeamento solicitado."}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` escolhe o campo 2 do primeiro arquivo, e `-2 1` escolhe o campo 1 do segundo."}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="Essas opções se parecem com seletores de campo e delimitador de outras ferramentas. Elas não são os seletores de `join`."}
:::

## Divisão por Quantidade de Linhas

`split` grava partes consecutivas de uma entrada em arquivos separados. Ele não é o inverso de uma operação `join` baseada em chaves.

```bash
$ split large.txt
```

O comportamento padrão do GNU grava até 1.000 linhas por arquivo de saída e usa o prefixo `x`, produzindo nomes como `xaa`, `xab` e `xac`.

Use `-l NUMBER` para escolher a quantidade de linhas e acrescente um último operando para definir o prefixo:

```bash
$ split -l 500 large.txt part-
```

Isso produz `part-aa`, `part-ab` e assim por diante, com no máximo 500 linhas em cada parte.

:::single-choice{#split-lines-with-prefix} Qual comando divide `large.txt` em partes de no máximo 500 linhas, com nomes iniciados por `part-`?

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="A opção `-b` seleciona bytes; portanto, essas partes seriam muito menores que 500 linhas em um texto comum."}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` define a quantidade máxima de linhas, e o último operando fornece o prefixo dos arquivos de saída."}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` combina registros com chaves de dois arquivos. Ele não divide uma entrada em partes."}
:::

## Divisão por Tamanho

Use `-b SIZE` para dividir a entrada por tamanho em bytes. Nesse contexto, sufixos do GNU como `K`, `M` e `G` representam potências de 1024:

```bash
$ split -b 10M archive.bin chunk-
```

Esse comando solicita partes de 10 mebibytes, com exceção de uma possível parte final menor. `split` não cria um manifesto nem metadados de remontagem; preserve a ordem dos sufixos e concatene as partes nessa ordem quando a reconstrução for apropriada.

:::single-choice{#split-ten-mebibytes} Qual comando divide `archive.bin` em partes de 10 MiB com o prefixo `chunk-`?

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="A opção `-l` espera uma quantidade de linhas, não um sufixo de tamanho em bytes para partes binárias."}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` não divide uma entrada binária nem oferece essa operação de tamanho de partes."}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="A opção `-b` seleciona o tamanho, `10M` solicita 10×1024×1024 bytes e `chunk-` é o prefixo."}
:::

Para praticar uniões por chave e o processamento de dados estruturados, experimente estes laboratórios:

1. **[Comando join do Linux: União de Arquivos](https://labex.io/labs/linux-linux-join-command-file-joining-219193)** — Este laboratório oferece uma introdução prática e direta ao comando `join`, permitindo que você pratique a mesclagem de linhas de dois arquivos de texto ordenados com base em um campo comum, exatamente como apresentado na lição.
2. **[Processamento de Dados de Funcionários](https://labex.io/labs/linux-processing-employees-data-388132)** — Aplique seus conhecimentos de `join` e de outros utilitários avançados da linha de comando do Linux, como `awk`, para combinar e processar dados de várias fontes, simulando um cenário real de análise de dados.

## Resumo

Agora você sabe combinar registros ordenados ou dividir uma entrada em partes sequenciais.

1. Una exatamente dois arquivos por campos-chave iguais.
2. Ordene as duas entradas de forma consistente por suas chaves.
3. Selecione campos-chave diferentes do padrão com `-1` e `-2`.
4. Divida por quantidade de linhas com `-l`.
5. Divida por tamanho em bytes com `-b` e um prefixo claro.
