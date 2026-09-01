---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "ja"
order_index: 7
title: "paste"
description: "paste を使い、対応する行を結合したり、指定した区切り文字で行を直列化したりする方法を学びます。"
meta_title: "paste - テキスト操作"
meta_description: "Linux の paste コマンドを使ってファイルの行を結合する方法を学びましょう。この必須の Linux コマンドチュートリアルで、区切り文字を発見し、ファイルを結合しましょう。"
meta_keywords: "Linux paste コマンド，paste コマンドチュートリアル，ファイル行の結合，Linux コマンド，初心者 Linux, Linux ガイド"
---

`paste` コマンドは行を列として結合します。標準では各入力ファイルから 1 行ずつ取り出し、タブでつないで、すべての入力が終わるまで繰り返します。

## ファイルを横に並べて結合する

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

列間の空白はタブです。ファイル全体を順番に書く `cat` と異なり、`paste` は対応する入力行を結合します。

:::single-choice{#paste-corresponding-lines} `first.txt` に `A`、`B`、`second.txt` に `1`、`2` が順に入っています。`paste first.txt second.txt` の標準出力はどれですか？

::option[`A`、`B`、`1`、`2` を 4 行に順に表示する。]{#paste-concatenated-files explanation="これはファイルを順番に書く動作です。`paste` は対応する行を結合します。"}
::option[`A`、`B`、`1`、`2` を区切りなしで 1 行に表示する。]{#paste-one-line-no-separator explanation="1 行への直列化には `-s` が必要で、標準の区切りはなしではなくタブです。"}
::option[`A` と `1`、次に `B` と `2` をタブ区切りで表示する。]{#paste-parallel-result .correct explanation="標準の並列モードは出力行ごとに各ファイルから 1 行を取り、フィールドをタブで区切ります。"}
:::

## 区切り文字を選ぶ

`-d LIST` で標準のタブを置き換えます。

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

シェルで意味を持つ区切り文字は引用します。`paste` は複数文字のリストを順に使えますが、2 列なら 1 文字が分かりやすいでしょう。

:::single-choice{#paste-colon-delimiter} `names.txt` と `roles.txt` の対応する行をコロンで結ぶコマンドはどれですか？

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="`-d` は各フィールド間の標準タブを指定されたコロンへ置き換えます。"}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="`-s` は直列モードを選び、`:` は区切りではなく入力パスとして扱われます。"}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="`-d` がなければ各オペランドは入力ファイルで、`:` というファイルを開こうとします。"}
:::

## 1 ファイルの行を直列化する

`-s` は各入力ファイルを直列に処理し、その行を 1 つの出力行へ結合します。

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

複数ファイルを `-s` へ渡すと、各ファイルがそれぞれ 1 出力行になります。

:::single-choice{#paste-serialize-with-spaces} `words.txt` の全行を空白区切りの 1 行にするコマンドはどれですか？

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="標準の並列モードでは、入力が 1 ファイルなら入力行ごとに出力され、ファイル間を結ぶ区切りは働きません。"}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="2 ファイルを標準のタブで別々に直列化し、要求された 1 ファイルの空白区切り結果にはなりません。"}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` がファイルの行を直列化し、`-d ' '` が間に空白を使います。"}
:::

## 長さの異なる入力を扱う

並列入力の行数が異なる場合、`paste` は最長のファイルが終わるまで続け、短いファイルの不足値を空フィールドにします。

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files} 並列 `paste` に渡した 1 ファイルが他より先に終わるとどうなりますか？

::option[最長の入力が終わるまで、そのファイルには空フィールドを使う。]{#paste-empty-fields .correct explanation="並列モードはすべてのファイルが尽きるまで続き、短い入力の不足行を空フィールドで表します。"}
::option[直ちに停止し、残りの行を捨てる。]{#paste-stop-shortest explanation="最長の入力まで続くため、別のファイルが終わっても残りの行は捨てません。"}
::option[短いファイルを先頭から繰り返す。]{#paste-repeat-shorter explanation="入力レコードを循環せず、尽きた入力は空フィールドになります。"}
:::

## stdin から 1 つの入力を読む

ファイルオペランドに `-` を使うと、その位置の入力を stdin から読みます。

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand} `producer | paste names.txt -` で `-` は何を意味しますか？

::option[結合結果を stderr へ書く。]{#paste-write-stderr explanation="ここでハイフンは入力元を示し、出力ストリームはリダイレクトしません。"}
::option[2 列間の区切り文字を削除する。]{#paste-remove-delimiter explanation="区切りは `-d` で選び、ハイフンは区切りを変えません。"}
::option[その入力列を stdin から読む。]{#paste-read-stdin .correct explanation="ハイフンは、そのオペランド位置で標準入力を使うよう `paste` に指示します。"}
:::

行指向データの結合を練習するには、次のラボを試してください。

1. **[シンプルなテキスト処理](https://labex.io/ja/labs/linux-simple-text-processing-18004)** - `tr`、`col`、`join`、`paste` でテキストデータを操作、分析します。

## まとめ

行指向の入力を一定した配置と区切りで結合できるようになりました。

1. 複数ファイルの対応する行を結合する。
2. `-d` で標準のタブ区切りを置き換える。
3. `-s` で 1 ファイルの行を直列化する。
4. 短い入力による空フィールドを解釈する。
5. stdin から入力する位置に `-` を使う。
