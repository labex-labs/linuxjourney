---
index: 13
lang: "pt"
title: "tr (Traduzir)"
meta_title: "tr (Traduzir) - Text-Fu"
meta_description: "Domine o comando tr do Linux para tradução e exclusão de caracteres. Este guia aborda como usar o tr para traduzir caracteres, usar opções como linux tr -d para remover caracteres e fornece exemplos práticos de manipulação de texto."
meta_keywords: "tr, comando tr, traduzir caracteres, linux tr -d, tr -d linux, traduzir caracteres, excluir caracteres, processamento de texto, comando Linux"
---

## Lesson Content

O comando `tr`, abreviação de translate (traduzir), é uma utilidade de linha de comando no Linux que traduz ou exclui caracteres da entrada padrão. É uma ferramenta útil para manipulação simples de texto e é frequentemente usada com pipes para processar a saída de outros comandos. A funcionalidade `trtranslate` é uma parte central do processamento de texto.

### Tradução Básica de Caracteres

O uso mais comum do `tr` é substituir um conjunto de caracteres por outro. Por exemplo, você pode facilmente traduzir todos os caracteres minúsculos para maiúsculos.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Neste exemplo, canalizamos a saída do `echo` para o comando `tr`. O comando `tr` então traduziu o intervalo de caracteres `a-z` para os caracteres correspondentes no intervalo `A-Z`.

### Excluindo Caracteres com -d

Outra funcionalidade poderosa é a capacidade de excluir caracteres específicos usando a opção `-d` (delete/excluir). Isso é particularmente útil para limpar texto. Por exemplo, se você deseja remover todos os dígitos de uma string, você pode usar `linux tr -d`.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Aqui, o comando `tr -d` excluiu cada caractere no conjunto especificado ('0' a '9') do fluxo de entrada. Este é um padrão comum para usuários de `tr -d linux`.

### Comprimindo Caracteres Repetidos

O comando `tr` também pode "comprimir" (squeeze) caracteres repetidos em uma única ocorrência usando a opção `-s` (squeeze/comprimir). Isso é ótimo para normalizar texto com espaços em branco extras.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Neste caso, `tr -s ' '` substituiu sequências de múltiplos espaços por um único espaço, tornando a saída muito mais limpa.

## Exercise

Para colocar seu conhecimento em prática, experimente o seguinte laboratório prático. Ele o ajudará a reforçar sua compreensão da tradução de caracteres e do processamento de texto.

1. **[Comando Linux tr: Tradução de Caracteres](https://labex.io/pt/labs/linux-linux-tr-command-character-translating-219198)** - Aprenda o comando `tr` do Linux para transformações em nível de caractere em fluxos de texto. Você praticará a tradução de caracteres, a exclusão de caracteres específicos, o trabalho com classes de caracteres e a compressão de caracteres repetidos.

Este laboratório o ajudará a aplicar os conceitos de manipulação de texto em cenários reais e a construir confiança com o comando `tr`.

## Quiz Question

Qual comando é usado para traduzir caracteres? (Por favor, responda apenas com letras minúsculas em inglês)

## Quiz Answer

tr
