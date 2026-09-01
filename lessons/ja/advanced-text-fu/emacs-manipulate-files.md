---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 10
title: "Emacs ファイル操作"
description: "Emacs でファイルを開く、保存する、別名で保存する、ディスクから読み直す、ファイルバッファーを確認する方法を学びます。"
meta_title: "Emacs ファイル操作 - 高度なテキスト操作"
meta_description: "Emacs のファイル操作を学びましょう：C-x C-s、C-x C-w、C-x C-f コマンドを使用してファイルを保存、名前を付けて保存、開く方法を習得します。Emacs の必須ファイル操作をマスターしましょう！"
meta_keywords: "Emacs, Emacs ファイル保存，Emacs ファイルを開く，Emacs チュートリアル，Linux コマンド，初心者 Emacs, Emacs ガイド"
---

Emacs はファイルをバッファーで開きます。編集ではまずバッファーが変わり、保存すると現在の内容が関連付けられたパス名へ書き込まれます。パーミッション、競合するディスク上の変更、そのほかのエラーで書き込みに失敗することがあるため、ミニバッファーのメッセージを読んでください。

## ファイルを開く

`find-file` を実行する `C-x C-f` を使い、ミニバッファーへパス名を入力して Enter を押します。

```text
C-x C-f
```

Emacs は、読み取り可能な既存ファイルをバッファーで開きます。パス名が存在しない場合は、新しいファイルを開くバッファーを準備します。後者の場合、保存に成功するまでディスク上にファイルは存在しません。

パス名の入力中は Tab 補完を使えます。ディレクトリを開くと、通常はテキストファイルとして扱わず、Emacs のディレクトリエディタである Dired が開きます。

:::single-choice{#emacs-find-file-key} パス名の入力を求め、そのファイルを開く Emacs のキーシーケンスはどれですか？

::option[`C-x C-s`]{#emacs-file-save explanation="これは現在のファイルバッファーを保存するもので、別のパス名を開く入力は求めません。"}
::option[`C-x C-c`]{#emacs-file-exit explanation="これはファイルを開かず、Emacs の終了を始めます。"}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="これは `find-file` を実行し、開くパス名をミニバッファーで求めます。"}
:::

:::single-choice{#emacs-find-missing-file} `C-x C-f` で存在しないパス名を開いた場合、通常、ディスク上のファイルはいつ作成されますか？

::option[新しいバッファーの保存に成功した後だけ。]{#emacs-file-created-on-save .correct explanation="ファイルが存在する前でもバッファーに編集内容を保持でき、保存時に作成されます。"}
::option[パス名を入力した直後。]{#emacs-file-created-immediately explanation="Emacs はまず新しいパス名に関連付けたバッファーを作り、ディスク上の作成は延期します。"}
::option[Emacs 自体を閉じた後だけ。]{#emacs-file-created-on-exit explanation="終了時に保存を尋ねることはありますが、ファイル作成は Emacs を閉じることではなく保存の成功に結び付いています。"}
:::

## 現在のバッファーを保存する

`save-buffer` を実行する `C-x C-s` で、現在のファイルバッファーを保存します。

```text
C-x C-s
```

バッファーに関連付けられたファイル名がなければ、Emacs が入力を求めます。書き込みに成功するとバッファーの変更済み表示が消え、失敗すると未保存のデータはバッファーに残り、エラーが報告されます。

:::single-choice{#emacs-save-current-buffer} 現在のファイルバッファーを保存するキーシーケンスはどれですか？

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` は現在のバッファーに対して `save-buffer` を実行します。"}
::option[`C-x C-w`]{#emacs-write-file-key explanation="これは別のファイル名を求め、バッファーが開くファイルを変更します。"}
::option[`C-x s`]{#emacs-save-some-key explanation="これは複数のファイルバッファーを確認して保存を尋ねるもので、現在の 1 つだけを対象にしません。"}
:::

## 別の名前で書き込む

`write-file` を実行する `C-x C-w` でパス名の入力を求め、そこへバッファーを書き込み、その新しいファイルを開くバッファーにします。

```text
C-x C-w
```

これが Emacs の「名前を付けて保存」の動作です。別のコピーを書き込んだ後も元のパス名を開き続ける操作とは異なります。

:::single-choice{#emacs-write-file-as} 現在のバッファーで通常の「名前を付けて保存」を行うキーシーケンスはどれですか？

::option[`C-x C-f`]{#emacs-find-file-other explanation="これは別のバッファーへ切り替わる可能性のあるファイルを開く操作で、現在のバッファーの「名前を付けて保存」ではありません。"}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="これはバッファーの破棄を尋ね、未保存の変更について確認することはありますが、新しい名前では保存しません。"}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` は選択したパスへ書き込み、そのファイルを開くバッファーにします。"}
:::

## 複数の変更済みバッファーを確認する

`save-some-buffers` を実行する `C-x s` で、変更済みのファイルバッファーを調べます。

```text
C-x s
```

通常、Emacs は対象となる変更済みバッファーごとに保存するか尋ねます。バッファー名を読み、意図的に回答してください。確認なしですべてを保存するショートカットではありません。

:::single-choice{#emacs-save-some-buffers} 通常、`C-x s` は何をしますか？

::option[変更済みのファイルバッファーを保存するか確認します。]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` は対象となる変更済みバッファーを確認し、どれを書き込むか尋ねます。"}
::option[名前を表示せず、すべてのバッファーを自動保存します。]{#emacs-silent-save-all explanation="通常の対話型コマンドは、すべてを無条件に書き込まず確認します。"}
::option[現在のバッファーを保存した後、すべてのバッファーを閉じます。]{#emacs-close-all-buffers explanation="このコマンドは複数バッファーの保存に関するもので、通常は閉じません。"}
:::

## ディスクから読み直す

ファイルがディスク上で変更され、現在のバッファー内容を意図的に破棄する場合は、`M-x revert-buffer` を実行し、確認プロンプトをよく読んでください。読み直すと未保存のバッファー編集を失うことがあるため、どちらの内容を採用するか確認してから使います。

決める前に比較するには、別のコピーを保存するか、バージョン管理や diff ツールを利用します。バッファーが変更済みの場合、再読み込み操作を無害なものとして扱わないでください。

## まとめ

これで、ファイルを開く操作と書き込む操作を混同せず、ファイルバッファーを管理できるようになりました。

1. `C-x C-f` でパス名を開く。
2. 存在しないファイルは、バッファーを保存したときにだけ作成する。
3. `C-x C-s` で現在のバッファーを保存する。
4. `C-x C-w` で新しい名前へ保存し、そのファイルを開く。
5. `C-x s` で複数の変更済みバッファーを確認する。
