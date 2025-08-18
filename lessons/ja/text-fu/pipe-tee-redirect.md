---
lang: "ja"
title: "pipe と tee"
meta_title: "pipe と tee - テキスト操作"
meta_description: "効率的なコマンドラインデータフローのために、Linux のパイプと tee コマンドを学びましょう。stdout、stdin、ファイル出力を理解しましょう。Linux スキルを向上させましょう！"
meta_keywords: "Linux pipe, tee command, Linux tutorial, stdout, stdin, beginner Linux, command line, Linux guide"
---

## Lesson Content

それでは、配管作業に取り掛かりましょう。実際には違いますが、それに近いものです。コマンドを試してみましょう。

```bash
ls -la /etc
```

非常に長い項目リストが表示されるはずです。実際、少し読みにくいです。この出力をファイルにリダイレクトする代わりに、`less`のような別のコマンドで出力を見ることができたら便利だと思いませんか？それができるのです！

```bash
ls -la /etc | less
```

縦棒で表されるパイプ演算子 `|` を使用すると、コマンドの `stdout` を取得し、それを別のプロセスの `stdin` にすることができます。この場合、`ls -la /etc` の `stdout` を取得し、それを `less` コマンドに*パイプ*しました。パイプコマンドは非常に便利で、今後もずっと使い続けるでしょう。

では、コマンドの出力を 2 つの異なるストリームに書き込みたい場合はどうでしょうか？それは `tee` コマンドで可能です。

```bash
ls | tee peanuts.txt
```

画面に `ls` の出力が表示されるはずです。`peanuts.txt` ファイルを開くと、同じ情報が表示されるはずです！

## Exercise

次のコマンドを試してください。

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

パイプ演算子を表すキーは何ですか？

## Quiz Answer

|
