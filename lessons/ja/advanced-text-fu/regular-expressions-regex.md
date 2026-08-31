---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 1
title: "正規表現 (Regular Expressions)"
description: "アンカー、文字集合、繰り返し、正規表現の種類が、テキストのパターンマッチングをどのように制御するかを学びます。"
meta_title: "正規表現 (regex) - 高度なテキスト操作術"
meta_description: "正規表現 (regex) のガイドで Linux の基本を習得しましょう。grep を使ったパターンマッチング（^, $, []などの構文）を学びます。これは Linux のテキスト操作を学びスキルアップする最良の方法の一つです。"
meta_keywords: "正規表現 linux, regex, linux の基本，パターンマッチング，grep, テキスト処理，linux 学習，linux チュートリアル，最速で linux 上級へ"
---

**regex** と略される正規表現は、テキストのパターンを記述します。`grep`、`sed`、`awk` などのツールで正規表現を使えますが、対応する構文は異なる場合があるため、必ずツールと正規表現の種類を確認してください。

GNU `grep` は、既定で基本正規表現（BRE）を使い、`-E` を指定すると拡張正規表現（ERE）を使います。このレッスンでは、まず両方に共通する構文を紹介し、その後で一般的な ERE の追加機能を説明します。

例では次の入力を使います。

```text
sally sells seashells
by the seashore
```

## リテラルテキストに一致させる

通常の文字の多くは、その文字自体に一致します。パターン `seashells` は、その正確な並びをどこかに含む行を選びます。

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

マッチングツールが受け取る前にシェルが展開または分割しないよう、正規表現のパターンは引用符で囲んでください。正規表現はシェルのパス名展開とも異なります。正規表現の `*` は直前の要素を繰り返しますが、シェルの glob における `*` は、それ自体がパス名の文字列に一致するワイルドカードです。

