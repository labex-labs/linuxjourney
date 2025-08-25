---
index: 6
lang: "pt"
title: "cut"
meta_title: "cut - Text-Fu"
meta_description: "Aprenda a usar o comando `cut` do Linux para extrair texto de arquivos. Este tutorial para iniciantes aborda o corte de caracteres e campos. Melhore suas habilidades de processamento de texto no Linux!"
meta_keywords: "comando cut, processamento de texto Linux, extrair texto, tutorial Linux, Linux para iniciantes, exemplos de cut, guia Linux"
---

## Lesson Content

Vamos aprender alguns comandos úteis que você pode usar para processar texto. Antes de começarmos, vamos criar um arquivo com o qual trabalharemos. Copie e cole o seguinte comando; depois de fazer isso, adicione um TAB entre "lazy" e "dog" (segure Ctrl-v + TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

O primeiro comando que aprenderemos é o comando `cut`. Ele extrai partes de texto de um arquivo.

Para extrair conteúdo por uma lista de caracteres:

```bash
cut -c 5 sample.txt
```

Isso exibe o 5º caractere em cada linha do arquivo. Neste caso, é "q"; observe que o espaço também conta como um caractere.

Para extrair o conteúdo por um campo, precisaremos fazer uma pequena modificação:

```bash
cut -f 2 sample.txt
```

A flag `-f` ou field corta o texto com base em campos. Por padrão, ele usa TABs como delimitadores, então tudo separado por um TAB é considerado um campo. Você deve ver "dog" como sua saída.

Você pode combinar a flag de campo com a flag de delimitador para extrair o conteúdo por um delimitador personalizado:

```bash
cut -f 1 -d ";" sample.txt
```

Isso mudará o delimitador TAB para um delimitador ";", e como estamos cortando o primeiro campo, o resultado deve ser "The quick brown".

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do processamento de texto com `cut` e outros comandos relacionados:

1. **[Comando Linux cut: Corte de Texto](https://labex.io/pt/labs/linux-linux-cut-command-text-cutting-219187)** - Este laboratório oferece uma introdução direta e prática ao comando `cut`, permitindo que você pratique a extração de colunas ou campos específicos de arquivos de texto, assim como discutido na lição.
2. **[Processamento de Texto Simples](https://labex.io/pt/labs/linux-simple-text-processing-18004)** - Expanda suas habilidades de manipulação de texto usando comandos poderosos como `tr`, `col`, `join` e `paste` para processar e analisar dados de texto de forma eficiente.
3. **[Controle de Sequência e Pipeline](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aumente sua eficiência na linha de comando aprendendo a controlar sequências de execução de comandos, utilizar pipelines e aproveitar ferramentas poderosas de processamento de texto como `cut`, `grep`, `wc`, `sort` e `uniq`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o processamento de texto no Linux.

## Quiz Question

Qual comando você usaria para obter o primeiro caractere de cada linha em um arquivo?

## Quiz Answer

cut -c 1
