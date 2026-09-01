---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "pt"
order_index: 4
title: "ls (Listar Diretórios)"
description: "Aprenda a usar as opções de ls para inspecionar arquivos, entradas ocultas, detalhes, tamanhos e ordem de classificação."
meta_title: "ls (Listar Diretórios) - Linha de Comando"
meta_description: "Aprenda o comando ls do Linux com exemplos para listar arquivos, arquivos ocultos, detalhes, tamanhos legíveis, classificação e combinações de opções."
meta_keywords: "comando ls, ls Linux, listar arquivos Linux, listar diretórios, ls -a, ls -l, ls -lh, ls -r, arquivos ocultos"
---

Agora que sabemos navegar pelo sistema de arquivos, como descobrimos o que está disponível? O comando `ls` lista arquivos e diretórios para que você possa inspecionar sua localização atual ou outro caminho.

## Uso Básico do Comando ls

Por padrão, `ls` lista os diretórios e arquivos do diretório atual. Você também pode fornecer um caminho para listar o conteúdo de outro diretório.

```bash
$ ls
$ ls /home/pete
```

Também é possível listar um arquivo específico:

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory} Qual comando lista o conteúdo de `/home/pete` sem entrar nesse diretório?

::option[`ls /home/pete`]{#ls-target-path .correct explanation="Fornecer o caminho de um diretório a `ls` lista seu conteúdo. O shell permanece no diretório de trabalho atual."}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` muda o diretório de trabalho do shell. Por si só, ele não realiza a listagem solicitada."}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` informa o diretório de trabalho atual e não recebe um destino para listar. Use `ls` com o caminho."}
:::

## Visualização de Arquivos Ocultos

Nem todos os arquivos de um diretório aparecem por padrão. No Linux, nomes de arquivos que começam com um ponto (`.`) ficam ocultos. Você pode exibi-los com a opção `-a`, de all.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

Arquivos com nomes iniciados por ponto ficam ocultos por padrão e frequentemente armazenam configurações, como `.bashrc`.

:::single-choice{#show-hidden-files} Qual comando inclui os arquivos ocultos na listagem?

::option[`ls -l`]{#long-format explanation="A opção `-l` acrescenta colunas detalhadas, mas não inclui por si só os nomes ocultos."}
::option[`ls -r`]{#reverse-order explanation="A opção `-r` inverte a ordem de classificação. Ela não altera a inclusão dos arquivos ocultos."}
::option[`ls -a`]{#all-files .correct explanation="A opção `-a` significa all, ou todos, e faz `ls` incluir os nomes iniciados por ponto."}
:::

## Obtenção de Informações Detalhadas

Outra opção essencial de `ls` é `-l`, que seleciona o formato longo. Ela mostra as permissões, o número de links, o proprietário, o grupo, o tamanho, a data de modificação e o nome.

```bash
$ ls -l
```

Veja um exemplo da saída:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

Para facilitar a leitura dos tamanhos, acrescente `-h`, de human-readable:

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details} Qual comando exibe os detalhes no formato longo com tamanhos legíveis?

::option[`ls -la`]{#long-all explanation="Esse comando combina o formato longo com a inclusão de arquivos ocultos. Ele não solicita unidades de tamanho legíveis."}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` seleciona o formato longo e `-h` facilita a leitura dos tamanhos. As opções podem ser combinadas em um único comando."}
::option[`ls -ltr`]{#long-time-reverse explanation="Esse comando combina formato longo, classificação por data de modificação e ordem inversa. Ele não inclui a opção de tamanho `-h`."}
:::

## Classificação em Ordem Inversa

Às vezes, você pode querer mudar a ordem de classificação. A opção `-r` lista os arquivos e diretórios em ordem inversa.

```bash
$ ls -r
```

Você pode classificar pela data de modificação com `-t` e depois inverter a ordem com `-r`:

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last} Qual comando classifica pela data de modificação e coloca as entradas mais recentes por último?

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` classifica pela data de modificação, enquanto `-r` inverte essa ordem. Juntas, elas colocam as entradas mais antigas antes das recentes."}
::option[`ls -lt`]{#time-default explanation="Esse comando classifica pela data de modificação, mas mantém a direção padrão, da mais recente para a mais antiga."}
::option[`ls -lr`]{#reverse-name-order explanation="Esse comando usa o formato longo e inverte a classificação padrão por nome. Sem `-t`, a data de modificação não controla a ordem."}
:::

## Combinação de Opções de Comando

Os comandos possuem sinalizadores, também chamados de opções, que acrescentam funcionalidades. Como vimos com `-a` e `-l`, você pode combiná-los em um único comando, como `ls -la`. A ordem dos sinalizadores muitas vezes não importa; portanto, `ls -al` funciona da mesma maneira.

```bash
$ ls -la
```

Algumas combinações úteis são:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## Opções Comuns de ls

- `-a`: mostra todos os arquivos, inclusive os ocultos.
- `-l`: usa o formato longo.
- `-h`: mostra tamanhos legíveis quando usado com `-l`.
- `-r`: inverte a ordem de classificação.
- `-t`: classifica pela data de modificação.
- `-S`: classifica pelo tamanho do arquivo.
- `-d`: lista o próprio diretório, em vez de seu conteúdo.

:::single-choice{#list-directory-entry-itself} Qual comando lista a entrada do diretório `projects/` em vez de seu conteúdo?

::option[`ls -d projects/`]{#directory-entry .correct explanation="A opção `-d` instrui `ls` a mostrar a própria entrada do diretório, em vez de abri-lo para listar o conteúdo."}
::option[`ls projects/`]{#directory-contents explanation="Sem `-d`, fornecer o caminho de um diretório faz `ls` exibir as entradas contidas nele."}
::option[`cd projects/`]{#change-to-directory explanation="`cd` muda o diretório de trabalho. Ele não lista a entrada de diretório solicitada."}
:::

Alguns sistemas exibem a saída de `ls` em cores diferentes conforme o tipo de arquivo. Esse comportamento costuma vir de um alias ou de uma configuração do ambiente; portanto, as cores podem variar entre sistemas.

Para reforçar sua compreensão do comando `ls`, experimente este laboratório prático:

- **[Comando ls do Linux: Listagem de Conteúdo](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)** — Pratique o uso de `ls` para listar e analisar com eficiência o conteúdo de arquivos e diretórios. Você aprenderá opções para listagens detalhadas, exibição de arquivos ocultos, tamanhos legíveis e técnicas de classificação.

Esse laboratório ajudará você a aplicar os conceitos em um cenário real e a ganhar confiança na listagem de diretórios no Linux.

## Resumo

Agora você sabe usar `ls` para inspecionar o conteúdo de diretórios e controlar como as entradas são exibidas.

1. Liste o diretório atual ou outro caminho.
2. Inclua arquivos ocultos em uma listagem.
3. Mostre informações detalhadas com tamanhos legíveis.
4. Classifique as entradas pela data de modificação em ordem inversa.
5. Liste uma entrada de diretório sem listar seu conteúdo.