:::single-choice{#regex-versus-shell-star}
`ab*` のような正規表現で、`*` は何をしますか？

::option[現在のディレクトリにある任意のファイル名に一致します。]{#regex-shell-glob explanation="これはコマンド文脈でのシェルのパス名展開であり、正規表現内の `*` の意味ではありません。"}
::option[直前の `b` を 0 回以上繰り返します。]{#regex-repeat-b .correct explanation="正規表現の量指定子は直前の要素に適用されるため、`ab*` は `a`、`ab`、`abb` などに一致します。"}
::option[文字列 `ab` 全体をちょうど 2 回繰り返します。]{#regex-repeat-ab-twice explanation="アスタリスクは直前の要素だけに適用され、文字列全体をちょうど 2 回ではなく 0 回以上繰り返します。"}
:::

## 一致位置を固定する

ブラケット式の外で、パターン先頭の `^` は、一致位置を行頭に固定します。

```plaintext
^by
```

`$` アンカーは行末に一致します。

```plaintext
seashore$
```

行全体をパターンに一致させる場合は、両方のアンカーを組み合わせます。

```text
^by the seashore$
```

:::single-choice{#regex-complete-line}
行全体が `by the seashore` である場合だけ一致するパターンはどれですか？

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="キャレットは行頭からの一致を要求し、ドル記号は行末で終わることを要求します。"}
::option[`by the seashore`]{#regex-unanchored-line explanation="アンカーがないため、前後に別のテキストを含む長い行の途中にも一致します。"}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="この意図では、末尾アンカーを一致対象テキストの前に、先頭アンカーを後ろに置くことはできません。"}
:::

## 1 文字に一致させる

通常の行単位の正規表現モードでは、ドットが任意の 1 文字に一致します。

```plaintext
b.
```

これは `by` に一致しますが、`ba` や `b7` にも一致します。`b` の後に 1 文字必要なので、`b` だけには一致しません。リテラルのピリオドには `\.` とエスケープするか、適切なブラケット式に入れてください。

:::single-choice{#regex-dot-character}
行全体を対象とするパターン `^b.$` に一致しない文字列はどれですか？

::option[`by`]{#regex-dot-by explanation="ドットが `y` に一致するため、2 文字の行はパターンを満たします。"}
::option[`b`]{#regex-dot-b .correct explanation="ドットは `b` の後に 1 文字を要求しますが、この文字列はそこで終わっています。"}
::option[`b7`]{#regex-dot-b7 explanation="ドットが数字の `7` に一致するため、2 文字の行はパターンを満たします。"}
:::

## ブラケット式を使う

ブラケット式は、指定した集合から 1 文字に一致します。

```plaintext
s[ae]lls
```

これは、その位置に `a` または `e` がある `salls` または `sells` に一致します。

`^` が `[` の直後の最初の文字なら、集合を否定します。

```plaintext
s[^e]lls
```

最初の `s` の次の文字が `e` 以外でなければならないため、`salls` には一致しますが `sells` には一致しません。

:::single-choice{#regex-negated-bracket}
`[^e]` は何に一致しますか？

::option[`e` 以外のちょうど 1 文字。]{#regex-not-e .correct explanation="ブラケット内先頭のキャレットは一覧の集合を補集合にしますが、ブラケット式が消費するのは 1 文字です。"}
::option[行頭の後に続く `e`。]{#regex-caret-e-anchor explanation="ブラケット式内先頭のキャレットは、行頭に固定するのではなく集合を否定します。"}
::option[文字 `e` の 0 回以上の繰り返し。]{#regex-repeat-e explanation="繰り返しには `*` などの量指定子が必要で、このブラケット式は `e` 以外の 1 文字に一致します。"}
:::

範囲を使うと、両端の間にある文字を表せます。

```plaintext
d[a-c]g
```

これは `dag`、`dbg`、`dcg` に一致します。範囲の動作はロケールの照合順序に依存することがあります。`[[:lower:]]`、`[[:upper:]]`、`[[:digit:]]` などの文字クラスの方が、意図を明確に表せることがよくあります。

## パターンを繰り返して組み合わせる

BRE と ERE のどちらでも、`*` は直前の要素を 0 回以上繰り返すことを意味します。

```text
seashells*
```

これは `seashell` の後に `s` が 0 個以上続く文字列に一致します。`grep -E` の ERE モードで使える一般的な演算子には次のものがあります。

- `+`：1 回以上の繰り返し
- `?`：0 回または 1 回の繰り返し
- `|`：左側または右側の式
- `(...)`：式のグループ化

たとえば、次のように使います。

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

これは、行全体が `cat`、`cats`、`dog`、`dogs` のいずれかである行を選びます。BRE モードではこれらの演算子のエスケープ規則が異なるため、種類を確認せずにパターンをコピーしてはいけません。

:::single-choice{#regex-extended-alternation}
パターン `^(cat|dog)s?$` で拡張正規表現の構文を有効にするコマンドはどれですか？

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` はすべての正規表現演算子をリテラルテキストとして扱うため、グループ化、選択、任意の繰り返しが無効になります。"}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` は拡張正規表現を選び、ここで示したグループ化、選択、任意の `s` を有効にします。"}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="既定の grep は BRE を使うため、エスケープしていないグループ化と選択の文字は、意図した ERE の意味を持ちません。"}
:::

Linux のテキストツールによる正規表現の選択を練習するには、次のハンズオンラボを利用してください。

1. **[Linux で grep を使用してテキストを検索する](https://labex.io/ja/labs/comptia-search-text-with-grep-in-linux-590841)**：`grep` でファイル内のテキストを検索し、基本検索、行番号表示、`^` と `$` による位置指定、基本および拡張正規表現を使った複雑なパターンマッチングを練習します。
2. **[テキスト処理と正規表現](https://labex.io/ja/labs/linux-text-processing-and-regular-expressions-18003)**：強力なテキスト処理ツール grep、sed、awk と、効率的なテキスト操作やパターンマッチングのための正規表現を学びます。
3. **[メールアドレスと数字の抽出](https://labex.io/ja/labs/linux-extracting-mails-and-numbers-17991)**：grep と正規表現を使ってファイルからメールアドレスと数字を抽出し、Linux の重要なテキスト処理スキルを練習します。

## まとめ

これで、行単位の基本的な正規表現を読み、作成できるようになりました。

1. 正規表現演算子とシェルのパス名ワイルドカードを区別する。
2. 一致位置を行頭または行末に固定する。
3. ドットまたはブラケット式で 1 文字に一致させる。
4. 集合を否定し、ロケールを考慮した文字クラスを使う。
5. BRE または ERE の構文を意図的に選ぶ。
