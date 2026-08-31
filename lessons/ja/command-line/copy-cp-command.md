---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "ja"
order_index: 10
title: "cp（コピー）"
description: "上書きと属性の保持を制御しながら、ファイルやディレクトリツリーをコピーする方法を学びます。"
meta_title: "cp（コピー） - コマンドライン"
meta_description: "Linuxのcpコマンドを学び、ファイルやディレクトリのコピー、複数ファイル、ワイルドカード、バックアップ、cp -r、cp -i、cp -pなどのオプションの使い方を例とともに解説します。"
meta_keywords: "linux cpコマンド, cpコマンド, linux ファイルコピー, cp -r, cp -i, cp -p, cp -a, cp -u, 再帰的コピー, linux ワイルドカード"
---

`cp` コマンドは、コピー元を残したままファイルとディレクトリをコピーします。基本構文は次のとおりです。

```bash
cp [OPTIONS] SOURCE DESTINATION
```

1 ファイルを別のパスへコピーする、複数ファイルをディレクトリへコピーする、ディレクトリツリーを再帰的にコピーするといった使い方ができます。

## 1 つのファイルをコピーする

コピー元を先、コピー先を後に置きます。

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

`/home/pete/Documents/cooldocs` が既存ディレクトリなら、その中に `mycoolfile` としてコピーが作られます。新しいコピー先ファイル名を指定することもできます。

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

2 番目の例では、コピーしたデータに `mycoolfile_backup` という名前が付きます。

:::single-choice{#copy-file-under-new-name}
`draft.txt` を残したまま、`final.txt` というファイルへコピーするコマンドはどれですか？

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv` は元のパス名を変更または移動するため、要求されたコピー元を残しません。"}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="コピー元とコピー先が逆です。`final.txt` から `draft.txt` へコピーします。"}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp` は `draft.txt` を読み、コピー元を残したまま `final.txt` を作成または置換します。"}
:::

## 複数のファイルをディレクトリへコピーする

すべてのコピー元を先に並べ、コピー先ディレクトリを最後に置きます。

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

コピー元が複数ある場合、最後の引数はディレクトリでなければなりません。

:::single-choice{#copy-multiple-files}
`a.txt` と `b.txt` を既存の `archive/` ディレクトリへコピーするコマンドはどれですか？

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="この形式の `cp` ではコピー先ディレクトリを最後に置きます。先頭に置くとオペランドの解釈が変わります。"}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="コピー元が複数ある場合、`cp` は最後の既存ディレクトリを、それより前の全ファイルのコピー先として扱います。"}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="すべてのコピー元オペランドはコピー先より前に置き、既存ディレクトリを最後にします。"}
:::

## ワイルドカードでファイルを選ぶ

シェルはワイルドカードパターンを複数のコピー元パスへ展開できます。

- `*`：任意の文字列に一致する
- `?`：任意の 1 文字に一致する
- `[]`：ブラケット内のいずれか 1 文字に一致する

たとえば、現在のディレクトリで名前が `.jpg` で終わるファイルを `Pictures` へコピーします。

```bash
$ cp *.jpg /home/pete/Pictures
```

特にコピー先に重要なデータがある場合、一括コピーの前に一致結果を確認します。

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern}
`*.jpg` をコピーする前に、パターンが現在一致する隠しファイル以外の名前を表示するコマンドはどれですか？

::option[`cp *.jpg`]{#copy-no-destination explanation="複数の名前が一致すると、明確なコピー先なしでコピーを試みます。確認操作ではありません。"}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="シェルが `ls` に対して同じパターンを展開するため、コピー前に一致する名前を確認できます。"}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="引用符がワイルドカード展開を防ぐため、`file` はリテラル文字列 `*.jpg` を受け取ります。通常の一致結果は確認できません。"}
:::

## ディレクトリツリーをコピーする

ディレクトリとその下のすべてをコピーするには、再帰操作が必要です。`-r` または `-R` を使います。

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

これは `Pumpkin` ディレクトリとその子孫を `Documents` へコピーします。

大文字の `-R` も再帰的なコピーを要求します。

```bash
$ cp -R website /home/pete/backups/
```

アーカイブモードの `-a` は、バックアップ形式のコピーに便利です。再帰的にコピーしながら、リンクや多数のファイル属性を保持します。

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree}
`project/` を再帰的にコピーし、リンクと多数の属性を保持するバックアップ形式のコピーには、どのコマンドが適していますか？

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p` は選択した属性を保持しますが、それだけではディレクトリコピーを再帰的にしません。"}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u` はコピー先の状態に応じてコピーする時期を制御しますが、それだけでは再帰的なディレクトリコピーになりません。"}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="アーカイブモードは再帰的なコピーを含み、バックアップ形式の結果になるようリンクと広範な属性を保持します。"}
:::

## 上書きを制御する

既定では、`cp` は既存のコピー先ファイルを置換できます。上書き前に確認するには `-i` を使います。

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

既存のコピー先を上書きしない場合は `-n` を使います。

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

`-f` は GNU `cp` に対し、既存のコピー先を書き込み用に開けない場合、その削除を試してコピーを再試行するよう指示します。対象を慎重に確認する代わりにはなりません。シェルのエイリアスが `-i` などのオプションを追加することもあるため、予期しないプロンプトが出たら設定を決めつけず調べてください。

:::single-choice{#skip-existing-destination}
`report.txt` を `backup/` へコピーし、同名のコピー先が存在すれば飛ばすコマンドはどれですか？

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="`-n` は `cp` が既存のコピー先ファイルを上書きするのを防ぎます。"}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i` は上書き前に尋ねるため、結果は回答次第です。既存のコピー先を必ず自動で飛ばすわけではありません。"}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f` は最初に開けないコピー先の置換に役立ちますが、上書き禁止の動作ではありません。"}
:::

## 属性を保持する、または新しいファイルだけをコピーする

`-p` でコピー元のモード、許可される場合は所有権、タイムスタンプを保持します。

```bash
$ cp -p mycoolfile /home/pete/backups/
```

コピー先が存在しないか、コピー元の方が新しい場合だけコピーするには `-u` を使います。

```bash
$ cp -u *.txt /home/pete/Documents/
```

そのほかの一般的なオプションには次のものがあります。

- `-f`：必要なら先にコピー先を削除し、上書きを強制する
- `-v`：コピーする各ファイルを表示する

ファイルとディレクトリツリーのコピーを練習するには、次のハンズオンラボを利用してください。

1. **[Linux cp コマンド：ファイルのコピー](https://labex.io/ja/labs/linux-linux-cp-command-file-copying-209744)**：基本操作、再帰コピー、属性保持、ワイルドカードなどを練習します。
2. **[ファイルとディレクトリの整理](https://labex.io/ja/labs/linux-organizing-files-and-directories-387877)**：`cp`、`mv`、`rm` でプロジェクト構造を整理し、ファイルを移動して不要なディレクトリを片付けます。

## まとめ

これでコピー先の扱いを制御しながら、ファイルとディレクトリツリーをコピーできるようになりました。

1. コピー元オペランドをコピー先より前に置く。
2. 一括コピー前にワイルドカードの一致結果を確認する。
3. ディレクトリツリーを再帰的またはアーカイブモードでコピーする。
4. 既存のコピー先を確認、飛ばす、意図的に置換する。
5. 必要に応じて属性を保持するか、新しいコピー元だけをコピーする。
