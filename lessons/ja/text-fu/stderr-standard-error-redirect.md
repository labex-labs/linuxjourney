---
title: "stderr (標準エラー)"
description: "Linux の stderr（標準エラー）リダイレクトについて学びます。Bash でのエラー処理のために、2>、2>&1、&>、および/dev/null を理解します。Linux コマンドラインスキルを向上させましょう！"
keywords: "Linux stderr, 標準エラー, 2> リダイレクト，2>&1, &> リダイレクト，/dev/null, Bash エラー処理，Linux チュートリアル，Linux 初心者"
---

## Lesson Content

ここで少し違うことを試してみましょう。システム上に存在しないディレクトリの内容を一覧表示し、その出力を再び `peanuts.txt` ファイルにリダイレクトしてみます。

```bash
ls /fake/directory > peanuts.txt
```

表示されるはずのものは次のとおりです。

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

おそらく、「そのメッセージはファイルに送信されるべきではなかったのか？」と考えているでしょう。実際には、標準エラー (stderr) と呼ばれる別の I/O ストリームがここで機能しています。デフォルトでは、stderr もその出力を画面に送信します。これは stdout とはまったく異なるストリームです。したがって、その出力を別の方法でリダイレクトする必要があります。

残念ながら、リダイレクターは `<` や `>` を使うほど簡単ではありませんが、かなり近いです。ファイルディスクリプタを使用する必要があります。ファイルディスクリプタは、ファイルまたはストリームにアクセスするために使用される非負の数値です。これについては後で詳しく説明しますが、今のところ、stdin、stdout、および stderr のファイルディスクリプタはそれぞれ 0、1、および 2 であることを知っておいてください。

したがって、stderr をファイルにリダイレクトしたい場合は、次のようにします。

```bash
ls /fake/directory 2> peanuts.txt
```

`peanuts.txt` には stderr メッセージのみが表示されるはずです。

では、stderr と stdout の両方を `peanuts.txt` ファイルで見たい場合はどうでしょうか？これもファイルディスクリプタを使って可能です。

```bash
ls /fake/directory > peanuts.txt 2>&1
```

これは `ls /fake/directory` の結果を `peanuts.txt` ファイルに送信し、次に `2>&1` を介して stderr を stdout にリダイレクトします。ここでの操作の順序は重要です。`2>&1` は stderr を stdout が指しているものに送信します。この場合、stdout はファイルを指しているので、`2>&1` も stderr をファイルに送信します。したがって、`peanuts.txt` ファイルを開くと、stderr と stdout の両方が表示されるはずです。この場合、上記のコマンドは stderr のみを出力します。

stdout と stderr の両方をファイルにリダイレクトするより短い方法があります。

```bash
ls /fake/directory &> peanuts.txt
```

では、そのような余計なものを一切表示したくなく、stderr メッセージを完全に削除したい場合はどうでしょうか？ `/dev/null` と呼ばれる特殊なファイルに出力をリダイレクトすることもでき、それはすべての入力を破棄します。

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

What is the following command doing?

```bash
ls /fake/directory >> /dev/null 2>&1
```

## Quiz Question

stderr のリダイレクターは何ですか？

## Quiz Answer

2>
