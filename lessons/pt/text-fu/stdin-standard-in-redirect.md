---
index: 2
lang: "pt"
title: "stdin (Entrada Padrão)"
meta_title: "stdin (Entrada Padrão) - Text-Fu"
meta_description: "Aprenda sobre o redirecionamento de stdin (entrada padrão) no Linux. Entenda como usar o operador '<' com arquivos e comandos. Explore exemplos práticos e melhore suas habilidades de linha de comando no Linux."
meta_keywords: "stdin, entrada padrão, redirecionamento Linux, operador <, tutorial Linux, linha de comando, iniciante, guia"
---

## Lesson Content

Na nossa lição anterior, aprendemos que temos diferentes streams stdout que podemos usar, como um arquivo ou a tela. Bem, também existem diferentes streams de entrada padrão (stdin) que podemos usar. Sabemos que temos stdin de dispositivos como o teclado, mas também podemos usar arquivos, saída de outros processos e o terminal. Vamos ver um exemplo.

Vamos usar o arquivo `peanuts.txt` da lição anterior para este exemplo. Lembre-se, ele tinha o texto "Hello World" nele.

```bash
cat < peanuts.txt > banana.txt
```

Assim como tínhamos `>` para redirecionamento de stdout, podemos usar `<` para redirecionamento de stdin.

Normalmente, no comando `cat`, você envia um arquivo para ele e esse arquivo se torna o stdin. Neste caso, redirecionamos `peanuts.txt` para ser nosso stdin. Então a saída de `cat peanuts.txt`, que seria "Hello World", é redirecionada para outro arquivo chamado `banana.txt`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do redirecionamento de entrada e saída no Linux:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados de comandos manipulando a saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) usando operadores como >, >>, 2> e o comando tee.
2. **[Redirecionamento de Fluxo de Dados](https://labex.io/pt/labs/linux-data-stream-redirection-17995)** - Aprenda a arte do redirecionamento de fluxo no Linux. Manipule os fluxos de entrada, saída e erro padrão, combine saídas e utilize /dev/null para operações avançadas de arquivo.
3. **[Controle de Sequência e Pipeline](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aprenda a controlar sequências de execução de comandos e utilizar pipelines, que são fundamentais para direcionar a saída de um comando como entrada para outro.

Esses laboratórios ajudarão você a aplicar os conceitos de redirecionamento de entrada e saída em cenários reais e a construir confiança com scripts de shell e manipulação de dados.

## Quiz Question

Qual redirecionador você usa para redirecionar stdin?

## Quiz Answer

<
