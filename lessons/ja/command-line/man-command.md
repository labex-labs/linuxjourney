---
lesson_id: "man-command"
course_id: "command-line"
lang: "ja"
order_index: 16
title: "manコマンド"
description: "インストール済みのマニュアルページを開き、移動、検索し、セクションを選ぶ方法を学びます。"
meta_title: "manコマンド - コマンドライン"
meta_description: "Linuxのmanコマンドを使ってマニュアルページの読み方、manページ内の検索、セクションの理解、コマンドオプションの調べ方を学びましょう。"
meta_keywords: "manコマンド, linux manページ, コマンドマニュアル, man ls, manセクション, manページ検索, コマンドラインヘルプ"
---

多くの Linux コマンド、インターフェース、設定ファイル、管理ツールには、マニュアルページ（man ページ）と呼ばれる参照文書がインストールされています。`man` コマンドはそれらを検索して表示します。

## マニュアルページを開く

`man` にトピック名を渡します。たとえば、`ls` のページを次のように開きます。

```bash
$ man ls
```

マニュアルページには通常、概要、説明、オプション、関連ファイル、相互参照が含まれますが、正確な構成はページごとに異なります。

:::single-choice{#open-ls-manual} インストール済みの `ls` マニュアルページを開くコマンドはどれですか？

::option[`help ls`]{#help-ls explanation="Bash の `help` はシェル組み込みコマンドを説明し、通常は外部の `ls` マニュアルページを開きません。"}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` はマニュアルデータベースで `ls` というトピックを検索し、一致するページを表示します。"}
::option[`ls --help`]{#ls-usage explanation="これは `ls` 自身に使用法概要を求めるもので、インストール済みマニュアルページは開きません。"}
:::

## ページ内を移動、検索する

多くのシステムでは、`man` が `less` などのページャーでページを表示します。ページを開いている間、矢印キーやページキーでスクロールし、次の操作を使えます。

- `/pattern` と入力して Enter を押し、前方検索する
- `n` で同じ方向へ検索を繰り返す
- `N` で反対方向へ検索を繰り返す
- `q` で終了する

ページャーはシステムや環境によって異なるため、正確なキーが常に同じとは限りません。上記は一般的な `less` 設定に適用されます。

:::single-choice{#search-man-page} `less` で man ページを開いているとき、`--recursive` の前方検索を始める操作はどれですか？

::option[`?--recursive` と入力して Enter を押す。]{#backward-man-search explanation="疑問符は後方検索を始め、要求とは反対方向を探します。"}
::option[`/--recursive` と入力して Enter を押す。]{#forward-man-search .correct explanation="`less` ではスラッシュが前方検索を始め、Enter でパターンを確定します。"}
::option[`n--recursive` と入力して Enter を押す。]{#repeat-man-search explanation="`n` は既存の検索を繰り返すもので、この形式で新しい検索パターンは入力しません。"}
:::

:::single-choice{#leave-man-page} 通常のページャーで man ページを開いているとき、シェルへ戻るキーはどれですか？

::option[`G`]{#man-page-end explanation="大文字の `G` は `less` でページ末尾へ移動しますが、ページャーを閉じません。"}
::option[`n`]{#next-man-match explanation="`n` は直近の検索を繰り返し、マニュアルページを開いたままにします。"}
::option[`q`]{#quit-man .correct explanation="`q` は通常のページャーを終了し、シェルへ制御を戻します。"}
:::

## マニュアルのセクションを選ぶ

マニュアルは番号付きセクションに分かれています。一般的なセクションには次のものがあります。

- `1`：ユーザーコマンド
- `2`：システムコール
- `3`：ライブラリ関数
- `5`：ファイル形式
- `8`：システム管理コマンド

同じトピックが複数のセクションに現れることがあります。明示的に選ぶには、トピックより前にセクションを置きます。

```bash
$ man 5 passwd
$ man 1 passwd
```

最初のコマンドはセクション 5 の `passwd` ファイル形式ページ、2 番目はセクション 1 のユーザーコマンドページを開きます。`passwd(5)` のような参照も同じ `topic(section)` 表記を使います。

:::single-choice{#open-passwd-file-format} `passwd` ファイル形式を説明するセクション 5 のページを開くコマンドはどれですか？

::option[`man passwd 5`]{#section-after-topic explanation="このコマンド形式ではセクション指定をトピックより前に置きます。この順序では `passwd(5)` を要求できません。"}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="セクション `5` を `passwd` より前に置くと、ファイル形式ページを明示的に選びます。"}
::option[`man 1 passwd`]{#passwd-command-page explanation="セクション 1 はユーザーコマンドなので、ファイル形式ではなく `passwd` コマンドページを選びます。"}
:::

## ページが見つからない場合

すべてのコマンド名に個別のマニュアルページがインストールされているとは限りません。`man` が項目なしと報告した場合は、次を試します。

- `type NAME` で Bash が名前をどう解決するか調べる
- Bash 組み込みコマンドなら `help NAME` を使う
- 外部プログラムが慣例に対応する場合は `NAME --help` を試す
- ディストリビューションに別の文書パッケージがあるか確認する

:::single-choice{#missing-builtin-manual} `type cd` が `cd` は Bash 組み込みコマンドだと報告し、個別の man ページがありません。次に試すコマンドはどれですか？

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` はマニュアルデータベースの項目を要約し、組み込みコマンド用の欠けた個別ページは提供できません。"}
::option[`file cd`]{#file-cd-name explanation="`file` はファイルシステムオブジェクトを分類しますが、ここで `cd` はパスではなくシェル組み込みコマンドとして解決されています。"}
::option[`help cd`]{#builtin-cd-help .correct explanation="Bash の `help` 組み込みコマンドが、シェル自身の `cd` 文書を提供します。"}
:::

## まとめ

これでインストール済みのマニュアル文書を見つけ、移動できるようになりました。

1. トピック名でページを開く。
2. 通常のページャーでページ内を検索、移動する。
3. ページャーを終了してシェルへ戻る。
4. 番号付きマニュアルセクションを選ぶ。
5. ページがない場合は別のヘルプ情報源を選ぶ。
