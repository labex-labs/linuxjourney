---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 12
title: "Emacs 編集"
description: "ポイントを移動し、リージョンを有効にして、Emacs のキルリングコマンドでテキストを編集する方法を学びます。"
meta_title: "Emacs 編集 - 高度なテキスト操作術"
meta_description: "この初心者向けガイドで Emacs 編集の基本を習得しましょう。強力な Linux テキストエディタである Emacs でのテキスト移動、カット、ペーストに不可欠なコマンドを学びます。"
meta_keywords: "Emacs, Emacs チュートリアル，Emacs コマンド，テキストエディタ，Linux エディタ，Emacs 移動，初心者 Emacs, Emacs ガイド"
---

Emacs では現在のカーソル位置を**ポイント**と呼びます。移動コマンドはポイントを移し、編集コマンドはその周辺にテキストを挿入、削除、キル、コピー、ヤンクします。以下のキー表記では、`C-` が Control、`M-` が Meta（一般には Alt）を意味します。

## 文字と行を単位に移動する

矢印キーなど、プラットフォームの移動キーも使えることがありますが、Emacs の標準的な移動コマンドは、端末とグラフィカルセッションのどちらでも利用できます。

- `C-f`：前方へ 1 文字移動する
- `C-b`：後方へ 1 文字移動する
- `C-n`：次の行へ移動する
- `C-p`：前の行へ移動する
- `C-a`：行頭へ移動する
- `C-e`：行末へ移動する

:::single-choice{#emacs-edit-next-line} ポイントを次の行へ移動する Emacs のキーはどれですか？

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` は反対方向の前の行へ移動します。"}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="next-line を表す `C-n` は、ポイントを画面上の次の行位置へ下向きに移動します。"}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` は次の行ではなく前方へ 1 文字移動します。"}
:::

## 単語とバッファー境界を単位に移動する

Meta コマンドはより大きな単位を移動します。

- `M-f`：前方へ 1 単語移動する
- `M-b`：後方へ 1 単語移動する
- `M-<`：バッファーの先頭へ移動する
- `M->`：バッファーの末尾へ移動する

多くのキーボードでは Alt が Meta として働きます。その組み合わせが使えない場合、`Esc` に続いて対象のキーを押すと、同等の Meta コマンドを送れることがあります。

:::single-choice{#emacs-edit-buffer-end} ポイントをバッファーの末尾へ移動する Emacs のキーはどれですか？

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` はバッファー全体ではなく現在行の末尾へ移動します。"}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` はバッファーの先頭へ移動します。"}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` はポイントを現在のバッファーの末尾へ移動します。"}
:::

## リージョンを定義する

**マーク**は保存されたバッファー位置です。ポイントとマークの間のテキストを**リージョン**と呼びます。一部の文書で `C-space` と表記される `C-SPC` を押して `set-mark-command` を実行し、その後ポイントを移動すると、アクティブなリージョンが広がります。

端末では `C-SPC` が `C-@` として符号化されることがあります。ハイライト表示は transient-mark の設定によって異なりますが、それでもポイントとマークがリージョンを定義します。

:::single-choice{#emacs-edit-set-mark} ポイント位置にマークを置き、リージョンの定義を始めるキーはどれですか？

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` はすでに定義されたリージョンをキルするもので、最初にマークを設定するコマンドではありません。"}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` はキルリングからテキストを挿入し、選択を始めません。"}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` がマークを置き、その後の移動によってマークとポイント間のリージョンが変わります。"}
:::

## リージョンをキルまたはコピーする

Emacs はキルまたはコピーしたテキストを**キルリング**へ保存します。

- `C-w`：アクティブなリージョンを削除し、キルリングへ追加する
- `M-w`：アクティブなリージョンを削除せず、キルリングへコピーする
- `C-k`：ポイントから行末までをキルする。繰り返すと改行も含められる

キルは、削除したテキストを後でヤンクできるよう保持するため、通常の削除以上の操作です。

:::single-choice{#emacs-edit-copy-region} アクティブなリージョンを削除せず、キルリングへコピーするキーはどれですか？

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`M-w` に割り当てられた `kill-ring-save` は、リージョンを削除せずコピーします。"}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` はリージョンをキルリングへ保存しながら削除します。"}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` は選択済みリージョンをそのままコピーせず、行末へ向かうテキストをキルします。"}
:::

## キルリングからヤンクする

`C-y` で直近のキルリングエントリをポイント位置へヤンクします。ヤンク直後の `M-y` は、挿入したテキストを以前のキルリングエントリへ置き換えます。`M-y` を繰り返すとエントリを順番に切り替えます。

```text
C-y
M-y
```

`C-y` の後に無関係なコマンドを実行すると、`M-y` は同じ yank-pop の文脈では動作しなくなります。

:::single-choice{#emacs-edit-yank-latest} 直近のキルリングエントリをポイント位置へ挿入するキーはどれですか？

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`C-y` に割り当てられた `yank` が、最新のキルリングテキストを現在のバッファーへ挿入します。"}
::option[`M-y`]{#emacs-edit-yank-pop explanation="通常、`M-y` は直前にヤンクしたエントリを以前のものへ置き換え、先行するヤンクの文脈に依存します。"}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` はポイントの後の文字を削除し、キルリングのテキストを取得しません。"}
:::

`*scratch*` または使い捨てのファイルで練習してください。ポイントを移動してマークを設定し、1 つのリージョンをコピーし、別のリージョンをキルして、両方をヤンクで戻します。結果を残す価値がある場合にだけ保存してください。

## まとめ

これで、ポイント、マーク、キルリングを使って Emacs のテキストを移動し、並べ替えられるようになりました。

1. Control コマンドで文字または行を単位に移動する。
2. Meta コマンドで単語またはバッファー境界を単位に移動する。
3. `C-SPC` でマークを設定し、リージョンを定義する。
4. `C-w` でキルし、`M-w` でコピーする。
5. `C-y` でヤンクし、直後に `M-y` でエントリを切り替える。
