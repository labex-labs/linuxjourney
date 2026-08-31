---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 11
title: "Emacs バッファ操作"
description: "Emacs のバッファーを切り替えて破棄し、表示ウィンドウを分割、選択、閉じる方法を学びます。"
meta_title: "Emacs バッファ操作 - 高度なテキスト操作術"
meta_description: "Emacs のバッファ操作に関する包括的なガイド。必須の Emacs コマンドを使って、効率的にバッファを切り替え、ウィンドウを分割し、ワークフローを管理する方法を学びましょう。emacs switch buffer コマンドを習得し、テキスト編集スキルを向上させましょう。"
meta_keywords: "emacs ナビゲーション，emacs バッファ切り替え，emacs バッファ管理，emacs コマンド，C-x b, C-x k, C-x 2, テキストエディタ，linux"
---

Emacs のバッファーはテキストやエディタ状態を保持し、ウィンドウはバッファーを表示します。バッファーは見えない状態でも存在でき、複数のウィンドウに 1 つのバッファーを表示することもできます。一方を管理しても、もう一方が自動的に管理されるわけではありません。

## バッファーを切り替える

`switch-to-buffer` を実行する `C-x b` でバッファー名を選び、現在のウィンドウに表示します。

```text
C-x b
```

ミニバッファーでは既存の名前を補完できます。新しい名前を入力すると、その名前を持つファイル以外のバッファーを作成できますが、ファイルのパス名を開く操作ではありません。

既定では、`C-x Right` が `next-buffer`、`C-x Left` が `previous-buffer` を実行し、選択中のウィンドウでバッファーを順番に切り替えます。

:::single-choice{#emacs-switch-buffer-key}
現在のウィンドウに表示するバッファー名の入力を求めるキーシーケンスはどれですか？

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="これはファイルのパス名を求めて開くため、既存のバッファーを名前で選ぶ操作とは異なります。"}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` はバッファー名を読み、そのバッファーを選択中のウィンドウに表示します。"}
::option[`C-x k`]{#emacs-buffer-kill explanation="これは選択中のウィンドウをバッファーへ切り替えず、バッファーを破棄するか尋ねます。"}
:::

## 選択中のウィンドウを分割する

`C-x 2` で選択中のウィンドウを上下に分割します。

```text
C-x 2
```

`C-x 3` で左右に分割します。

```text
C-x 3
```

新しいウィンドウには、初めは同じバッファーが表示されることがよくあります。各ウィンドウで個別にバッファーを切り替えられます。

:::single-choice{#emacs-split-side-by-side}
選択中の Emacs ウィンドウを左右に分割するキーシーケンスはどれですか？

::option[`C-x 1`]{#emacs-window-one explanation="これはほかのウィンドウを削除し、選択中のウィンドウをフレーム内の唯一のウィンドウにします。"}
::option[`C-x 2`]{#emacs-window-below explanation="これは左右ではなく上下のウィンドウを作ります。"}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`C-x 3` に割り当てられた `split-window-right` が、左右のウィンドウを作ります。"}
:::

## ウィンドウを選択して閉じる

`other-window` を実行する `C-x o` で、次のウィンドウを選びます。

```text
C-x o
```

ウィンドウの表示を削除するには次を使います。

- `C-x 0`：選択中のウィンドウを削除する
- `C-x 1`：現在のフレーム内にあるほかのウィンドウを削除する

通常、ウィンドウを削除しても、表示していたバッファーは残ります。そのバッファーを別のウィンドウに再表示できます。

:::single-choice{#emacs-select-other-window}
ポイントとキーボードフォーカスを別の Emacs ウィンドウへ移すキーシーケンスはどれですか？

::option[`C-x 0`]{#emacs-delete-selected-window explanation="これは別のウィンドウへフォーカスを移さず、選択中のウィンドウを削除します。"}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` はフレーム内の別のウィンドウへ選択を切り替えます。"}
::option[`C-x b`]{#emacs-switch-in-window explanation="これは選択中のウィンドウに表示するバッファーを変えますが、選択するウィンドウは変えません。"}
:::

:::single-choice{#emacs-keep-one-window}
選択中のウィンドウを残し、フレーム内のほかのウィンドウを削除するキーシーケンスはどれですか？

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` は、選択中のウィンドウをフレーム内の唯一のウィンドウにします。"}
::option[`C-x 0`]{#emacs-delete-current-window explanation="これは選択中のウィンドウを残さず、そのウィンドウ自体を削除します。"}
::option[`C-x 2`]{#emacs-add-lower-window explanation="これはフレームを 1 ウィンドウに減らさず、別のウィンドウを追加します。"}
:::

## バッファーを破棄する

`kill-buffer` を実行する `C-x k` で、Emacs から削除するバッファーを選びます。

```text
C-x k
```

既定の選択は現在のバッファーです。ファイルバッファーに未保存の変更がある場合、Emacs は破棄前に警告します。プロンプトをよく読んでください。変更済みバッファーを破棄すると、編集内容を失う可能性があります。

バッファーの破棄とウィンドウの削除は異なります。表示中のバッファーを破棄すると、Emacs は各ウィンドウに別のバッファーを表示します。一方、ウィンドウを削除しても、そのバッファーはそのまま残せます。

:::single-choice{#emacs-kill-buffer-key}
Emacs のバッファーを破棄するか尋ねるキーシーケンスはどれですか？

::option[`C-x 0`]{#emacs-kill-window-only explanation="これはウィンドウ表示を削除しますが、通常バッファーは残します。"}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` は、必要な変更済みバッファーの確認後、選択したバッファーを Emacs から削除します。"}
::option[`C-x b`]{#emacs-kill-switch explanation="これは現在のウィンドウを名前付きバッファーへ切り替え、破棄はしません。"}
:::

これらのコマンドは `*scratch*` と使い捨てのバッファーで練習してください。ファイルバッファーを破棄する前に、変更済み表示が未保存の作業を示していないか確認します。

## まとめ

これで、Emacs が保持するものと各ウィンドウが表示するものを管理できるようになりました。

1. `C-x b` で選択中のウィンドウのバッファーを切り替える。
2. `C-x 2` で下、`C-x 3` で右に分割する。
3. `C-x o` で別のウィンドウを選択する。
4. `C-x 0` または `C-x 1` でウィンドウ表示を削除する。
5. 未保存の変更を確認してから、`C-x k` でバッファーを破棄する。
