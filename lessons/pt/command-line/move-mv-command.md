---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "pt"
order_index: 11
title: "mv (Mover)"
description: "Aprenda a renomear e mover arquivos ou diretórios evitando substituições indesejadas."
meta_title: "mv (Mover) - Linha de Comando"
meta_description: "Aprenda o comando mv do Linux com exemplos para mover e renomear arquivos e diretórios, mover vários arquivos e evitar substituições."
meta_keywords: "comando mv Linux, comando mv, mover arquivos Linux, renomear arquivo Linux, renomear diretório Linux, mv -i, mv -n, mv -t"
---

O comando `mv` renomeia um arquivo ou diretório, ou o move para outro local. Ao contrário de `cp`, ele não mantém o caminho original após uma movimentação bem-sucedida.

A sintaxe básica é:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## Renomeação de Arquivos e Diretórios

Para renomear um item, coloque primeiro o caminho atual e depois o novo caminho.

Para renomear um arquivo:

```bash
$ mv oldfile newfile
```

A mesma ordem dos operandos renomeia um diretório:

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} Qual comando renomeia `cat` como `dog` no diretório atual?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` trata `cat` como o caminho de origem e `dog` como seu novo caminho de destino."}
::option[`mv dog cat`]{#rename-dog explanation="A ordem dos operandos está invertida. Esse comando tentaria renomear um `dog` existente como `cat`."}
::option[`cp cat dog`]{#copy-cat explanation="`cp` criaria uma cópia chamada `dog` e manteria `cat`. Ele não realizaria a renomeação solicitada."}
:::

## Movimentação de Itens para um Diretório

Quando o último operando é um diretório existente, `mv` coloca a origem dentro dele:

```bash
$ mv file2 /home/pete/Documents
```

Para mover várias origens, liste-as primeiro e coloque o diretório de destino por último:

```bash
$ mv file_1 file_2 somedirectory/
```

O GNU `mv` também oferece `-t` para colocar o diretório de destino antes das origens:

```bash
$ mv -t somedirectory/ file_1 file_2
```

Ao contrário de `cp`, `mv` não precisa de uma opção recursiva para um diretório.

:::single-choice{#move-multiple-files} Qual comando move `file_1` e `file_2` para o diretório existente `archive/`?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="Sem a opção GNU `-t`, uma movimentação com várias origens espera o diretório de destino por último. Essa não é a forma padrão."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` não usa `-r` para mover arquivos ou diretórios. A forma comum com várias origens já realiza a movimentação solicitada."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="Com várias origens, o diretório de destino existente é o último operando e recebe os dois arquivos."}
:::

## Controle dos Destinos Existentes

Por padrão, `mv` pode substituir um destino existente. Inspecione os caminhos de origem e destino antes de executar uma movimentação e escolha uma política de substituição quando necessário:

- `-i`: solicita confirmação antes de substituir um destino existente.

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`: não sobrescreve um destino existente.

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`: no GNU/Linux, cria um backup do destino que seria substituído. O sufixo padrão do backup geralmente é `~`.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`: mostra cada movimentação conforme ela ocorre.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} Qual comando move `draft.txt` para `finished/` somente se isso não sobrescrever um destino existente?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="A opção `-i` pergunta o que fazer quando há um destino. Ainda pode ocorrer uma substituição se o usuário a confirmar."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="A opção `-b` permite a substituição e mantém um backup do destino anterior. Ela não impede a sobrescrita."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="A opção `-n` ignora uma movimentação que sobrescreveria um destino existente."}
:::

## Movimentação de Diretórios e Correspondências de Curingas

Um diretório pode ser movido sem `-r`:

```bash
$ mv project /home/pete/Documents/
```

Curingas do shell podem selecionar várias origens:

```bash
$ ls *.txt
$ mv *.txt notes/
```

Visualizar as correspondências com `ls` ajuda a detectar um padrão amplo demais antes de alterar vários caminhos.

:::single-choice{#move-directory-without-recursion} Qual comando move o diretório `project/` para `/srv/archive/`?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` não precisa nem oferece suporte a `-r` para essa finalidade. Os diretórios são tratados pela operação comum de movimentação."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="A sintaxe comum de `mv` move um diretório para um diretório de destino existente sem um sinalizador recursivo."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="Um `cp` simples não move o diretório e precisaria de uma opção recursiva para copiá-lo. A origem também continuaria no lugar."}
:::

:::single-choice{#preview-text-file-move} Você pretende executar `mv *.txt notes/`. Qual comando visualiza os caminhos selecionados pelo mesmo curinga?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="As aspas impedem o shell de expandir `*`; assim, o comando procura um nome literal com asterisco em vez de mostrar o conjunto da movimentação."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="O shell expande `*.txt` para `ls` da mesma forma que faria para `mv`, permitindo inspecionar primeiro os nomes não ocultos selecionados."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="O modo detalhado relata as movimentações enquanto elas acontecem. Ele realiza a operação, em vez de oferecer uma visualização somente para leitura."}
:::

Para praticar a movimentação e a renomeação de itens, experimente estes laboratórios:

1. **[Comando mv do Linux: Movimentação e Renomeação de Arquivos](https://labex.io/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** — Pratique o uso de `mv` para mover e renomear arquivos e diretórios, conhecendo suas opções e comportamentos.
2. **[Organização de Arquivos e Diretórios](https://labex.io/labs/linux-organizing-files-and-directories-387877)** — Aplique seu conhecimento de `mv`, junto com `cp` e `rm`, em um desafio prático para organizar um projeto, mover arquivos e eliminar diretórios desnecessários.

## Resumo

Agora você sabe renomear e mover arquivos ou diretórios protegendo os destinos existentes.

1. Coloque a origem antes de seu novo caminho.
2. Coloque o diretório de destino depois de várias origens.
3. Pergunte, ignore ou crie um backup antes de substituir um destino.
4. Mova diretórios sem uma opção recursiva.
5. Visualize as correspondências de curingas antes de uma movimentação em massa.
