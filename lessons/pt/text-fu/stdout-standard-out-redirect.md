---
index: 1
lang: "pt"
title: "stdout (Saída Padrão)"
meta_title: "stdout (Saída Padrão) - Text-Fu"
meta_description: "Comece sua jornada para aprender Linux dominando a saída padrão (stdout) e o redirecionamento de E/S. Esta lição aborda como redirecionar a saída de comandos para arquivos usando os operadores > e >>, uma habilidade fundamental para qualquer usuário Linux."
meta_keywords: "Linux, aprender linux, stdout, redirecionamento de E/S, saída padrão, redirecionar saída, bash, shell scripting, comandos Linux, tutorial Linux"
---

## Lesson Content

À medida que você continua a aprender Linux, você viu como os comandos produzem saída. Isso nos leva ao tópico importante de streams de E/S (entrada/saída), especificamente a saída padrão ou **stdout**. Vamos explorar este conceito executando o seguinte comando:

```bash
echo Hello World > peanuts.txt
```

Após executar isso, você encontrará um novo arquivo chamado `peanuts.txt` em seu diretório atual. Se você visualizar seu conteúdo, verá o texto "Hello World". Vamos analisar o que aconteceu.

### Entendendo a Saída Padrão (stdout)

Primeiro, considere o comando sem o caractere especial:

```bash
echo Hello World
```

Por padrão, muitos comandos enviam seus resultados para **stdout**, que é a tela do seu terminal. É por isso que `echo Hello World` exibe o texto diretamente no seu shell. Os processos usam streams de E/S para receber entrada (entrada padrão ou stdin) e enviar saída. O redirecionamento de E/S nos permite alterar esse comportamento padrão, dando-nos maior controle sobre nossos dados.

### Redirecionando stdout com >

O caractere `>` é um operador de redirecionamento. Ele intercepta os dados que se destinam ao **stdout** e os envia para um novo destino.

```bash
>
```

No nosso exemplo, ele envia a saída de `echo Hello World` para um arquivo em vez da tela. Se o arquivo não existir, ele será criado. **Tenha cuidado**, pois se o arquivo já existir, este operador sobrescreverá completamente seu conteúdo.

### Anexando stdout com >>

E se você quiser adicionar a um arquivo sem apagar seu conteúdo? Para isso, usamos o operador `>>`.

```bash
echo Hello World >> peanuts.txt
```

Este operador anexa a saída ao final do arquivo especificado. Se o arquivo ainda não existir, ele será criado, assim como o operador `>`. Dominar o redirecionamento de **stdout** é um passo fundamental na sua jornada Linux.

## Exercise

Para solidificar sua compreensão do redirecionamento de E/S, experimente este laboratório prático:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados dos comandos manipulando a saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) usando operadores como `>`, `>>`, `2>` e o comando `tee`.

Este laboratório o ajudará a aplicar esses conceitos em cenários do mundo real e a ganhar confiança com o redirecionamento de E/S.

## Quiz Question

Qual redirecionador você usa para anexar saída a um arquivo?

## Quiz Answer

`>>`
