---
lesson_id: "alias-command"
course_id: "command-line"
lang: "ja"
order_index: 18
title: "alias"
description: "Bash でコマンドエイリアスを作成、確認、永続化、回避、削除する方法を学びます。"
meta_title: "alias - コマンドライン"
meta_description: "Linuxのaliasコマンドを学び、一時的なエイリアスの作成、.bashrcへの保存、エイリアスの一覧表示、unaliasによる削除の例を紹介します。"
meta_keywords: "linux alias コマンド, alias コマンド, bash alias, .bashrc alias, unalias コマンド, コマンドショートカット linux, シェル alias"
---

エイリアスは対話型シェルに対し、行を実行する前に 1 つのコマンド語を別の文字列へ置き換えるよう指示します。頻繁に使うコマンドを短くしたり、好みのオプションを付けたりできます。

## 現在のシェルでエイリアスを作成する

Bash では `alias NAME='REPLACEMENT'` でエイリアスを定義します。等号の前後に空白を入れてはいけません。

```bash
$ alias ll='ls -la'
```

定義後、`ll` をコマンドとして入力すると `ls -la` へ展開されます。引用符は、定義時に置換文字列を 1 つにまとめます。

エイリアスは、単純なコマンド接頭辞の置き換えに適しています。引数をより構造的に処理する場合はシェル関数を使います。

:::single-choice{#define-ll-alias}
現在のシェルで `ll` を `ls -la` のエイリアスとして定義する Bash コマンドはどれですか？

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="`=` の前後の空白が定義を別々のシェル語へ分割するため、Bash は有効なエイリアス代入を受け取りません。"}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="必要な `NAME=REPLACEMENT` 形式を使い、空白を含む置換文字列を引用しています。"}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` は既存のエイリアス名を削除し、置換を作成しません。"}
:::

## 将来の Bash セッションでエイリアスを読み込む

プロンプトで定義したエイリアスは現在のシェルに属し、終了すると消えます。対話型の非ログイン Bash セッションは通常 `~/.bashrc` を読むため、個人用 Bash エイリアスは一般にこのファイルへ置きます。

```bash
alias ll='ls -la'
```

ファイルを編集した後、新しい対話型 Bash セッションを始めるか、現在のシェルで再読み込みします。

```bash
$ source ~/.bashrc
```

シェルの起動動作は、シェル、ログインモード、ディストリビューションの設定によって異なります。たとえば Zsh ユーザーは通常、Bash の `.bashrc` ではなく Zsh の設定を使います。

:::single-choice{#persist-bash-alias}
将来の対話型非ログイン Bash セッションが読み込むよう、個人用エイリアスを通常どこに定義しますか？

::option[ユーザーの `~/.bashrc` ファイル。]{#bashrc-alias .correct explanation="対話型非ログイン Bash は通常 `~/.bashrc` を読むため、個人用 Bash エイリアスの一般的な場所です。"}
::option[エイリアス対象コマンドが使う実行可能ファイル。]{#edit-executable explanation="インストール済み実行可能ファイルの変更はシェルのエイリアス展開とは無関係で、管理されたシステムファイルを損傷する可能性があります。"}
::option[現在の端末のスクロールバック履歴。]{#terminal-scrollback explanation="スクロールバックは表示済みテキストを記録するだけで、Bash は起動設定として実行しません。"}
:::

## エイリアスと名前の解決を調べる

引数なしの `alias` で、現在のシェルにあるエイリアスを一覧表示します。

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

`type NAME` で、Bash が特定の名前をどう解決するか調べます。

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias}
Bash が現在 `ll` をエイリアス、関数、組み込みコマンド、実行可能ファイルのどれとして解決するか表示するコマンドはどれですか？

::option[`file ll`]{#file-ll explanation="`file` はファイルシステムのパスを分類します。エイリアスはシェルの状態にあり、`ll` というファイルに対応する必要はありません。"}
::option[`type ll`]{#type-ll .correct explanation="`type` 組み込みコマンドは、現在の Bash セッションが `ll` という名前をどう解決するか報告します。"}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` はマニュアルページの説明を問い合わせます。通常、個人用エイリアスにはマニュアルデータベースの項目がありません。"}
:::

## エイリアスを回避、削除する

1 つのコマンドラインだけエイリアスを回避するには、コマンド名の前にバックスラッシュを付けるか、Bash の `command` 組み込みコマンドの後へ置きます。

```bash
$ \ls
$ command ls
```

基になるコマンドの通常動作が必要な場合に便利です。エイリアスは短く予測可能に保ち、見慣れたコマンド名の背後に意外または破壊的な動作を隠さないでください。

:::single-choice{#bypass-ls-alias}
現在の Bash セッションに `ls` というエイリアスがあります。1 回だけ回避するコマンドはどれですか？

::option[`alias ls`]{#show-ls-alias explanation="これは `ls` エイリアスの定義を表示し、基になるコマンドは実行しません。"}
::option[`command ls`]{#command-ls .correct explanation="`command` がコマンド語になるため、Bash はその後の `ls` をエイリアス展開せず、通常のコマンド解決を行います。"}
::option[`source ls`]{#source-ls explanation="`source` はファイルをシェルコードとして現在のシェルへ読み込みます。エイリアスを回避する安全で適切な方法ではありません。"}
:::

`unalias` で現在のシェルからエイリアスを削除します。

```bash
$ unalias ll
```

`~/.bashrc` に定義が残っていれば、将来のシェルが再作成できます。永続的に削除する場合は、その設定行も削除または変更してください。

:::single-choice{#remove-current-alias}
現在の Bash セッションから `ll` エイリアスを削除するコマンドはどれですか？

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` は現在のシェルのエイリアステーブルから指定した名前を削除します。"}
::option[`alias ll=''`]{#empty-ll explanation="定義を削除せず、空の展開へ置き換えます。"}
::option[`command ll`]{#command-ll explanation="`command` はその行でエイリアス展開を回避できますが、シェル状態からは削除しません。"}
:::

## まとめ

これで単純で確認可能なエイリアスを使い、Bash をカスタマイズできるようになりました。

1. 正しく引用して一時的なエイリアスを定義する。
2. 将来のセッションでは `~/.bashrc` から個人用エイリアスを読み込む。
3. エイリアスとコマンド解決を調べる。
4. 1 回だけエイリアスを回避する。
5. 必要に応じて有効な定義と保存済みの定義の両方を削除する。
