---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "ja"
order_index: 12
title: "シンボリックリンク"
description: "シンボリックリンクとハードリンクについて、パス名解決、inode の同一性、ファイルシステムの範囲の違いを学びます。"
meta_title: "シンボリックリンク - ファイルシステム"
meta_description: "Linux のシンボリックリンク（シンリンク）とハードリンクを探求します。ln コマンドでの作成方法、ls でのリンク数の確認方法、そして ls でのシンボリックリンクとハードリンクの出力の違いを理解しましょう。"
meta_keywords: "Linux シンボリックリンク，ハードリンク，ln コマンド，シンリンク，ls シンボリックリンク，Linux リンク数，ls リンク，Linux ファイルシステム，Linux チュートリアル"
---

ディレクトリエントリは inode に名前を与えます。ハードリンクは同じ inode に対する別のディレクトリエントリを作成し、シンボリックリンクは解決すべきパス名を内容として持つ別の inode を作成します。この違いによって、同一性、寿命、ファイルシステムをまたぐ動作が決まります。

## シンボリックリンクを作成して調べる

`ln -s TARGET LINK_NAME` でシンボリックリンクを作成します。

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

シンボリックリンクは独自の inode を持ち、`myfile` というテキストを保存しています。プログラムが `myfilelink` をたどると、パス名解決はその対象へ続きます。リンクをたどらずに保存されたテキストを表示するには、次を使います。

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic}
対象テキストが `myfile` のシンボリックリンク `myfilelink` を作るコマンドはどれですか？

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="`-s` オプションはシンボリックリンクを要求し、その後に対象と新しいリンク名を指定します。"}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="`-s` がなければ、`ln` は既存 inode へのハードリンクを要求します。"}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="readlink はシンボリックリンクを調べるもので、作成はしません。"}
:::

## 相対パスと絶対パスのシンボリックリンク対象

絶対パスの対象は `/` から始まります。相対パスの対象はシンボリックリンクを含むディレクトリを基準に解決されます。後で誰かがリンクを開くときのシェルの現在のディレクトリではありません。

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

`tree` 階層全体を移動しても、この相対関係は保たれます。リンクまたは対象だけを移動すると壊れることがあります。存在しない対象をシンボリックリンクに保存することもでき、その状態を dangling link または broken link と呼びます。

