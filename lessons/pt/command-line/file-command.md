---
index: 6
lang: "pt"
title: "file"
meta_title: "file - Linha de Comando"
meta_description: "Aprenda o comando file no Linux com exemplos para identificar arquivos de texto, imagens, scripts, arquivos compactados, binários e tipos MIME."
meta_keywords: "comando linux file, comando file, identificar tipo de arquivo linux, tipo mime linux, arquivo de texto, arquivo binário, arquivo compactado"
---

## Lesson Content

Na lição anterior, aprendemos sobre o `touch`. Vamos revisitar isso por um momento. Você percebeu que o nome do arquivo não seguia as convenções padrão de nomenclatura, como provavelmente já viu em outros sistemas operacionais como o Windows? Normalmente, você esperaria que um arquivo chamado `banana.jpeg` fosse um arquivo de imagem JPEG.

No Linux, os nomes dos arquivos não precisam representar o conteúdo do arquivo. Você pode criar um arquivo chamado `funny.gif` que na verdade não seja um GIF.

Para descobrir que tipo de arquivo é um arquivo, você pode usar o comando `file`. Ele mostrará uma descrição do conteúdo do arquivo.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### Por Que Extensões de Arquivo Não São Suficientes

As ferramentas do Linux geralmente não exigem uma extensão de arquivo para decidir o que é um arquivo. Um script shell pode ser chamado `backup`, um arquivo de texto pode ser chamado `README`, e uma imagem pode ter a extensão errada. O comando `file` inspeciona o conteúdo e os metadados do arquivo para fazer um palpite melhor.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### Verificando Vários Arquivos

Você pode verificar vários arquivos de uma vez:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Curingas também funcionam:

```bash
$ file *
```

### Mostrando Tipos MIME

A opção `-i` imprime informações no estilo MIME, o que é útil ao trabalhar com arquivos web ou scripts.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### Opções Comuns do file

- `-i`: Mostra informações do tipo MIME.
- `-b`: Modo breve, omite o nome do arquivo na saída.
- `-L`: Segue links simbólicos.
- `-z`: Tenta inspecionar arquivos compactados.

Por exemplo:

```bash
$ file -b notes.txt
ASCII text
```

### Perguntas Comuns

**O file depende apenas das extensões?** Não. Ele inspeciona principalmente o conteúdo do arquivo e assinaturas conhecidas.

**O file pode estar errado?** Sim. Ele faz um palpite educado, especialmente para arquivos incomuns ou danificados.

**Por que o file diz "data"?** O arquivo não corresponde a um tipo conhecido mais específico, ou pode ser dados binários sem uma assinatura reconhecível.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar seu entendimento sobre inspeção de conteúdo e propriedades de arquivos:

1. **[Linux ls Command: Content Listing](https://labex.io/pt/labs/linux-linux-ls-command-content-listing-219205)** - Aprenda o comando `ls` do Linux para listar e analisar eficientemente o conteúdo de arquivos e diretórios, que frequentemente precede ou segue o uso do comando `file` para entender o que há em seus diretórios.
2. **[Linux cat Command: File Concatenating](https://labex.io/pt/labs/linux-linux-cat-command-file-concatenating-210986)** - Pratique visualizar e manipular arquivos de texto, uma tarefa comum após identificar o tipo de um arquivo.
3. **[Linux more Command: File Scrolling](https://labex.io/pt/labs/linux-linux-more-command-file-scrolling-214299)** - Aprimore suas habilidades na linha de comando para navegar e explorar arquivos de texto grandes, construindo a partir da capacidade de identificar tipos de arquivos e depois inspecionar seu conteúdo.

Esses laboratórios ajudarão você a aplicar os conceitos de inspeção de arquivos e visualização de conteúdo em cenários reais e a ganhar confiança no gerenciamento de arquivos no Linux.

## Quiz Question

Qual comando você pode usar para descobrir o tipo de um arquivo?

## Quiz Answer

file
