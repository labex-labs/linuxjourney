---
lesson_id: "the-shell"
course_id: "command-line"
lang: "pt"
order_index: 1
title: "O Shell"
description: "Aprenda o que é o shell do Linux e como os comandos são executados."
meta_title: "O Shell - Linha de Comando"
meta_description: "Aprenda o que é o shell do Linux, como funciona o prompt do Bash e como executar seu primeiro comando com exemplos acessíveis para iniciantes."
meta_keywords: "shell Linux, shell Bash, linha de comando, terminal Linux, prompt do shell, comando echo, comandos básicos Linux"
---

## O que É o Shell do Linux

Boas-vindas à sua jornada pelo Linux! O primeiro passo é entender o shell do Linux. Um shell é um programa que recebe os comandos digitados por você, pede ao sistema operacional que os execute e mostra o resultado no terminal.

Se você já usou uma interface gráfica, está acostumado a clicar em janelas, menus e botões. Na linha de comando, você digita instruções precisas. Aplicativos chamados “Terminal”, “Console” ou “Konsole” normalmente abrem uma sessão de shell para você.

O terminal é a janela ou o aplicativo em que você digita, enquanto o shell é o programa executado dentro dele.

O shell é útil porque é rápido, permite criar scripts e está disponível em quase todos os sistemas Linux. À medida que aprender mais comandos, você poderá combiná-los para inspecionar arquivos, gerenciar diretórios, pesquisar textos, instalar programas e automatizar tarefas repetitivas.

:::single-choice{#distinguish-shell-and-terminal}
Qual afirmação descreve corretamente a relação entre um terminal e um shell?

::option[O terminal fornece a janela, enquanto o shell é executado dentro dela.]{#shell-runs-in-terminal .correct explanation="O terminal é a interface usada por você, e o shell é o programa que processa comandos dentro dela."}
::option[O terminal recebe os comandos, enquanto o shell apenas exibe a saída.]{#terminal-accepts-commands explanation="Essa afirmação inverte as funções. O terminal fornece a interface, enquanto o shell recebe e executa os comandos."}
::option[Terminal e shell são dois nomes para o mesmo programa.]{#terminal-equals-shell explanation="Eles trabalham juntos, mas não são o mesmo programa. Um terminal abre uma sessão dentro da qual um shell é executado."}
:::

## Interação com o Shell Bash

Neste curso, vamos nos concentrar no Bash, abreviação de Bourne Again Shell. O Bash é um dos shells mais comuns no Linux e oferece uma boa base, mesmo que mais tarde você use `zsh`, `fish` ou outro shell.

Ao abrir um terminal, você verá o prompt do shell. Sua aparência pode variar, mas ele costuma mostrar o nome do usuário, o nome da máquina e o diretório atual.

```plaintext
pete@icebox:/home/pete $
```

O símbolo `$` indica que o shell está pronto para receber sua entrada como um usuário comum. Você não digita esse símbolo ao inserir comandos; ele é mostrado pelo shell. Se vir `#`, normalmente estará trabalhando como usuário root, que tem mais poder e também envolve mais riscos.

:::single-choice{#interpret-dollar-prompt}
O que o `$` no final do prompt de exemplo indica?

::option[O shell está sendo executado com os privilégios do usuário root.]{#root-user-ready explanation="Um prompt de root normalmente termina em `#`, não em `$`. O acesso root traz mais poder e riscos."}
::option[O shell está aguardando uma entrada de um usuário comum.]{#normal-user-ready .correct explanation="O `$` identifica o prompt de um usuário comum e mostra que o shell está pronto para receber um comando."}
::option[O próximo comando deve começar com um cifrão.]{#type-dollar-first explanation="O `$` pertence ao prompt. Você digita apenas o comando que vem depois dele, sem copiar o símbolo."}
:::

Os comandos geralmente seguem este padrão:

```bash
command options arguments
```

Por exemplo, em `echo Hello World`, `echo` é o comando e `Hello World` é o texto fornecido a ele.

:::single-choice{#identify-command-name}
Em `echo Hello World`, qual parte é o nome do comando?

::option[`Hello`]{#hello-command explanation="`Hello` vem depois do nome do comando e, portanto, faz parte do texto fornecido a `echo`."}
::option[`World`]{#world-command explanation="`World` também é um texto fornecido a `echo`, não o nome do comando executado."}
::option[`echo`]{#echo-command .correct explanation="`echo` dá nome ao programa que o shell deve executar. As palavras seguintes são fornecidas a esse programa como argumentos."}
:::

## Seu Primeiro Comando Linux

Vamos começar com um dos comandos Linux mais básicos para iniciantes: `echo`. Esse comando exibe no terminal o texto fornecido por você.

```bash
$ echo Hello World
Hello World
```

Experimente mais alguns exemplos:

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

As aspas são úteis quando você quer que o shell trate várias palavras como um único trecho de texto.

:::single-choice{#group-words-with-quotes}
Qual comando faz o shell tratar `Hello from Bash` como um único trecho de texto entre aspas?

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="As aspas agrupam as três palavras em um único argumento fornecido a `echo`."}
::option[`echo Hello from Bash`]{#unquoted-words explanation="Esse comando mostra as mesmas palavras, mas o shell as trata como argumentos separados, pois não estão entre aspas."}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="Colocar a linha inteira entre aspas faz o shell procurar um comando com todo esse nome, em vez de executar `echo` com um texto."}
:::

Para praticar essas habilidades, explore a abrangente [![Trilha de Aprendizado do Shell](https://labex.io/cdn-cgi/image/width=200,height=200,quality=80,format=auto,onerror=redirect/https://file.labex.io/path/FaVTnI4iqZP0.png)Trilha de Aprendizado do Shell](https://labex.io/learn/shell).

## Dicas Comuns para Iniciantes

- Pressione `Enter` para executar um comando.
- Use a tecla `Seta para cima` para recuperar um comando anterior.
- Comandos e nomes de arquivos diferenciam maiúsculas de minúsculas no Linux.
- Os espaços importam. `echo hello` e `echohello` são diferentes.
- Se um comando parecer travado, `Ctrl-C` geralmente o cancela.

## Resumo

Agora você sabe explicar a função de um shell e interagir com um prompt básico.

1. Diferencie um terminal de um shell.
2. Identifique um prompt de comando.
3. Execute um comando simples com `echo`.
