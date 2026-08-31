---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "ja"
order_index: 17
title: "whatis コマンド"
description: "簡潔なマニュアルページの説明を取得し、そのセクション番号を解釈する方法を学びます。"
meta_title: "whatis - コマンドライン"
meta_description: "Linuxのwhatisコマンドを学び、manページから一行のコマンド説明を取得し、複数のマニュアルセクションを理解する方法を例とともに解説します。"
meta_keywords: "whatis コマンド, linux whatis, コマンド説明 linux, manページ概要, コマンドラインヘルプ, apropos"
---

コマンド名は覚えていても用途を忘れた場合、`whatis` はマニュアルページのデータベースから短い説明を表示します。

## 正確な名前を検索する

`whatis` に 1 つ以上の正確なトピック名を渡します。各結果は、インストール済みマニュアルページに記録された `NAME` セクションから得られます。

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

出力は説明であり、コマンドオプションや使用例の一覧ではありません。詳しい情報が必要な場合は `man cat` または `cat --help` を使います。

:::single-choice{#describe-known-command}
`cat` という名前を知っており、マニュアルページの 1 行説明を見たい場合、どのコマンドを実行しますか？

::option[`man cat`]{#manual-cat explanation="`man cat` は完全なマニュアルページを開き、要求された 1 行の説明より多くの情報を提供します。"}
::option[`apropos cat`]{#apropos-cat explanation="`apropos` は説明をキーワード検索し、多数の関連トピックを返すことがあります。正確な名前の検索より範囲が広い操作です。"}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis` は正確なトピック名を検索し、マニュアルデータベースから簡潔な説明を表示します。"}
:::

## セクション番号を読む

同じトピックに複数セクションのマニュアルページがある場合、`whatis` は複数の結果を表示できます。

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

括弧内の番号がマニュアルセクションです。`passwd(1)` はユーザーコマンド、`passwd(5)` はファイル形式を説明します。`man 1 passwd` または `man 5 passwd` で明示的に開けます。

:::single-choice{#interpret-whatis-section}
出力 `passwd (5) - the password file` で、`(5)` は何を識別しますか？

::option[`passwd` コマンドが受け付ける 5 番目のオプション。]{#fifth-option explanation="番号はオプションの位置ではありません。オプションは選択したマニュアルページ内で説明されます。"}
::option[ファイル形式ページを含むマニュアルセクション。]{#section-five .correct explanation="セクション 5 はファイル形式と慣例に使われるため、`passwd(5)` はそのマニュアルセクションを指します。"}
::option[`passwd` という名前を共有する 5 つのマニュアルページ。]{#five-pages explanation="複数の結果が存在することはありますが、括弧内の値はページ数ではなく 1 つのセクションを識別します。"}
:::

## `whatis`、`man`、`apropos` を使い分ける

- `whatis NAME`：正確なマニュアルトピック名の簡潔な説明を表示する
- `man NAME`：完全なマニュアルページを開く
- `apropos KEYWORD`：マニュアルページの名前と説明からキーワードを検索する

例を示します。

```bash
$ apropos password
```

作業内容は分かるもののコマンド名が分からない場合は `apropos`、名前を知っている場合は `whatis` を使います。

:::single-choice{#search-by-purpose}
コマンド名は分かりませんが、マニュアルの説明からキーワード `password` を検索したい場合、どのコマンドが適していますか？

::option[`apropos password`]{#apropos-password .correct explanation="`apropos` はマニュアルページの名前と説明からキーワードを検索し、関連トピックを見つける助けになります。"}
::option[`whatis password`]{#exact-password explanation="`whatis` は `password` という正確なマニュアルトピックを探し、一般的なキーワード検索は行いません。"}
::option[`man password`]{#manual-password explanation="`man` はそのトピック名のページを開こうとし、要求された説明検索は行いません。"}
:::

## 説明が表示されない場合

`whatis` が該当なしと報告する場合、トピックにインストール済みマニュアルページがないか、マニュアルデータベースが古い可能性があります。その名前の実行可能ファイル、エイリアス、関数、組み込みコマンドが存在しない証明にはなりません。`type NAME` で Bash がコマンド名をどう解決するか調べ、適切なヘルプ情報源を選んでください。

:::single-choice{#whatis-versus-type}
`whatis deploy` でマニュアルの説明が見つかりません。Bash が `deploy` をエイリアス、関数、組み込みコマンド、実行可能ファイルのどれとして解決するか確認するコマンドはどれですか？

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="マニュアルデータベースへの問い合わせ方法を変えても、Bash の全エイリアス、関数、組み込みコマンド、パス解決は表示しません。"}
::option[`man 5 deploy`]{#manual-five-deploy explanation="これはセクション 5 のページを開こうとし、Bash がコマンド名をどう解決するかは判断しません。"}
::option[`type deploy`]{#resolve-deploy .correct explanation="Bash の `type` は、マニュアル説明の有無にかかわらず、現在のシェルがコマンド名をどう解決するか報告します。"}
:::

## まとめ

これでマニュアルデータベースから簡潔な説明を取得し、解釈できるようになりました。

1. `whatis` で正確なトピックを検索する。
2. 括弧内に示されるマニュアルセクションを読む。
3. 完全なページが必要なら `man` を使う。
4. 名前ではなくキーワードを知っている場合は `apropos` を使う。
