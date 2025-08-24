---
index: 8
lang: "ja"
title: "less"
meta_title: "less - コマンドライン"
meta_description: "Linux の'less'コマンドを使って、テキストファイルを効率的に表示・ナビゲートする方法を学びましょう。この初心者向けガイドで、ページング、検索、終了をマスターします。"
meta_keywords: "less command, Linux less, view text files, navigate files, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

シンプルな出力よりも大きなテキストファイルを表示する場合、`less`はより便利です。（実際には似たようなことをする`more`というコマンドがありますが、これは皮肉なことです。）テキストはページ形式で表示されるため、テキストファイルをページごとに移動できます。

`less`でファイルの内容を見てみましょう。`less`コマンドに入ると、ファイル内を移動するために他のキーボードコマンドを使用できます。

```bash
less /home/pete/Documents/text1
```

`less`内を移動するには、以下のコマンドを使用します。

- `q` - `less`を終了してシェルに戻るために使用します。
- `Page up`, `Page down`, `Up` and `Down` - 矢印キーとページキーを使用して移動します。
- `g` - テキストファイルの先頭に移動します。
- `G` - テキストファイルの末尾に移動します。
- `/search` - テキストドキュメント内で特定のテキストを検索できます。検索したい単語の前に`/`を付けます。
- `h` - `less`を使用中に`less`の使い方について少し助けが必要な場合は、ヘルプを使用します。

## Exercise

ファイルに対して`less`を実行し、ファイル内をページアップしたり移動したりしてください。特定の単語を検索してみてください。ファイルの先頭または末尾に素早く移動してください。

`less`コマンドの実践的な演習には、このインタラクティブなラボを試してください。

- [Linux less Command: File Paging](https://labex.io/ja/labs/linux-linux-less-command-file-paging-214301)

## Quiz Question

`less`コマンドを終了するにはどうすればよいですか？

## Quiz Answer

q
