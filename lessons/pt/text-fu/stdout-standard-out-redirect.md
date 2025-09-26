---
index: 1
lang: "pt"
title: "stdout (Saída Padrão)"
meta_title: "stdout (Saída Padrão) - Text-Fu"
meta_description: "Aprenda sobre stdout e redirecionamento de I/O no Linux. Entenda como redirecionar a saída de comandos para arquivos usando os operadores > e >>. Comece sua jornada Linux hoje!"
meta_keywords: "Linux stdout, redirecionamento de I/O, comandos Linux, redirecionar saída, tutorial Linux, Linux para iniciantes, guia Linux, shell scripting"
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

Sabemos que isso imprime "Hello World" na tela, mas como? Os processos usam streams de I/O para receber entrada e retornar saída. Por padrão, o comando `echo` recebe entrada (entrada padrão ou stdin) do teclado e retorna saída (saída padrão ou stdout) para a tela. Então, é por isso que quando você digita `echo Hello World` no seu shell, você obtém "Hello World" na tela. No entanto, o redirecionamento de I/O nos permite mudar esse comportamento padrão, nos dando maior flexibilidade de arquivo.

Vamos prosseguir para a próxima parte do comando:

```bash
>
```

O `>` é um operador de redirecionamento que nos permite mudar para onde a saída padrão vai. Ele nos permite enviar a saída de `echo Hello World` para um arquivo em vez da tela. Se o arquivo ainda não existir, ele o criará para nós. No entanto, se ele existir, ele o sobrescreverá (você pode adicionar um sinalizador de shell para evitar isso, dependendo do shell que você está usando).

E é basicamente assim que o redirecionamento de stdout funciona!

Bem, digamos que eu não quisesse sobrescrever meu `peanuts.txt`. Felizmente, existe um operador de redirecionamento para isso também: `>>`.

```bash
echo Hello World >> peanuts.txt
```

Isso anexará "Hello World" ao final do arquivo `peanuts.txt`. Se o arquivo ainda não existir, ele o criará para nós, assim como o redirecionador `>`!

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do redirecionamento de I/O:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados de comandos manipulando a saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) usando operadores como `>`, `>>`, `2>`, e o comando `tee`.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança com o redirecionamento de I/O.

## Quiz Question

Qual redirecionador você usa para anexar a saída a um arquivo?

## Quiz Answer

>>