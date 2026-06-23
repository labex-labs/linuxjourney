---
index: 6
lang: "ja"
title: "file コマンド"
meta_title: "file コマンド - コマンドライン"
meta_description: "Linuxのfileコマンドを使って、テキストファイル、画像、スクリプト、圧縮アーカイブ、バイナリ、MIMEタイプを識別する方法を例とともに学びましょう。"
meta_keywords: "linux file コマンド, file コマンド, ファイルタイプ識別 linux, mime タイプ linux, テキストファイル, バイナリファイル, アーカイブファイル"
---

## Lesson Content

前のレッスンでは `touch` について学びました。少し振り返ってみましょう。ファイル名が、Windowsなど他のオペレーティングシステムでよく見られるような標準的な命名規則に従っていなかったことに気づきましたか？通常、`banana.jpeg` というファイル名ならJPEG画像ファイルであることが期待されます。

Linuxでは、ファイル名がファイルの内容を表す必要はありません。実際にはGIFでないのに `funny.gif` という名前のファイルを作成することもできます。

ファイルがどのような種類のファイルかを調べるには、`file` コマンドを使います。ファイルの内容の説明を表示してくれます。

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### なぜファイル拡張子だけでは不十分なのか

Linuxのツールは通常、ファイルの種類を判断するのにファイル拡張子を必要としません。シェルスクリプトは `backup` と名付けられることもありますし、テキストファイルは `README` と呼ばれることもありますし、画像ファイルが間違った拡張子を持つこともあります。`file` コマンドはファイルの内容やメタデータを調べて、より正確な推測を行います。

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### 複数ファイルの確認

複数のファイルを一度に調べることもできます：

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

ワイルドカードも使えます：

```bash
$ file *
```

### MIMEタイプの表示

`-i` オプションはMIMEスタイルの情報を表示します。これはウェブファイルやスクリプトを扱う際に便利です。

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### よく使う file のオプション

- `-i`: MIMEタイプ情報を表示する。
- `-b`: 簡潔モード。出力にファイル名を含めない。
- `-L`: シンボリックリンクをたどる。
- `-z`: 圧縮ファイルの中身を調べようとする。

例えば：

```bash
$ file -b notes.txt
ASCII text
```

### よくある質問

**file は拡張子だけを頼りにしていますか？** いいえ。主にファイルの内容や既知のシグネチャを調べています。

**file が間違うことはありますか？** はい。特に珍しいファイルや破損したファイルの場合は推測に過ぎません。

**file が「data」と表示するのはなぜですか？** ファイルがより具体的な既知のタイプに一致しないか、認識可能なシグネチャを持たないバイナリデータである可能性があります。

## Exercise

練習が上達の鍵です！ファイルの内容や属性を調べる理解を深めるための実践的なラボを紹介します：

1. **[Linux ls コマンド：内容一覧表示](https://labex.io/ja/labs/linux-linux-ls-command-content-listing-219205)** - Linuxの `ls` コマンドを学び、ファイルやディレクトリの内容を効率的に一覧・分析する方法を習得します。これは `file` コマンドで内容を理解する前後によく使われます。
2. **[Linux cat コマンド：ファイル連結](https://labex.io/ja/labs/linux-linux-cat-command-file-concatenating-210986)** - ファイルの種類を特定した後によく行う、テキストファイルの閲覧や操作を練習します。
3. **[Linux more コマンド：ファイルスクロール](https://labex.io/ja/labs/linux-linux-more-command-file-scrolling-214299)** - 大きなテキストファイルをコマンドラインでナビゲート・探索するスキルを向上させ、ファイルタイプを特定して内容を調べる能力を強化します。

これらのラボは、実際のシナリオでファイルの検査や内容の閲覧の概念を応用し、Linuxでのファイル管理に自信を持つ助けとなります。

## Quiz Question

ファイルの種類を調べるために使うコマンドは何ですか？

## Quiz Answer

file
