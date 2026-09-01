---
lesson_id: "help-command"
course_id: "command-line"
lang: "ja"
order_index: 15
title: "help"
description: "コマンドに応じて、組み込みヘルプ、プログラムの使用法、マニュアルページを選ぶ方法を学びます。"
meta_title: "help - コマンドライン"
meta_description: "Bashのhelp、--help出力、manページ、typeコマンドを使ってLinuxコマンドラインのヘルプを得る方法を学びます。"
meta_keywords: "linux help コマンド, bash help, コマンドライン ヘルプ, --help, シェル組み込み, man コマンド, type コマンド"
---

すべてのコマンドオプションを暗記する必要はありません。Bash と多くのインストール済みプログラムは、端末内で構文を直接説明できます。ただし、適切なヘルプ情報源は、使っているコマンドの種類によって異なります。

## Bash 組み込みコマンドのヘルプを表示する

Bash は、シェル自体が実装するコマンド向けに `help` 組み込みコマンドを提供します。`cd`、`history`、`type` などが該当します。

組み込みコマンド名を引数として渡します。

```bash
$ help echo
```

出力には組み込みコマンドの構文と動作が記載されます。引数なしで `help` を実行すると、Bash がヘルプを持つ組み込みコマンドを一覧表示します。

:::single-choice{#help-for-bash-cd} Bash の `cd` 組み込みコマンドに関するヘルプ項目を表示するコマンドはどれですか？

::option[`cd --help`]{#cd-help-option explanation="一部の組み込みコマンドはオプションを認識することがありますが、Bash 専用の文書インターフェースは、`help` に組み込みコマンド名を続ける形式です。"}
::option[`help cd`]{#help-cd .correct explanation="Bash の `help` 組み込みコマンドは、指定した組み込みコマンド、ここでは `cd` の文書を検索します。"}
::option[`type cd`]{#type-cd explanation="`type` は Bash が `cd` という名前をどのように解決するかを説明しますが、完全なヘルプ項目は表示しません。"}
:::

## プログラムの使用法概要を要求する

多くの外部プログラムは、`--help` を受け取って使用法の概要を表示する慣例に従います。

```bash
$ ls --help
```

広く使われる慣例ですが、すべてのプログラムに共通するわけではありません。どのプログラムも同じオプションに対応すると思い込まず、出力と終了状態を読んでください。

:::single-choice{#quick-ls-usage} 外部の `ls` プログラムが提供する簡単な使用法概要を一般に表示するコマンドはどれですか？

::option[`help ls`]{#bash-help-ls explanation="Bash の `help` はシェル組み込みコマンドを説明し、一般的なシステムでは外部の `ls` の使用法ページは提供しません。"}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls` は一般的な `--help` の慣例に従い、使用法とオプションを表示します。"}
::option[`type --help ls`]{#type-help-ls explanation="これは `ls` に使用法を説明させず、`type` 組み込みコマンド自身のオプション処理を問い合わせます。"}
:::

## Bash が名前を解決する方法を調べる

`type` を使うと、Bash が名前を組み込みコマンド、エイリアス、関数、キーワード、実行可能ファイルのどれとして解決するか確認できます。

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

結果は、エイリアス、関数、インストール済みプログラム、`PATH` によって異なります。Bash が最初に使う 1 つだけでなく、既知のすべての解決結果を見るには `type -a NAME` を使います。

:::single-choice{#identify-command-resolution} `deploy` がエイリアス、関数、組み込みコマンド、実行可能ファイルのどれか分かりません。名前の解決方法を確認する Bash コマンドはどれですか？

::option[`type deploy`]{#type-deploy .correct explanation="`type` 組み込みコマンドは、現在のシェル環境で Bash がそのコマンド名をどう解釈するか報告します。"}
::option[`help deploy`]{#help-deploy explanation="`help` は Bash 組み込みコマンドの文書を探し、通常はエイリアス、関数、外部ファイルを識別しません。"}
::option[`deploy --help`]{#deploy-help explanation="これはコマンドの実行を試み、そのコマンド自身のオプション対応に依存します。Bash が名前をどう解決したかは先に説明しません。"}
:::

## 詳細度を選ぶ

- Bash 組み込みコマンドには `help COMMAND` を使う
- 多くの外部コマンドの簡単な概要には `COMMAND --help` を使う
- 詳細なインストール済みマニュアルページには `man COMMAND` を使う
- 1 行の説明には `whatis COMMAND` を使う

次のレッスンでは、マニュアルページと 1 行の説明を詳しく扱います。

:::single-choice{#choose-detailed-manual} 短い使用法概要ではなく、外部コマンド `ls` の詳細な文書が必要です。どのコマンドを試しますか？

::option[`man ls`]{#man-ls .correct explanation="`man ls` はインストール済みのマニュアルページを開き、通常は構文、オプション、動作をより詳しく説明します。"}
::option[`whatis ls`]{#whatis-ls explanation="`whatis` は簡潔なマニュアルページ説明を表示するため、要求された詳細な文書ではありません。"}
::option[`type ls`]{#type-ls explanation="`type` は Bash が `ls` をどう解決するか報告し、プログラムの詳細なマニュアルは表示しません。"}
:::

## まとめ

これで Bash がコマンドを解決する方法に応じて、ヘルプ情報源を選べるようになりました。

1. Bash 組み込みコマンドには `help` を使う。
2. プログラムの簡単な使用法には `--help` を試す。
3. `type` で名前の解決方法を調べる。
4. `man` で詳細な文書を開く。
