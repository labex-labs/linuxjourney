---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "pt"
order_index: 16
title: "grep"
description: "Aprenda a selecionar linhas com cadeias fixas ou expressões regulares e interpretar os resultados de grep."
meta_title: "grep - Text-Fu"
meta_description: "Aprenda a usar o comando grep do Linux para pesquisar padrões de texto, contar linhas, fornecer padrões com segurança e interpretar os resultados."
meta_keywords: "comando grep, grep -e, grep -c, grep -f, grep -o, grep Linux, pesquisar texto, correspondência padrões, processamento texto"
---

O comando `grep` seleciona linhas da entrada que correspondem a um padrão. Ele pode pesquisar arquivos indicados ou stdin, mostrar o contexto das correspondências, contar linhas selecionadas e comunicar por seu status de saída se encontrou algo.

## Correspondência de Linhas em um Arquivo

Forneça um padrão seguido de um ou mais arquivos de entrada:

```bash
$ grep 'fox' sample.txt
```

Por padrão, o GNU `grep` interpreta o padrão como uma expressão regular básica e mostra cada linha selecionada. Coloque os padrões entre aspas para impedir que espaços e metacaracteres do shell sejam interpretados antes.

Use `-F` quando o padrão deva ser tratado como uma cadeia fixa, não como expressão regular:

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string}
Qual comando pesquisa `products.txt` pelo texto literal `price: $5.00` sem tratar os caracteres do padrão como sintaxe de expressão regular?

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` seleciona a correspondência por cadeia fixa, e as aspas simples protegem o cifrão da expansão do shell."}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` ativa expressões regulares estendidas, nas quais `$` e `.` possuem significados especiais."}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` seleciona as linhas sem correspondência e ainda usa a interpretação de expressão regular por padrão."}
:::

## Seleção da Sintaxe do Padrão

O GNU `grep` oferece três modos comuns de padrão:

- padrão: expressões regulares básicas;
- `-E`: expressões regulares estendidas, incluindo operadores como `|`, `+` e `?` sem barras invertidas;
- `-F`: cadeias fixas, sem operadores de expressão regular.

Âncoras como `^` e `$` correspondem ao início e ao fim de uma linha. Para localizar nomes terminados no sufixo literal `.txt` em uma lista:

```bash
$ grep -E '\.txt$' filenames.txt
```

A barra invertida torna o ponto literal; um `.` sem escape em uma expressão regular corresponde a qualquer caractere individual.

:::single-choice{#grep-literal-txt-suffix}
Qual expressão regular estendida corresponde a linhas terminadas no sufixo literal `.txt`?

::option[`'.txt$'`]{#grep-anychar-txt explanation="O ponto não possui escape; portanto, ele corresponde a qualquer caractere antes de `txt`, não especificamente a um ponto literal."}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` corresponde a um ponto literal, e `$` ancora a correspondência no final da linha."}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="Essa forma ancora no início e ainda usa um ponto sem escape, expressando outra correspondência."}
:::

## Fornecimento Seguro de Padrões

Use `-e PATTERN` para fornecer explicitamente um padrão. Isso é particularmente útil quando ele começa com `-`, pois as aspas sozinhas não impedem a interpretação como opção:

```bash
$ grep -e '-v' settings.conf
```

Você pode repetir `-e` para selecionar linhas correspondentes a qualquer padrão fornecido. Use `-f patterns.txt` para ler um padrão por linha de um arquivo.

:::single-choice{#grep-hyphen-pattern}
Qual comando pesquisa `settings.conf` pelo padrão `-v`, em vez de interpretá-lo como uma opção?

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="As aspas protegem os caracteres da expansão do shell, mas `grep` ainda pode interpretar o argumento `-v` como sua opção de inversão."}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="Essa forma ativa a correspondência invertida e não fornece `settings.conf` como padrão e entrada da maneira solicitada."}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="A opção `-e` declara que o argumento seguinte é um padrão, mesmo começando com hífen."}
:::

## Controle da Saída Selecionada

- `-i`: ignora diferenças entre maiúsculas e minúsculas.
- `-n`: prefixa as linhas selecionadas com seus números.
- `-v`: seleciona as linhas que não correspondem.
- `-c`: mostra a quantidade de linhas selecionadas para cada arquivo de entrada.
- `-o`: mostra apenas cada parte correspondente não vazia, não a linha completa.

