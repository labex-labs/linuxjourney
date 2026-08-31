---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 9
title: "Emacs"
description: "Emacs を起動し、キー表記を読み、バッファー、ウィンドウ、フレームを区別する方法を学びます。"
meta_title: "Emacs - 高度なテキスト操作"
meta_description: "Linux 用の強力で拡張可能なテキストエディタである Emacs を学びましょう。Emacs のバッファと基本的な使い方を理解しましょう。今日から Emacs の旅を始めましょう！"
meta_keywords: "Emacs, Linux テキストエディタ，Emacs チュートリアル，Emacs バッファ，Linux コマンド，初心者，ガイド"
---

GNU Emacs は、Emacs Lisp で動作をカスタマイズできる拡張可能なテキストエディタです。プレーンテキスト編集、プログラミング用モード、ファイルとバッファーの管理、多数のオプションパッケージに対応します。すべての拡張を導入しなくても、中核となる編集コマンドを学べます。

## Emacs を確認して起動する

Emacs がインストール済みだと決めつけず、シェルでどのように解決されるか確認します。

```bash
$ command -v emacs
/usr/bin/emacs
```

通常の表示選択で Emacs を起動します。

```bash
$ emacs
```

グラフィカルセッションでは、グラフィカルなフレームが作成されることがあります。現在の端末内で Emacs を実行する場合は、no window system の略である `-nw` を使います。

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start}
グラフィカルなウィンドウシステムを使わず、現在の端末内で Emacs を起動するコマンドはどれですか？

::option[`emacs -w`]{#emacs-window-option explanation="これは、ここで紹介した no-window-system の形式ではありません。"}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="`-nw` オプションは、グラフィカルなウィンドウシステムを使わず端末上で実行するよう Emacs に指示します。"}
::option[`command -v emacs`]{#emacs-check-only explanation="これはコマンド解決を確認するだけで、エディタは起動しません。"}
:::

## ファイルを開く

Emacs の起動時にファイルを開くには、パス名を渡します。

```bash
$ emacs notes.txt
```

ファイルが存在すれば、Emacs はバッファーへ読み込みます。存在しなければ、そのパス名に関連付けた新しいバッファーを作ります。ファイルが実際に作成されるのは、保存に成功した後です。書き込みが成功するかどうかは、引き続きファイルシステムのパーミッションによって決まります。

:::single-choice{#emacs-open-file-buffer}
まだ存在しない `notes.txt` に対して `emacs notes.txt` を実行すると、通常どうなりますか？

::option[そのパス名に関連付けた新しいバッファーを開きます。]{#emacs-new-file-buffer .correct explanation="バッファーに `notes.txt` 用の新しいテキストを保持でき、実際のファイル作成は保存まで延期されます。"}
::option[エディタの起動前にディスク上へファイルを作成します。]{#emacs-immediate-file explanation="保存に成功するまでディスクファイルを作らず、新しいバッファーをパス名へ関連付けられます。"}
::option[開くファイルはすべて既存でなければならないため、起動を拒否します。]{#emacs-refuse-new-file explanation="Emacs は、存在しないパス名に関連付けたバッファーで新しいファイルを作成できます。"}
:::

## バッファー、ウィンドウ、フレームを理解する

Emacs では、関連しながらも異なるオブジェクトを使います。

- **バッファー**：テキストまたはほかのエディタ状態を保持する。開いたファイルの内容はバッファー内にある
- **ウィンドウ**：Emacs フレーム内でバッファーを表示する領域
- **フレーム**：グラフィカルフレームや端末フレームなど、Emacs の最上位の表示

複数のバッファーが見えない状態で存在でき、2 つのウィンドウに同じバッファーを表示することもできます。ウィンドウを閉じても、そのバッファーが破棄されたりファイルが削除されたりするとは限りません。

:::single-choice{#emacs-buffer-definition}
Emacs のバッファーとは何ですか？

::option[最上位のグラフィカルアプリケーションフレーム。]{#emacs-buffer-frame explanation="フレームが最上位の表示オブジェクトであり、バッファーはエディタの内容や状態を保持します。"}
::option[編集可能なテキストやほかのエディタ状態を保持するオブジェクト。]{#emacs-buffer-content .correct explanation="開いたファイルの内容と多くのファイル以外の表示は、Emacs のバッファーに置かれます。"}
::option[以前のコマンドを含むシェル履歴ファイル。]{#emacs-buffer-history explanation="シェル履歴は Emacs のバッファーストレージとは別です。"}
:::

## Emacs のキー表記を読む

Emacs の文書では短い表記を使います。

- `C-x`：Control を押しながら `x` を押す
- `M-x`：Meta を押しながら `x` を押す。現代の端末やデスクトップでは、一般に Alt が Meta として働く
- `C-x C-f`：Control+x、続いて Control+f と押すキーシーケンス

端末によっては一部のキーが横取りまたは再割り当てされることがあります。`Esc` に続いてキーを押す操作が、Meta の組み合わせの代わりになることもあります。

:::single-choice{#emacs-key-sequence-notation}
`C-x C-f` と表記された Emacs のキーシーケンスは、どのように入力しますか？

::option[Control を押しながら `x`、次に Control を押しながら `f` を押します。]{#emacs-control-x-f .correct explanation="各 `C-` 接頭辞は直後のキーに適用され、2 つの組み合わせを順番に入力します。"}
::option[リテラル文字列 `C-x C-f` をバッファーへ入力します。]{#emacs-literal-key-text explanation="この表記は、挿入するテキストではなくコントロールキーのイベントを表します。"}
::option[Control、`x`、`f` を 1 つの組み合わせとして同時に押します。]{#emacs-simultaneous-x-f explanation="この表記は 3 キーの 1 回の組み合わせではなく、連続する 2 つの組み合わせです。"}
:::

## 組み込みチュートリアルを始める

Emacs 内で `C-h t` と入力すると、対話型チュートリアルが開きます。安全な練習用バッファーで、移動、挿入、保存、終了を学べます。`C-h` はヘルプの接頭辞で、`C-h C-h` はヘルプの使い方に関するヘルプを表示します。

Emacs がメニューやウェルカムバッファーを表示しても、重要なファイルで試行錯誤するより、チュートリアルの方が体系的な出発点になります。

:::single-choice{#emacs-open-tutorial}
Emacs の組み込みチュートリアルを開くキーシーケンスはどれですか？

::option[`C-x C-s`]{#emacs-save-buffer explanation="このシーケンスは現在のバッファーを保存し、チュートリアルは開きません。"}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="このシーケンスはレッスンではなく、Emacs の終了を始めます。"}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="ヘルプ接頭辞 `C-h` に `t` を続けると、Emacs チュートリアルが始まります。"}
:::

## まとめ

これで Emacs を起動し、その基本的なインターフェース概念を解釈できるようになりました。

1. `emacs` コマンドが利用できるか確認する。
2. `-nw` でグラフィカル表示または端末での動作を選ぶ。
3. 既存または新しいパス名をバッファーで開く。
4. バッファー、ウィンドウ、フレームを区別する。
5. キー表記を読み、組み込みチュートリアルを開く。
