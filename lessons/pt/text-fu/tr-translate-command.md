---
index: 13
lang: "pt"
title: "tr (Traduzir)"
meta_title: "tr (Traduzir) - Text-Fu"
meta_description: "Aprenda o comando Linux tr com exemplos para traduzir caracteres, deletar caracteres, comprimir repetições, usar classes de caracteres e limpar texto."
meta_keywords: "comando linux tr, comando tr, tr -d, tr -s, traduzir caracteres, deletar caracteres, classes de caracteres, processamento de texto linux"
---

## Lesson Content

O comando `tr`, abreviação de translate (traduzir), é uma ferramenta de linha de comando que traduz, deleta ou comprime caracteres da entrada padrão. É útil para manipulação simples de texto e frequentemente usado com pipes para processar a saída de outros comandos.

A sintaxe básica é:

```bash
tr [OPTIONS] SET1 [SET2]
```

Ao contrário de ferramentas como `sed` ou `awk`, o `tr` trabalha caractere por caractere. Ele não entende palavras, colunas ou expressões regulares da mesma forma. Isso o torna rápido e simples para tarefas como mudar maiúsculas/minúsculas, remover dígitos e normalizar espaços repetidos.

### Tradução Básica de Caracteres

O uso mais comum do `tr` é substituir um conjunto de caracteres por outro. Por exemplo, você pode facilmente traduzir todos os caracteres minúsculos para maiúsculos.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Neste exemplo, enviamos a saída do `echo` para o comando `tr`. O comando `tr` então traduziu o intervalo de caracteres `a-z` para os caracteres correspondentes no intervalo `A-Z`.

Você também pode traduzir um caractere para outro:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

Cada caractere em `SET1` corresponde ao caractere na mesma posição em `SET2`.

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Aqui, `a` vira `A`, `b` vira `B` e `c` vira `C`.

### Deletando Caracteres com -d

Outra funcionalidade poderosa é a capacidade de deletar caracteres específicos usando a opção `-d`. Isso é particularmente útil para limpar texto. Por exemplo, se você quiser remover todos os dígitos de uma string, pode usar:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Aqui, `tr -d` deletou todos os caracteres no conjunto especificado, de `0` a `9`.

Você pode remover pontuação de uma string usando uma classe de caracteres:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Também é possível remover caracteres de nova linha para juntar linhas:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### Comprimindo Caracteres Repetidos

O comando `tr` também pode "comprimir" caracteres repetidos em uma única ocorrência usando a opção `-s`. Isso é ótimo para normalizar texto com espaços extras.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Neste caso, `tr -s ' '` substituiu sequências de múltiplos espaços por um único espaço, deixando a saída muito mais limpa.

Você pode comprimir novas linhas repetidas também:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### Usando Classes de Caracteres

Classes de caracteres tornam os comandos `tr` mais fáceis de ler e mais portáveis. Classes comuns incluem:

- `[:lower:]`: Letras minúsculas.
- `[:upper:]`: Letras maiúsculas.
- `[:digit:]`: Dígitos.
- `[:alpha:]`: Letras.
- `[:alnum:]`: Letras e dígitos.
- `[:space:]`: Caracteres de espaço em branco.
- `[:punct:]`: Caracteres de pontuação.

Por exemplo, converta texto minúsculo para maiúsculo com classes de caracteres:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

Delete tudo exceto letras e dígitos usando `-c` com `-d`. A opção `-c` significa complemento, ou "tudo que não está neste conjunto."

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### Combinando Deletar e Comprimir

Você pode combinar opções ao limpar texto. Este exemplo deleta pontuação, depois comprime espaços repetidos:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Para entrada separada por tabulações, você pode traduzir tabs em vírgulas:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### Opções Comuns do tr

Aqui estão as opções que você usará com mais frequência:

- `-d`: Deleta caracteres em `SET1`.
- `-s`: Comprime caracteres repetidos em `SET1`.
- `-c`: Usa o complemento de `SET1`.
- `-t`: Trunca `SET1` ao tamanho de `SET2` antes de traduzir.

### Perguntas Comuns

**Por que o tr lê de um pipe?** O `tr` lê da entrada padrão, então é comumente usado após comandos como `echo`, `cat`, `printf` ou outros que produzem texto.

**O tr substitui palavras?** Não. O `tr` traduz caracteres, não palavras. Use `sed` quando precisar substituir palavras inteiras ou padrões.

**Por que meu comando tr mudou caracteres um por um?** É assim que o `tr` funciona. Ele mapeia cada caractere em `SET1` para o caractere correspondente em `SET2`.

**Por que devo colocar conjuntos como 'a-z' entre aspas?** Colocar entre aspas evita que o shell interprete caracteres especiais antes do `tr` recebê-los.

## Exercise

Para colocar seu conhecimento em prática, experimente o seguinte laboratório prático. Ele ajudará a reforçar seu entendimento sobre tradução de caracteres e processamento de texto.

1. **[Comando Linux tr: Tradução de Caracteres](https://labex.io/pt/labs/linux-linux-tr-command-character-translating-219198)** - Aprenda o comando Linux `tr` para transformações a nível de caracteres em fluxos de texto. Você praticará traduzir caracteres, deletar caracteres específicos, trabalhar com classes de caracteres e comprimir caracteres repetidos.

Este laboratório ajudará você a aplicar os conceitos de manipulação de texto em cenários reais e ganhar confiança com o comando `tr`.

## Quiz Question

Qual comando é usado para traduzir caracteres? (Por favor, responda apenas com letras minúsculas em inglês)

## Quiz Answer

tr
