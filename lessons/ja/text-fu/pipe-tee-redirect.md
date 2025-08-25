---
index: 4
lang: "ja"
title: "パイプと tee"
meta_title: "パイプと tee - Text-Fu"
meta_description: "効率的なコマンドラインデータフローのために Linux パイプと tee コマンドを学びましょう。stdout、stdin、ファイル出力を理解しましょう。Linux スキルを向上させましょう！"
meta_keywords: "Linux pipe, tee command, Linux tutorial, stdout, stdin, beginner Linux, command line, Linux guide"
---

## Lesson Content

それでは、配管について少し説明しましょう。実際にはそうではありませんが、ある意味ではそうです。コマンドを試してみましょう。

```bash
ls -la /etc
```

非常に長いアイテムのリストが表示されるはずです。実際、少し読みにくいです。この出力をファイルにリダイレクトする代わりに、`less`のような別のコマンドで出力を表示できたら便利だと思いませんか？できますよ！

```bash
ls -la /etc | less
```

縦棒で表されるパイプ演算子`|`を使用すると、コマンドの`stdout`を取得し、それを別のプロセスの`stdin`にすることができます。この場合、`ls -la /etc`の`stdout`を取得し、それを`less`コマンドに_パイプ_しました。パイプコマンドは非常に便利で、永遠に使い続けるでしょう。

では、コマンドの出力を 2 つの異なるストリームに書き込みたい場合はどうすればよいでしょうか？それは`tee`コマンドで可能です。

```bash
ls | tee peanuts.txt
```

画面に`ls`の出力が表示されるはずです。`peanuts.txt`ファイルを開くと、同じ情報が表示されるはずです！

## Exercise

習うより慣れろ！入出力リダイレクトとパイプラインの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux での入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`、`>>`、`2>`、`tee`コマンドなどの演算子を使用して、標準出力 (stdout)、標準エラー (stderr)、標準入力 (stdin) を操作することで、コマンドからのデータフローを制御する練習をします。
2. **[シーケンス制御とパイプライン](https://labex.io/ja/labs/linux-sequence-control-and-pipeline-17994)** - コマンド実行シーケンスを制御し、パイプラインを利用し、`cut`、`grep`、`wc`、`sort`、`uniq`などの強力なテキスト処理ツールを活用する方法を学びます。
3. **[データストリームのリダイレクト](https://labex.io/ja/labs/linux-data-stream-redirection-17995)** - 標準入力、出力、エラーのストリームの操作、出力の結合、`/dev/null`の利用など、Linux ストリームリダイレクトの技術を学びます。

これらの演習は、パイプとリダイレクトの概念を実際のシナリオに適用し、コマンドラインでのデータ操作に自信をつけるのに役立ちます。

## Quiz Question

パイプ演算子を表すキーは何ですか？

## Quiz Answer

|
