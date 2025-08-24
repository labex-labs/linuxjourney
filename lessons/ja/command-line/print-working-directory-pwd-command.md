---
index: 2
lang: "ja"
title: "pwd (Print Working Directory)"
meta_title: "pwd (Print Working Directory) - コマンドライン"
meta_description: "Linux で現在の作業ディレクトリを表示するために'pwd'コマンドを使用する方法を学びます。初心者向けに Linux ファイルシステムパスとナビゲーションを理解します。"
meta_keywords: "pwd コマンド，Linux ディレクトリ，現在のディレクトリ，Linux パス，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

## Lesson Content

Linux では、すべてがファイルです。Linux を深く学ぶにつれて、このことを理解するでしょうが、今はそのことを心に留めておいてください。すべてのファイルは階層的なディレクトリツリーに整理されています。ファイルシステム内の最初のディレクトリは、適切にルートディレクトリと名付けられています。ルートディレクトリには多くのフォルダとファイルがあり、それらはさらに多くのフォルダとファイルを格納できます。ディレクトリツリーがどのように見えるかの例を次に示します。

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

これらのファイルとディレクトリの場所はパスと呼ばれます。もし`home`というフォルダがあり、その中に`pete`というフォルダがあり、さらにその中に`Movies`というフォルダがあった場合、そのパスは`/home/pete/Movies`のようになります。とてもシンプルでしょう？

ファイルシステムのナビゲーションは、現実世界と同じように、自分がどこにいて、どこへ行くのかを知っていれば役立ちます。自分がどこにいるかを確認するには、`pwd`コマンドを使用できます。このコマンドは「print working directory」を意味し、現在いるディレクトリを表示するだけです。パスはルートディレクトリから始まることに注意してください。

```bash
pwd
```

あなたはどこにいますか？私はどこにいますか？試してみてください。

## Exercise

`pwd`コマンドを実際に練習するには、このインタラクティブなラボを試してください。

- [Linux pwd Command: Directory Displaying](https://labex.io/ja/labs/linux-linux-pwd-command-directory-displaying-209734)

## Quiz Question

現在いるディレクトリを見つけるにはどうすればよいですか？

## Quiz Answer

pwd
