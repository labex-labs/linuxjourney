---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "pt"
order_index: 12
title: "sort"
description: "Aprenda a ordenar linhas de texto por valores lexicais, numéricos ou de campos selecionados com sort."
meta_title: "sort - Text-Fu"
meta_description: "Aprenda a usar o comando sort do Linux para ordenar arquivos de texto, inverter resultados, comparar números e classificar por campos."
meta_keywords: "comando sort Linux, sort -r, sort -n, tutorial Linux, linha de comando, Linux para iniciantes, guia sort"
---

O comando `sort` lê linhas completas, ordena-as de acordo com as regras de comparação selecionadas e grava o resultado em stdout. Ele não altera o arquivo de entrada, a menos que você escolha explicitamente uma operação de saída.

## Ordenação de Linhas Completas

Considere `animals.txt`:

```text
dog
cow
cat
elephant
bird
```

Ordene as linhas em ordem crescente:

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

A ordenação do texto segue o locale atual, que pode afetar maiúsculas, acentos e pontuação. Use um locale consistente, como `LC_ALL=C`, quando um script exigir uma comparação reproduzível orientada por bytes:

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending} O que `sort animals.txt` faz sem uma opção de chave ou comparação numérica?

::option[Ordena linhas completas de acordo com o locale atual.]{#sort-locale-lines .correct explanation="Por padrão, `sort` compara linhas inteiras usando as regras de ordenação do locale ativo."}
::option[Ordena as palavras dentro de cada linha, mas mantém fixa a ordem das linhas.]{#sort-words-within-lines explanation="`sort` trata cada linha como um registro. Ele não reorganiza palavras dentro das linhas."}
::option[Reescreve automaticamente `animals.txt` no lugar.]{#sort-auto-rewrite explanation="O resultado ordenado vai para stdout por padrão, e o arquivo de entrada permanece inalterado."}
:::

## Inversão do Resultado

Acrescente `-r` para inverter o resultado da comparação:

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order} Qual comando ordena `animals.txt` em ordem inversa?

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="A opção `-n` solicita uma comparação numérica. Ela não significa ordem inversa."}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="A opção `-u` suprime chaves duplicadas. Ela não inverte a saída."}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="A opção `-r` inverte a ordenação escolhida pelas outras regras de comparação."}
:::

## Comparação de Números

A ordem lexical compara caracteres; por isso, `10` normalmente vem antes de `2`. Use `-n` para uma comparação numérica comum:

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

Combine opções quando necessário. `sort -nr scores.txt` compara numericamente e coloca os valores maiores primeiro.

:::single-choice{#sort-numbers-descending} Qual comando ordena as linhas numéricas de `scores.txt` da maior para a menor?

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="A comparação numérica é selecionada, mas a direção padrão coloca os valores menores primeiro."}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` seleciona a comparação numérica e `-r` a inverte, produzindo uma ordem numérica decrescente."}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="Essa forma inverte a comparação textual, mas não solicita uma comparação numérica; valores como `10` e `2` podem ficar em uma ordem inesperada."}
:::

## Ordenação por um Campo

Use `-k START[,END]` para escolher uma chave. Por padrão, os campos são separados por sequências de espaços. Para registros separados por dois-pontos, use `-t ':'`:

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

Aqui, `-t ':'` seleciona o delimitador, `-k 2,2` limita a chave ao campo 2 e o `n` anexado compara essa chave numericamente. Sem o `,2` final, uma chave iniciada no campo 2 normalmente continua até o fim da linha.

:::single-choice{#sort-second-colon-field} Qual comando ordena `users.txt` numericamente apenas por seu segundo campo separado por dois-pontos?

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="Essa forma usa campos separados por espaços e seleciona o campo 1, não o segundo campo separado por dois-pontos."}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` extrai o campo 2, mas não ordena os registros originais por essa chave."}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="Os dois-pontos definem os limites, `2,2` restringe a chave ao campo 2 e `n` aplica uma comparação numérica."}
:::

## Remoção de Duplicatas e Salvamento da Saída

Use `-u` para mostrar uma linha para cada chave de comparação igual:

```bash
$ sort -u names.txt
```

Isso ordena e remove duplicatas segundo as regras selecionadas. Se quiser apenas remover duplicatas adjacentes de dados já ordenados, o comando `uniq`, abordado mais adiante, pode fazer isso.

Para gravar o resultado em um arquivo, o redirecionamento comum é adequado quando o destino é diferente da entrada:

```bash
$ sort names.txt > names-sorted.txt
```

Não execute `sort names.txt > names.txt`; o shell trunca a entrada antes que `sort` a leia. O GNU `sort -o names.txt names.txt` organiza sua própria saída com segurança quando você pretende usar o mesmo caminho:

```bash
$ sort -o names.txt names.txt
```

Mantenha um backup ou grave e verifique um resultado separado quando os dados originais forem importantes.

:::single-choice{#sort-safe-same-file} No GNU/Linux, qual comando solicita que `sort` grave com segurança o resultado ordenado de volta em `names.txt`, sem que o redirecionamento do shell o trunque primeiro?

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="O GNU `sort` gerencia a saída de `-o` depois da leitura necessária; assim, o shell não trunca antecipadamente a entrada com `>`."}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="O shell trunca `names.txt` antes de iniciar `sort`; portanto, o comando pode perder a entrada."}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="Essa forma grava as linhas únicas ordenadas em stdout e deixa o arquivo de entrada inalterado."}
:::

Para praticar a ordenação e a análise de dados orientados por linhas, experimente estes laboratórios:

1. **[Comando sort do Linux: Ordenação de Texto](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** — Este laboratório oferece uma introdução direta ao comando `sort`, permitindo que você pratique a ordenação de linhas de arquivos de texto de várias formas, inclusive em ordem crescente e decrescente.
2. **[Contagem e Ordenação de Palavras](https://labex.io/labs/linux-word-count-and-sorting-388125)** — Aplique a ordenação junto com a contagem de palavras para analisar dados, encontrar padrões frequentes e organizar resultados.

## Resumo

Agora você sabe escolher regras de comparação e destinos para textos ordenados.

1. Ordene linhas completas sob um locale explícito quando a reprodução for importante.
2. Inverta os resultados com `-r`.
3. Compare valores numéricos com `-n`.
4. Selecione uma chave de campo limitada com `-t` e `-k`.
5. Remova duplicatas ou salve a saída sem truncar a entrada.
