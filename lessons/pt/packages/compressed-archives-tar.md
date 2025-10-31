---
index: 3
lang: "pt"
title: "tar e gzip"
meta_title: "tar e gzip - Pacotes"
meta_description: "Um guia completo sobre o uso de tar e gzip no Linux. Aprenda sobre compressão tar, como criar e extrair arquivos, e a diferença entre gzip e tar. Domine comandos para compactar arquivos tar gz e gerencie seus pacotes de software de forma eficaz."
meta_keywords: "tar e gzip, compressão tar, gzip tar, compactar tar gz, gzip e tar, arquivamento Linux, compressão de arquivos, comando tar, comando gzip, tutorial Linux"
---

## Lesson Content

Antes de mergulhar nos gerenciadores de pacotes, é essencial entender o arquivamento e a compressão de arquivos. Ao baixar software online, você frequentemente o encontrará empacotado em formatos arquivados e compactados. Esta lição foca em duas utilidades fundamentais para esse propósito: `tar` e `gzip`.

### Entendendo Arquivamento vs. Compressão

É importante distinguir entre arquivamento e compressão. **Arquivamento** é o processo de combinar múltiplos arquivos e diretórios em um único arquivo, conhecido como um arquivo (archive). Isso facilita o gerenciamento e a transferência de um grupo de arquivos. **Compressão**, por outro lado, é o processo de reduzir o tamanho de um arquivo para economizar espaço em disco e acelerar as transferências. A utilidade `tar` é usada para arquivamento, enquanto `gzip` é usada para compressão. Frequentemente, você verá `gzip e tar` usados em conjunto.

### Compactando Arquivos Únicos com gzip

O programa `gzip` é usado para compactar arquivos individuais no Linux. Quando você compacta um arquivo com `gzip`, ele é substituído por um arquivo com a extensão `.gz`.

Para compactar um arquivo:

```bash
gzip meuarquivolegal
```

Isso criará `meuarquivolegal.gz` e removerá o original. Para descompactar o arquivo, você pode usar `gunzip`:

```bash
gunzip meuarquivolegal.gz
```

### Criando Arquivos com tar

Embora o `gzip` seja ótimo para compressão, ele não consegue agrupar vários arquivos em um único arquivo. Para isso, usamos a utilidade `tar` (Tape Archive). Um arquivo criado com `tar` é frequentemente chamado de "tarball" e tem a extensão `.tar`.

Para criar um novo arquivo contendo múltiplos arquivos:

```bash
tar cvf meuarquivo.tar arquivo1 arquivo2 diretorio1
```

Vamos analisar as opções:

- `c`: **c**riar um novo arquivo.
- `v`: modo **v**erboso, que lista os arquivos à medida que são processados.
- `f`: **f**ile (arquivo), que especifica que o próximo argumento é o nome do arquivo de arquivamento.

### O Poder de tar e gzip Combinados

A verdadeira força vem do uso de `tar e gzip` em conjunto. Você pode primeiro criar um arquivo `.tar` e depois compactá-lo com `gzip`, resultando em um arquivo `.tar.gz`. No entanto, `tar` fornece uma maneira conveniente de lidar com a **compressão tar** em uma única etapa usando a opção `z`. Este processo é às vezes referido como a criação de um arquivo **gzip tar**.

Para criar um arquivo compactado, que é uma forma comum de **compactar arquivos tar gz**:

```bash
tar czvf meuarquivo.tar.gz arquivo1 arquivo2 diretorio1
```

Aqui, a opção `z` diz ao `tar` para usar o `gzip` para compressão.

### Extraindo Arquivos tar e gzip

Para extrair arquivos de um arquivo, você usa a opção `x`.

Para extrair um arquivo `.tar` simples:

```bash
tar xvf meuarquivo.tar
```

Para descompactar e extrair um arquivo `.tar.gz` em um único comando, basta adicionar a opção `z` novamente:

```bash
tar xzvf meuarquivo.tar.gz
```

Vamos revisar as opções de extração:

- `x`: **e**xtrair arquivos de um arquivo.
- `z`: Descompactar o arquivo usando **g**z**ip**.
- `v`: modo **v**erboso, listando arquivos à medida que são extraídos.
- `f`: **f**ile (arquivo), especificando o arquivo de arquivamento a ser extraído.

A mnemônica útil para isso é: e**X**trair **Z**ee **V**ery **F**ast! (Extrair o Muito Rápido!)

`tar` é um comando tão essencial, mas frequentemente esquecido. xkcd relevante: `https://xkcd.com/1168`

### Outras Utilidades

Embora `tar` e `gzip` sejam extremamente comuns, você encontrará outros formatos de arquivamento e compressão em sua jornada no Linux. Estes incluem `bzip2` (que cria arquivos `.bz2` e usa a flag `j` no `tar`), `xz` (criando arquivos `.xz` com a flag `J`), e as utilidades familiares `zip`/`unzip`. Cada um tem seu próprio conjunto de comandos e taxas de compressão, mas os conceitos subjacentes permanecem os mesmos.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de arquivamento e compressão de arquivos:

1. **[Empacotamento e Compressão de Arquivos](https://labex.io/pt/labs/linux-file-packaging-and-compression-385413)** - Aprenda técnicas essenciais de compressão e empacotamento de arquivos no Linux usando ferramentas como tar, gzip e zip.
2. **[Criar e Restaurar um Backup com tar no Linux](https://labex.io/pt/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Ganhe experiência prática criando e restaurando backups do sistema de arquivos usando o comando tar.
3. **[Backup do Log do Sistema](https://labex.io/pt/labs/linux-backup-system-log-17989)** - Aprenda a habilidade essencial de fazer backup de arquivos de log do sistema usando o comando tar e formatação de data.

Estes laboratórios ajudarão você a aplicar os conceitos de arquivamento e compressão em cenários reais e a construir confiança no gerenciamento de arquivos no Linux.

## Quiz Question

Qual flag do tar é usada para criar arquivos? Por favor, responda com uma única letra minúscula em inglês.

## Quiz Answer

c
