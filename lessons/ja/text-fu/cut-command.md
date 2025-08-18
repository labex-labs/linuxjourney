---
lang: "ja"
title: "cut"
meta_title: "cut - テキスト操作"
meta_description: "Linux の`cut`コマンドを使ってファイルからテキストを抽出する方法を学びましょう。この初心者向けのチュートリアルでは、文字とフィールドの切り取りについて説明します。Linux のテキスト処理スキルを向上させましょう！"
meta_keywords: "cut コマンド，Linux テキスト処理，テキスト抽出，Linux チュートリアル，初心者向け Linux, cut の例，Linux ガイド"
---

## Lesson Content

テキストを処理するために使用できるいくつかの便利なコマンドを学習します。始める前に、作業するファイルを作成しましょう。次のコマンドをコピーして貼り付けます。その後、「lazy」と「dog」の間に TAB を追加します（Ctrl-v + TAB を押したままにします）。

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

最初に学習するコマンドは `cut` コマンドです。これはファイルからテキストの一部を抽出します。

文字のリストで内容を抽出するには：

```bash
cut -c 5 sample.txt
```

これは、ファイルの各行の 5 番目の文字を出力します。この場合、「q」です。スペースも文字としてカウントされることに注意してください。

フィールドで内容を抽出するには、少し修正が必要です。

```bash
cut -f 2 sample.txt
```

`-f` または field フラグは、フィールドに基づいてテキストを切り取ります。デフォルトでは、区切り文字として TAB を使用するため、TAB で区切られたものはすべてフィールドと見なされます。出力は「dog」になるはずです。

フィールドフラグと区切り文字フラグを組み合わせて、カスタム区切り文字で内容を抽出できます。

```bash
cut -f 1 -d ";" sample.txt
```

これにより、TAB 区切り文字が「;」区切り文字に変更され、最初のフィールドを切り取っているため、結果は「The quick brown」になるはずです。

## Exercise

次のコマンドは何をしますか？なぜですか？

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

ファイル内の各行の最初の文字を取得するために使用するコマンドは何ですか？

## Quiz Answer

cut -c 1
