---
index: 7
lang: "pt"
title: "cat"
meta_title: "cat - Linha de Comando"
meta_description: "Aprenda o comando cat do Linux com exemplos para visualizar arquivos, concatenar arquivos, numerar linhas, criar arquivos e usar redirecionamento com segurança."
meta_keywords: "comando linux cat, comando cat, visualizar arquivo linux, concatenar arquivos, cat -n, cat -b, redirecionamento cat, linux cat"
---

## Lesson Content

Após aprender a navegar no sistema de arquivos, o próximo passo é visualizar o conteúdo dos arquivos. Uma ferramenta fundamental e versátil para isso é o comando `cat`. O nome `cat` é uma abreviação de "concatenate" (concatenar), o que indica sua capacidade de ligar arquivos juntos.

### Visualizando o Conteúdo de Arquivos

O uso mais básico do comando `cat` é exibir o conteúdo de um único arquivo diretamente no seu terminal.

```bash
$ cat myfile.txt
```

Este comando imprimirá todo o conteúdo de `myfile.txt` na tela. Embora seja perfeito para arquivos de configuração curtos ou trechos de texto, não é ideal para visualizar arquivos grandes, pois o texto passará muito rápido. Cobriremos ferramentas mais adequadas para arquivos grandes em uma lição posterior.

### Concatenando Arquivos

Fiel ao seu nome, o `cat` pode combinar, ou concatenar, vários arquivos e exibir sua saída combinada. Ele lê os arquivos na ordem em que são fornecidos e os imprime sequencialmente.

```bash
$ cat dogfile birdfile
```

Este comando exibirá primeiro o conteúdo de `dogfile`, imediatamente seguido pelo conteúdo de `birdfile`.

Para salvar a saída combinada em um novo arquivo, use o redirecionamento:

```bash
$ cat dogfile birdfile > animals
```

### Criando Arquivos com Redirecionamento

Você também pode usar o `cat` com o operador de redirecionamento de saída (`>`) para criar novos arquivos. Esta é uma maneira rápida de escrever texto em um arquivo diretamente do seu terminal.

```bash
$ cat > newfile.txt
```

Após executar este comando, você pode digitar seu texto. Pressione `Ctrl+D` em uma nova linha para salvar e sair. Isso criará `newfile.txt` com o texto que você digitou. Tenha cuidado, pois usar `>` em um arquivo existente irá sobrescrevê-lo completamente.

Para acrescentar a um arquivo em vez de sobrescrevê-lo, use `>>`.

```bash
$ cat >> notes.txt
```

### Opções Comuns do Comando cat

O comando `cat` possui várias opções para modificar seu comportamento.

- `-n`: Numera todas as linhas de saída, começando do 1.
- `-b`: Numera apenas as linhas de saída que não estão vazias.
- `-s`: Comprime múltiplas linhas em branco em uma única linha em branco.
- `-A`: Mostra caracteres não imprimíveis, tabulações e finais de linha.

Exemplos:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

### Quando Não Usar cat

Use `cat` para arquivos curtos. Para arquivos longos, use `less` para que você possa rolar, buscar e sair sem inundar seu terminal.

```bash
$ less /var/log/syslog
```

### Perguntas Comuns

**O que significa cat?** Significa concatenar.

**O cat pode editar um arquivo?** Não interativamente. Ele pode criar ou sobrescrever arquivos com redirecionamento, mas um editor de texto é melhor para editar.

**Qual a diferença entre > e >>?** `>` sobrescreve um arquivo. `>>` acrescenta ao final de um arquivo.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing file contents:

1. **[Linux cat Command: File Concatenating](https://labex.io/pt/labs/linux-linux-cat-command-file-concatenating-210986)** - Learn the `cat` command for viewing, concatenating, and manipulating text files, enhancing your command-line skills for efficient text file handling.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/pt/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using commands like `cat` to efficiently view and navigate text files, including system logs and configuration files, to extract critical information.

These labs will help you apply the concepts in real scenarios and build confidence with file content viewing in Linux.

## Quiz Question

Qual comando é usado para exibir o conteúdo de um arquivo na linha de comando? (Nota: Sua resposta deve ser uma única palavra em inglês, toda em minúsculas.)

## Quiz Answer

cat