:::single-choice{#symlinks-relative-resolution}
シンボリックリンクの相対的な対象は、どこを基準に解決されますか？

::option[作成したユーザーのホームディレクトリ。]{#symlinks-creator-home explanation="作成者の識別情報が、永続的な解決基準になることはありません。"}
::option[最初に一覧表示したシェルの現在のディレクトリ。]{#symlinks-listing-shell explanation="一覧表示時のコンテキストによって、保存された対象関係が書き換わることはありません。"}
::option[シンボリックリンクを含むディレクトリ。]{#symlinks-containing-directory .correct explanation="パス探索では、シンボリックリンクの位置で保存済みの相対テキストを置き換えます。"}
:::

## ハードリンクを作成する

`-s` を付けずに、既存の通常ファイルに別の名前を作成します。

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

両方の名前が、同じファイルシステムと inode 番号に対応します。リンク数は 2 になります。どちらかが本質的な「元ファイル」というわけではありません。一方の名前から内容を変更すると共有オブジェクトが変わり、一方を削除してももう一方は残ります。

inode 番号はそのファイルシステム内でだけ意味を持つため、ハードリンクはファイルシステムの境界を越えられません。また Linux は、循環やセキュリティ上の問題を防ぐため、一般ユーザーによるディレクトリへのハードリンクを制限し、所有していないファイルへのリンクも制限する場合があります。

:::single-choice{#symlinks-hard-link-inode}
1 つの通常ファイルに対する 2 つのハードリンクが共有するものは何ですか？

::option[似たファイル名だけで、ファイルデータは別々。]{#symlinks-separate-data explanation="それは独立したコピーであり、ハードリンクではありません。"}
::option[別のシンボリックリンク inode 内に保存されたパス名。]{#symlinks-stored-path explanation="パステキストを保存するのは、シンボリックリンクを特徴付ける仕組みです。"}
::option[同じ inode とファイル内容。]{#symlinks-same-inode .correct explanation="各ディレクトリエントリは、同一のファイルシステムオブジェクトに名前を付けます。"}
:::

## 寿命と削除

シンボリックリンクを削除すると、その対象ではなくリンクオブジェクトが削除されます。

```bash
$ rm -- myfilelink
```

ハードリンク名を削除すると、共有 inode のリンク数が減ります。リンク数が 0 になり、開いているファイル記述やほかのファイルシステム参照が残っていない場合にだけ、ファイルシステムはオブジェクトを回収できます。

ディレクトリへのシンボリックリンクを削除する際は、末尾にスラッシュを付けないでください。コマンドによっては、末尾のスラッシュによるパス解決でディレクトリとしてリンクをたどる場合があります。`ls -ld -- LINK` で調べ、リンク名を意図的に削除してください。

:::single-choice{#symlinks-remove-symbolic}
通常、シンボリックリンク自体を削除するとどうなりますか？

::option[シンボリックリンクの inode と名前が削除され、対象は残ります。]{#symlinks-remove-link-only .correct explanation="シンボリックリンクの unlink は、保存された対象テキストが指すオブジェクトを操作しません。"}
::option[対象と、それに対するすべてのハードリンクが自動的に消去されます。]{#symlinks-remove-target explanation="シンボリックリンクは別のファイルシステムオブジェクトであり、対象を所有していません。"}
::option[削除前に、対象がシンボリックリンクの中へコピーされます。]{#symlinks-copy-target explanation="削除時に、対象の内容がリンク内へ保存されることはありません。"}
:::

## リンクを安全にたどる

シンボリックリンクは、特権プログラムを想定外のディレクトリ外へ誘導したり、検証と使用の間に対象を変えたりできます。安全なプログラムでは、確認してから開くパス名競合を避け、言語とオペレーティングシステムに適した、ディレクトリ相対、リンク非追跡、解決範囲制限のインターフェースを使う必要があります。

日常的な調査には次を使います。

- `ls -ld LINK` はリンク自体を表示する
- `readlink LINK` は保存された対象テキストを出力する
- GNU coreutils では通常、`stat LINK` がリンクのメタデータを報告し、`stat -L LINK` はリンクをたどる
- `find -L` はリンクをたどるため循環に遭遇することがあり、意図した場合だけ使用する

`lrwxrwxrwx` と表示されるパーミッションは、一般的なアクセス許可を意味しません。アクセスは、ディレクトリの探索、リンク追跡方針、対象のパーミッションによって決まり、一部の保護ディレクトリ規則ではシンボリックリンクの所有権も関係します。

:::single-choice{#symlinks-readlink-output}
既定で `readlink LINK` が出力するものは何ですか？

::option[シンボリックリンクに保存されたパス名テキスト。]{#symlinks-readlink-target-text .correct explanation="対象ファイルの内容を読まず、リンクオブジェクトを調べます。"}
::option[対象となる通常ファイルの全バイト内容。]{#symlinks-readlink-file-content explanation="対象の内容には、意図的に解決した後でファイル読み取りコマンドを使います。"}
::option[ファイルシステム上にあるすべてのハードリンク。]{#symlinks-readlink-all-hard explanation="ハードリンクの探索には inode を考慮したファイルシステム検索が必要で、シンボリックリンクの対象テキストとは無関係です。"}
:::

使い捨てのファイルでリンクを練習し inode 番号を比較するには、[Linux でファイルとディレクトリを管理する](https://labex.io/ja/labs/comptia-manage-files-and-directories-in-linux-590835) を利用してください。

## まとめ

これで、適切な種類のファイルシステムリンクを選び、調べられるようになりました。

1. パス名に基づくシンボリックリンクには `ln -s TARGET LINK` を使う。
2. 相対的な対象は、リンクを含むディレクトリを基準に解決する。
3. 同じファイルシステムの inode に別名を付けるには `ln EXISTING LINK` を使う。
4. シンボリックリンクの unlink とハードリンクの unlink を区別する。
5. 特権操作や再帰操作では、安全でないリンク追跡を避ける。
