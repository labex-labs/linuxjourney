---
lang: "pt"
title: "pipe e tee"
description: "Aprenda sobre pipes e o comando tee do Linux para um fluxo de dados eficiente na linha de comando. Entenda stdout, stdin e saída de arquivo. Melhore suas habilidades em Linux!"
keywords: "pipe Linux, comando tee, tutorial Linux, stdout, stdin, Linux para iniciantes, linha de comando, guia Linux"
---

## Lesson Content

Vamos agora para um pouco de encanamento, não literalmente, mas de certa forma. Vamos tentar um comando:

```bash
ls -la /etc
```

Você deve ver uma lista muito longa de itens; é um pouco difícil de ler, na verdade. Em vez de redirecionar essa saída para um arquivo, não seria bom se pudéssemos apenas ver a saída em outro comando como `less`? Bem, podemos!

```bash
ls -la /etc | less
```

O operador pipe `|`, representado por uma barra vertical, nos permite obter o `stdout` de um comando e torná-lo o `stdin` para outro processo. Neste caso, pegamos o `stdout` de `ls -la /etc` e então o _pipamos_ para o comando `less`. O comando pipe é extremamente útil, e continuaremos a usá-lo por toda a eternidade.

Bem, e se eu quisesse escrever a saída do meu comando para dois fluxos diferentes? Isso é possível com o comando `tee`:

```bash
ls | tee peanuts.txt
```

Você deve ver a saída de `ls` na sua tela, e se você abrir o arquivo `peanuts.txt`, você deve ver a mesma informação!

## Exercise

Try the following commands:

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

Qual tecla representa o operador pipe?

## Quiz Answer

|
