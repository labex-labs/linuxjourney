---
index: 2
lang: "pt"
title: "stdin (Entrada Padrão)"
meta_title: "stdin (Entrada Padrão) - Text-Fu"
meta_description: "Aprenda sobre o redirecionamento de stdin (entrada padrão) no Linux. Entenda como usar o operador '<' com arquivos e comandos. Explore exemplos práticos e melhore suas habilidades de linha de comando no Linux."
meta_keywords: "stdin, entrada padrão, redirecionamento Linux, operador <, tutorial Linux, linha de comando, iniciante, guia"
---

## Lesson Content

Em nossa lição anterior, aprendemos que temos diferentes streams de stdout que podemos usar, como um arquivo ou a tela. Bem, também existem diferentes streams de entrada padrão (stdin) que podemos usar. Sabemos que temos stdin de dispositivos como o teclado, mas também podemos usar arquivos, saída de outros processos e o terminal. Vamos ver um exemplo.

Vamos usar o arquivo `peanuts.txt` da lição anterior para este exemplo. Lembre-se, ele continha o texto "Hello World".

```bash
cat < peanuts.txt > banana.txt
```

Assim como tínhamos `>` para redirecionamento de stdout, podemos usar `<` para redirecionamento de stdin.

Normalmente, no comando `cat`, você envia um arquivo para ele e esse arquivo se torna o stdin. Neste caso, redirecionamos `peanuts.txt` para ser nosso stdin. Então a saída de `cat peanuts.txt`, que seria "Hello World", é redirecionada para outro arquivo chamado `banana.txt`.

## Exercise

Experimente alguns comandos:

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

Qual redirecionador você usa para redirecionar stdin?

## Quiz Answer

<