Por exemplo, conte as linhas que contêm `fox`, ignorando maiúsculas e minúsculas:

```bash
$ grep -ic 'fox' sample.txt
```

`-c` conta linhas selecionadas, não a quantidade total de correspondências dentro delas. Uma linha com `fox fox` contribui com um para a contagem. Quando você precisar especificamente das ocorrências não sobrepostas com o GNU `grep`, `grep -o PATTERN | wc -l` é um pipeline possível.

:::single-choice{#grep-count-lines}
`data.txt` possui uma linha com `error error` e duas linhas sem correspondência. O que `grep -c 'error' data.txt` informa?

::option[`2`, porque a palavra ocorre duas vezes em uma linha.]{#grep-count-occurrences explanation="`-c` conta linhas selecionadas, não correspondências individuais dentro de uma linha."}
::option[`1`, porque exatamente uma linha corresponde.]{#grep-count-one-line .correct explanation="A única linha é selecionada uma vez, mesmo que o padrão apareça duas vezes nela."}
::option[`3`, porque o arquivo contém três linhas ao todo.]{#grep-count-total-lines explanation="Somente as linhas selecionadas contribuem para `grep -c`; as linhas sem correspondência são excluídas."}
:::

## Filtragem de stdin e Pesquisa em Diretórios

Quando nenhum arquivo de entrada é indicado, `grep` lê stdin e se encaixa naturalmente em um pipeline:

```bash
$ env | grep '^USER='
```

Use `-r` para pesquisar recursivamente os arquivos legíveis abaixo de um diretório:

```bash
$ grep -r 'listen_port' config/
```

Diagnósticos como erros de permissão vão para stderr e não fazem parte da entrada pesquisada. Restrinja o caminho e compreenda as permissões em vez de elevar o acesso imediatamente.

:::single-choice{#grep-pipeline-input}
Em `generate-report | grep 'failed'`, qual entrada `grep` pesquisa?

::option[Um arquivo chamado `generate-report` no diretório atual.]{#grep-report-file explanation="A palavra à esquerda é executada como comando e não é fornecida a `grep` como operando de arquivo."}
::option[O fluxo stdout produzido por `generate-report`.]{#grep-report-stdout .correct explanation="O pipe conecta stdout do produtor a stdin de `grep`."}
::option[O fluxo stderr produzido por `generate-report`.]{#grep-report-stderr explanation="Um pipe simples transporta stdout. Stderr permanece separada, a menos que seja redirecionada explicitamente."}
:::

## Interpretação do Status de Saída

Em pesquisas comuns, o GNU `grep` retorna o status `0` quando seleciona pelo menos uma linha, `1` quando nenhuma linha é selecionada e `2` em caso de erro. Isso permite que scripts testem uma correspondência sem tratar “nenhuma correspondência” como a mesma condição de um arquivo ilegível ou padrão inválido.

Opções como `-q` suprimem a saída comum e param depois que uma correspondência é encontrada, sendo úteis em testes condicionais. Não deduza sucesso apenas por uma tela vazia: `-q`, redirecionamento, ausência de correspondência e erro podem produzir pouca ou nenhuma stdout, mas seus status são diferentes.

Para praticar pesquisas com cadeias fixas e expressões regulares, experimente estes laboratórios:

1. **[Pesquisa de Texto com grep no Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** — Pratique pesquisas básicas, números de linha, âncoras e expressões regulares básicas e estendidas com `grep`.
2. **[Comando grep do Linux: Pesquisa de Padrões](https://labex.io/labs/linux-linux-grep-command-pattern-searching-219192)** — Aprenda a pesquisar e corresponder padrões em arquivos de texto e a definir padrões complexos com expressões regulares.
3. **[Agulha no Palheiro](https://labex.io/labs/linux-needle-in-the-haystack-388109)** — Aprenda a usar o poder do comando `grep` para pesquisar padrões específicos, contar ocorrências, extrair valores únicos e combinar vários critérios de pesquisa em diversos arquivos de log.

## Resumo

Agora você sabe pesquisar textos orientados por linhas e diferenciar correspondências de erros.

1. Escolha a correspondência básica, estendida ou por cadeia fixa.
2. Coloque padrões entre aspas e use `-e` para um hífen inicial.
3. Conte linhas selecionadas sem confundi-las com ocorrências.
4. Filtre stdin ou pesquise recursivamente em um diretório específico.
5. Interprete os status de saída de correspondência, ausência de correspondência e erro.
