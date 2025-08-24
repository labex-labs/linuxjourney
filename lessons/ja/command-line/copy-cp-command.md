---
index: 10
lang: "ja"
title: "cp (コピー)"
meta_title: "cp (コピー) - コマンドライン"
meta_description: "Linux の cp コマンドを使ってファイルやディレクトリをコピーする方法を学びましょう。-r やワイルドカードなどのオプションを理解しましょう。今日から Linux の旅を始めましょう！"
meta_keywords: "cp command, copy files Linux, Linux tutorial, beginner Linux, cp -r, Linux wildcards, Linux guide"
---

## Lesson Content

これらのファイルのコピーを始めましょう。他のオペレーティングシステムでファイルをコピー＆ペーストするのと同様に、シェルはそれをさらに簡単な方法で提供します。

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` はコピーしたいファイルで、`/home/pete/Documents/cooldocs` はファイルをコピーする場所です。

複数のファイルやディレクトリをコピーしたり、ワイルドカードを使用したりできます。ワイルドカードは、パターンベースの選択に置き換えることができる文字で、検索の柔軟性を高めます。すべてのコマンドでワイルドカードを使用して、柔軟性を高めることができます。

- `*` ワイルドカードのワイルドカード。すべての単一文字または任意の文字列を表すために使用されます。
- `?` 1 文字を表すために使用されます
- `[]` 角括弧内の任意の文字を表すために使用されます

```bash
cp *.jpg /home/pete/Pictures
```

これにより、現在のディレクトリにある `.jpg` 拡張子を持つすべてのファイルが `Pictures` ディレクトリにコピーされます。

便利なコマンドは `-r` フラグを使用することです。これにより、ディレクトリ内のファイルとディレクトリが再帰的にコピーされます。

いくつかのファイルを含むディレクトリを `Documents` ディレクトリに `cp` してみてください。うまくいきませんでしたね？それは、`-r` コマンドで内部のファイルとディレクトリもコピーする必要があるからです。

```bash
cp -r Pumpkin/ /home/pete/Documents
```

注意すべき点として、同じファイル名を持つディレクトリにファイルをコピーすると、そのファイルはコピー元の内容で上書きされます。これは、誤って上書きされたくないファイルがある場合には良くありません。ファイルを上書きする前にプロンプトを表示するには、`-i` フラグ（インタラクティブ）を使用できます。

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

いくつかのファイルをコピーしてください。重要なものを上書きしないように注意してください。

`cp` コマンドの実践的な練習には、このインタラクティブなラボを試してください。

- [Linux cp Command: File Copying](https://labex.io/ja/labs/linux-linux-cp-command-file-copying-209744)

## Quiz Question

ディレクトリをコピーするために指定する必要があるフラグは何ですか？

## Quiz Answer

-r
