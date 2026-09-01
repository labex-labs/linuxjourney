---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "ja"
order_index: 3
title: "cd（ディレクトリの変更）"
description: "`cd` とパスやショートカットを使い、Linux ファイルシステム内を移動する方法を学びます。"
meta_title: "cd（ディレクトリの変更） - コマンドライン"
meta_description: "絶対パス、相対パス、ホームディレクトリのショートカット、親ディレクトリ、前のディレクトリへの移動などの例を使ってLinuxのcdコマンドを学びましょう。"
meta_keywords: "cdコマンド, linux cdコマンド, ディレクトリ変更, cd 親ディレクトリ, cd ホーム, cd 前のディレクトリ, 絶対パス, 相対パス"
---

Linux ファイルシステム内を移動するには、パスで目的地を指定します。中心となるツールは、change directory の略である `cd` コマンドです。シェルの現在の作業ディレクトリを変更します。

目的地は通常ファイルではなくディレクトリでなければなりません。ディレクトリが存在しない、名前の入力が誤っている、入る権限がない場合、`cd` は場所を変更せずエラーを報告します。

基本構文は次のとおりです。

```bash
cd [DIRECTORY]
```

## パスを理解する

パスの指定方法には、絶対パスと相対パスがあります。

- **絶対パス**：ルートディレクトリ（`/`）から始まる完全なパス。例：`/home/pete/Desktop`
- **相対パス**：現在位置を基準にするパス。`/home/pete/Documents` にいて `taxes` というサブディレクトリへ入るなら、`taxes/` を使える

:::single-choice{#recognize-absolute-cd-path} 絶対パスを正しく説明しているものはどれですか？

::option[シェルが現在使っているディレクトリから始まります]{#begins-at-current-directory explanation="シェルの現在位置に依存するパスは相対パスです。必ずしもルートから始まりません。"}
::option[親ディレクトリを含まず、最後のディレクトリ名だけを含みます]{#contains-final-name-only explanation="目的地名 1 つは通常、現在のディレクトリからの相対パスとして解釈されます。絶対パスは `/` からの経路を含みます。"}
::option[`/` で表されるルートディレクトリから始まります]{#begins-at-root .correct explanation="絶対パスはファイルシステムのルートから始まります。先頭の `/` により、現在のディレクトリに依存しない出発点になります。"}
:::

## `cd` コマンドを使う

絶対パスで特定のディレクトリへ移動するには、次のように入力します。

```bash
$ cd /home/pete/Pictures
```

このコマンドは `Pictures` ディレクトリへ直接移動します。

`pwd` で場所を確認できます。

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory} `cd` の後でシェルの現在位置を確認するコマンドはどれですか？

::option[`cd`]{#cd-command explanation="`cd` は現在のディレクトリを変更しますが、通常、結果の完全なパスは表示しません。`pwd` で確認します。"}
::option[`ls`]{#ls-command explanation="`ls` はディレクトリ内容を表示します。場所を調べる助けにはなりますが、場所そのものを報告するのは `pwd` です。"}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` は現在の作業ディレクトリを表示し、`cd` で移動した場所を確認できます。"}
:::

## サブディレクトリへ移動する

すでにディレクトリ内にいて、そのサブディレクトリへ移動する場合は相対パスを使います。たとえば現在位置が `/home/pete/Pictures` で、その中に `Hawaii` フォルダーがあるなら、次のように移動できます。

```bash
$ cd Hawaii
```

フォルダー名だけを使えるのは、すでに親ディレクトリの `/home/pete/Pictures` にいるためです。

## 重要な移動用ショートカット

完全なパスを毎回入力するのは面倒です。シェルには、移動を速くするショートカットがあります。

- `.`（現在のディレクトリ）：現在いるディレクトリを表す
- `..`（親ディレクトリ）：現在のディレクトリを含む 1 つ上の階層を表す
- `~`（ホームディレクトリ）：`/home/pete` など、個人のホームディレクトリを表す
- `-`（前のディレクトリ）：直前にいたディレクトリへ戻る

`cd` と組み合わせて使います。

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory} `/home/pete/Pictures` から `/home/pete` へ移動するコマンドはどれですか？

::option[`cd .`]{#cd-current explanation="`.` は現在のディレクトリを表すため、`/home/pete/Pictures` にとどまります。"}
::option[`cd -`]{#cd-previous explanation="`-` は直前の作業ディレクトリへ戻りますが、必ずしも親とは限りません。1 つ上へ行く場合は `..` を使います。"}
::option[`cd ..`]{#cd-parent .correct explanation="`..` は現在のディレクトリの親を表します。`Pictures` の親は `/home/pete` です。"}
:::

:::single-choice{#return-to-previous-directory} 現在のディレクトリの直前に使っていたディレクトリへ戻るコマンドはどれですか？

::option[`cd -`]{#previous-directory .correct explanation="`cd -` は直前の作業ディレクトリへ切り替えます。その場所はファイルシステム内のどこでもかまいません。"}
::option[`cd ..`]{#parent-directory explanation="`cd ..` は親ディレクトリへ移動します。親と直前のディレクトリは常に同じとは限りません。"}
::option[`cd ~`]{#home-directory explanation="`cd ~` はホームディレクトリへ移動し、直前に訪れたディレクトリは追跡しません。"}
:::

これらのショートカットを試し、コマンドラインで効率よく移動できるようにしましょう。

## 実用的な `cd` の例

ホームディレクトリへ移動します。

```bash
$ cd
```

ディレクトリ引数なしで `cd` を実行しても、ホームディレクトリへ移動します。

2 階層上へ移動します。

```bash
$ cd ../..
```

空白を含む名前のディレクトリへ、引用符を使って移動します。

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces} `Vacation Photos` を 1 つのディレクトリ名として扱うコマンドはどれですか？

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="引用符がないため、シェルは `Vacation` と `Photos` を 1 つの名前ではなく別々の引数として渡します。"}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="行全体を引用すると、シェルはそれを 1 つのコマンド名として扱います。コマンド自体はパスの引用符の外に置きます。"}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="引用符が 2 つの単語を、`cd` に渡す 1 つのパス引数へまとめます。"}
:::

前のディレクトリへ戻ります。

```bash
$ cd -
/home/pete/Documents
```

Linux のディレクトリ移動を身に付けるには、次のハンズオンラボを利用してください。

1. **[Linux cd コマンド：ディレクトリの変更](https://labex.io/ja/labs/linux-linux-cd-command-directory-changing-209733)**：パスを理解し、`cd` で効率よくファイルシステムを移動する方法を学びます。
2. **[Linux のディレクトリ移動](https://labex.io/ja/labs/linux-directory-navigation-387844)**：基本的なコマンドでディレクトリを移動し、スキルを試します。
3. **[新しいプロジェクト構造のセットアップ](https://labex.io/ja/labs/linux-setting-up-a-new-project-structure-387859)**：`mkdir` や `cd` で特定のプロジェクト構造を作成し、その中を移動します。

## まとめ

これで `cd` を使い、完全なパスやシェルのショートカットでディレクトリ間を移動できるようになりました。

1. 絶対パスと相対パスを区別する。
2. ディレクトリを変更し、`pwd` で結果を確認する。
3. 親、ホーム、前のディレクトリへ移動する。
4. 空白を含むディレクトリ名へ入る。
5. 一般的なパスとパーミッションのエラーを認識する。
