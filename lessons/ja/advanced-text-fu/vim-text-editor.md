---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 3
title: "Vim (Vi Improved)"
description: "Vim とは何か、vi とどのような関係にあるか、ファイル、ヘルプ、ガイド付き練習を開く方法を学びます。"
meta_title: "Vim (Vi Improved) - 高度なテキスト操作"
meta_description: "強力で軽量なテキストエディタである Vim（vi improved）を発見しましょう。このレッスンでは、ほとんどの Linux システムにプリインストールされている Vim の基本を紹介します。"
meta_keywords: "Vim, vi improved, vim vi improved, Linux テキストエディタ，Vim チュートリアル，Vi エディタ，vim improved, Linux コマンド"
---

Vim は設定可能なテキストエディタで、その名前は **Vi Improved** を意味します。オリジナルの `vi` エディタに由来するモード式の編集モデルを維持しながら、複数段階の取り消し、構文対応、スクリプト機能、充実したヘルプシステムなどを追加しています。

## Vim と vi の関係

`vi` は、歴史的なエディタと一般的なコマンドインターフェースの両方を指します。ある Linux システムでは `vi` が互換性を重視したモードの Vim を起動し、別のシステムでは異なる vi 実装を起動することがあります。すべての `vi` コマンドが Vim の全機能を提供するとは考えないでください。

現在のシェルで何が解決されるかを確認します。

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

解決されたパスだけでは、`vi` と `vim` が同じ実装かどうかは分かりません。`type -a vi vim` とエディタのバージョン出力から、さらに詳しい情報を得られます。

:::single-choice{#vim-name-origin}
Vim という名前は何を意味しますか？

::option[Visual Input Manager]{#vim-visual-input explanation="これはエディタ名の由来ではありません。"}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim はモードを使いますが、この語句が名前を表すわけではありません。"}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim は vi 互換エディタの改良版として始まり、そのことが名前に表れています。"}
:::

:::single-choice{#vim-check-command}
Bash が現在 `vim` という名前を解決できるか確認するコマンドはどれですか？

::option[`vim --create`]{#vim-create-option explanation="これはシェルの解決確認ではなく、Vim をインストールまたは検出する方法でもありません。"}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="このシェル組み込みコマンドは、その名前で使われるコマンドがあれば報告します。"}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="これは設定ファイル候補の 1 つを調べるだけで、Vim の実行可能ファイルが使えるかは確定できません。"}
:::

## Vim とファイルを開く

名前のないバッファーで Vim を起動します。

```bash
$ vim
```

ファイルを編集するにはパス名を渡します。

```bash
$ vim filename.txt
```

`filename.txt` が存在して読み取り可能なら、Vim はその内容をバッファーへ読み込みます。パスが存在しなければ、その名前に関連付けた新しいバッファーを開きます。バッファーの書き込みに成功するまで、ファイルは作成されません。

Vim がファイルシステムのパーミッションを回避することはありません。ファイルを開けても、そのパスへ変更を保存できるとは限りません。

:::single-choice{#vim-open-missing-path}
まだ存在しないパスを `vim draft.txt` で指定すると、通常どうなりますか？

::option[Vim が新しいバッファーを開き、書き込んだときにだけファイルを作成します。]{#vim-new-buffer .correct explanation="パス名はバッファーに記憶されますが、ディスク上の作成は保存に成功するまで行われません。"}
::option[Vim はインターフェースを開く前に、ディスク上へ空のファイルを作成します。]{#vim-immediate-create explanation="新しいバッファーはパス名に関連付けられますが、保存に成功するまでファイルは作成されません。"}
::option[すべてのパス名は既存でなければならないため、Vim は起動を拒否します。]{#vim-refuse-missing explanation="Vim は存在しないパス用の新しいバッファーを開き、そこで新しいファイルを作成できます。"}
:::

## 組み込みの学習リソースを使う

Vim のインストールに `vimtutor` が含まれている場合、シェルから実行すると対話形式の練習レッスンが始まります。

```bash
$ vimtutor
```

Vim 内では `Esc` でノーマルモードに入り、`:help` と入力して Enter を押すとヘルプシステムが開きます。コマンドの後に特定のトピックを指定できます。

```vim
:help user-manual
:help :write
```

ヘルプタグは厳密なので、句読記号が重要なことがあります。ヘルプ内のリンクで `Ctrl+]` を押すと移動し、`Ctrl+T` で戻ります。

:::single-choice{#vim-guided-tutorial}
インストールされている場合、Vim のガイド付きチュートリアルを開始するシェルコマンドはどれですか？

::option[`vim --quiz`]{#vim-quiz-option explanation="Vim はこのオプションを標準のガイド付きチュートリアルには使いません。"}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` は、安全に実践できるよう設計された対話型チュートリアルのコピーを開きます。"}
::option[`help vim`]{#vim-shell-help explanation="Bash の `help` はシェル組み込みコマンドを説明するもので、Vim の対話型チュートリアルを起動しません。"}
:::

## 使い捨てのファイルで練習する

自分が所有するディレクトリ内のファイルから始めます。

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

後続のレッスンで、検索、移動、挿入、編集、保存を紹介します。安全に終了する方法を覚えるまでは、`Esc` でノーマルモードへ戻り、`:q!` と入力して Enter を押すと、現在のウィンドウで保存していない変更を破棄できることを覚えておいてください。このコマンドは、その変更を意図的に破棄する場合にだけ使います。

:::single-choice{#vim-abandon-practice-changes}
使い捨ての練習ファイルで、現在のウィンドウを終了し、保存していない変更を破棄する Vim コマンドはどれですか？

::option[`:w`]{#vim-write-only explanation="`:w` はバッファーを書き込みますが、現在のウィンドウは終了しません。"}
::option[`:wq`]{#vim-write-quit explanation="`:wq` は終了前に変更を保存するため、破棄しません。"}
::option[`:q!`]{#vim-quit-force .correct explanation="`!` は、変更済みバッファーの警告を無視し、変更を書き込まず終了するよう Vim に指示します。"}
:::

Vim でファイルを開き、編集、保存する練習には、次のハンズオンラボを利用してください。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)**：実際の Linux 環境で、Vim と Nano の両方を使ってファイルの作成、テキスト編集、保存、移動を練習します。

## まとめ

これで Vim を識別し、バッファーを開き、安全な学習リソースを見つけられるようになりました。

1. 1 つの実装だと決めつけず、Vim と vi の関係を説明する。
2. `vim` コマンドが利用できるか確認する。
3. 既存ファイルまたは名前付きの新しいバッファーを開く。
4. `vimtutor` または Vim の組み込みヘルプを開く。
5. 意図した場合にだけ、保存していない練習内容を破棄する。
