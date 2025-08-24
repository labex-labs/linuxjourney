---
index: 1
lang: "pt"
title: "O Shell"
meta_title: "O Shell - Linha de Comando"
meta_description: "Aprenda sobre o shell Linux, Bash e comandos básicos como 'echo'. Entenda os prompts do shell e comece sua jornada no Linux com este guia amigável para iniciantes."
meta_keywords: "shell Linux, Bash, comando echo, tutorial Linux, linha de comando, Linux para iniciantes, prompt de shell, guia Linux"
---

## Lesson Content

O mundo é seu, ou melhor, o shell é seu. O que é o shell? O shell é basicamente um programa que recebe seus comandos do teclado e os envia para o sistema operacional para serem executados. Se você já usou uma GUI, provavelmente já viu programas como "Terminal" ou "Console"; estes são apenas programas que iniciam um shell para você. Ao longo de todo este curso, aprenderemos sobre as maravilhas do shell.

Neste curso, usaremos o programa shell Bash (Bourne Again Shell). Quase todas as distribuições Linux usarão o shell Bash por padrão. Existem outros shells disponíveis, como `ksh`, `zsh` e `tsch`, mas não abordaremos nenhum deles.

Vamos direto ao assunto! Dependendo da distribuição, seu prompt de shell pode mudar, mas na maioria das vezes, ele deve seguir o seguinte formato:

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

Percebe o `$` no final do prompt? Diferentes shells terão prompts diferentes. No nosso caso, o `$` é para um usuário normal usando Bash, Bourne ou Korn shell. Você não adiciona o símbolo do prompt ao digitar o comando; apenas saiba que ele está lá.

Vamos começar com um comando simples, `echo`. O comando `echo` apenas imprime os argumentos de texto na tela.

```bash
echo Hello World
```

## Exercise

Para prática prática com comandos básicos do Linux, recomendamos o curso interativo: [Linux Basic Commands Practice Online](https://labex.io/pt/courses/linux-basic-commands-practice-online)

## Quiz Question

O que deve ser exibido na tela quando você digita `echo Hello World`?

## Quiz Answer

Hello World