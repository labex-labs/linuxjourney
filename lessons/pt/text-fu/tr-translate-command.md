---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "pt"
order_index: 13
title: "tr (Traduzir)"
description: "Aprenda a traduzir, excluir e agrupar conjuntos de caracteres em um fluxo de entrada padrão."
meta_title: "tr (Traduzir) - Text-Fu"
meta_description: "Aprenda o comando tr do Linux com exemplos para traduzir, excluir e agrupar caracteres repetidos, usar classes e limpar textos."
meta_keywords: "comando tr Linux, tr -d, tr -s, traduzir caracteres, excluir caracteres, classes caracteres, processamento texto Linux"
---

O comando `tr`, abreviação de translate, traduz, exclui ou agrupa caracteres lidos de stdin. Ele não aceita operandos comuns de arquivos de entrada; por isso, use um pipe ou redirecionamento de entrada para fornecer os dados.

A sintaxe básica é:

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` trabalha com conjuntos de caracteres, não com palavras nem expressões regulares gerais. Use outra ferramenta quando uma transformação depender de uma palavra completa, da estrutura da linha ou do contexto ao redor.

## Tradução de Caracteres

Com dois conjuntos, os caracteres de `SET1` são mapeados pela posição para os caracteres de `SET2`:

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Aqui, as posições do intervalo de letras minúsculas são mapeadas para as posições correspondentes em maiúsculas. Coloque as expressões dos conjuntos entre aspas para que o shell as forneça inalteradas.

Você também pode traduzir um caractere para outro:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Os caracteres que não estão em `SET1` passam inalterados.

:::single-choice{#tr-map-characters}
O que `printf '%s\n' 'abc123' | tr 'abc' 'ABC'` mostra?

::option[`ABCABC`]{#tr-uppercase-digits explanation="Os dígitos não pertencem ao conjunto de origem; portanto, `tr` não os substitui por letras."}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="Cada um de `a`, `b` e `c` é mapeado para o caractere na mesma posição em `ABC`; os dígitos permanecem iguais."}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` traduz os caracteres correspondentes da entrada. Ele não acrescenta o conjunto de destino ao fluxo."}
:::

## Exclusão de Caracteres

Use `-d` com um conjunto para remover todos os caracteres correspondentes:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Cada dígito é removido independentemente; `tr` não identifica um número completo como token.

Classes de caracteres podem descrever grupos definidos pelo locale atual:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Excluir novas linhas une as linhas da entrada sem inserir um separador:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

:::single-choice{#tr-delete-digits}
Qual comando remove todos os dígitos de stdin e mantém os outros caracteres inalterados?

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="A opção `-d` exclui do fluxo todos os caracteres da classe de dígitos."}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="A opção `-s` agrupa dígitos repetidos, mas preserva um caractere de cada sequência."}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="Uma tradução normalmente exige um segundo conjunto. Um conjunto sozinho não solicita uma exclusão."}
:::

## Agrupamento de Caracteres Repetidos

Use `-s SET` para substituir cada sequência de um caractere listado por uma única ocorrência:

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Esse conjunto contém um espaço comum; portanto, tabulações e novas linhas não são agrupadas pelo comando.

Também é possível agrupar novas linhas repetidas:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

:::single-choice{#tr-squeeze-spaces}
Qual comando reduz cada sequência de espaços comuns em stdin a um único espaço?

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="A opção `-s` agrupa os membros repetidos do conjunto fornecido, que contém um espaço comum."}
::option[`tr -d ' '`]{#tr-delete-space explanation="A opção `-d` remove todos os espaços comuns, em vez de preservar um por sequência."}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="Um conjunto de tradução vazio não é a forma clara e portável de solicitar o agrupamento. Use `-s` para caracteres repetidos."}
:::

## Uso de Classes de Caracteres e Complementos

Em muitos locales, as classes deixam a intenção mais clara que intervalos escritos à mão. Algumas classes comuns são:

- `[:lower:]`: letras minúsculas.
- `[:upper:]`: letras maiúsculas.
- `[:digit:]`: dígitos.
- `[:alpha:]`: letras.
- `[:alnum:]`: letras e dígitos.
- `[:space:]`: caracteres de espaço em branco.
- `[:punct:]`: caracteres de pontuação.

Por exemplo, converta um texto em minúsculas para maiúsculas usando classes:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

A opção `-c` complementa `SET1`, ou seja, representa todos os caracteres que não pertencem ao conjunto. Combine-a com `-d` para manter apenas determinados tipos:

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

Isso também remove a nova linha, pois ela não é alfanumérica. Acrescente ou preserve separadores conscientemente quando os limites dos registros forem importantes.

:::single-choice{#tr-keep-alphanumeric}
O que `tr -cd '[:alnum:]'` faz com stdin?

::option[Exclui os caracteres alfanuméricos e mantém todo o restante.]{#tr-delete-alnum explanation="O complemento altera os caracteres que `-d` seleciona. O conjunto alfanumérico em si é preservado."}
::option[Exclui todos os caracteres que não são alfanuméricos.]{#tr-delete-nonalnum .correct explanation="`-c` complementa o conjunto alfanumérico, e `-d` exclui o conjunto resultante de caracteres não alfanuméricos."}
::option[Converte todas as letras e dígitos em maiúsculas.]{#tr-uppercase-alnum explanation="Não há um conjunto de tradução de destino; portanto, o comando não realiza conversão de maiúsculas."}
:::

## Criação de Transformações de Fluxo

Vários processos `tr` podem ser conectados quando as transformações ficam mais claras como etapas separadas:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Para uma entrada simples separada por tabulações, traduza os caracteres de tabulação em vírgulas:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

Como `tr` lê stdin, um arquivo pode ser fornecido com `<`:

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

Redirecione stdout para outro arquivo se precisar salvar o resultado. Não a redirecione de volta ao caminho de entrada, pois o shell o truncaria antes que `tr` o lesse.

:::single-choice{#tr-read-file-input}
Qual comando faz `tr` ler `names.txt` como stdin e converter caracteres minúsculos em maiúsculos?

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` não recebe um nome de arquivo comum dessa forma; o operando extra torna a sintaxe inválida."}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="Essa forma lê o arquivo corretamente, mas exclui as letras minúsculas em vez de traduzi-las."}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="O shell abre `names.txt` em stdin, e `tr` mapeia a classe de minúsculas para a de maiúsculas."}
:::

Para praticar transformações de fluxos no nível dos caracteres, experimente este laboratório:

1. **[Comando tr do Linux: Tradução de Caracteres](https://labex.io/labs/linux-linux-tr-command-character-translating-219198)** — Aprenda a usar o comando `tr` do Linux para transformar caracteres em fluxos de texto. Você praticará a tradução e a exclusão de caracteres específicos, o trabalho com classes de caracteres e o agrupamento de caracteres repetidos.

## Resumo

Agora você sabe transformar fluxos de caracteres com operações específicas de `tr`.

1. Mapeie caracteres entre conjuntos correspondentes.
2. Exclua caracteres selecionados com `-d`.
3. Agrupe caracteres repetidos com `-s`.
4. Use conscientemente classes dependentes do locale e complementos.
5. Forneça a entrada por stdin, não como operando de nome de arquivo.
