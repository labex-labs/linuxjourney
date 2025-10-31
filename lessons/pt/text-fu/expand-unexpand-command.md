---
index: 10
lang: "pt"
title: "Expandir e Desexpandir"
meta_title: "Expandir e Desexpandir - Text-Fu"
meta_description: "Domine a formatação de texto no Linux com nosso guia sobre os comandos expand e unexpand. Aprenda a converter tabulações em espaços e espaços em tabulações para layouts de arquivo consistentes."
meta_keywords: "comando expand, comando unexpand, tabulações Linux, espaços Linux, formatação de texto, tutorial Linux, Linux iniciante, guia Linux"
---

## Lesson Content

Espaçamentos inconsistentes podem tornar os arquivos de texto difíceis de ler. Embora as tabulações (tabs) sirvam para criar recuos uniformes, sua largura de exibição pode variar entre diferentes editores e sistemas. Isso pode perturbar a formatação e o alinhamento do texto. Felizmente, o Linux fornece ferramentas simples para gerenciar isso, convertendo entre tabulações e espaços. Este guia Linux para iniciantes o guiará pelo processo.

### Convertendo Tabulações em Espaços com o Comando expand

Quando você precisa garantir um espaçamento consistente, pode converter tabulações em um número padrão de espaços usando o comando `expand`. Este comando lê um arquivo e substitui cada caractere de tabulação por um conjunto de caracteres de espaço, imprimindo o resultado na saída padrão.

```bash
expand sample.txt
```

Por padrão, o comando `expand` converte cada tabulação em 8 espaços. Este utilitário simples é uma ferramenta poderosa para melhorar a formatação de texto.

### Salvando a Saída Convertida

O comando `expand` apenas imprime o texto convertido no seu terminal. Para salvar as alterações, você deve redirecionar a saída para um novo arquivo.

```bash
expand sample.txt > result.txt
```

Este comando pega a saída de `expand sample.txt` e a grava em `result.txt`, fornecendo um novo arquivo com espaços em vez de tabulações.

### Convertendo Espaços em Tabulações com o Comando unexpand

A operação inversa, converter espaços de volta em tabulações, é tratada pelo comando `unexpand`. Isso pode ser útil para reduzir o tamanho do arquivo ou aderir a padrões de codificação que exigem tabulações.

```bash
unexpand -a result.txt
```

Por padrão, `unexpand` converte apenas os espaços iniciais em cada linha. A opção `-a` instrui o comando `unexpand` a converter todas as instâncias de 8 espaços em uma tabulação, não apenas aquelas no início de uma linha, fornecendo um controle mais abrangente sobre seus espaços e tabulações no Linux.

## Exercise

Para dominar a manipulação de texto e o redirecionamento no Linux, a prática é fundamental. Os seguintes laboratórios práticos ajudarão a reforçar sua compreensão:

1. **[Redirecionamento de Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados dos comandos, manipulando a saída padrão (stdout), o erro padrão (stderr) e a entrada padrão (stdin) usando operadores como `>` e `>>`.
2. **[Processamento Simples de Texto](https://labex.io/pt/labs/linux-simple-text-processing-18004)** - Aprenda a usar comandos poderosos como `tr`, `col`, `join` e `paste` para manipular e analisar dados de texto de forma eficiente, aprimorando suas habilidades de linha de comando para processamento de dados.
3. **[Processamento de Texto e Expressões Regulares](https://labex.io/pt/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda as poderosas ferramentas de processamento de texto `grep`, `sed` e `awk`, e use expressões regulares para manipulação eficiente de texto e correspondência de padrões no Linux.

Concluir esses laboratórios o ajudará a aplicar os conceitos de transformação de texto e manipulação de arquivos em cenários do mundo real, aumentando sua confiança com ferramentas essenciais da linha de comando do Linux.

## Quiz Question

Qual comando é usado para converter tabulações em espaços? (Por favor, responda usando o nome do comando em inglês minúsculo.)

## Quiz Answer

expand
