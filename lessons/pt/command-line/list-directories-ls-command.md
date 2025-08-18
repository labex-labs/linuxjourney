---
index: 4
lang: "pt"
title: "ls (Listar Diretórios)"
meta_title: "ls (Listar Diretórios) - Linha de Comando"
meta_description: "Aprenda a usar o comando 'ls' no Linux para listar o conteúdo do diretório, visualizar arquivos ocultos e entender os detalhes dos arquivos. Melhore suas habilidades de linha de comando Linux!"
meta_keywords: "comando ls, listar diretórios, tutorial Linux, arquivos ocultos, comandos Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Agora que sabemos como nos mover pelo sistema, como descobrimos o que está disponível para nós? No momento, é como se estivéssemos nos movendo no escuro. Bem, podemos usar o maravilhoso comando `ls` para listar o conteúdo do diretório. O comando `ls` listará diretórios e arquivos no diretório atual por padrão; no entanto, você pode especificar qual caminho deseja listar os diretórios.

```bash
ls
ls /home/pete
```

`ls` é uma ferramenta bastante útil; ele também mostra informações detalhadas sobre os arquivos e diretórios que você está visualizando.

Além disso, observe que nem todos os arquivos em um diretório estarão visíveis. Nomes de arquivos que começam com `.` estão ocultos. Você pode visualizá-los, no entanto, com o comando `ls` e passar a flag `-a` para ele (`a` para all).

```bash
ls -a
```

Existe também mais uma flag útil do `ls`, `-l` para long. Isso mostra uma lista detalhada de arquivos em um formato longo. Isso mostrará informações detalhadas, começando da esquerda: permissões de arquivo, número de links, nome do proprietário, grupo do proprietário, tamanho do arquivo, carimbo de data/hora da última modificação e nome do arquivo/diretório.

```bash
ls -l
```

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

Comandos têm o que são chamados de flags (ou argumentos ou opções, como você quiser chamá-los) para adicionar mais funcionalidades. Veja como adicionamos `-a` e `-l`; bem, você pode adicioná-los juntos com `-la`. A ordem das flags determina a ordem em que elas aparecem. Na maioria das vezes, isso realmente não importa, então você também pode fazer `ls -al` e ainda funcionaria.

```bash
ls -la
```

## Exercise

Execute `ls` com diferentes flags e veja a saída que você recebe.

## Quiz Question

Qual comando você usaria para ver arquivos ocultos?

## Quiz Answer

ls -a
