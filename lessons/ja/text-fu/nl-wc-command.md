---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "ja"
order_index: 15
title: "wc と nl"
description: "wc で行、単語、バイト、文字を数え、nl で行番号を付ける方法を学びます。"
meta_title: "wc と nl - Text-Fu"
meta_description: "この Linux チュートリアルで wc コマンドと nl コマンドをマスターしましょう。Linux での単語数の数え方、ファイルへの行番号の追加方法、基本的なファイル分析の方法を学びます。コマンドラインスキルを向上させたい初心者にとって完璧なガイドです。"
meta_keywords: "wc コマンド，nl コマンド，Linux 単語数カウント，ファイル内の単語数を数える Linux, Linux 行番号，nl コマンド Linux, ファイル分析，テキスト処理 Linux, Linux コマンドライン，初心者向け Linux チュートリアル"
---

`wc` コマンドはテキストストリームの性質を数え、`nl` は入力へ生成した行番号を付けて書き出します。どちらもファイルまたは stdin を読み、結果を stdout へ送ります。

## wc の標準出力を読む

件数オプションなしの `wc` は、改行文字数、単語数、バイト数を表示し、ファイルを指定した場合はその名前を続けます。

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

左から、`2` は行として報告される改行文字数、`3` は空白区切りの単語数、`15` はこの ASCII 例のバイト数です。`wc -l` が数えるのは見た目上の行ではなく改行文字なので、末尾に改行のない最後の行は数えられません。

:::single-choice{#wc-default-columns} `wc file.txt` の標準出力で、最初の 3 つの数値は何を表しますか？

::option[行、単語、バイトの順。]{#wc-lines-words-bytes .correct explanation="標準の `wc` は、ファイル名の前に改行数、単語数、バイト数を報告します。"}
::option[バイト、単語、行の順。]{#wc-bytes-words-lines explanation="同じ測定値ですが順序が違います。行数が最初です。"}
::option[ファイル、文字、段落の順。]{#wc-files-characters-paragraphs explanation="標準列はファイル数や段落数を数えず、3 番目はバイト数です。"}
:::

## 1 つの件数を要求する

必要な測定だけを選べます。

- `-l`：改行文字数。
- `-w`：単語数。
- `-c`：バイト数。
- `-m`：現在のロケールに従った文字数。

```bash
$ wc -w colors.txt
3 colors.txt
```

```bash
$ printf 'one two\n' | wc -w
2
```

ASCII ではバイト数と文字数は等しいですが、UTF-8 などのマルチバイト符号化では異なることがあります。ファイルオペランドなしで stdin を使うと、通常はファイル名ラベルが付きません。

:::single-choice{#wc-word-count-only} `essay.txt` の単語数だけを報告するコマンドはどれですか？

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="`-l` は単語ではなく改行文字を報告します。"}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="`-w` は単語数の測定を選びます。"}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="`-c` は空白区切りの単語ではなくバイトを報告します。"}
:::

:::single-choice{#wc-characters-not-bytes} 現在のロケールで、バイトではなく文字を数えるよう `wc` に指示するオプションはどれですか？

::option[`-m`]{#wc-character-option .correct explanation="`-m` は文字数を報告し、マルチバイトテキストではバイト数と異なることがあります。"}
::option[`-c`]{#wc-byte-option explanation="`-c` はバイトを報告します。UTF-8 などでは 1 文字が複数バイトを占めることがあります。"}
::option[`-w`]{#wc-word-option explanation="`-w` は文字やバイトではなく単語を数えます。"}
:::

複数ファイルを指定すると、`wc` はファイルごとの結果と `total` 行を表示します。GNU `wc -L` は入力行の最大表示幅を報告します。

## nl で空でない行に番号を付ける

`nl` は標準で、入力の論理的な本文にある空でない行へ番号を付けます。`notes.txt` の 2 行目が空の場合を考えます。

```text
alpha

beta
```

空行は保持されますが番号は付きません。

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl` は番号付き出力を書くだけで、`notes.txt` を変更しません。

:::single-choice{#nl-default-blank-lines} `nl notes.txt` は標準で本文の空行をどう扱いますか？

::option[空行を出力から完全に省く。]{#nl-omit-blank explanation="空行は出力に残りますが、標準では番号を割り当てません。"}
::option[番号を付けずに保持する。]{#nl-preserve-unnumbered .correct explanation="標準の本文形式は空でない行へ番号を付け、空行を番号なしで通します。"}
::option[空でない行と同じ連番を付ける。]{#nl-number-blank-default explanation="本文の全行へ番号を付けるには `-ba` など別の形式が必要です。"}
:::

## すべての行に番号を付ける

`-ba` は、すべての行を番号付けする本文形式 `a` を選びます。

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

`-w 3` は番号欄の幅、`-s ': '` は番号後の区切りを変更します。

:::single-choice{#nl-number-all-lines} `notes.txt` の空行を含む本文全行へ番号を付けるコマンドはどれですか？

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="番号欄の幅を変えますが、空でない行だけという標準規則は変えません。"}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="`-b` は本文形式を選び、形式 `a` は本文のすべての行へ番号を付けます。"}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="改行文字数を表示するだけで、ファイル内容へ行番号を付けて再出力しません。"}
:::

テキストの集計と番号付けを練習するには、次のラボを試してください。

1. **[Linux wc コマンド：テキストの集計](https://labex.io/ja/labs/linux-linux-wc-command-text-counting-219200)** - `wc` で単語、行、文字を数えます。
2. **[Linux nl コマンド：行番号付け](https://labex.io/ja/labs/linux-linux-nl-command-line-numbering-210988)** - `nl` でテキストファイルへ行番号を付けます。
3. **[単語数の集計と並べ替え](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - `wc` と並べ替えを組み合わせて分析します。

## まとめ

元データを編集せず、テキストストリームを測定して見える行番号を付けられるようになりました。

1. `wc` の標準列である行、単語、バイトを解釈する。
2. `-l`、`-w`、`-c`、`-m` で 1 つの件数を選ぶ。
3. バイト数と文字数を区別する。
4. `nl` の標準動作で空でない行へ番号を付ける。
5. `nl -ba` で空行にも番号を付ける。
