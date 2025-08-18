---
lang: "ja"
title: "head"
meta_title: "head - テキスト操作"
meta_description: "Linux の 'head' コマンドを使ってファイルの先頭を表示する方法を学びます。行数を指定する -n などのオプションを理解します。必須の Linux コマンドチュートリアル。"
meta_keywords: "head command, Linux head, view file beginning, Linux tutorial, Linux commands, beginner Linux, head -n, Linux guide"
---

## Lesson Content

非常に長いファイルがあるとします。実際、選択肢はたくさんあります。`cat /var/log/syslog` を実行してみてください。何ページにもわたるテキストが表示されるはずです。このテキストファイルの最初の数行だけを見たい場合はどうすればよいでしょうか？それは `head` コマンドで可能です。デフォルトでは、`head` コマンドはファイルの最初の 10 行を表示します。

```bash
head /var/log/syslog
```

行数を好きなように変更することもできます。代わりに最初の 15 行を見たいとします。

```bash
head -n 15 /var/log/syslog
```

`-n` フラグは「行数」を意味します。

## Exercise

次のコマンドは何をしますか、そしてその理由は？

```bash
had -c 15 /var/log/syslog
```

## Quiz Question

`head` コマンドで表示したい行数を変更するために使用するフラグは何ですか？

## Quiz Answer

-n
