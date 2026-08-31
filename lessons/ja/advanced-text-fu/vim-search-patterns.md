---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 4
title: "Vim 検索パターン"
description: "Vim で前方または後方を検索し、パターンの一致を繰り返す、調整する、ハイライトを消す方法を学びます。"
meta_title: "Vim 検索パターン - 高度なテキスト操作"
meta_description: "パターンを使用して Vim で順方向および逆方向の検索を実行する方法を学びます。「n」と「N」で結果を移動し、テキストをすばやく見つけるための Vim 検索テクニックを習得します。"
meta_keywords: "Vim 検索，Vim 検索コマンド，Vim コマンド，Linux テキストエディタ，Vim チュートリアル，Vim ガイド，検索パターン"
---

Vim は現在のカーソル位置からパターンを検索します。ノーマルモードで前方または後方の検索を入力し、その後はパターンを再入力せずに一致箇所を繰り返し移動できます。

## 前方を検索する

ノーマルモードで `/` を入力し、パターンを入力して Enter を押します。Vim はカーソルより後にある次の一致へ移動します。

```vim
/pretty
```

検索には Vim の正規表現構文が使われるため、`.`、`*`、`[`、`\` などの文字は特別な意味を持つことがあります。パターンの残りを very nomagic として扱うには先頭に `\V` を付けるか、特殊文字を意図的にエスケープしてください。

:::single-choice{#vim-search-forward-key}
ノーマルモードから `pretty` の前方検索を始めるコマンドはどれですか？

::option[`?pretty` に続けて Enter]{#vim-backward-pretty explanation="疑問符は、現在のカーソル位置から後方への検索を始めます。"}
::option[`/pretty` に続けて Enter]{#vim-forward-pretty .correct explanation="スラッシュは前方検索を始め、Enter でパターンを確定します。"}
::option[`:pretty` に続けて Enter]{#vim-command-pretty explanation="コロンは Ex コマンド用のコマンドラインモードへ入り、この形の `pretty` は検索として扱われません。"}
:::

## 後方を検索する

`?` を入力し、パターンを入力して Enter を押すと、カーソルより前にある一致へ移動します。

```vim
?pretty
```

これは本質的に「ファイル内の最後の一致」を意味しません。結果は現在のカーソル位置によって決まります。Vim の既定の `wrapscan` 設定では、検索が先頭または末尾で折り返すことがあります。`:set nowrapscan` で折り返しを無効にできます。

:::single-choice{#vim-search-backward-key}
カーソルから前にあるテキストを探すノーマルモードの検索接頭辞はどれですか？

::option[`/`]{#vim-slash-forward explanation="スラッシュは、前にあるテキストではなくカーソルから前方を検索します。"}
::option[`?`]{#vim-question-backward .correct explanation="疑問符は、現在のカーソル位置から後方へのパターン検索を始めます。"}
::option[`:`]{#vim-colon-command explanation="コロンは Ex コマンドラインを開始し、後方検索の接頭辞ではありません。"}
:::

## 検索を繰り返す

どちらの検索を行った後でも、次のキーを使えます。

- `n` を押すと、元の検索方向に繰り返す
- `N` を押すと、反対方向に繰り返す

したがって、`/pretty` の後では `n` が前方、`N` が後方へ移動します。`?pretty` の後では `n` が後方、`N` が前方へ移動します。

:::single-choice{#vim-repeat-backward-search}
`?error` を実行した後、同じ後方へ検索を繰り返すキーはどれですか？

::option[`n`]{#vim-same-question-search .correct explanation="小文字の `n` は直近の検索を元の方向へ繰り返します。この場合は後方です。"}
::option[`N`]{#vim-opposite-question-search explanation="大文字の `N` は元の検索方向を反転するため、`?` 検索の後なら前方へ移動します。"}
::option[`/`]{#vim-new-forward-search explanation="スラッシュは新しい前方検索を始めてパターンを待つため、前の検索を繰り返しません。"}
:::

## カーソル下の単語を検索する

ノーマルモードでカーソルを単語の上に置き、次を使います。

- `*`：その単語全体を前方へ検索する
- `#`：その単語全体を後方へ検索する

これらのコマンドは直近の検索パターンを設定するため、`n` と `N` で検索を続けられます。

:::single-choice{#vim-current-word-forward}
カーソル下の単語全体を前方へ検索するノーマルモードのキーはどれですか？

::option[`#`]{#vim-hash-current-word explanation="ハッシュキーはカーソル下の単語を後方へ検索します。"}
::option[`*`]{#vim-star-current-word .correct explanation="アスタリスクはカーソル下の単語から単語全体のパターンを作り、前方へ検索します。"}
::option[`n`]{#vim-repeat-current-pattern explanation="`n` は既存の検索を繰り返すもので、現在の単語から新しいパターンを作りません。"}
:::

## 大文字と小文字、ハイライトを制御する

Vim のオプションで大文字と小文字の扱いを変更できます。

- `:set ignorecase`：検索で大文字と小文字を区別しない
- `:set smartcase`：`ignorecase` も有効なとき、パターンに大文字があれば大文字と小文字を区別する
- パターン内の `\c`：その検索で大文字と小文字を区別しない
- `\C`：その検索で大文字と小文字を区別する

たとえば `/\cerror` は、現在の大文字と小文字のオプションにかかわらず、`error`、`Error`、`ERROR` に一致します。

検索のハイライトが有効な場合、`:nohlsearch` は検索パターンを削除せず、現在の視覚的なハイライトだけを消します。次の検索や繰り返しで、一致箇所が再びハイライトされます。

:::single-choice{#vim-force-case-insensitive}
現在の設定にかかわらず、`error` の 1 回の Vim 検索で大文字と小文字を区別しないパターンはどれですか？

::option[`/\Cerror`]{#vim-pattern-match-case explanation="大文字の `\C` は大文字と小文字を区別するよう強制するため、逆の動作です。"}
::option[`/:error`]{#vim-pattern-colon-error explanation="このパターン内のコロンはリテラル文字であり、大文字と小文字の扱いを選びません。"}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="`\c` はその検索で大文字と小文字を区別しないため、表記の異なる文字列にも一致します。"}
:::

管理されたファイルで Vim の移動と検索を練習するには、次のハンズオンラボを利用してください。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)**：Vim と Nano でテキストファイルの作成、編集、保存、移動を練習します。

## まとめ

これで、Vim のバッファーを検索し、一致箇所の間を予測どおりに移動できるようになりました。

1. `/` で前方検索、`?` で後方検索を始める。
2. `n` で同じ方向、`N` で反対方向へ検索を繰り返す。
3. `*` または `#` でカーソル下の単語全体を検索する。
4. 1 つのパターンまたはオプションで大文字と小文字の扱いを制御する。
5. 現在の検索パターンを失わず、ハイライトを消す。
