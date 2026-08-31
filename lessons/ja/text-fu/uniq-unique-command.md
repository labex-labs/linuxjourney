---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "ja"
order_index: 14
title: "uniq (重複なし)"
description: "uniq を使い、隣接する同一行のグループをまとめ、数え、絞り込む方法を学びます。"
meta_title: "uniq (重複なし) - Text-Fu"
meta_description: "Linux の uniq コマンドを使用して、テキストから重複する隣接行をフィルタリングおよび削除する方法を探ります。-c、-u、-d などのオプションを使用して uniq Linux ツールを使用する方法や、sort と組み合わせて強力なテキスト処理を行う方法を学びましょう。"
meta_keywords: "uniq コマンド，Linux uniq, uniq linux, 重複削除，sort uniq, テキスト処理，データクレンジング，Linux チュートリアル"
---

`uniq` コマンドは各入力行を直前の行と比較します。隣接する同一行のグループをまとめ、数え、選択できますが、ファイル全体に散らばった重複は検索しません。

## 隣接する重複行をまとめる

`reading.txt` にグループ化された値があるとします。

```plaintext
book
book
paper
paper
article
article
magazine
```

絞り込みオプションなしの `uniq` は、各隣接グループから代表 1 行を表示します。

```bash
$ uniq reading.txt
book
paper
article
magazine
```

結果は stdout へ送られるため、入力ファイルは変わりません。

:::single-choice{#uniq-collapse-adjacent}
`uniq reading.txt` は標準で何をしますか？

::option[ファイル全体を並べ替えてから、繰り返された値をすべて除く。]{#uniq-auto-sort explanation="`uniq` は入力順を保ち、並べ替えません。離れた同じ行は別のグループのままです。"}
::option[隣接する同一行の各グループから 1 行を表示する。]{#uniq-one-per-group .correct explanation="標準の `uniq` は連続する同一行を 1 出力行へまとめます。"}
::option[`reading.txt` から重複行を直接削除する。]{#uniq-edit-file explanation="標準では絞り込んだテキストを stdout へ書き、入力ファイルを編集しません。"}
:::

## 隣接グループを数える

`-c` は、各出力グループの前に連続する入力行数を付けます。

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

同じ行をあらかじめ隣接させていなければ、これは全体の合計ではなく連続長です。

:::single-choice{#uniq-count-groups}
`uniq -c` の数値は何を表しますか？

::option[各入力行の文字数。]{#uniq-character-count explanation="`uniq -c` は文字数を数えません。文字やバイトの合計には `wc` などを使います。"}
::option[各グループにある連続する同一行の数。]{#uniq-consecutive-count .correct explanation="`-c` はまとめた各隣接グループに、その行数を付けます。"}
::option[ファイル内のあらゆる場所にある一致行の総数。]{#uniq-global-count explanation="並べ替えなどで先にまとめなければ、離れた同一行は別のグループになります。"}
:::

## 一意または重複したグループを選ぶ

`-u` は 1 行だけのグループ、`-d` は 2 行以上の各隣接グループから代表 1 行を表示します。

```bash
$ uniq -u reading.txt
magazine
```

```bash
$ uniq -d reading.txt
book
paper
article
```

GNU `uniq -D` は重複グループ内の全行を表示しますが、小文字の `-d` はグループごとに値を 1 回だけ表示します。

:::single-choice{#uniq-only-singletons}
ちょうど 1 回だけ現れる隣接グループだけを表示するコマンドはどれですか？

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="重複と単独の両方を含む全グループを件数付きで表示します。"}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="小文字の `-d` は重複グループを表示するため、逆の選択です。"}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="`-u` は隣接する連続長がちょうど 1 のグループを選びます。"}
:::

:::single-choice{#uniq-one-per-duplicate-group}
複数回現れる各隣接グループにつき 1 行を表示するコマンドはどれですか？

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="`-d` は重複した隣接グループを選び、グループごとに代表 1 行を出力します。"}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="GNU の大文字 `-D` は、代表 1 行だけでなく重複グループに属する全行を表示します。"}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="`-u` は重複ではなく単独のグループを選びます。"}
:::

## 離れた重複をグループ化する

同一行が離れていると別のグループになります。

```plaintext
book
paper
book
paper
article
magazine
article
```

隣が異なるため、`uniq` は何もまとめません。

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

順序を変えてよい場合は、先に並べ替えて同じ完全な行を隣接させます。

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

両段階で一貫したロケールと比較方針を使います。`sort -u reading.txt` なら、1 コマンドで並べ替え、等しいキーごとに 1 行を残せます。

:::single-choice{#uniq-separated-duplicates}
同じ行が `reading.txt` 内に散らばり、出力順を変えてもよい場合、完全な各行を 1 つずつ並べて出力するパイプラインはどれですか？

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="並べ替えで同じ完全な行を隣接させ、`uniq` が各グループを 1 行へまとめます。"}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="離れた同じ行が隣接する前に `uniq` が動くため、その後に並べても重複行が残ることがあります。"}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="既存の隣接グループを数えて出力を制限するだけで、離れた重複を全体でまとめません。"}
:::

入力ファイルがなければ `uniq` は stdin を読むため、`sort` の後で自然に使えます。GNU の `-i` は大文字小文字を無視し、`-f`、`-s`、`-w` は比較領域を飛ばしたり制限したりできます。行の一部で同一性を定義するときだけ使います。

重複のグループ化、集計、絞り込みを練習するには、次のラボを試してください。

1. **[Linux uniq コマンド：重複の絞り込み](https://labex.io/ja/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - `sort` と `uniq` で重複行を特定、絞り込み、分析します。
2. **[Linux sort コマンド：テキストの並べ替え](https://labex.io/ja/labs/linux-linux-sort-command-text-sorting-219196)** - `uniq` の前処理に重要な `sort` を練習します。
3. **[単語数の集計と並べ替え](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - `wc` と `sort` でテキストを分析します。

## まとめ

`uniq` で隣接する同一行のグループを分析できるようになりました。

1. 隣接する各重複グループを 1 行へまとめる。
2. `-c` で連続する出現数を数える。
3. `-u` で単独グループを選ぶ。
4. `-d` または GNU `-D` で重複グループを選ぶ。
5. 離れた重複をまとめる必要がある場合は先に並べ替える。
