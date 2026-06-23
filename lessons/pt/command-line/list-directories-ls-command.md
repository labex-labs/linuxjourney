---
index: 4
lang: "pt"
title: "ls (Listar Diretórios)"
meta_title: "ls (Listar Diretórios) - Linha de Comando"
meta_description: "Aprenda o comando Linux ls com exemplos para listar arquivos, arquivos ocultos, saída em formato longo, tamanhos legíveis, ordenação e combinação de opções."
meta_keywords: "comando ls, linux ls, listar arquivos linux, listar diretórios, ls -a, ls -l, ls -lh, ls -r, arquivos ocultos"
---

## Lesson Content

Agora que sabemos como navegar pelo sistema de arquivos, como descobrimos o que está disponível para nós? O comando `ls` lista arquivos e diretórios para que você possa inspecionar sua localização atual ou outro caminho.

### Uso Básico do Comando ls

Por padrão, o comando `ls` listará os diretórios e arquivos no seu diretório atual. No entanto, você também pode especificar um caminho para listar o conteúdo de um diretório diferente.

```bash
$ ls
$ ls /home/pete
```

Você também pode listar um arquivo específico:

```bash
$ ls /etc/hosts
/etc/hosts
```

### Visualizando Arquivos Ocultos

Nem todos os arquivos em um diretório são visíveis por padrão. No Linux, nomes de arquivos que começam com um ponto (`.`) são ocultos. Você pode visualizá-los com a opção `-a`, que significa todos.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### Obtendo Informações Detalhadas

Outra opção essencial do `ls` é `-l` para formato longo. Ela mostra permissões de arquivo, número de links, proprietário, grupo, tamanho, hora da modificação e nome.

```bash
$ ls -l
```

Aqui está um exemplo da saída:

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

Para tamanhos de arquivo mais fáceis de entender, adicione `-h` para saída legível por humanos:

```bash
$ ls -lh
```

### Ordenação em Ordem Reversa

Às vezes, você pode querer mudar a ordem de ordenação. A opção `-r` lista arquivos e diretórios em ordem reversa.

```bash
$ ls -r
```

Você pode ordenar por tempo de modificação com `-t`, e depois inverter com `-r`:

```bash
$ ls -lt
$ ls -ltr
```

### Combinando Flags de Comando

Comandos têm flags, também chamadas opções, para adicionar mais funcionalidades. Como vimos com `-a` e `-l`, você pode combiná-las em um único comando como `ls -la`. A ordem das flags geralmente não importa, então `ls -al` funciona da mesma forma.

```bash
$ ls -la
```

Combinações úteis incluem:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

### Opções Comuns do ls

- `-a`: Mostra todos os arquivos, incluindo os ocultos.
- `-l`: Usa formato longo.
- `-h`: Mostra tamanhos legíveis com `-l`.
- `-r`: Inverte a ordem de ordenação.
- `-t`: Ordena por tempo de modificação.
- `-S`: Ordena por tamanho do arquivo.
- `-d`: Lista o diretório em si ao invés do seu conteúdo.

### Perguntas Comuns

**Por que alguns nomes de arquivos começam com um ponto?** Arquivos com ponto são ocultos por padrão e frequentemente armazenam configurações, como `.bashrc`.

**Como listar apenas o diretório em si?** Use `ls -d directory/`.

**Como vejo os arquivos mais novos por último?** Use `ls -ltr`.

**Por que o ls mostra cores?** Muitos sistemas configuram o `ls` para colorir tipos de arquivos através de um alias ou configuração de ambiente.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar seu entendimento do comando `ls`:

- **[Comando Linux ls: Listagem de Conteúdo](https://labex.io/pt/labs/linux-linux-ls-command-content-listing-219205)** - Pratique o uso do comando `ls` para listar e analisar eficientemente o conteúdo de arquivos e diretórios. Você aprenderá várias opções para listagens detalhadas, exibição de arquivos ocultos, tamanhos legíveis e técnicas de ordenação para aprimorar suas habilidades na linha de comando.

Este laboratório ajudará você a aplicar os conceitos em um cenário real e ganhar confiança com a listagem de diretórios no Linux.

## Quiz Question

Qual comando você usaria para ver arquivos ocultos? Por favor, responda em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas.

## Quiz Answer

ls -a
