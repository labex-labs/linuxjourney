---
lesson_id: "list-directories-ls-command"
course_id: "command-line"
lang: "ja"
order_index: 4
title: "ls（ディレクトリの一覧表示）"
description: "`ls` のオプションを使い、ファイル、隠し項目、詳細、サイズ、並び順を確認する方法を学びます。"
meta_title: "ls（ディレクトリの一覧表示） - コマンドライン"
meta_description: "Linuxのlsコマンドを学び、ファイル一覧、隠しファイル、長い形式の出力、人間に読みやすいサイズ、ソート、オプションの組み合わせの例を紹介します。"
meta_keywords: "lsコマンド, linux ls, ファイル一覧 linux, ディレクトリ一覧, ls -a, ls -l, ls -lh, ls -r, 隠しファイル"
---

ファイルシステム内の移動方法が分かったら、利用できるものを調べましょう。`ls` コマンドはファイルとディレクトリを一覧表示し、現在位置または別のパスを確認できます。

## `ls` コマンドの基本的な使い方

既定では、`ls` は現在のディレクトリ内にあるディレクトリとファイルを一覧表示します。パスを指定し、別のディレクトリの内容を表示することもできます。

```bash
$ ls
$ ls /home/pete
```

特定のファイルも指定できます。

```bash
$ ls /etc/hosts
/etc/hosts
```

:::single-choice{#list-another-directory}
`/home/pete` へ移動せず、その内容を一覧表示するコマンドはどれですか？

::option[`ls /home/pete`]{#ls-target-path .correct explanation="`ls` にディレクトリパスを渡すと、その内容を一覧表示します。シェルは現在の作業ディレクトリにとどまります。"}
::option[`cd /home/pete`]{#cd-target-path explanation="`cd` はシェルの作業ディレクトリを変更し、それだけでは要求された一覧表示を行いません。"}
::option[`pwd /home/pete`]{#pwd-target-path explanation="`pwd` は現在の作業ディレクトリを報告し、一覧表示する目的地は受け取りません。代わりにパスを指定した `ls` を使います。"}
:::

## 隠しファイルを表示する

ディレクトリ内のすべてのファイルが既定で見えるわけではありません。Linux では、名前がドット（`.`）で始まるファイルは隠しファイルです。all を表す `-a` オプションで表示できます。

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

ドットファイルは既定で隠され、`.bashrc` のように設定を保存することがよくあります。

:::single-choice{#show-hidden-files}
隠しファイルを一覧に含めるコマンドはどれですか？

::option[`ls -l`]{#long-format explanation="`-l` は詳細な列を追加しますが、それだけでは隠しファイル名を含めません。"}
::option[`ls -r`]{#reverse-order explanation="`-r` は並び順を逆にしますが、隠しファイルを含めるかどうかは変えません。"}
::option[`ls -a`]{#all-files .correct explanation="`-a` は all を意味するため、ドットで始まる名前も `ls` の一覧に含まれます。"}
:::

## 詳細情報を表示する

もう 1 つ重要なオプションが、長い形式を表す `-l` です。ファイルのパーミッション、リンク数、所有者、グループ、サイズ、変更時刻、名前を表示します。

```bash
$ ls -l
```

出力例を示します。

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

サイズを読みやすくするには、human-readable を表す `-h` を追加します。

```bash
$ ls -lh
```

:::single-choice{#show-readable-file-details}
人が読みやすいサイズで長い形式の詳細を表示するコマンドはどれですか？

::option[`ls -la`]{#long-all explanation="これは長い形式と隠しファイルを組み合わせますが、人が読みやすいサイズ単位は要求しません。"}
::option[`ls -lh`]{#long-human-readable .correct explanation="`-l` が長い形式を選び、`-h` がサイズを読みやすくします。フラグは 1 つのコマンドで組み合わせられます。"}
::option[`ls -ltr`]{#long-time-reverse explanation="これは長い形式、変更時刻による並べ替え、逆順を組み合わせますが、サイズ用の `-h` は含みません。"}
:::

## 逆順に並べる

並び順を変えたい場合、`-r` オプションでファイルとディレクトリを逆順にします。

```bash
$ ls -r
```

`-t` で変更時刻順に並べ、`-r` で反転できます。

```bash
$ ls -lt
$ ls -ltr
```

:::single-choice{#show-newest-files-last}
変更時刻で並べ、最新の項目を最後にするコマンドはどれですか？

::option[`ls -ltr`]{#time-reversed .correct explanation="`-t` が変更時刻で並べ、`-r` がその順序を反転します。組み合わせると古い項目が新しい項目より前になります。"}
::option[`ls -lt`]{#time-default explanation="変更時刻で並べますが、既定の新しいものが先の方向を維持します。最新の項目を最後にはしません。"}
::option[`ls -lr`]{#reverse-name-order explanation="長い形式で既定の名前順を反転します。`-t` がないため、変更時刻は順序を制御しません。"}
:::

## コマンドのフラグを組み合わせる

コマンドには機能を追加するフラグ、つまりオプションがあります。`-a` と `-l` は `ls -la` のように 1 つのコマンドへまとめられます。フラグの順序は重要でないことが多く、`ls -al` も同じように動作します。

```bash
$ ls -la
```

便利な組み合わせには次のものがあります。

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

## 一般的な `ls` オプション

- `-a`：隠しファイルを含むすべてのファイルを表示する
- `-l`：長い形式を使う
- `-h`：`-l` とともに、人が読みやすいサイズを表示する
- `-r`：並び順を逆にする
- `-t`：変更時刻で並べる
- `-S`：ファイルサイズで並べる
- `-d`：ディレクトリの内容ではなく、ディレクトリ自体を一覧表示する

:::single-choice{#list-directory-entry-itself}
`projects/` の内容ではなく、そのディレクトリエントリ自体を表示するコマンドはどれですか？

::option[`ls -d projects/`]{#directory-entry .correct explanation="`-d` は `ls` に、ディレクトリを開いて内容を表示せず、エントリ自体を表示するよう指示します。"}
::option[`ls projects/`]{#directory-contents explanation="`-d` なしでディレクトリパスを渡すと、`ls` はその中の項目を表示します。"}
::option[`cd projects/`]{#change-to-directory explanation="`cd` は作業ディレクトリを変更し、要求されたディレクトリエントリを一覧表示しません。"}
:::

システムによっては、`ls` がファイルの種類ごとに異なる色で出力します。一般にエイリアスや環境設定による動作なので、色はシステムごとに異なる場合があります。

`ls` コマンドの理解を深めるには、次のハンズオンラボを利用してください。

- **[Linux ls コマンド：内容の一覧表示](https://labex.io/ja/labs/linux-linux-ls-command-content-listing-219205)**：`ls` でファイルとディレクトリの内容を効率よく一覧、分析し、詳細表示、隠しファイル、読みやすいサイズ、並べ替えの各オプションを練習します。

## まとめ

これで `ls` を使い、ディレクトリ内容を調べ、項目の表示方法を制御できるようになりました。

1. 現在のディレクトリまたは別のパスを一覧表示する。
2. 隠しファイルを一覧へ含める。
3. 読みやすいサイズで詳細情報を表示する。
4. 変更時刻で並べ、順序を反転する。
5. 内容ではなく、ディレクトリエントリ自体を表示する。
