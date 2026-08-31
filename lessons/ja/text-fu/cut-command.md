---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "ja"
order_index: 6
title: "cut"
description: "cut を使い、各行から文字位置または区切られたフィールドを選択する方法を学びます。"
meta_title: "cut - Text-Fu"
meta_description: "Linux の`cut`コマンドを使用して、ファイルから特定のテキストセクションを抽出する方法を学びます。このガイドでは、文字およびフィールド（`cut f`）による切り取り、カスタム区切り文字での`cut f`の使用方法を解説します。Linux テキスト処理を習得するのに最適です。"
meta_keywords: "cut コマンド，Linux テキスト処理，テキスト抽出，cut f, cut f 方法，Linux チュートリアル，cut の例，Linux ガイド，フィールド切り取り"
---

`cut` コマンドは、入力の各行から指定した文字位置またはフィールドを選びます。区切り文字とフィールド位置が一定した構造化テキストに適しています。

例に使うタブ区切りファイルを作ります。`printf` は `\t` をタブ、`\n` を改行として解釈します。

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## 文字位置を選択する

各行の位置を選ぶには `-c LIST` を使います。位置は 1 から始まります。

```bash
$ cut -c 1 team.tsv
n
a
b
```

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

リストには個別の位置や範囲を指定できます。空白、タブ、句読点も位置を占め、`cut` は各行を独立して処理します。

:::single-choice{#cut-first-character}
`names.txt` の各行から最初の文字を表示するコマンドはどれですか？

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="`-c` は文字位置を選び、位置 1 は各行の最初の文字です。"}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="`-f` はタブ区切りの最初のフィールドを選ぶため、複数文字を含むことがあります。"}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="`-d` はフィールドの区切り文字を指定し、フィールド選択と併用します。文字位置は選びません。"}
:::

## タブ区切りフィールドを選択する

フィールドは `-f LIST` で選び、標準の区切り文字はタブです。

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

文字選択と同様、`1`、`1,3`、`2-4`、`-3`、`2-` などをリストに指定できます。

:::single-choice{#cut-second-tab-field}
`team.tsv` の各行から 2 番目のタブ区切りフィールドを表示するコマンドはどれですか？

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="これはタブ区切りの 2 番目のフィールドではなく、各行の 2 文字目を選びます。"}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="`-d` がなければフィールドモードはタブを区切りに使い、`-f 2` が 2 番目を選びます。"}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="`2` を区切り文字にしようとしますが、フィールドリストがなく、フィールド 2 は選びません。"}
:::

## 独自の区切り文字を選ぶ

タブ以外で区切られたフィールドでは、`-d CHARACTER` と `-f` を使います。

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

この形式の区切り文字は 1 文字です。引用符のないセミコロンはシェルで制御用の意味を持つため引用します。

:::single-choice{#cut-semicolon-role-field}
`team.txt` の 2 番目のセミコロン区切りフィールドを表示するコマンドはどれですか？

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="これはコロン区切りのフィールドを選びますが、ファイルはセミコロン区切りです。"}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="引用したセミコロンが区切りを設定し、`-f 2` が各行の 2 番目を選びます。"}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="文字選択と不正なフィールド引数を混在させています。区切りは `-d` の後、番号は `-f` の後です。"}
:::

## 区切り文字のない行を扱う

フィールドモードでは、区切り文字のない行は通常そのまま表示されます。抑制するには `-s` を加えます。

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

これは一般的な CSV の検証には使えません。CSV には引用された区切り、埋め込み改行、エスケープ規則があるため、CSV 対応ツールを使ってください。

:::single-choice{#cut-suppress-undelimited}
`cut -d ':' -f 1` で `-s` は何をしますか？

::option[選択したフィールドを並べ替えてから表示する。]{#cut-s-sort explanation="`cut` は並べ替えず、`-s` も順序とは無関係です。"}
::option[連続する区切り文字を 1 つとして扱う。]{#cut-s-squeeze explanation="`-s` は区切り文字をまとめません。空のフィールドにも位置として意味があります。"}
::option[選択した区切り文字を含まない行を抑制する。]{#cut-s-suppress .correct explanation="フィールドモードで `-s` は、区切られていない行がそのまま通過するのを防ぎます。"}
:::

## stdin から読み取る

ファイルを指定しない場合や入力オペランドに `-` を使う場合、`cut` は stdin を読みます。そのためパイプラインの処理段階に適しています。

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input}
`generate-data | cut -d ':' -f 1` で、`cut` はどこから入力を読みますか？

::option[パイプを通じて `generate-data` の stdout から。]{#cut-pipe-stdin .correct explanation="パイプが生成側の stdout を `cut` の stdin へ接続し、別の入力ファイルは指定されていません。"}
::option[`generate-data` という名前のファイルから。]{#cut-pipe-file explanation="`generate-data` は左側のコマンドとして実行され、`cut` へファイル名として渡されません。"}
::option[`cut` の標準エラーストリームから。]{#cut-pipe-stderr explanation="通常のパイプは前のコマンドの stdout を標準入力へ渡し、`cut` の stderr からは読みません。"}
:::

位置とフィールドの選択を練習するには、次のラボを試してください。

1. **[Linux cut コマンド：テキストの切り出し](https://labex.io/ja/labs/linux-linux-cut-command-text-cutting-219187)** - `cut` でテキストファイルから列やフィールドを抽出します。
2. **[シーケンス制御とパイプライン](https://labex.io/ja/labs/linux-sequence-control-and-pipeline-17994)** - パイプラインと `cut`、`grep`、`wc`、`sort`、`uniq` を学びます。

## まとめ

`cut` を使い、行指向テキストから一定した位置を選択できるようになりました。

1. 個別の文字位置や範囲を選択する。
2. `-f` でタブ区切りフィールドを抽出する。
3. `-d` で 1 文字の区切りを指定する。
4. 必要に応じて区切りのない行を抑制する。
5. ファイルまたは stdin から構造化テキストを読む。
