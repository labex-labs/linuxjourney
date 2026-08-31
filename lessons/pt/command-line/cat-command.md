---
lesson_id: "cat-command"
course_id: "command-line"
lang: "pt"
order_index: 7
title: "cat"
description: "Aprenda a exibir, concatenar e redirecionar conteúdo de arquivos com segurança usando o comando cat."
meta_title: "cat - Linha de Comando"
meta_description: "Aprenda o comando cat do Linux com exemplos para visualizar e concatenar arquivos, numerar linhas, criar arquivos e usar redirecionamento com segurança."
meta_keywords: "comando cat Linux, comando cat, visualizar arquivo Linux, concatenar arquivos, cat -n, cat -b, redirecionamento cat, cat Linux"
---

Depois de aprender a identificar arquivos, o próximo passo é ler seu conteúdo. O comando `cat` exibe arquivos e une seus conteúdos; seu nome é uma abreviação de “concatenate”.

## Visualização do Conteúdo de um Arquivo

O uso mais simples de `cat` exibe um arquivo diretamente no terminal:

```bash
$ cat myfile.txt
```

O comando grava o arquivo inteiro na saída padrão. Isso funciona bem para textos curtos, mas um arquivo longo pode passar rápido demais pela tela.

:::single-choice{#display-short-file}
Qual comando exibe todo o conteúdo de `myfile.txt` no terminal?

::option[`file myfile.txt`]{#classify-myfile explanation="`file` informa o provável tipo do arquivo. Ele não mostra todo o texto armazenado."}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` atualiza horários ou cria um arquivo ausente. Ele não exibe o conteúdo."}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` lê `myfile.txt` e grava seu conteúdo na saída padrão, que neste caso é o terminal."}
:::

## Concatenação de Arquivos

Quando você fornece vários arquivos a `cat`, ele os lê na ordem dos operandos e grava seus conteúdos um após o outro:

```bash
$ cat dogfile birdfile
```

Esse comando exibe primeiro `dogfile` e depois `birdfile`. Para salvar a saída combinada em um novo arquivo, redirecione a saída padrão com `>`:

```bash
$ cat dogfile birdfile > animals
```

O shell cria `animals` ou o trunca antes de executar `cat` e então envia a saída combinada para ele. Não use um dos arquivos de entrada como destino, pois ele pode ser esvaziado antes que `cat` consiga lê-lo.

:::single-choice{#combine-files-in-order}
Qual comando grava `part1`, seguido de `part2`, em um arquivo novo ou substituído chamado `whole`?

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="O redirecionamento possui um único destino, enquanto as outras palavras se tornam operandos de `cat`. Isso não expressa a ordem de entrada e saída solicitada."}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` emite os dois arquivos na ordem indicada, e `>` redireciona essa saída combinada para `whole`."}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="Esse comando grava as mesmas duas entradas em `whole`, mas lê `part2` antes de `part1`. A ordem dos operandos controla a saída."}
:::

## Leitura da Entrada do Terminal para um Arquivo

Quando nenhum arquivo de entrada é fornecido, `cat` lê a entrada padrão. Você pode combinar esse comportamento com `>` para digitar um texto no terminal e gravá-lo em um arquivo:

```bash
$ cat > newfile.txt
```

Depois de executar o comando, digite o texto desejado. Pressione `Ctrl+D` para enviar um sinal de fim de arquivo e retornar ao shell. Tenha cuidado: se `newfile.txt` já existir, `>` truncará seu conteúdo anterior.

Use `>>` para acrescentar a nova entrada em vez de substituir o conteúdo existente:

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input}
Você quer digitar mais texto no final de um `notes.txt` existente. Qual comando inicia essa operação sem truncar o arquivo?

::option[`cat > notes.txt`]{#overwrite-notes explanation="Um único `>` redireciona a entrada depois de truncar o destino. O texto existente em `notes.txt` seria perdido."}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="O operador `>>` abre o destino para acréscimo; assim, o texto lido por `cat` é adicionado depois do conteúdo existente."}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="Usar o mesmo arquivo como entrada e destino de `>` pode truncá-lo antes que `cat` o leia. Essa não é uma operação segura de acréscimo."}
:::

## Formatação da Saída

Várias opções facilitam a inspeção da saída:

- `-n`: numera todas as linhas de saída a partir de 1.
- `-b`: numera apenas as linhas de saída não vazias.
- `-s`: reduz várias linhas vazias consecutivas a uma só.
- `-A`: mostra caracteres não imprimíveis, tabulações e finais de linha.

Exemplos:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines}
Qual comando numera apenas as linhas não vazias de `notes.txt`?

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="A opção `-b` numera as linhas de saída não vazias e deixa as linhas vazias sem numeração."}
::option[`cat -n notes.txt`]{#number-all-lines explanation="A opção `-n` numera todas as linhas de saída, inclusive as vazias. Ela não atende à condição solicitada."}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="A opção `-s` reduz linhas vazias repetidas a uma. Ela não acrescenta números de linha."}
:::

## Escolha de um Visualizador para Arquivos Longos

Use `cat` quando quiser toda a saída de uma só vez. Para um arquivo longo, `less` costuma ser mais conveniente, pois permite rolar, pesquisar e sair sem inundar o terminal:

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file}
Qual comando é mais adequado para ler interativamente um arquivo de log longo?

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` oferece rolagem, pesquisa e uma saída controlada, sendo adequado à leitura interativa de arquivos longos."}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` grava o log inteiro no terminal de uma só vez. Um arquivo longo pode passar pela tela antes que você consiga inspecioná-lo."}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` altera os horários e pode exigir permissões. Ele não é um comando para ler o log."}
:::

Para praticar a exibição e a combinação do conteúdo de arquivos, experimente estes laboratórios:

1. **[Comando cat do Linux: Concatenação de Arquivos](https://labex.io/labs/linux-linux-cat-command-file-concatenating-210986)** — Aprenda a usar `cat` para visualizar, concatenar e manipular arquivos de texto, aprimorando suas habilidades de linha de comando.
2. **[Visualização de Arquivos de Log e Configuração no Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** — Pratique comandos como `cat` para visualizar e percorrer arquivos de texto, inclusive logs e configurações do sistema, e extrair informações importantes.

## Resumo

Agora você sabe usar `cat` para exibir e combinar conteúdo de arquivos escolhendo um redirecionamento seguro.

1. Exiba todo o conteúdo de um arquivo curto.
2. Concatene arquivos na ordem escolhida.
3. Substitua ou acrescente ao destino de forma consciente.
4. Numere ou simplifique as linhas de saída.
5. Escolha `less` quando a leitura interativa for mais adequada.
