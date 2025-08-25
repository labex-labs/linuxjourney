---
index: 3
lang: "ja"
title: "cd (Change Directory)"
meta_title: "cd (Change Directory) - コマンドライン"
meta_description: "Linux でディレクトリを移動するために 'cd' コマンドを使用する方法を学びます。絶対パス、相対パス、および便利なショートカットを理解します。Linux の学習を始めましょう！"
meta_keywords: "cd コマンド，ディレクトリ変更，Linux パス，絶対パス，相対パス，Linux チュートリアル，初心者 Linux, Linux ナビゲーション"
---

## Lesson Content

自分がどこにいるか分かったところで、ファイルシステム内を少し移動してみましょう。パスを使って移動する必要があることを覚えておいてください。パスを指定するには、絶対パスと相対パスの 2 つの異なる方法があります。

- 絶対パス：これはルートディレクトリからのパスです。ルートは最高責任者です。ルートディレクトリは通常スラッシュ (`/`) で示されます。パスが `/` で始まる場合、それはルートディレクトリから開始していることを意味します。例えば、`/home/pete/Desktop`。

- 相対パス：これはファイルシステム内で現在いる場所からのパスです。もし私が `/home/pete/Documents` にいて、`Documents` 内の `taxes` というディレクトリに行きたい場合、`/home/pete/Documents/taxes` のようにルートからの完全なパスを指定する必要はありません。代わりに `taxes/` と指定するだけで済みます。

パスの仕組みが分かったところで、目的のディレクトリに移動するための何かが必要です。幸いなことに、それを行うための `cd` または「change directory」があります。

```bash
cd /home/pete/Pictures
```

これで、ディレクトリの場所が `/home/pete/Pictures` に変更されました。

このディレクトリの中に `Hawaii` というフォルダがあります。そのフォルダには次のように移動できます。

```bash
cd Hawaii
```

フォルダ名だけを使ったことに気づきましたか？それは、私がすでに `/home/pete/Pictures` にいたからです。

絶対パスと相対パスを使って常に移動するのはかなり疲れることがあります。幸いなことに、役立つショートカットがいくつかあります。

- `.` (現在のディレクトリ): これは現在いるディレクトリです。
- `..` (前のディレクトリ): 現在のディレクトリの 1 つ上のディレクトリに移動します。
- `~` (ホームディレクトリ): このディレクトリは、`/home/pete` のような「ホームディレクトリ」にデフォルトで設定されます。
- `-` (直前のディレクトリ): これは、直前にいたディレクトリに移動します。

```bash
cd .
cd ..
cd ~
cd -
```

試してみてください！

## Exercise

練習は完璧をもたらします！Linux ディレクトリナビゲーションの理解を深めるための実践的なラボをいくつか紹介します。

1.  **[Linux cd Command: Directory Changing](https://labex.io/ja/labs/linux-linux-cd-command-directory-changing-209733)** - Linux の `cd` コマンドを学び、ファイルシステムを効率的にナビゲートする方法、ディレクトリ変更の様々なテクニック、パスの理解、ファイル構造の探索について学びます。
2.  **[Linux Directory Navigation](https://labex.io/ja/labs/linux-directory-navigation-387844)** - 基本的な Linux コマンドラインスキルを試して、必須コマンドを使ってディレクトリをナビゲートします。
3.  **[Setting Up a New Project Structure](https://labex.io/ja/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir` や `cd` などの必須コマンドを使って、特定のプロジェクト構造を作成し、それをナビゲートすることで、Linux ディレクトリ管理スキルを練習します。

これらのラボは、実際のシナリオで概念を適用し、Linux ファイルシステムのナビゲートに自信をつけるのに役立ちます。

## Quiz Question

`/home/pete/Pictures` にいて、`/home/pete` に行きたい場合、どのようなショートカットを使うのが良いですか？

## Quiz Answer

cd ..
