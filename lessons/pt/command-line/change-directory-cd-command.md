---
index: 3
lang: "pt"
title: "cd (Mudar Diretório)"
meta_title: "cd (Mudar Diretório) - Linha de Comando"
meta_description: "Aprenda o comando Linux cd com exemplos para caminhos absolutos, caminhos relativos, atalhos para diretório home, diretórios pai e navegação para diretório anterior."
meta_keywords: "comando cd, comando linux cd, mudar diretório, cd diretório pai, cd home, cd diretório anterior, caminho absoluto, caminho relativo"
---

## Lesson Content

Para se movimentar pelo sistema de arquivos Linux, você usa caminhos para especificar seu destino. A ferramenta principal para isso é o comando `cd`, abreviação de change directory (mudar diretório). Ele altera o diretório de trabalho atual do shell.

A sintaxe básica é:

```bash
cd [DIRECTORY]
```

### Entendendo Caminhos

Existem duas formas de especificar um caminho: absoluto e relativo.

- **Caminho absoluto**: O caminho completo começando a partir do diretório raiz (`/`). Por exemplo: `/home/pete/Desktop`.

- **Caminho relativo**: Um caminho baseado na sua localização atual. Se você está em `/home/pete/Documents` e quer acessar um subdiretório chamado `taxes`, pode usar `taxes/`.

### Usando o Comando cd

Para mudar para um diretório específico usando um caminho absoluto, digite:

```bash
$ cd /home/pete/Pictures
```

Esse comando te leva diretamente para o diretório `Pictures`.

Você pode confirmar sua localização com `pwd`:

```bash
$ pwd
/home/pete/Pictures
```

### Navegando para um Subdiretório

Se você já está em um diretório e quer entrar em um subdiretório, use um caminho relativo. Por exemplo, se sua localização atual é `/home/pete/Pictures` e ele contém uma pasta chamada `Hawaii`, você pode navegar para dentro dela com:

```bash
$ cd Hawaii
```

Note que usamos apenas o nome da pasta. Isso porque já estávamos no diretório pai dela, `/home/pete/Pictures`.

### Atalhos Essenciais para Navegação

Navegar com caminhos completos pode ser cansativo. Felizmente, o shell oferece vários atalhos para tornar a movimentação muito mais rápida.

- `.` (diretório atual): Representa o diretório em que você está atualmente.
- `..` (diretório pai): Leva você um nível acima, para o diretório que contém o atual.
- `~` (diretório home): Um atalho para seu diretório pessoal home, como `/home/pete`.
- `-` (diretório anterior): Leva você de volta ao último diretório em que esteve.

Você pode usar esses atalhos com `cd`:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

Experimente esses atalhos para se tornar mais eficiente na linha de comando.

### Exemplos Práticos de cd

Vá para seu diretório home:

```bash
$ cd
```

Suba dois níveis:

```bash
$ cd ../..
```

Vá para um diretório cujo nome contém espaços, colocando-o entre aspas:

```bash
$ cd "Vacation Photos"
```

Volte para o diretório anterior:

```bash
$ cd -
/home/pete/Documents
```

### Perguntas Comuns

**Por que o cd diz "No such file or directory"?** O caminho não existe a partir da sua localização atual, ou o nome foi digitado incorretamente. Use `ls` para listar os diretórios disponíveis.

**Por que o cd diz "Permission denied"?** Você não tem permissão para entrar naquele diretório.

**O que acontece quando executo cd sem argumentos?** Ele te leva para seu diretório home.

**O cd funciona em arquivos?** Não. `cd` muda para diretórios, não para arquivos comuns.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux directory navigation:

1. **[Linux cd Command: Directory Changing](https://labex.io/pt/labs/linux-linux-cd-command-directory-changing-209733)** - Learn the Linux `cd` command to efficiently navigate your file system, including various techniques for changing directories, understanding paths, and exploring the file structure.
2. **[Linux Directory Navigation](https://labex.io/pt/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through directories using essential commands.
3. **[Setting Up a New Project Structure](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with navigating the Linux filesystem.

## Quiz Question

Se você está em `/home/pete/Pictures` e quer navegar para o diretório pai (`/home/pete`), qual é o comando completo que você deve usar? Por favor, responda em inglês, prestando atenção a maiúsculas e espaços.

## Quiz Answer

cd ..
