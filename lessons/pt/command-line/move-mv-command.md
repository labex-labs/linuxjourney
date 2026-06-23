---
index: 11
lang: "pt"
title: "mv (Mover)"
meta_title: "mv (Mover) - Linha de Comando"
meta_description: "Aprenda o comando Linux mv com exemplos para mover arquivos, renomear arquivos e diretórios, mover múltiplos arquivos e evitar sobrescritas."
meta_keywords: "comando linux mv, comando mv, mover arquivos linux, renomear arquivo linux, renomear diretório linux, mv -i, mv -n, mv -t"
---

## Lesson Content

O comando `mv`, abreviação de "mover", é uma ferramenta fundamental em qualquer ambiente Linux. Ele serve a dois propósitos principais: renomear arquivos ou diretórios e movê-los para um local diferente.

A sintaxe básica é:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

Ao contrário do `cp`, que cria uma cópia, o `mv` altera onde o item original está localizado ou como ele é chamado.

### Renomeando Arquivos e Diretórios

Um dos usos mais comuns do `mv` é renomear. A sintaxe é simples: especifique o nome antigo e o novo nome.

Para renomear um arquivo:

```bash
$ mv oldfile newfile
```

Essa mesma lógica se aplica para renomear diretórios:

```bash
$ mv old_directory_name new_directory_name
```

### Movendo Arquivos e Diretórios

A outra função principal do comando `mv` é mover itens de um local para outro.

Para mover um único arquivo para um diretório diferente:

```bash
$ mv file2 /home/pete/Documents
```

Você também pode mover múltiplos arquivos de uma vez. Basta listar todos os arquivos de origem seguidos pelo diretório de destino:

```bash
$ mv file_1 file_2 somedirectory/
```

Em sistemas GNU/Linux, uma opção útil para isso é `-t`, que permite especificar o diretório de destino primeiro. Isso pode ser mais claro ao mover muitos arquivos.

```bash
$ mv -t somedirectory/ file_1 file_2
```

Ao contrário do comando `cp`, você não precisa de uma opção recursiva para mover um diretório. O `mv` lida com diretórios por padrão.

### Opções Importantes para o Comando mv

Por padrão, se você mover um arquivo para um destino onde já existe um arquivo com o mesmo nome, o `mv` irá sobrescrevê-lo sem aviso. Para evitar perda acidental de dados, você pode usar as seguintes opções:

- **-i (interativo)**: Esta é uma funcionalidade de segurança crucial. Ela solicitará confirmação antes de sobrescrever qualquer arquivo existente.

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b (backup)**: Se você pretende sobrescrever um arquivo, mas quer manter a versão antiga, essa opção cria um backup do arquivo de destino. O backup normalmente é renomeado com um sufixo til (`~`).

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v (verbose)**: Essa opção faz o comando `mv` imprimir o que está fazendo, mostrando cada arquivo sendo movido ou renomeado.

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

Outra opção útil é `-n`, que significa sem sobrescrever. Ela impede a sobrescrição de um arquivo de destino existente.

```bash
$ mv -n source_file destination_directory
```

### Exemplos Comuns de mv

Renomear um arquivo:

```bash
$ mv draft.txt final.txt
```

Mover um diretório:

```bash
$ mv project /home/pete/Documents/
```

Mover todos os arquivos de texto para uma pasta:

```bash
$ mv *.txt notes/
```

Visualize as correspondências de curingas com `ls` antes de mover muitos arquivos.

### Perguntas Comuns

**O mv copia arquivos?** Não. O `mv` move ou renomeia o item original.

**O mv pode sobrescrever arquivos?** Sim. Use `mv -i` para perguntar antes ou `mv -n` para evitar sobrescrever.

**Preciso de mv -r para diretórios?** Não. O `mv` move diretórios sem `-r`.

## Exercise

A prática leva à perfeição! A experiência prática é crucial para dominar comandos Linux como o `mv`. Estes laboratórios ajudarão você a consolidar seu entendimento sobre mover e renomear arquivos e diretórios em um ambiente real:

1. **[Comando Linux mv: Movendo e Renomeando Arquivos](https://labex.io/pt/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Pratique o uso do comando `mv` para mover e renomear arquivos e diretórios, incluindo o entendimento de suas várias opções e comportamentos.
2. **[Organizando Arquivos e Diretórios](https://labex.io/pt/labs/linux-organizing-files-and-directories-387877)** - Aplique seu conhecimento do `mv` (junto com `cp` e `rm`) em um desafio prático para organizar a estrutura de um projeto, mover arquivos e limpar diretórios.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e ganhar confiança no gerenciamento de arquivos e diretórios usando o comando `mv`.

## Quiz Question

Usando o comando `mv`, como você renomearia um arquivo chamado `cat` para `dog`? Por favor, forneça o comando completo. Nota: A resposta é sensível a maiúsculas e deve ser inserida em inglês minúsculo.

## Quiz Answer

mv cat dog
