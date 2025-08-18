---
index: 3
lang: "pt"
title: "tar e gzip"
meta_title: "tar e gzip - Pacotes"
meta_description: "Aprenda a usar tar e gzip para arquivamento e compressão de arquivos no Linux. Entenda os comandos para criar, extrair e comprimir arquivos. Comece com este guia para iniciantes!"
meta_keywords: "tar, gzip, arquivamento Linux, compressão de arquivos, comando tar, comando gzip, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Antes de entrarmos na instalação de pacotes e nos diferentes gerenciadores, precisamos discutir o arquivamento e a compressão de arquivos, porque você provavelmente os encontrará ao procurar software na internet.

Você provavelmente já sabe o que é um arquivo compactado; você provavelmente já encontrou tipos de arquivo como .rar e .zip. Estes são arquivos de arquivos; eles contêm muitos arquivos dentro deles, mas vêm neste único arquivo muito organizado conhecido como arquivo compactado.

### Comprimindo arquivos com gzip

gzip é um programa usado para comprimir arquivos no Linux; eles terminam com a extensão .gz.

Para comprimir um arquivo:

```bash
gzip mycoolfile
```

Para descomprimir o arquivo:

```bash
gunzip mycoolfile.gz
```

### Criando arquivos com tar

Infelizmente, o gzip não consegue adicionar vários arquivos em um único arquivo para nós. Felizmente, temos o programa tar que faz isso. Quando você cria um arquivo usando tar, ele terá uma extensão .tar.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - create (criar)
- `v` - tell the program to be verbose and let us see what it's doing (dizer ao programa para ser detalhado e nos deixar ver o que ele está fazendo)
- `f` - the filename of the tar file has to come after this option; if you are creating a tar file, you'll have to come up with a name (o nome do arquivo tar deve vir depois desta opção; se você estiver criando um arquivo tar, terá que inventar um nome)

### Descompactando arquivos com tar

Para extrair o conteúdo de um arquivo tar, use:

```bash
tar xvf mytarfile.tar
```

- `x` - extract (extrair)
- `v` - tell the program to be verbose and let us see what it's doing (dizer ao programa para ser detalhado e nos deixar ver o que ele está fazendo)
- `f` - the file you want to extract (o arquivo que você deseja extrair)

### Comprimindo/descomprimindo arquivos com tar e gzip

Muitas vezes você verá um arquivo tar que foi comprimido, como: `mycompressedarchive.tar.gz`. Tudo o que você precisa fazer é trabalhar de fora para dentro, então primeiro remova a compressão com `gunzip` e então você pode descompactar o arquivo tar. Ou você pode, alternativamente, usar a opção **z** com tar, que simplesmente o instrui a usar o utilitário gzip ou gunzip.

Crie um arquivo tar comprimido:

```bash
tar czf myfile.tar.gz
```

Descomprimir e descompactar:

```bash
tar xzf file.tar
```

Se precisar de ajuda para lembrar: e**X**traia todos os ar**Z**uivos!

tar é um daqueles comandos que é tão importante e, no entanto, você nunca realmente se lembra dele. xkcd relevante: `https://xkcd.com/1168`

### Outros Utilitários

Ao longo de sua jornada com Linux, você encontrará outros tipos de arquivo e compressão, como: bzip2, compress, zip, unzip, etc. Eles são um pouco menos comuns, mas lembre-se de que diferentes utilitários exigirão diferentes comandos.

## Exercise

Familiarize-se com a documentação do tar e veja as outras opções disponíveis na manpage.

## Quiz Question

Qual flag do tar é usada para criar arquivos?

## Quiz Answer

c
