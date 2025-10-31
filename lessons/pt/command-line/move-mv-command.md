---
index: 11
lang: "pt"
title: "mv (Mover)"
meta_title: "mv (Mover) - Linha de Comando"
meta_description: "Um guia completo para o comando mv no Linux. Aprenda a usar o comando bash mv para mover e renomear arquivos e diretórios, utilize opções como linux mv -t e evite sobrescritas acidentais."
meta_keywords: "comando mv, comando mv no linux, linux mv, bash mv, mv -r linux, linux mv -t, mover arquivos, renomear arquivos, linha de comando linux"
---

## Lesson Content

O comando `mv`, abreviação de "move" (mover), é uma utilidade fundamental em qualquer ambiente Linux. Ele serve a dois propósitos principais: renomear arquivos ou diretórios e movê-los para um local diferente. Sua funcionalidade é semelhante em muitos aspectos ao comando `cp`.

### Renomeando Arquivos e Diretórios

Um dos usos mais comuns do `mv command in linux` é para renomear. A sintaxe é direta: você especifica o nome antigo e o novo nome.

Para renomear um arquivo:

```bash
mv oldfile newfile
```

Essa mesma lógica se aplica ao renomear diretórios:

```bash
mv old_directory_name new_directory_name
```

### Movendo Arquivos e Diretórios

A outra função principal do comando `mv` é mover itens de um local para outro.

Para mover um único arquivo para um diretório diferente:

```bash
mv file2 /home/pete/Documents
```

Você também pode mover vários arquivos de uma vez. Basta listar todos os arquivos de origem seguidos pelo diretório de destino:

```bash
mv file_1 file_2 /somedirectory
```

Uma opção útil para isso é `linux mv -t`, que permite especificar o diretório de destino primeiro. Isso pode ser mais claro ao mover muitos arquivos.

```bash
mv -t /somedirectory file_1 file_2
```

Ao contrário do comando `cp`, você não precisa da flag `-r` para mover um diretório. O comando `bash mv` lida com diretórios por padrão. Embora alguns usuários procurem por `mv -r linux`, essa opção não é necessária para mover diretórios com `mv`.

### Opções Importantes para o Comando mv

Por padrão, se você mover um arquivo para um destino onde um arquivo com o mesmo nome já existe, `mv` o sobrescreverá sem aviso. Para evitar perda acidental de dados, você pode usar as seguintes opções:

- **-i (interactive/interativo)**: Este é um recurso de segurança crucial. Ele solicitará confirmação antes de sobrescrever qualquer arquivo existente.

  ```bash
  mv -i source_file destination_directory
  ```

- **-b (backup)**: Se você pretende sobrescrever um arquivo, mas deseja manter a versão antiga, esta opção cria um backup do arquivo de destino. O backup geralmente é renomeado com um sufixo til (`~`).

  ```bash
  mv -b file1 directory_with_file1
  ```

- **-v (verbose/detalhado)**: Esta opção faz com que o comando `mv` imprima o que está fazendo, mostrando cada arquivo sendo movido ou renomeado.

  ```bash
  mv -v file1 file2 /somedirectory
  ```

Dominar o `mv command` é essencial para o gerenciamento eficiente de arquivos na linha de comando.

## Exercise

Prática leva à perfeição! A experiência prática é crucial para dominar comandos Linux como `mv`. Estes laboratórios ajudarão você a solidificar sua compreensão de como mover e renomear arquivos e diretórios em um ambiente real:

1.  **[Comando mv do Linux: Movimentação e Renomeação de Arquivos](https://labex.io/pt/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Pratique o uso do comando `mv` para mover e renomear arquivos e diretórios, incluindo a compreensão de suas várias opções e comportamentos.
2.  **[Organizando Arquivos e Diretórios](https://labex.io/pt/labs/linux-organizing-files-and-directories-387877)** - Aplique seu conhecimento de `mv` (junto com `cp` e `rm`) em um desafio prático para organizar uma estrutura de projeto, mover arquivos e limpar diretórios.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento de arquivos e diretórios usando o comando `mv`.

## Quiz Question

Usando o comando `mv`, como você renomearia um arquivo chamado `cat` para `dog`? Por favor, forneça o comando completo. Nota: A resposta diferencia maiúsculas de minúsculas e deve ser inserida em inglês minúsculo.

## Quiz Answer

mv cat dog
