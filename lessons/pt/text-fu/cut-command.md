---
index: 6
lang: "pt"
title: "cortar"
meta_title: "cortar - Text-Fu"
meta_description: "Aprenda a usar o comando Linux `cut` para extrair seções específicas de texto de arquivos. Este guia aborda o corte por caractere e campo (`cut f`), incluindo como usar cut f com delimitadores personalizados. Perfeito para dominar o processamento de texto no Linux."
meta_keywords: "comando cut, processamento de texto Linux, extrair texto, cut f, como usar cut f, tutorial Linux, exemplos cut, guia Linux, corte de campo"
---

## Lesson Content

Vamos aprender alguns comandos úteis para processar texto. Antes de começar, vamos criar um arquivo para trabalhar. Copie e cole o seguinte comando. Após colar, você precisará adicionar um caractere TAB literal entre "lazy" e "dog" (você pode fazer isso frequentemente pressionando Ctrl-v e depois TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

O primeiro comando que exploraremos é o `cut`, que extrai porções de texto de um arquivo.

### Cortando por Caractere

Você pode extrair conteúdo com base na posição do caractere usando a flag `-c`.

```bash
cut -c 5 sample.txt
```

Este comando exibe o 5º caractere de cada linha do arquivo. No nosso caso, a saída é "q". Note que espaços também contam como caracteres.

### Cortando por Campo com cut f

Um recurso mais poderoso é cortar por campos. A sintaxe `cut f`, usando a flag `-f`, permite extrair texto com base na posição do campo. Por padrão, `cut` usa o caractere TAB como delimitador, o que significa que tudo separado por um TAB é considerado um campo distinto.

Vamos ver como cortar f com base em campos:

```bash
cut -f 2 sample.txt
```

Como inserimos um TAB entre "lazy" e "dog", este comando trata "dog" como o segundo campo. Sua saída deve ser "dog".

### Usando Delimitadores Personalizados

Você também pode combinar a flag de campo com a flag de delimitador (`-d`) para especificar um delimitador personalizado. Isso é útil ao trabalhar com arquivos que usam caracteres como vírgulas ou ponto e vírgula para separar dados.

```bash
cut -f 1 -d ";" sample.txt
```

Este comando altera o delimitador de TAB para ponto e vírgula (`;`). Como estamos cortando o primeiro campo (`-f 1`), o resultado será "The quick brown".

## Exercise

Praticar leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do processamento de texto com `cut` e outros comandos relacionados:

1. **[Comando cut do Linux: Corte de Texto](https://labex.io/pt/labs/linux-linux-cut-command-text-cutting-219187)** - Este laboratório oferece uma introdução prática e direta ao comando `cut`, permitindo que você pratique a extração de colunas ou campos específicos de arquivos de texto, assim como discutido na lição.
2. **[Processamento Simples de Texto](https://labex.io/pt/labs/linux-simple-text-processing-18004)** - Expanda suas habilidades de manipulação de texto usando comandos poderosos como `tr`, `col`, `join` e `paste` para processar e analisar dados de texto de forma eficiente.
3. **[Controle de Sequência e Pipeline do Linux](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aumente sua eficiência na linha de comando aprendendo a controlar sequências de execução de comandos, utilizar pipelines e aproveitar ferramentas poderosas de processamento de texto como `cut`, `grep`, `wc`, `sort` e `uniq`.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança com o processamento de texto no Linux.

## Quiz Question

Qual comando você usaria para obter o primeiro caractere de cada linha em um arquivo?

## Quiz Answer

cut -c 1
