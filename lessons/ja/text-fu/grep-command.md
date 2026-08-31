---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "ja"
order_index: 16
title: "grep"
description: "固定文字列または正規表現で行を選択し、grep の結果を解釈する方法を学びます。"
meta_title: "grep - テキスト操作の達人"
meta_description: "Linux で強力な grep コマンドを使用してテキストパターンを検索する方法を学びます。このガイドでは、基本的な使い方、grep -e コマンド、カウントのための grep -c、および効果的なテキスト処理のためのその他の重要なオプションを網羅しています。"
meta_keywords: "grep コマンド，grep -e コマンド，grep -c, grep -f, grep -o, grep -e 例，linux grep, テキスト検索，パターンマッチング，テキスト処理，linux チュートリアル"
---

`grep` コマンドは、パターンに一致する入力行を選びます。指定ファイルまたは stdin を検索し、一致行の周辺を表示し、選択行を数え、終了ステータスで一致の有無を伝えられます。

## ファイル内の行を照合する

パターンの後に 1 つ以上の入力ファイルを渡します。

```bash
$ grep 'fox' sample.txt
```

GNU `grep` は標準でパターンを基本正規表現として解釈し、選択した各行を表示します。空白やシェルのメタ文字が先に解釈されないよう、パターンを引用します。

正規表現ではなく固定文字列として扱うには `-F` を使います。

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string}
正規表現として解釈せず、`products.txt` から文字列 `price: $5.00` を検索するコマンドはどれですか？

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` は固定文字列照合を選び、単一引用符はドル記号をシェル展開から保護します。"}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` は拡張正規表現を有効にし、`$` と `.` は文字どおりではなく特別な意味を持ちます。"}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` は一致しない行を選び、標準では正規表現として解釈します。"}
:::

## パターン構文を選ぶ

GNU `grep` でよく使う 3 つのモードは次のとおりです。

- 標準：基本正規表現。
- `-E`：`|`、`+`、`?` などをバックスラッシュなしで使う拡張正規表現。
- `-F`：正規表現演算子を使わない固定文字列。

`^` と `$` は行頭と行末に一致します。テキスト一覧から文字どおりの接尾辞 `.txt` で終わるファイル名を照合するには次を使います。

```bash
$ grep -E '\.txt$' filenames.txt
```

バックスラッシュはドットを文字どおりにし、正規表現でエスケープされていない `.` は任意の 1 文字に一致します。

:::single-choice{#grep-literal-txt-suffix}
文字どおりの接尾辞 `.txt` で終わる行に一致する拡張正規表現はどれですか？

::option[`'.txt$'`]{#grep-anychar-txt explanation="ドットがエスケープされていないため、文字どおりのピリオドではなく `txt` の前の任意の 1 文字に一致します。"}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` は文字どおりのピリオド、`$` は行末へ一致を固定します。"}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="行頭へ固定し、ドットもエスケープされていないため、異なる一致を表します。"}
:::

## パターンを安全に渡す

`-e PATTERN` はパターンを明示的に渡します。引用符だけではオプション解析を止められないため、パターンが `-` で始まる場合に特に便利です。

```bash
$ grep -e '-v' settings.conf
```

`-e` は繰り返して、いずれかのパターンに一致する行を選べます。`-f patterns.txt` はファイルから 1 行 1 パターンで読みます。

:::single-choice{#grep-hyphen-pattern}
`-v` をオプションとして解釈させず、`settings.conf` からパターン `-v` を検索するコマンドはどれですか？

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="引用符はシェル展開を防ぎますが、`grep` は渡された `-v` を一致反転オプションとして解釈できます。"}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="一致反転を有効にし、要求された形でパターンと入力を指定していません。"}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="`-e` は、次の引数がハイフンで始まってもパターンであると明示します。"}
:::

## 選択結果の出力を制御する

- `-i`：大文字小文字の違いを無視する。
- `-n`：選択行に行番号を付ける。
- `-v`：一致しない行を選ぶ。
- `-c`：入力ファイルごとの選択行数を表示する。
- `-o`：完全な選択行ではなく、空でない一致部分だけを表示する。

