---
index: 8
lang: "ja"
title: "less"
meta_title: "less - コマンドライン"
meta_description: "Linuxの「less」コマンドを使用して、効率的なテキストファイルの表示とナビゲーションを行う方法を学びます。この初心者向けのガイドで、ページング、検索、終了をマスターしましょう。"
meta_keywords: "lessコマンド, Linux less, テキストファイル表示, ファイルナビゲート, Linuxチュートリアル, 初心者Linux, Linuxガイド"
---

## Lesson Content

シンプルな出力よりも大きなテキストファイルを表示する場合、`less`はより優れています。（実際には似たようなことをする`more`というコマンドもあるので、これは皮肉です。）テキストはページ単位で表示されるため、テキストファイルをページごとに移動できます。

`less`でファイルのコンテンツを見てみましょう。`less`コマンドに入ると、ファイル内を移動するために他のキーボードコマンドを使用できます。

```bash
less /home/pete/Documents/text1
```

`less`内を移動するには、以下のコマンドを使用します。

- `q` - `less`を終了してシェルに戻るために使用します。
- `Page up`、`Page down`、`Up`、`Down` - 矢印キーとページキーを使用して移動します。
- `g` - テキストファイルの先頭に移動します。
- `G` - テキストファイルの末尾に移動します。
- `/search` - テキストドキュメント内で特定のテキストを検索できます。検索したい単語の前に`/`を付けます。
- `h` - `less`を使用中に`less`の使い方について少し助けが必要な場合は、ヘルプを使用します。

## Exercise

練習は完璧をもたらします！Linuxでテキストファイルを表示およびナビゲートする理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux lessコマンド: ファイルのページング](https://labex.io/ja/labs/linux-linux-less-command-file-paging-214301)** - 検索、行番号、パターンマッチングなど、効率的なテキストファイルの表示とナビゲーションのためのLinuxの「less」コマンドを学びます。
2. **[Linux moreコマンド: ファイルのスクロール](https://labex.io/ja/labs/linux-linux-more-command-file-scrolling-214299)** - 基本的な使用法、特定の行からの開始、表示のカスタマイズなど、効率的なテキストファイルの表示のためのLinuxの「more」コマンドを学びます。
3. **[Linuxでのログファイルと設定ファイルの表示](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat`、`more`、`less`などのコマンドを使用して、システムログや設定ファイルを含むテキストファイルを効率的に表示およびナビゲートするためのLinuxコマンドラインの必須スキルを学びます。

これらの演習は、実際のシナリオで概念を適用し、テキストファイルの操作とナビゲーションに自信を持つのに役立ちます。

## Quiz Question

`less`コマンドを終了するにはどうすればよいですか？

## Quiz Answer

q