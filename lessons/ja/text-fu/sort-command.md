---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "ja"
order_index: 12
title: "sort"
description: "sort を使い、テキスト行を辞書順、数値順、または選択したフィールド値で並べる方法を学びます。"
meta_title: "sort - テキスト処理の達人"
meta_description: "Linux の sort コマンドを使ってテキストファイルをソートする方法を学びましょう。逆順ソートや数値ソートなどのオプションを発見してください。Linux コマンドラインスキルを向上させましょう！"
meta_keywords: "Linux sort コマンド，sort -r, sort -n, Linux チュートリアル，コマンドライン，初心者 Linux, sort ガイド"
---

`sort` コマンドは完全な行を読み、選択した比較規則で並べ、結果を stdout へ書きます。出力操作を明示しない限り、入力ファイルは変更しません。

## 行全体を並べ替える

`animals.txt` を昇順に並べます。

```text
dog
cow
cat
elephant
bird
```

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

テキストの順序は現在のロケールに従うため、大文字小文字、アクセント、句読点の扱いが変わることがあります。スクリプトで再現可能なバイト順が必要なら、`LC_ALL=C sort animals.txt` のように一貫したロケールを使います。

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending}
キーや数値オプションなしの `sort animals.txt` は何をしますか？

::option[現在のロケールに従って入力の行全体を並べる。]{#sort-locale-lines .correct explanation="標準の `sort` は有効なロケールの照合規則で行全体を比較します。"}
::option[各行内の単語だけを並べ、行順は固定する。]{#sort-words-within-lines explanation="`sort` は各行をレコードとして扱い、個々の行内の単語は並べ替えません。"}
::option[`animals.txt` を自動的にその場で書き換える。]{#sort-auto-rewrite explanation="標準では結果を stdout へ送り、入力ファイルは変更しません。"}
:::

## 結果を逆順にする

`-r` を付けると比較結果が逆になります。

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order}
`animals.txt` を逆順に並べるコマンドはどれですか？

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="`-n` は数値比較を指定し、逆順を意味しません。"}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="`-u` は重複キーを抑制し、出力を逆順にはしません。"}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="`-r` は他の比較規則で選ばれた順序を逆にします。"}
:::

## 数値を比較する

辞書順は文字を比較するため、通常 `10` は `2` より前になります。通常の数値比較には `-n` を使います。

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

必要ならオプションを組み合わせます。`sort -nr scores.txt` は数値で比較し、大きい値から並べます。

:::single-choice{#sort-numbers-descending}
`scores.txt` の数値行を大きい順に並べるコマンドはどれですか？

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="数値比較ですが、標準の方向では小さい値から並びます。"}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` が数値比較、`-r` が逆順を指定し、数値の降順になります。"}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="テキスト照合を逆にするだけで数値比較ではなく、`10` と `2` などが予想外の順になります。"}
:::

## フィールドで並べ替える

キーは `-k START[,END]` で選びます。標準では連続する空白がフィールド区切りです。コロン区切りなら `-t ':'` を使います。

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

`-t ':'` が区切り、`-k 2,2` がキーをフィールド 2 だけに限定し、末尾の `n` が数値比較を指定します。`,2` がない場合、フィールド 2 から始まるキーは通常、行末まで続きます。

:::single-choice{#sort-second-colon-field}
`users.txt` の第 2 コロン区切りフィールドだけを数値順にするコマンドはどれですか？

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="標準の空白区切りでフィールド 1 を選び、2 番目のコロン区切りフィールドではありません。"}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` はフィールド 2 を抽出しますが、元のレコードをそのキーで並べ替えません。"}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="コロンが境界を定め、`2,2` がキーをフィールド 2 に限定し、`n` が数値比較を指定します。"}
:::

## 重複を除き、出力を保存する

`-u` は、選択した比較キーが等しいものごとに 1 行を出力します。

```bash
$ sort -u names.txt
```

```bash
$ sort names.txt > names-sorted.txt
```

並べ替えと重複除去を同時に行います。入力と異なる出力先なら通常のリダイレクトで構いません。`sort names.txt > names.txt` はシェルが読み取り前に入力を切り詰めるため使わないでください。GNU `sort` で同じパスへ意図的に書くなら次を使えます。

```bash
$ sort -o names.txt names.txt
```

元データが重要なら、バックアップを取るか、別に書いた結果を検証してください。

:::single-choice{#sort-safe-same-file}
GNU/Linux で、シェルリダイレクトによる切り詰めを避け、並べ替え結果を `names.txt` へ安全に書き戻すコマンドはどれですか？

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="GNU `sort` は必要に応じて読み取った後に `-o` 出力を管理するため、シェルが `>` で先に入力を切り詰めません。"}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="シェルは `sort` を起動する前に `names.txt` を切り詰めるため、入力を失う恐れがあります。"}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="重複を除いた並べ替え結果を stdout へ書き、入力ファイルは変更しません。"}
:::

行指向データの並べ替えを練習するには、次のラボを試してください。

1. **[Linux sort コマンド：テキストの並べ替え](https://labex.io/ja/labs/linux-linux-sort-command-text-sorting-219196)** - テキスト行を昇順、降順などで並べます。
2. **[単語数の集計と並べ替え](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - 単語数と並べ替えを組み合わせてデータを分析します。

## まとめ

並べ替えるテキストの比較規則と出力先を選べるようになりました。

1. 再現性が重要なら明示したロケールで行全体を並べる。
2. `-r` で結果を逆順にする。
3. `-n` で数値を比較する。
4. `-t` と `-k` で範囲を限定したフィールドキーを選ぶ。
5. 入力を切り詰めずに重複を除去または結果を保存する。
