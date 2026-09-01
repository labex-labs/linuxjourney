---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 2
title: "テキストエディタ"
description: "Linux の管理や開発に使う端末テキストエディタを選び、設定する方法を学びます。"
meta_title: "テキストエディタ - 高度なテキスト操作"
meta_description: "Vim や Emacs のような Linux テキストエディタについて学びましょう。システムナビゲーションにおけるそれらの用途と重要性を発見してください。Linux テキストエディタの旅を始めましょう！"
meta_keywords: "Linux テキストエディタ，Vim, Emacs, Linux コマンド，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

Linux の設定、スクリプト、ソースコード、ログは、一般にプレーンテキストとして保存されます。端末エディタを使えば、ローカル端末、リモートの SSH セッション、グラフィカルデスクトップのない環境でも、それらのファイルを操作できます。

## 環境に適したエディタを選ぶ

すべての人や作業に最適なエディタが 1 つだけあるわけではありません。グラフィカルエディタ、端末エディタ、統合開発環境は、いずれも状況に応じて適切な選択肢になります。コマンドラインで作業する場合は、インストール済みで、安全に終了でき、基本的な編集モデルを理解しているエディタを選んでください。

Vim や Emacs がインストール済みだと決めつけず、現在のシェルでコマンドを解決できるか確認します。

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

結果が空で終了状態が 0 以外なら、その名前は現在のコマンド検索では見つかっていません。最小構成のシステムでは `vi` だけが提供されることもあれば、Nano が含まれる場合や、対話型エディタがまったくない場合もあります。

:::single-choice{#editors-check-availability} 現在のシェルが `vim` という実行可能ファイルを解決できるか確認するコマンドはどれですか？

::option[`vim --install`]{#editors-vim-install explanation="Vim はこのコマンドを移植可能なインストール確認として使わず、パッケージのインストール方法もディストリビューションごとに異なります。"}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="これは設定パスが存在する場合にその種類を判定しますが、`vim` を解決できるかは調べません。"}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="このシェル組み込みコマンドはコマンド解決を確認し、利用可能なら解決結果を出力します。"}
:::

## Vim のモデルを理解する

Vim はモードを持つエディタです。同じキーでも、現在のモードによって意味が変わります。

- ノーマルモードでは、キーを移動や編集のコマンドとして解釈する
- 挿入モードでは、入力したテキストを挿入する
- コマンドラインモードでは、書き込みや終了などのコマンドを受け付ける

練習すれば、このモデルによって繰り返しのキーボード編集を効率よく行えますが、初心者は現在のモードを意識する必要があります。後続のレッスンで、Vim の操作を 1 つずつ紹介します。

:::single-choice{#editors-vim-modal-meaning} Vim がモードを持つとは、どういう意味ですか？

::option[すべてのファイルが別々のグラフィカルウィンドウで開く。]{#editors-vim-windows explanation="ウィンドウとバッファーは別の概念です。モードとは、エディタの状態によってキーの動作が変わることを指します。"}
::option[Vim は一度に 1 種類のテキストファイルしか編集できない。]{#editors-vim-file-type explanation="Vim は多くのファイル形式に対応します。モードは操作モデルを表し、ファイルの制限ではありません。"}
::option[現在のモードに応じて、キーが異なる操作を行う。]{#editors-vim-modes .correct explanation="たとえば、ノーマルモードではコマンドを実行するキーが、挿入モードでは文字を入力します。"}
:::

## Emacs のモデルを理解する

Emacs は一般に、拡張可能な環境の中でキーの組み合わせと名前付きコマンドを使います。ファイルはバッファーで開かれ、メジャーモードとマイナーモードが内容や作業に応じた動作を設定します。Emacs は端末でもグラフィカルなフレームでも実行できます。

Vim と Emacs はどちらも、設定や拡張によって基本編集をはるかに超える機能を利用できます。カスタマイズを追加する前に、プレーンテキストファイルを開く、変更する、保存する、閉じるという操作から始めてください。

:::single-choice{#editors-emacs-buffer} Emacs の用語では、開いたファイルの編集可能なテキストは通常どこに保持されますか？

::option[バッファー内。]{#editors-emacs-buffer-answer .correct explanation="Emacs はファイルをバッファーで開き、そこに表示または編集するテキストを保持します。"}
::option[シェルのエイリアステーブル内。]{#editors-emacs-alias-table explanation="エイリアスはシェルのコマンド解決に属し、エディタのテキストは保存しません。"}
::option[端末のスクロールバック内だけ。]{#editors-emacs-scrollback explanation="端末のスクロールバックは表示済み出力を記録しますが、Emacs は編集可能なテキストをバッファーで管理します。"}
:::

## 使用するエディタを設定する

多くのコマンドラインプログラムは、エディタを起動するときに `VISUAL` または `EDITOR` を参照します。たとえば、現在の Bash セッションとその子プロセスから起動するコマンドで Vim を選ぶには、次のようにします。

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

これらの変数が表すのは設定上の希望であり、プログラムをインストールするものではありません。実際に存在するコマンドを使い、テストしてから適切なシェル起動ファイルへ export を記述してください。

:::single-choice{#editors-editor-variable} `export EDITOR=vim` は何をしますか？

::option[今後の子プロセスに、`vim` が優先するエディタ値だと伝えます。]{#editors-export-preference .correct explanation="export は、現在のシェルから起動するコマンドが継承する環境へ設定値を置きます。"}
::option[システムの全ユーザーに Vim をインストールします。]{#editors-install-vim explanation="環境変数の代入は、パッケージをインストールせず、ほかのユーザーのシステムも変更しません。"}
::option[すべてのプログラムで Vim のキーバインドを有効にします。]{#editors-global-bindings explanation="プログラムはエディタ起動のために変数を参照できますが、独自の操作モデルは置き換えられません。"}
:::

## 重要なファイルを危険にさらさず練習する

自分が所有するディレクトリに、使い捨てのファイルを作って練習します。

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

システム設定やほかのユーザーのデータから始めないでください。重要なファイルを変更する前にはバックアップを作り、保存と終了の方法を理解し、`cat` や `diff` などの読み取り専用コマンドで結果を確認します。

:::single-choice{#editors-first-practice-file} 慣れていないエディタを最初に練習するファイルとして、最も安全なものはどれですか？

::option[root で開いた重要なブート設定ファイル。]{#editors-boot-file explanation="誤った変更で通常起動できなくなるおそれがあり、権限を高めるほどミスの影響も大きくなります。"}
::option[自分が所有するディレクトリ内の使い捨てテキストファイル。]{#editors-disposable-file .correct explanation="練習用ファイルなら、移動、保存、終了を学ぶ間に誤編集しても影響を限定できます。"}
::option[バックアップのない共有本番ファイル。]{#editors-production-file explanation="共有データで確認せずに練習すると、ほかの人の作業を妨げ、簡単な復旧手段もありません。"}
:::

端末でテキストファイルを開き、編集、保存する練習には、次のハンズオンラボを利用してください。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)**：vi/vim と nano の両方で、ファイルの作成、テキスト編集、保存、移動を練習します。

## まとめ

これで、端末エディタを選び、安全な練習手順を用意できるようになりました。

1. エディタのコマンドが利用できるか確認する。
2. Vim のモードを使った操作モデルを認識する。
3. Emacs のバッファーと拡張可能なモードを認識する。
4. インストールと混同せず、エディタの設定値を指定する。
5. 重要なファイルを編集する前に、使い捨てのテキストで練習する。
