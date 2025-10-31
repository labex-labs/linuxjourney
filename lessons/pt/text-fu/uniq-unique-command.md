---
index: 14
lang: "pt"
title: "uniq (Único)"
meta_title: "uniq (Único) - Text-Fu"
meta_description: "Explore o comando uniq no Linux para filtrar e remover linhas adjacentes duplicadas de texto. Aprenda a usar a ferramenta uniq linux com opções como -c, -u, -d e combine-a com sort para processamento de texto poderoso."
meta_keywords: "comando uniq, uniq Linux, uniq linux, remover duplicatas, sort uniq, processamento de texto, limpeza de dados, tutorial Linux"
---

## Lesson Content

O comando `uniq` (unique) é uma ferramenta essencial para o processamento de texto no Linux. Ele ajuda a filtrar e gerenciar linhas duplicadas dentro de um arquivo de texto, mas é importante entender como ele funciona para usá-lo de forma eficaz.

### Remoção Básica de Duplicatas

A função principal do comando `uniq` é remover linhas adjacentes duplicadas. Imagine que você tem um arquivo chamado `reading.txt` com o seguinte conteúdo:

```plaintext
book
book
paper
paper
article
article
magazine
```

Para remover as linhas repetidas, você pode executar o comando `uniq`:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Como você pode ver, `uniq` exibe uma versão do arquivo com as linhas adjacentes duplicadas removidas.

### Opções Avançadas de Filtragem

O comando `uniq` também fornece várias opções para uma análise mais detalhada.

Para contar as ocorrências de cada linha, use a flag `-c` (count):

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Para exibir apenas as linhas que não são repetidas (ou seja, são únicas), use a flag `-u` (unique):

```bash
$ uniq -u reading.txt
magazine
```

Inversamente, para exibir apenas as linhas que são repetidas, use a flag `-d` (duplicated):

```bash
$ uniq -d reading.txt
book
paper
article
```

### A Importância da Ordenação

Um detalhe crítico sobre o comando **uniq linux** é que ele só detecta linhas duplicadas se elas estiverem diretamente adjacentes uma à outra. Se as duplicatas estiverem espalhadas pelo arquivo, `uniq` não as identificará.

Considere esta versão de `reading.txt` onde as duplicatas não são adjacentes:

```plaintext
book
paper
book
paper
article
magazine
article
```

Executar `uniq` neste arquivo produzirá um resultado surpreendente:

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

Nenhuma linha foi removida porque nenhuma linha idêntica estava lado a lado. Para resolver isso, você deve primeiro ordenar o conteúdo do arquivo. Ao canalizar (`pipe`) a saída de `sort` para `uniq`, você garante que todas as linhas idênticas se tornem adjacentes, permitindo que `uniq` funcione corretamente. Esta combinação é um padrão poderoso e comum em scripts de shell.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Este comando primeiro ordena as linhas alfabeticamente e, em seguida, `uniq` filtra as duplicatas, fornecendo uma lista limpa de entradas exclusivas.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do processamento de texto com `uniq` e `sort`:

1. **[Comando uniq do Linux: Filtragem de Duplicatas](https://labex.io/pt/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Aprenda a usar o comando `uniq` do Linux em combinação com `sort` para identificar, filtrar e analisar linhas duplicadas em arquivos de texto.
2. **[Comando sort do Linux: Ordenação de Texto](https://labex.io/pt/labs/linux-linux-sort-command-text-sorting-219196)** - Pratique o uso do comando `sort` para organizar linhas de arquivos de texto, um passo crucial antes de usar `uniq` de forma eficaz.
3. **[Contagem de Palavras e Ordenação](https://labex.io/pt/labs/linux-word-count-and-sorting-388125)** - Aprenda as ferramentas essenciais de processamento de texto do Linux, `wc` (contagem de palavras) e `sort`, neste desafio prático. Aprenda a contar linhas, palavras e caracteres, encontrar padrões frequentes e ordenar dados de forma eficiente para várias tarefas de análise de texto.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança com o processamento de texto e a manipulação de dados no Linux.

## Quiz Question

Qual comando você usaria para remover linhas duplicadas adjacentes em um arquivo? Por favor, responda usando apenas o nome do comando em letras minúsculas em inglês.

## Quiz Answer

uniq
