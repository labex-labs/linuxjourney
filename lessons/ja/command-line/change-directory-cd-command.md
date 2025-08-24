---
index: 3
lang: "ja"
title: "cd (ディレクトリ変更)"
meta_title: "cd (ディレクトリ変更) - コマンドライン"
meta_description: "Linux で「cd」コマンドを使ってディレクトリを移動する方法を学びましょう。絶対パス、相対パス、便利なショートカットを理解しましょう。Linux の旅を始めましょう！"
meta_keywords: "cd command, change directory, Linux paths, absolute path, relative path, Linux tutorial, beginner Linux, Linux navigation"
---

## Lesson Content

自分がどこにいるか分かったところで、ファイルシステム内を少し移動してみましょう。パスを使って移動する必要があることを覚えておいてください。パスを指定する方法には、絶対パスと相対パスの 2 種類があります。

- 絶対パス：これはルートディレクトリからのパスです。ルートは最高責任者です。ルートディレクトリは通常スラッシュ (`/`) で示されます。パスが `/` で始まる場合、それはルートディレクトリから開始していることを意味します。例：`/home/pete/Desktop`。

- 相対パス：これはファイルシステム内で現在いる場所からのパスです。もし私が `/home/pete/Documents` にいて、`Documents` 内の `taxes` というディレクトリに移動したい場合、`/home/pete/Documents/taxes` のようにルートからの完全なパスを指定する必要はありません。代わりに `taxes/` と指定するだけで移動できます。

パスの仕組みが分かったところで、目的のディレクトリに移動するのに役立つものが必要です。幸いなことに、それを行うために `cd` または「change directory」があります。

```bash
cd /home/pete/Pictures
```

これで、ディレクトリの場所を `/home/pete/Pictures` に変更しました。

このディレクトリから、`Hawaii` という名前のフォルダがあります。そのフォルダには次のように移動できます。

```bash
cd Hawaii
```

フォルダ名だけを使ったことに気づきましたか？それは、私がすでに `/home/pete/Pictures` にいたからです。

常に絶対パスと相対パスで移動するのはかなり疲れることがあります。幸いなことに、役立ついくつかのショートカットがあります。

- `.` (現在のディレクトリ): これは現在いるディレクトリです。
- `..` (前のディレクトリ): 現在のディレクトリの 1 つ上のディレクトリに移動します。
- `~` (ホームディレクトリ): このディレクトリは、`/home/pete` のような「ホームディレクトリ」にデフォルトで設定されます。
- `-` (前のディレクトリ): これは、直前にいたディレクトリに移動します。

```bash
cd .
cd ..
cd ~
cd -
```

試してみてください！

## Exercise

1. `cd` コマンドを何もフラグを付けずに実行してください。どこに移動しますか？

`cd` コマンドの実践的な練習には、このインタラクティブなラボを試してください。

- [Linux cd Command: Directory Changing](https://labex.io/ja/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

`/home/pete/Pictures` にいて、`/home/pete` に移動したい場合、どのようなショートカットを使うのが良いですか？

## Quiz Answer

cd ..
