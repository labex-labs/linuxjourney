---
index: 4
lang: "pt"
title: "pipe e tee"
meta_title: "pipe e tee - Text-Fu"
meta_description: "Aprenda pipes e o comando tee do Linux para um fluxo de dados eficiente na linha de comando. Entenda stdout, stdin e saída de arquivo. Melhore suas habilidades em Linux!"
meta_keywords: "pipe Linux, comando tee, tutorial Linux, stdout, stdin, Linux para iniciantes, linha de comando, guia Linux"
---

## Lesson Content

Vamos entrar em um pouco de encanamento agora, não realmente, mas de certa forma. Vamos tentar um comando:

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

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão do redirecionamento de entrada/saída e pipelines:

1. **[Redirecionando Entrada e Saída no Linux](https://labex.io/pt/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Pratique o controle do fluxo de dados de comandos manipulando a saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) usando operadores como `>`, `>>`, `2>` e o comando `tee`.
2. **[Controle de Sequência e Pipeline](https://labex.io/pt/labs/linux-sequence-control-and-pipeline-17994)** - Aprenda a controlar sequências de execução de comandos, utilizar pipelines e aproveitar ferramentas poderosas de processamento de texto como `cut`, `grep`, `wc`, `sort` e `uniq`.
3. **[Redirecionamento de Fluxo de Dados](https://labex.io/pt/labs/linux-data-stream-redirection-17995)** - Aprenda a arte do redirecionamento de fluxo no Linux, incluindo a manipulação de fluxos de entrada, saída e erro padrão, combinando saídas e utilizando `/dev/null`.

Esses laboratórios o ajudarão a aplicar os conceitos de piping e redirecionamento em cenários reais e a construir confiança na manipulação de dados na linha de comando.

## Quiz Question

Qual tecla representa o operador pipe?

## Quiz Answer

|
