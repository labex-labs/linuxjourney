---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "ja"
order_index: 11
title: "mv（移動）"
description: "意図しない上書きを避けながら、ファイルやディレクトリの名前を変更し、移動する方法を学びます。"
meta_title: "mv（移動） - コマンドライン"
meta_description: "Linuxのmvコマンドを学び、ファイルの移動、ファイルやディレクトリの名前変更、複数ファイルの移動、上書き回避の方法を例とともに解説します。"
meta_keywords: "linux mv コマンド, mv コマンド, linux ファイル移動, linux ファイル名前変更, linux ディレクトリ名前変更, mv -i, mv -n, mv -t"
---

`mv` コマンドは、ファイルやディレクトリの名前を変更するか、別の場所へ移動します。`cp` とは異なり、移動に成功した後は元のパス名を残しません。

基本構文は次のとおりです。

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## ファイルとディレクトリの名前を変更する

現在のパス名を先、新しいパス名を後に置きます。

ファイルの名前を変更します。

```bash
$ mv oldfile newfile
```

同じオペランド順でディレクトリ名も変更できます。

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} 現在のディレクトリで `cat` を `dog` へ名前変更するコマンドはどれですか？

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv` は `cat` をコピー元パス、`dog` を新しいコピー先パスとして扱います。"}
::option[`mv dog cat`]{#rename-dog explanation="オペランドの順序が逆で、既存の `dog` を `cat` へ名前変更しようとします。"}
::option[`cp cat dog`]{#copy-cat explanation="`cp` は `cat` を残したまま `dog` というコピーを作り、要求された名前変更にはなりません。"}
:::

## 項目をディレクトリへ移動する

最後のオペランドが既存ディレクトリなら、`mv` はその中へコピー元を置きます。

```bash
$ mv file2 /home/pete/Documents
```

複数のコピー元を移動するには、すべてを先に並べ、対象ディレクトリを最後に置きます。

```bash
$ mv file_1 file_2 somedirectory/
```

GNU `mv` には、対象ディレクトリをコピー元より前に置く `-t` もあります。

```bash
$ mv -t somedirectory/ file_1 file_2
```

`cp` とは異なり、`mv` でディレクトリを移動するために再帰オプションは必要ありません。

:::single-choice{#move-multiple-files} `file_1` と `file_2` の両方を、既存の `archive/` ディレクトリへ移動するコマンドはどれですか？

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="GNU `-t` がなければ、複数のコピー元を移動するときは対象ディレクトリを最後に置きます。これは標準の複数コピー元形式ではありません。"}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv` はファイルやディレクトリの移動に `-r` を使いません。通常の複数コピー元形式で処理できます。"}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="コピー元が複数ある場合、既存の対象ディレクトリを最後のオペランドに置き、両ファイルを受け取ります。"}
:::

## 既存のコピー先を制御する

既定では、`mv` は既存のコピー先を置換できます。実行前にコピー元とコピー先のパス名を確認し、必要に応じて上書き方針を選びます。

- `-i`：既存のコピー先を置換する前に確認する

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`：既存のコピー先を上書きしない

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`：GNU/Linux で、置換されるコピー先のバックアップを作る。既定の接尾辞は通常 `~`

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`：各移動を実行時に表示する

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} 既存のコピー先を上書きしない場合だけ、`draft.txt` を `finished/` へ移動するコマンドはどれですか？

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="`-i` はコピー先が存在する場合に処理を尋ね、確認すれば上書きできます。"}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="`-b` は以前のコピー先をバックアップしながら置換を許可し、上書き自体は防ぎません。"}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="`-n` は既存のコピー先を上書きする移動を飛ばします。"}
:::

## ディレクトリとワイルドカードの一致結果を移動する

`-r` なしでディレクトリを移動できます。

```bash
$ mv project /home/pete/Documents/
```

シェルのワイルドカードで複数のコピー元を選べます。

```bash
$ ls *.txt
$ mv *.txt notes/
```

`ls` で一致結果を確認すると、複数のパス名を変更する前に、広すぎるパターンへ気付けます。

:::single-choice{#move-directory-without-recursion} `project/` ディレクトリを `/srv/archive/` へ移動するコマンドはどれですか？

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv` はこの目的に `-r` を必要とせず、対応もしません。通常の移動操作でディレクトリを扱います。"}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="通常の `mv` 構文で、再帰フラグなしにディレクトリを既存の対象ディレクトリへ移動します。"}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="通常の `cp` はディレクトリを移動せず、コピーには再帰オプションが必要です。元のディレクトリも残ります。"}
:::

:::single-choice{#preview-text-file-move} `mv *.txt notes/` を実行する前に、同じワイルドカードが選ぶパス名を確認するコマンドはどれですか？

::option[`ls '*.txt'`]{#literal-text-pattern explanation="引用符が `*` の展開を防ぐため、移動対象ではなくアスタリスクを含むリテラル名を探します。"}
::option[`ls *.txt`]{#list-text-matches .correct explanation="シェルは `mv` と同様に `ls` の `*.txt` を展開し、選択される隠しファイル以外の名前を先に確認できます。"}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="詳細モードは移動の実行中に報告します。読み取り専用の確認ではなく操作を実行します。"}
:::

項目の移動と名前変更を練習するには、次のハンズオンラボを利用してください。

1. **[Linux mv コマンド：ファイルの移動と名前変更](https://labex.io/ja/labs/linux-linux-mv-command-file-moving-and-renaming-209743)**：`mv` でファイルとディレクトリを移動、名前変更し、オプションと動作を学びます。
2. **[ファイルとディレクトリの整理](https://labex.io/ja/labs/linux-organizing-files-and-directories-387877)**：`mv`、`cp`、`rm` を使い、プロジェクト構造を整理します。

## まとめ

これで既存のコピー先を保護しながら、ファイルやディレクトリの名前を変更、移動できるようになりました。

1. コピー元を新しいパス名より前に置く。
2. 複数のコピー元の後に対象ディレクトリを置く。
3. コピー先の置換前に確認、スキップ、バックアップを選ぶ。
4. 再帰オプションなしでディレクトリを移動する。
5. 一括移動前にワイルドカードの一致結果を確認する。
