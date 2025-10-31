---
index: 2
lang: "pt"
title: "stdin (Entrada Padrão)"
meta_title: "stdin (Entrada Padrão) - Text-Fu"
meta_description: "Domine operações de linha de comando Linux aprendendo a redirecionar stdin (entrada padrão). Este guia aborda a relação entre stdin e stdout, o uso do operador '<' e exemplos práticos como 'cat stdin' para gerenciar fluxos de dados com eficácia."
meta_keywords: "stdin, entrada padrão, redirecionar stdin, cat stdin, stdin e stdout, entrada padrão Linux, redirecionamento Linux, linha de comando, fluxo de entrada"
---

## Lesson Content

Na nossa lição anterior, aprendemos sobre o redirecionamento do fluxo de saída padrão (stdout). Da mesma forma, também podemos gerenciar o fluxo de entrada padrão (`stdin`). Por padrão, um programa recebe seu `stdin` do teclado, mas também podemos usar arquivos ou a saída de outros processos como fonte de entrada.

### Entendendo stdin e stdout

Todo processo de linha de comando no Linux opera com pelo menos dois fluxos de dados fundamentais: entrada padrão (`stdin`) e saída padrão (`stdout`). Um programa lê dados de `stdin` e escreve seus resultados em `stdout`. Entender como controlar ambos, `stdin e stdout`, é crucial para um trabalho eficaz na linha de comando.

### Como Redirecionar stdin

Assim como usamos `>` para redirecionamento de stdout, usamos o operador `<` para `redirecionar stdin`. Este recurso poderoso permite que você diga a um comando para ler sua entrada de um arquivo em vez de esperar que você a digite no teclado. Este é um conceito central do redirecionamento de entrada.

### Exemplo Prático com cat stdin

Vamos revisitar o arquivo `peanuts.txt` da lição anterior, que contém o texto "Hello World". Considere o seguinte comando:

```bash
cat < peanuts.txt > banana.txt
```

Aqui está uma análise do que acontece:

1. A parte `< peanuts.txt` diz ao shell para `redirecionar stdin` para o comando `cat`, fazendo com que ele leia de `peanuts.txt` em vez do teclado.
2. O comando `cat` processa sua entrada. Neste caso, usar `cat stdin` significa que ele lê o conteúdo de `peanuts.txt`.
3. A parte `> banana.txt` redireciona a saída padrão do `cat` para um novo arquivo chamado `banana.txt`.

Em última análise, o conteúdo de `peanuts.txt` é copiado para `banana.txt`. Este exemplo demonstra efetivamente como gerenciar tanto `stdin quanto stdout` em um único comando eficiente.

## Exercise

Para solidificar sua compreensão, experimente estes exercícios práticos focados no redirecionamento de entrada e saída no Linux:

1. **[Redirecionamento de Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados dos comandos manipulando a saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) usando operadores como >, >>, 2> e o comando tee.
2. **[Redirecionamento de Fluxo de Dados](https://labex.io/pt/labs/linux-data-stream-redirection-17995)** - Aprenda a arte do redirecionamento de fluxo no Linux. Manipule os fluxos de entrada, saída e erro padrão, combine saídas e utilize /dev/null para operações de arquivo avançadas.
3. **[Controle de Sequência e Pipeline no Linux](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aprenda a controlar sequências de execução de comandos e a utilizar pipelines, que são fundamentais para direcionar a saída de um comando como entrada para outro.

Estes laboratórios ajudarão você a aplicar os conceitos de redirecionamento de entrada e saída em cenários reais e a construir confiança com scripting de shell e manipulação de dados.

## Quiz Question

Qual operador é usado para redirecionar stdin? Por favor, responda apenas com o símbolo necessário.

## Quiz Answer

<