大文字小文字を無視して `fox` を含む行を数える例です。

```bash
$ grep -ic 'fox' sample.txt
```

`-c` は一致の総出現数ではなく選択された行を数えます。`fox fox` を含む 1 行も件数は 1 です。GNU `grep` で重ならない一致の出現数が必要なら、`grep -o PATTERN | wc -l` というパイプラインも使えます。

:::single-choice{#grep-count-lines}
`data.txt` に `error error` を含む行が 1 行、一致しない行が 2 行あります。`grep -c 'error' data.txt` は何を報告しますか？

::option[`2`。1 行に単語が 2 回現れるため。]{#grep-count-occurrences explanation="`-c` は 1 行内の個々の一致ではなく、選択された行を数えます。"}
::option[`1`。一致する行がちょうど 1 行のため。]{#grep-count-one-line .correct explanation="パターンが同じ行に 2 回現れても、その行は 1 回だけ選択されます。"}
::option[`3`。ファイル全体が 3 行のため。]{#grep-count-total-lines explanation="`grep -c` に寄与するのは選択行だけで、一致しない行は除外されます。"}
:::

## stdin の絞り込みとディレクトリ検索

入力ファイルがなければ `grep` は stdin を読み、パイプラインで自然に使えます。

```bash
$ env | grep '^USER='
```

ディレクトリ以下の読み取り可能なファイルを再帰検索するには `-r` を使います。

```bash
$ grep -r 'listen_port' config/
```

権限エラーなどの診断は stderr へ送られ、照合入力にはなりません。すぐに権限を昇格するのではなく、検索範囲を絞り、権限を理解してください。

:::single-choice{#grep-pipeline-input}
`generate-report | grep 'failed'` で `grep` は何を検索しますか？

::option[現在のディレクトリにある `generate-report` というファイル。]{#grep-report-file explanation="左側はコマンドとして実行され、`grep` へファイルオペランドとして渡されません。"}
::option[`generate-report` が生成した stdout ストリーム。]{#grep-report-stdout .correct explanation="パイプが生成側の stdout を `grep` の stdin へ接続します。"}
::option[`generate-report` が生成した stderr ストリーム。]{#grep-report-stderr explanation="通常のパイプが運ぶのは stdout で、stderr は明示的にリダイレクトしない限り別です。"}
:::

## 終了ステータスを解釈する

通常の検索で GNU `grep` は、少なくとも 1 行を選ぶと `0`、1 行も選ばなければ `1`、エラーなら `2` を返します。これによりスクリプトは「一致なし」を読み取れないファイルや不正なパターンと区別できます。

`-q` は通常の出力を抑制し、一致を見つけると停止するため条件判定に便利です。表示が空だからといって成否を決めないでください。`-q`、リダイレクト、一致なし、エラーはいずれも stdout がほぼ空になり得ますが、ステータスは異なります。

固定文字列と正規表現の検索を練習するには、次のラボを試してください。

1. **[Linux で grep を使ってテキストを検索する](https://labex.io/ja/labs/comptia-search-text-with-grep-in-linux-590841)** - 基本検索、行番号、アンカー、基本・拡張正規表現を練習します。
2. **[Linux grep コマンド：パターン検索](https://labex.io/ja/labs/linux-linux-grep-command-pattern-searching-219192)** - `grep` と正規表現でテキスト内のパターンを検索します。
3. **[干し草の中の針](https://labex.io/ja/labs/linux-needle-in-the-haystack-388109)** - `grep` でパターン検索、件数集計、一意値の抽出、複数条件の組み合わせを行います。

## まとめ

行指向テキストを検索し、一致とエラーを区別できるようになりました。

1. 基本、拡張、固定文字列の照合を選ぶ。
2. パターンを引用し、先頭がハイフンなら `-e` を使う。
3. 選択行数と出現数を混同せずに数える。
4. stdin を絞り込むか、対象を絞ったディレクトリを再帰検索する。
5. 一致、一致なし、エラーの終了ステータスを解釈する。
