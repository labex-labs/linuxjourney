---
index: 5
lang: "pt"
title: "touch"
meta_title: "touch - Linha de Comando"
meta_description: "Aprenda o comando touch no Linux com exemplos para criar arquivos vazios, atualizar timestamps, definir datas, usar arquivos de referência e evitar sobrescritas."
meta_keywords: "comando linux touch, comando touch, criar arquivo linux, atualizar timestamp linux, touch -d, touch -r, touch -c"
---

## Lesson Content

O comando `touch` é uma utilidade padrão em sistemas operacionais do tipo Unix. Embora seu propósito principal seja alterar os timestamps de arquivos, ele também é comumente usado para criar arquivos novos e vazios.

A sintaxe básica é:

```bash
touch [OPTIONS] FILE...
```

### Criando Novos Arquivos

A maneira mais simples de criar um arquivo vazio é usar `touch` seguido do nome do arquivo. Se o arquivo não existir, o `touch` o cria.

```bash
$ touch mysuperduperfile
```

Após executar este comando, um novo arquivo vazio chamado `mysuperduperfile` aparecerá no seu diretório atual. Você pode criar múltiplos arquivos de uma vez listando seus nomes.

```bash
$ touch file1.txt file2.txt file3.log
```

Isso é útil ao configurar a estrutura de um projeto ou criar arquivos placeholder antes de adicionar conteúdo.

### Atualizando Timestamps de Arquivos

A função original do `touch` é atualizar os timestamps de acesso e modificação de um arquivo ou diretório. Se você usar `touch` em um arquivo existente, ele atualiza seus timestamps para o horário atual.

Você pode verificar isso usando `ls -l` para checar o timestamp de um arquivo, executando `touch` nele e depois verificando novamente.

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### Controle Avançado de Timestamps

O comando `touch` também oferece opções para manipulação mais precisa dos timestamps.

Use um arquivo de referência com `-r` para copiar os timestamps de um arquivo para outro.

```bash
$ touch -r file1.txt file2.txt
```

Defina uma data e hora específicas com `-d`:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Use `-c` quando quiser atualizar um arquivo somente se ele já existir. Com `-c`, o `touch` não criará um arquivo ausente.

```bash
$ touch -c existing-file.txt
```

### Opções Comuns do touch

- `-a`: Altera somente o tempo de acesso.
- `-m`: Altera somente o tempo de modificação.
- `-c`: Não cria o arquivo se ele não existir.
- `-d "DATA"`: Usa uma string de data específica.
- `-r ARQUIVO`: Usa o timestamp de outro arquivo como referência.
- `-t TIMESTAMP`: Usa um timestamp em formato numérico compacto.

Por exemplo, isto altera somente o tempo de modificação:

```bash
$ touch -m notes.txt
```

### Perguntas Comuns

**O touch adiciona texto a um arquivo?** Não. O `touch` cria um arquivo vazio ou atualiza timestamps. Use um editor, `echo` ou `cat` para adicionar texto.

**O touch sobrescreve um arquivo existente?** Não. Ele atualiza os timestamps, mas não substitui o conteúdo do arquivo.

**Por que usar touch em scripts?** É uma forma rápida de garantir que um arquivo exista ou marcar que uma tarefa ocorreu em um determinado momento.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of creating and managing file system objects:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/pt/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This will help you understand the broader concept of creating new items in the file system.
2. **[Setting Up a New Project Structure](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts of file system creation and organization in real scenarios and build confidence with Linux commands.

## Quiz Question

Como você cria um arquivo chamado `myfile`? Por favor, responda usando apenas o comando em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas.

## Quiz Answer

touch myfile
