---
title: "tar и gzip"
description: "Научитесь использовать tar и gzip для архивирования и сжатия файлов в Linux. Изучите команды для создания, извлечения и сжатия файлов. Начните с этого руководства для начинающих!"
keywords: "tar, gzip, архивирование Linux, сжатие файлов, команда tar, команда gzip, учебник Linux, Linux для начинающих"
---

## Lesson Content

Прежде чем мы перейдем к установке пакетов и различным менеджерам, нам необходимо обсудить архивирование и сжатие файлов, потому что вы, скорее всего, столкнетесь с ними при поиске программного обеспечения в интернете.

Вы, вероятно, уже знаете, что такое файловый архив; вы, скорее всего, сталкивались с такими типами файлов, как .rar и .zip. Это архивы файлов; они содержат множество файлов внутри себя, но они представлены в виде одного очень аккуратного файла, известного как архив.

### Compressing files with gzip

gzip — это программа, используемая для сжатия файлов в Linux; они имеют расширение .gz.

Чтобы сжать файл:

```bash
gzip mycoolfile
```

Чтобы разархивировать файл:

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

К сожалению, gzip не может добавить несколько файлов в один архив. К счастью, у нас есть программа tar, которая это делает. Когда вы создаете архив с помощью tar, он будет иметь расширение .tar.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - create
- `v` - tell the program to be verbose and let us see what it's doing
- `f` - the filename of the tar file has to come after this option; if you are creating a tar file, you'll have to come up with a name

### Unpacking archives with tar

Чтобы извлечь содержимое tar файла, используйте:

```bash
tar xvf mytarfile.tar
```

- `x` - extract
- `v` - tell the program to be verbose and let us see what it's doing
- `f` - the file you want to extract

### Compressing/uncompressing archives with tar and gzip

Часто вы будете видеть tar файл, который был сжат, например: `mycompressedarchive.tar.gz`. Все, что вам нужно сделать, это работать снаружи внутрь, поэтому сначала удалите сжатие с помощью `gunzip`, а затем вы сможете распаковать tar файл. Или вы можете использовать опцию **z** с tar, которая просто указывает ему использовать утилиту gzip или gunzip.

Создать сжатый tar файл:

```bash
tar czf myfile.tar.gz
```

Разархивировать и распаковать:

```bash
tar xzf file.tar
```

Если вам нужна помощь в запоминании этого: e**X**tract all **Z**ee **F**iles!

tar — одна из тех команд, которая настолько важна, но которую вы никогда по-настоящему не запоминаете. Соответствующий xkcd: <https://xkcd.com/1168/>

### Other Utilities

На протяжении вашего пути с Linux вы столкнетесь с другими типами архивов и сжатия, такими как: bzip2, compress, zip, unzip и т.д. Они встречаются немного реже, но просто имейте в виду, что для разных утилит потребуются разные команды.

## Exercise

Ознакомьтесь с документацией tar и изучите другие доступные опции в manpage.

## Quiz Question

Какой флаг tar используется для создания архивов?

## Quiz Answer

c
