---
lang: "pt"
title: "stdout (Saída Padrão)"
description: "Aprenda sobre o stdout do Linux e o redirecionamento de I/O. Entenda como redirecionar a saída de comandos para arquivos usando os operadores > e >>. Comece sua jornada no Linux hoje!"
keywords: "Linux stdout, redirecionamento de I/O, comandos Linux, redirecionar saída, tutorial Linux, Linux para iniciantes, guia Linux, shell scripting"
---

## Lesson Content

Até agora, nos familiarizamos com muitos comandos e suas saídas, e isso nos leva ao nosso próximo assunto: streams de I/O (entrada/saída). Vamos executar o seguinte comando e discutiremos como isso funciona.

```bash
echo Hello World > peanuts.txt
```

O que acabou de acontecer? Bem, verifique o diretório onde você executou esse comando e, eis que você deve ver um arquivo chamado `peanuts.txt`. Olhe dentro desse arquivo e você deverá ver o texto "Hello World". Muitas coisas aconteceram em um único comando, então vamos detalhá-lo.

Primeiro, vamos detalhar a primeira parte:

```bash
echo Hello World
```

Sabemos que isso imprime "Hello World" na tela, mas como? Os processos usam streams de I/O para receber entrada e retornar saída. Por padrão, o comando `echo` recebe entrada (entrada padrão ou stdin) do teclado e retorna saída (saída padrão ou stdout) para a tela. Então, é por isso que, quando você digita `echo Hello World` no seu shell, você obtém "Hello World" na tela. No entanto, o redirecionamento de I/O nos permite alterar esse comportamento padrão, nos dando maior flexibilidade de arquivo.

Vamos prosseguir para a próxima parte do comando:

```bash
>
```

O `>` é um operador de redirecionamento que nos permite alterar para onde a saída padrão vai. Ele nos permite enviar a saída de `echo Hello World` para um arquivo em vez de para a tela. Se o arquivo ainda não existir, ele o criará para nós. No entanto, se ele já existir, ele o sobrescreverá (você pode adicionar uma flag de shell para evitar isso, dependendo do shell que você está usando).

E é basicamente assim que o redirecionamento de stdout funciona!

Bem, digamos que eu não quisesse sobrescrever meu `peanuts.txt`. Felizmente, existe um operador de redirecionamento para isso também: `>>`.

```bash
echo Hello World >> peanuts.txt
```

Isso anexará "Hello World" ao final do arquivo `peanuts.txt`. Se o arquivo ainda não existir, ele o criará para nós, assim como o redirecionador `>`!

## Exercise

Experimente alguns comandos:

```bash
ls -l /var/log > myoutput.txt
echo Hello World > rm
> somefile.txt
```

## Quiz Question

Qual redirecionador você usa para anexar a saída a um arquivo?

## Quiz Answer

> >
