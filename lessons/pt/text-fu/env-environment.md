---
index: 5
lang: "pt"
title: "env (Ambiente)"
meta_title: "env (Ambiente) - Text-Fu"
meta_description: "Explore o que o comando env faz no Linux. Este guia explica como visualizar e usar variáveis de ambiente do Linux como PATH, HOME e USER com o comando env."
meta_keywords: "env, env linux, comando env linux, o que o env faz no linux, variáveis de ambiente, variável PATH, variáveis de shell"
---

## Lesson Content

Seu sistema Linux usa variáveis de ambiente para armazenar informações que o shell e outros processos podem acessar. Essas variáveis contêm dados úteis sobre sua sessão de usuário e configuração do sistema.

### Explorando Variáveis de Ambiente Básicas

You can view the value of a specific variable by prefixing its name with a `$` symbol. For example, run the following command:

```bash
echo $HOME
```

This command will display the path to your home directory, which might look something like `/home/pete`.

Now, try another one:

```bash
echo $USER
```

This will output your current username. But where does this information come from? It's stored in your shell's environment.

### O que o env faz no Linux

To see all the environment variables currently set for your session, you can use the `env` command. The `linux env command` is a fundamental tool for inspecting your shell's configuration.

```bash
env
```

Running the `env` command will output a list of key-value pairs. Here is a short example of what you might see:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Understanding the `linux env` is crucial for managing your system effectively.

### A Importância da Variável PATH

One of the most important variables in your `env linux` output is `PATH`. You can view its contents specifically with:

```bash
echo $PATH
```

This command returns a colon-separated list of directories. When you type a command, your system searches through these directories to find the corresponding executable file.

Imagine you manually install a program in a non-standard directory like `/opt/coolapp/bin`. If you try to run it by typing `coolcommand`, you might get a "command not found" error. This happens because the directory containing your program is not listed in the `PATH` variable, so the shell doesn't know where to look for it.

To fix this, you can modify the `PATH` variable to include the new directory. By adding your custom directory to `PATH`, you enable the shell to find and execute your programs from anywhere in the terminal.

### Definindo uma Variável de Ambiente para a Sessão Atual

Running the following command in your terminal sets the environment variable `TEST` for the current session only:

```bash
export TEST=test
```

After this, if you run:

```bash
echo $TEST
```

The output will be:

```
test
```

This variable will be available as long as the terminal session remains open. Once you close and reopen the terminal, the variable will no longer exist.

### Tornando a Variável de Ambiente Persistente Entre Sessões

If you want the environment variable to be available in every terminal session (even after closing and reopening the terminal), you need to add it to your shell’s startup file. In the case of Bash (the default shell for many Linux distributions and macOS), this file is usually `.bashrc` in your home directory.

Here's how you do it:

1. Open `.bashrc` in your preferred text editor. For example:

```bash
nano ~/.bashrc
```

2. Add the `export` line to the end of the file:

```bash
export TEST=test
```

3. Save and exit the editor (in Nano, this would be `Ctrl+X`, then `Y` to confirm, and `Enter`).

4. To apply the changes immediately without reopening the terminal, run:

```bash
source ~/.bashrc
```

After this, the `TEST` variable will be available in all future terminal sessions, and running `echo $TEST` will print `test` even after you close and reopen the terminal.

### Uma Nota Sobre Arquivos de Configuração do Shell

- For **Bash** (the default on many systems), the relevant file is `~/.bashrc` for non-login interactive shells.
- For **Zsh**, the equivalent file is usually `~/.zshrc`.
- For **Fish**, you'd typically use `~/.config/fish/config.fish`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das variáveis de ambiente do Linux:

1. **[Gerenciar Ambiente e Configuração do Shell no Linux](https://labex.io/pt/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Pratique a criação e o gerenciamento de variáveis locais e de ambiente, entendendo a herança e tornando as configurações persistentes modificando o arquivo `.bashrc`.
2. **[Variáveis de Ambiente no Linux](https://labex.io/pt/labs/linux-environment-variables-in-linux-385274)** - Aprenda o conceito e o uso de variáveis de ambiente, como criá-las, modificá-las e gerenciá-las, e seu papel na configuração do sistema.
3. **[Configurar Variáveis de Ambiente do Linux](https://labex.io/pt/labs/linux-configure-linux-environment-variables-437861)** - Ganhe experiência prática criando, definindo e gerenciando variáveis de ambiente em um sistema Linux.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento do seu ambiente de shell Linux.

## Quiz Question

Qual comando exibe todas as suas variáveis de ambiente atuais? (Por favor, responda em inglês, usando apenas o nome do comando em minúsculas)

## Quiz Answer

env
