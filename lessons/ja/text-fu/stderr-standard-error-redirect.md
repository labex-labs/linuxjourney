---
index: 3
lang: "ja"
title: "stderr (標準エラー)"
meta_title: "stderr (標準エラー) - Text-Fu"
meta_description: "Linux の stderr（標準エラー）リダイレクトについて学びます。Bash でのエラー処理のために、2>、2>&1、&>、および/dev/null を理解します。Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "Linux stderr, 標準エラー, 2> リダイレクト，2>&1, &> リダイレクト，/dev/null, Bash エラー処理，Linux チュートリアル，初心者 Linux"
---

## Lesson Content

今度は少し違うことを試してみましょう。システム上に存在しないディレクトリの内容を一覧表示し、その出力を再び `peanuts.txt` ファイルにリダイレクトしてみましょう。

```bash
ls /fake/directory > peanuts.txt
```

表示されるはずのものは次のとおりです。

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

さて、あなたはおそらく、そのメッセージはファイルに送信されるべきではなかったのか、と考えているでしょう。実際には、標準エラー (stderr) と呼ばれる別の I/O ストリームがここで機能しています。デフォルトでは、stderr もその出力を画面に送信します。これは stdout とはまったく異なるストリームです。したがって、その出力を別の方法でリダイレクトする必要があります。

残念ながら、リダイレクタは `<` や `>` を使うほど簡単ではありませんが、かなり近いです。ファイルディスクリプタを使用する必要があります。ファイルディスクリプタは、ファイルまたはストリームにアクセスするために使用される非負の数値です。これについては後で詳しく説明しますが、今のところ、stdin、stdout、および stderr のファイルディスクリプタはそれぞれ 0、1、および 2 であることを知っておいてください。

したがって、stderr をファイルにリダイレクトしたい場合は、次のようにします。

```bash
ls /fake/directory 2> peanuts.txt
```

`peanuts.txt` には stderr メッセージのみが表示されるはずです。

では、stderr と stdout の両方を `peanuts.txt` ファイルで見たい場合はどうすればよいでしょうか？これもファイルディスクリプタで可能です。

```bash
ls /fake/directory > peanuts.txt 2>&1
```

これは `ls /fake/directory` の結果を `peanuts.txt` ファイルに送信し、次に `2>&1` を介して stderr を stdout にリダイレクトします。ここでの操作の順序が重要です。`2>&1` は stderr を stdout が指しているものに送信します。この場合、stdout はファイルを指しているので、`2>&1` も stderr をファイルに送信します。したがって、`peanuts.txt` ファイルを開くと、stderr と stdout の両方が表示されるはずです。私たちの場合、上記のコマンドは stderr のみを出力します。

stdout と stderr の両方をファイルにリダイレクトするより短い方法があります。

```bash
ls /fake/directory &> peanuts.txt
```

では、そのような不要なものをすべて排除し、stderr メッセージを完全に削除したい場合はどうすればよいでしょうか？特別なファイル `/dev/null` に出力をリダイレクトすると、すべての入力が破棄されます。

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

練習は完璧をもたらします！入出力リダイレクトの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux での入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - この演習では、Linux シェルでの入出力のリダイレクトについて学びます。>、>>、2>、および tee コマンドなどの演算子を使用して、標準出力 (stdout)、標準エラー (stderr)、および標準入力 (stdin) を操作することにより、コマンドからのデータフローを制御する練習をします。

この演習は、実際のシナリオで I/O リダイレクトの概念を適用し、Linux でのデータストリームの管理に自信をつけるのに役立ちます。

## Quiz Question

stderr のリダイレクタは何ですか？

## Quiz Answer

2>
