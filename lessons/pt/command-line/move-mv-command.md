---
index: 11
lang: "pt"
title: "mv (Mover)"
meta_title: "mv (Mover) - Linha de Comando"
meta_description: "Aprenda a usar o comando Linux mv para mover e renomear arquivos/diretórios. Entenda suas opções e evite sobrescrições. Comece sua jornada no Linux!"
meta_keywords: "comando mv, Linux mv, mover arquivos Linux, renomear arquivos Linux, tutorial Linux, iniciante, guia Linux"
---

## Lesson Content

Usado para mover arquivos e também renomeá-los. Bastante semelhante ao comando `cp` em termos de sinalizadores e funcionalidade.

Você pode renomear arquivos assim:

```bash
mv oldfile newfile
```

Ou você pode realmente mover um arquivo para um diretório diferente:

```bash
mv file2 /home/pete/Documents
```

E mover mais de um arquivo:

```bash
mv file_1 file_2 /somedirectory
```

Você também pode renomear diretórios:

```bash
mv directory1 directory2
```

Assim como `cp`, se você `mv` um arquivo ou diretório, ele sobrescreverá qualquer coisa no mesmo diretório. Então você pode usar o sinalizador `-i` para ser avisado antes de sobrescrever qualquer coisa.

```bash
mv -i directory1 directory2
```

Digamos que você queira `mv` um arquivo para sobrescrever o anterior. Você também pode fazer um backup desse arquivo, e ele apenas renomeará a versão antiga com um `~`.

```bash
mv -b directory1 directory2
```

## Exercise

A prática leva à perfeição! A experiência prática é crucial para dominar comandos Linux como `mv`. Estes laboratórios o ajudarão a solidificar seu entendimento sobre como mover e renomear arquivos e diretórios em um ambiente real:

1. **[Comando Linux mv: Movendo e Renomeando Arquivos](https://labex.io/pt/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Pratique o uso do comando `mv` para mover e renomear arquivos e diretórios, incluindo a compreensão de suas várias opções e comportamentos.
2. **[Organizando Arquivos e Diretórios](https://labex.io/pt/labs/linux-organizing-files-and-directories-387877)** - Aplique seu conhecimento de `mv` (juntamente com `cp` e `rm`) em um desafio prático para organizar uma estrutura de projeto, mover arquivos e limpar diretórios.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de arquivos e diretórios usando o comando `mv`.

## Quiz Question

Como você renomeia um arquivo chamado `cat` para `dog`?

## Quiz Answer

mv cat dog
