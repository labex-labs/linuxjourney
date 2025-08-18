---
lang: "ja"
title: "tar と gzip"
meta_description: "Linux で tar と gzip を使用してファイルのアーカイブと圧縮を行う方法を学びます。ファイルの作成、抽出、圧縮のためのコマンドを理解します。この初心者向けガイドから始めましょう！"
meta_keywords: "tar, gzip, Linux アーカイブ，ファイル圧縮，tar コマンド，gzip コマンド，Linux チュートリアル，初心者 Linux"
---

## Lesson Content

パッケージのインストールと様々なマネージャーについて説明する前に、ファイルのアーカイブと圧縮について議論する必要があります。なぜなら、インターネットでソフトウェアを探す際に、これらに遭遇する可能性が非常に高いからです。

ファイルアーカイブが何であるかはすでにご存じかもしれません。おそらく、.rar や.zip といったファイルタイプに遭遇したことがあるでしょう。これらはファイルのアーカイブであり、中に多くのファイルが含まれていますが、アーカイブとして知られる非常にすっきりとした単一のファイルとして提供されます。

### Compressing files with gzip

gzip は Linux でファイルを圧縮するために使用されるプログラムで、拡張子は.gz です。

ファイルを圧縮するには：

```bash
gzip mycoolfile
```

ファイルを解凍するには：

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

残念ながら、gzip は複数のファイルを 1 つのアーカイブに追加することはできません。幸いなことに、tar プログラムがあります。tar を使用してアーカイブを作成すると、.tar 拡張子が付与されます。

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - 作成 (create)
- `v` - プログラムに詳細な情報を表示させ、何をしているかを確認できるようにする (verbose)
- `f` - tar ファイルのファイル名は、このオプションの後に指定する必要があります。tar ファイルを作成する場合は、名前を考案する必要があります (filename)

### Unpacking archives with tar

tar ファイルの内容を抽出するには、次を使用します。

```bash
tar xvf mytarfile.tar
```

- `x` - 抽出 (extract)
- `v` - プログラムに詳細な情報を表示させ、何をしているかを確認できるようにする (verbose)
- `f` - 抽出したいファイル (file)

### Compressing/uncompressing archives with tar and gzip

`mycompressedarchive.tar.gz`のように、圧縮された tar ファイルをよく見かけるでしょう。必要なのは、外側から作業することです。まず`gunzip`で圧縮を解除し、その後 tar ファイルを解凍できます。または、tar で**z**オプションを使用することもできます。これは、gzip または gunzip ユーティリティを使用するように指示するだけです。

圧縮された tar ファイルを作成する：

```bash
tar czf myfile.tar.gz
```

解凍して展開する：

```bash
tar xzf file.tar
```

これを覚えるのに役立つヒント：e**X**tract all **Z**ee **F**iles!

tar は非常に重要でありながら、なかなか覚えられないコマンドの一つです。関連する xkcd: <https://xkcd.com/1168/>

### Other Utilities

Linux での学習を通じて、bzip2、compress、zip、unzip などの他のアーカイブおよび圧縮タイプに遭遇するでしょう。これらは少し一般的ではありませんが、異なるユーティリティには異なるコマンドが必要であることを覚えておいてください。

## Exercise

tar のドキュメントに慣れ親しみ、man ページで利用可能な他のオプションを確認してください。

## Quiz Question

アーカイブを作成するために使用される tar フラグは何ですか？

## Quiz Answer

c
