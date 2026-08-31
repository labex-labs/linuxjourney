---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "pt"
order_index: 1
title: "stdout (Saída Padrão)"
description: "Aprenda como a saída padrão flui para o terminal e como o Bash a redireciona para arquivos."
meta_title: "stdout (Saída Padrão) - Text-Fu"
meta_description: "Comece a dominar a saída padrão, ou stdout, e o redirecionamento de E/S. Aprenda a enviar a saída de comandos para arquivos com os operadores > e >>."
meta_keywords: "Linux, aprender Linux, stdout, redirecionamento E/S, saída padrão, redirecionar saída, Bash, scripts shell, comandos Linux, tutorial Linux"
---

Os programas se comunicam por meio de fluxos de entrada e saída. A saída padrão, abreviada como **stdout**, é o fluxo que um programa normalmente usa para seus resultados comuns. Em um terminal, o shell conecta inicialmente esse fluxo à tela do terminal.

## Gravação na Saída Padrão

O comando `echo` grava seus argumentos em stdout:

```bash
$ echo Hello World
Hello World
```

Stdout é o descritor de arquivo `1`, um número que se torna útil ao redirecionar mais de um fluxo. Os programas também podem ter entrada padrão, ou stdin, e erro padrão, ou stderr; as próximas lições examinam esses fluxos.

:::single-choice{#stdout-default-destination}
Sem redirecionamento, para onde `echo Hello World` normalmente envia sua saída comum em um terminal interativo?

::option[Para um arquivo chamado `stdout` no diretório atual.]{#stdout-file explanation="A saída padrão é um fluxo, não um arquivo chamado `stdout` criado automaticamente. Um arquivo só é usado quando há redirecionamento."}
::option[Para o terminal por meio da saída padrão.]{#stdout-terminal .correct explanation="O shell normalmente conecta stdout de um comando ao terminal; por isso, a saída de `echo` é exibida ali."}
::option[Para o fluxo de entrada padrão do comando.]{#stdout-to-stdin explanation="A entrada padrão transporta dados para dentro de um programa. `echo` envia seu resultado comum para fora por stdout."}
:::

## Substituição de um Arquivo com >

O Bash interpreta `>` como um operador de redirecionamento de saída. Ele abre o arquivo de destino e conecta a stdout do comando a ele:

```bash
$ echo Hello World > peanuts.txt
```

O texto deixa de aparecer no terminal porque stdout é enviada para `peanuts.txt`. Se o arquivo não existir, o shell o criará. Se existir, o shell o truncará antes que o comando grave, e o conteúdo anterior será perdido.

Use `cat` para inspecionar o resultado:

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file}
`notes.txt` já contém texto. O que `echo new > notes.txt` faz?

::option[Substitui o conteúdo do arquivo por `new`.]{#stdout-replace-existing .correct explanation="O shell trunca o destino existente para `>` e direciona a saída de `echo` para o arquivo agora vazio."}
::option[Acrescenta `new` depois do texto existente.]{#stdout-add-existing explanation="O acréscimo exige `>>`. Um único `>` não preserva o conteúdo anterior do destino."}
::option[Exibe `new` sem alterar o arquivo.]{#stdout-display-only explanation="O redirecionamento envia stdout para `notes.txt`; portanto, a saída comum não permanece no terminal."}
:::

Como o shell abre o destino antes de executar o comando, verifique o caminho antes de pressionar Enter. Um nome digitado incorretamente ou um arquivo existente não pretendido pode ser truncado mesmo que o comando falhe depois.

## Acréscimo a um Arquivo com >>

Use `>>` quando a nova stdout deve ser acrescentada depois do conteúdo existente de um arquivo:

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

Assim como `>`, `>>` cria um destino ausente. A diferença está na abertura de um arquivo existente: `>>` acrescenta em vez de truncar.

:::single-choice{#stdout-append-file}
Qual comando acrescenta `Finished` ao final de `status.log` sem apagar o conteúdo existente?

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="Um único `>` trunca o destino existente antes da gravação. Ele apagaria o conteúdo anterior do log."}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo` produz o texto, e `>>` acrescenta essa stdout ao arquivo de destino."}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="Esse comando pede que `cat` leia um arquivo chamado `Finished`. Ele não produz o texto solicitado na stdout."}
:::

## O Redirecionamento Pertence ao Shell

O shell reconhece `>` e `>>`, remove esses operadores dos argumentos fornecidos ao programa, abre o arquivo e organiza a conexão do fluxo. O comando simplesmente continua gravando em stdout como de costume.

Isso significa que a mesma sintaxe de redirecionamento funciona com muitos comandos:

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role}
Quem normalmente interpreta `>` em `pwd > current-directory.txt`?

::option[O comando `pwd`, depois de receber `>` como argumento.]{#stdout-pwd-redirection explanation="O shell consome a sintaxe de redirecionamento; portanto, `pwd` normalmente não recebe `>` nem o destino como argumentos comuns."}
::option[O shell Bash, antes de iniciar `pwd`.]{#stdout-bash-redirection .correct explanation="O Bash abre o destino e conecta o descritor de arquivo 1 antes de executar o comando."}
::option[O terminal, depois que `pwd` mostra o caminho na tela.]{#stdout-terminal-redirection explanation="O fluxo é redirecionado antes da gravação da saída; assim, o terminal nem chega a receber essa stdout."}
:::

Para praticar o redirecionamento dos fluxos padrão, experimente este laboratório:

1. **[Redirecionamento de Entrada e Saída no Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** — Pratique o controle do fluxo de dados dos comandos manipulando saída padrão (stdout), erro padrão (stderr) e entrada padrão (stdin) com operadores como `>`, `>>`, `2>` e o comando `tee`.

## Resumo

Agora você sabe redirecionar a saída padrão de um comando sem confundir substituição com acréscimo.

1. Reconheça stdout como o fluxo dos resultados comuns dos comandos.
2. Substitua o conteúdo de um arquivo com `>`.
3. Preserve o conteúdo existente e acrescente com `>>`.
4. Verifique o destino antes que o shell o abra.
