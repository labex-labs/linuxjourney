---
index: 7
lang: "pt"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Aprenda a usar o comando paste do Linux para mesclar linhas de arquivos. Descubra delimitadores e combine arquivos com este tutorial essencial do comando Linux."
meta_keywords: "comando paste Linux, tutorial comando paste, mesclar linhas de arquivo, comandos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

O comando `paste` é semelhante ao comando `cat`; ele mescla linhas em um arquivo. Vamos criar um novo arquivo com o seguinte conteúdo:

```
sample2.txt
The
quick
brown
fox
```

Vamos combinar todas essas linhas em uma única linha:

```bash
paste -s sample2.txt
```

O delimitador padrão para `paste` é TAB, então agora há uma linha com TABs separando cada palavra.

Vamos mudar este delimitador (`-d`) para algo um pouco mais legível:

```bash
paste -d ' ' -s sample2.txt
```

Agora tudo deve estar em uma linha delimitada por espaços.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do processamento de texto e manipulação de dados no Linux:

1. **[Processamento de Texto Simples](https://labex.io/pt/labs/linux-simple-text-processing-18004)** - Aprenda a usar comandos poderosos como `tr`, `col`, `join` e `paste` para manipular e analisar dados de texto de forma eficiente.
2. **[Redirecionamento de Fluxo de Dados](https://labex.io/pt/labs/linux-data-stream-redirection-17995)** - Aprenda a arte do redirecionamento de fluxo no Linux e como manipular os fluxos de entrada, saída e erro padrão, o que é fundamental para entender como comandos como `paste` operam.
3. **[Controle de Sequência e Pipeline](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aprenda a controlar sequências de execução de comandos e utilizar pipelines, aprimorando sua capacidade de combinar `paste` com outros comandos para tarefas de dados complexas.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o processamento e manipulação de dados no Linux.

## Quiz Question

Qual flag você usa com `paste` para fazer com que tudo vá para uma única linha?

## Quiz Answer

-s
