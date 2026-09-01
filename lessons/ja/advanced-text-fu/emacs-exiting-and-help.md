---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 13
title: "Emacs の終了とヘルプ"
description: "Emacs を安全に終了し、処理中のコマンドを取り消し、ヘルプを調べ、変更を取り消す方法を学びます。"
meta_title: "Emacs の終了とヘルプ - 高度なテキスト操作"
meta_description: "Emacs の終了コマンドとヘルプへのアクセス方法を学びましょう。この初心者向けチュートリアルで、基本的な Emacs のナビゲーションと元に戻す機能を理解します。"
meta_keywords: "Emacs 終了，Emacs ヘルプ，Emacs 元に戻す，Emacs チュートリアル，Linux テキストエディタ，初心者ガイド"
---

Emacs には、キー、関数、変数、有効なモードに応じたヘルプがあります。また、終了時には変更済みのファイルバッファーを保護し、それぞれを書き込むかどうか選ぶ機会を与えます。

## Emacs を終了する

`save-buffers-kill-terminal` を実行する `C-x C-c` で、Emacs セッションまたは端末接続の終了を要求します。

```text
C-x C-c
```

Emacs は、関連する変更済みのファイルバッファーを確認し、保存するか尋ねます。各バッファー名を読み、意図的に回答してください。動作中のプロセスについて尋ねられることもあります。決める前に作業を確認する必要があれば、終了を取り消します。

`emacsclient` のワークフローや Emacs サーバーでは、フレームとサーバーの正確な動作が異なる場合があります。それでも、変更済みバッファーのプロンプトには十分注意してください。

:::single-choice{#emacs-exit-key} 通常の Emacs 終了を要求し、変更済みバッファーを確認するキーシーケンスはどれですか？

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="これは選択した 1 つのバッファーを破棄するもので、Emacs セッションの終了は要求しません。"}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="これは Emacs を閉じず、処理中のコマンドまたはプロンプトを取り消します。"}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="これは、関連する未保存の作業への確認を含む、通常のバッファー保存と終了の手順を実行します。"}
:::

## ヘルプディスパッチャーを開く

標準のヘルプ接頭辞は `C-h` です。help for help を実行する `C-h C-h` で、利用できるヘルプコマンドの案内を表示します。

```text
C-h C-h
```

2 番目のキーで、必要なヘルプの種類を選びます。

:::single-choice{#emacs-help-for-help} Emacs のヘルプシステムの使い方を説明するキーシーケンスはどれですか？

::option[`C-h C-h`]{#emacs-help-help .correct explanation="ヘルプ接頭辞にもう一度 `C-h` を続けると、ヘルプディスパッチャー自体に関するヘルプが開きます。"}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="これは、ここで紹介した help-for-help のシーケンスではありません。"}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="これは広範なヘルプメニューを説明せず、チュートリアルを直接開きます。"}
:::

## キーとエディタ状態を説明する

便利なヘルプコマンドには次のものがあります。

- `C-h k KEY`：キーシーケンスが実行する内容を説明する
- `C-h f FUNCTION`：Emacs Lisp 関数を説明する
- `C-h v VARIABLE`：Emacs Lisp 変数を説明する
- `C-h m`：現在のメジャーモードとマイナーモードを説明する
- `C-h t`：対話型チュートリアルを開く

たとえば `C-h k C-x C-s` と入力すると、save-buffer のキーバインドに関する文書を確認できます。

:::single-choice{#emacs-describe-key} `C-x C-s` の動作を調べたい場合、そのキーシーケンスの前にどのヘルプ接頭辞を入力しますか？

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` はキーシーケンスを待ち、割り当てられたコマンドを説明します。"}
::option[`C-h f`]{#emacs-describe-function explanation="これはキーシーケンスからバインドを調べず、関数名の入力を求めます。"}
::option[`C-h v`]{#emacs-describe-variable explanation="これは変数名の入力を求め、キーバインドは調べません。"}
:::

## 処理中のコマンドを取り消す

プロンプト、入力途中のキーシーケンス、インクリメンタル検索、そのほか取り消したいコマンドから抜けられない場合は、`keyboard-quit` に割り当てられた `C-g` を使います。

```text
C-g
```

すでに行われたバッファー変更を取り消したり、Emacs を終了したりするものではありません。現在のやり取りを止め、可能な場合は通常の編集へ制御を戻します。

:::single-choice{#emacs-cancel-pending-command} 通常、現在の Emacs プロンプトまたは処理中のコマンドを取り消すキーはどれですか？

::option[`C-x C-c`]{#emacs-cancel-exit explanation="これは現在のプロンプトだけを取り消さず、Emacs の終了手順を始めます。"}
::option[`C-y`]{#emacs-cancel-yank explanation="これはキルリングからテキストをヤンクし、コマンドを取り消しません。"}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` は現在のコマンド操作を中断し、Emacs へ制御を戻します。"}
:::

## バッファー変更を取り消す

一般的な Emacs 設定では、`C-/`、`C-_`、`C-x u` のいずれかで undo を実行します。

```text
C-/
```

取り消しコマンドを繰り返すと、最近のバッファー変更を遡ります。カーソル移動だけなら、通常はバッファー変更ではありません。Emacs のバージョンや設定によっては `undo-redo` や高度な履歴ツールを利用できます。実際の取り消しとやり直しのキーバインドに `C-h k` を使い、ローカルの動作を確認してください。

:::single-choice{#emacs-undo-change} 最近の Emacs バッファー変更を取り消す標準的なキーバインドはどれですか？

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` は標準的な undo のキーバインドで、一般的な設定では `C-_` と `C-x u` も使えます。"}
::option[`C-x C-s`]{#emacs-undo-save explanation="これは undo 履歴をたどらず、現在のバッファーを保存します。"}
::option[`C-w`]{#emacs-undo-kill explanation="これはアクティブなリージョンをキルして別の変更を加え、変更を取り消しません。"}
:::

`*scratch*` を開き、使い捨ての変更を加えて undo を使い、`C-h k` で不明なキーを調べ、`C-g` でミニバッファーのプロンプトを取り消してから通常どおり終了する練習をしてください。

## まとめ

これで、未保存の作業を無視せず、ヘルプを利用して Emacs を終了できるようになりました。

1. `C-x C-c` で変更済みバッファーの確認を経て終了する。
2. `C-h C-h` で help for help を開く。
3. キー、関数、変数、有効なモードを説明するヘルプを使う。
4. `C-g` で処理中のコマンドを取り消す。
5. 確認済みのローカルキーバインドで最近のバッファー変更を取り消す。
