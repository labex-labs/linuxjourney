---
lesson_id: "history-command"
course_id: "command-line"
lang: "ja"
order_index: 9
title: "history コマンド"
description: "Bash でコマンド履歴を確認、検索、再利用、管理する方法を学びます。"
meta_title: "history - コマンドライン"
meta_description: "Linuxのhistoryコマンドを学び、コマンド履歴の表示、再実行、逆検索、エントリの削除、端末のクリア方法を例とともに解説します。"
meta_keywords: "linux history コマンド, bash history, history -c, history -d, history -w, Ctrl-R, コマンド履歴, clear コマンド"
---

対話型シェルは、入力したコマンドの記録を保持できます。このレッスンでは Bash を扱い、`history` 組み込みコマンドで記録を表示、管理します。ほかのシェルでは、ショートカット、ファイル、設定が異なる場合があります。

## Bash の履歴を表示する

`history` を実行して現在の履歴一覧を表示します。

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

各行には履歴番号とコマンドが含まれます。

:::single-choice{#show-command-history}
現在の番号付き履歴一覧を表示する Bash コマンドはどれですか？

::option[`clear`]{#clear-display explanation="`clear` は見えている端末領域を更新し、以前のコマンドは表示しません。"}
::option[`history -w`]{#write-history explanation="`history -w` は現在の一覧を履歴ファイルへ書き込みます。目的は表示ではなく保存です。"}
::option[`history`]{#show-history .correct explanation="`history` 組み込みコマンドは現在の履歴一覧にあるコマンドを、通常は履歴番号とともに表示します。"}
:::

## 以前のコマンドを再利用する

Bash には、コマンドを呼び出す、またはただちに実行するためのショートカットがあります。

- **上矢印**：以前のコマンドを呼び出し、確認または編集する
- **`!!`**：直近のコマンドへ展開して実行する
- **番号で実行**：`!102` で履歴番号 102 のコマンドを実行する
- **接頭辞で実行**：`!cat` で `cat` から始まる直近のコマンドを実行する

`!` で始まる履歴展開は、Enter を押すとすぐにコマンドを実行することがあります。特に権限を高める場合や重要なファイルを操作する前は、少しでも疑問があれば一致結果を先に確認してください。

:::single-choice{#repeat-most-recent-command}
直近に実行したコマンドを繰り返す Bash の履歴展開はどれですか？

::option[`!102`]{#event-number explanation="この展開は履歴番号 102 のコマンドを選びます。そのエントリが直近とは限りません。"}
::option[`!cat`]{#event-prefix explanation="これはテキストが `cat` で始まる直近のコマンドを選びます。種類を問わない直近のコマンドという意味ではありません。"}
::option[`!!`]{#previous-event .correct explanation="Bash の `!!` は、行を確定すると直前のコマンドへ展開して実行します。"}
:::

## 履歴を対話的に検索する

`Ctrl+R` を押して逆方向のインクリメンタル検索を始め、探すコマンドの一部を入力します。もう一度 `Ctrl+R` を押すと、さらに古い一致へ移動します。

Enter を押すと表示中の一致を実行します。先に確認または編集する場合は、矢印キーを使ってコマンドを編集行へ置きます。

:::single-choice{#search-before-executing}
以前の Bash コマンドの一部を覚えており、対話的に探したい場合、最初に何を押しますか？

::option[`Ctrl+D`]{#end-input explanation="多くの端末の文脈で `Ctrl+D` は入力終端を示し、待機中のシェルを終了することがあります。履歴検索は始めません。"}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` は通常、現在の操作を中断または取り消し、コマンド履歴は検索しません。"}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` はコマンド履歴の逆方向インクリメンタル検索を始め、文字を追加すると一致を絞り込みます。"}
:::

## 履歴一覧を管理する

`history` 組み込みコマンドは、現在の一覧を変更または保存できます。

- `history -c`：現在のメモリ内履歴一覧を消去する
- `history -w`：現在の一覧を、通常は `~/.bash_history` である設定済み履歴ファイルへ書き込む
- `history -d <offset>`：指定した履歴位置のエントリを削除する

例を示します。

```bash
$ history -d 101
$ history -w
```

メモリ内の一覧を消去しても、古いコマンドがすべてのファイル、バックアップ、ほかの動作中シェルから消えたとは限りません。履歴の動作は Bash の設定と、セッションがファイルを読み書きするタイミングにも依存します。

:::single-choice{#save-current-history-list}
現在の Bash 履歴一覧を設定済みの履歴ファイルへ書き込むコマンドはどれですか？

::option[`history -c`]{#clear-current-list explanation="`-c` はメモリ内の一覧を消去し、現在の一覧の保存は要求しません。"}
::option[`history -d 101`]{#delete-one-entry explanation="`-d` は選択した履歴エントリを 1 つ削除し、一覧全体を保存しません。"}
::option[`history -w`]{#write-current-list .correct explanation="`-w` は現在の履歴一覧を設定済みの履歴ファイルへ書き込みます。"}
:::

## 画面の消去と名前の補完

見えている端末領域を新しくしたい場合は `clear` を使います。

```bash
$ clear
```

Bash の履歴一覧は消去されません。端末によっては、以前の表示内容がスクロールバックに残ることもあります。

再入力を減らすには Tab 補完も使えます。コマンド、ファイル名、ディレクトリ名を入力し始めて Tab を押します。一意に決まれば Bash が補完し、複数候補があれば候補を表示することがあります。

コマンドラインは履歴へ保存されることがあるため、より安全な入力方法が利用できる場合、パスワード、トークン、そのほかの秘密情報をコマンドへ直接書かないでください。

:::single-choice{#distinguish-clear-from-history-clear}
メモリ内のコマンド履歴を削除せず、見えている端末を更新したい場合、どのコマンドを実行しますか？

::option[`clear`]{#clear-visible-area .correct explanation="`clear` は Bash のメモリ内履歴一覧を維持したまま、見えている端末領域を更新します。"}
::option[`history -c`]{#clear-memory explanation="これは現在のメモリ内履歴一覧からエントリを削除します。表示だけでなく履歴を変更します。"}
::option[`history -d 1`]{#delete-first-entry explanation="これは Bash に選択した履歴エントリの削除を要求し、見えている端末領域は消去しません。"}
:::

## まとめ

これで履歴を意図的に管理しながら、Bash コマンドを見つけて再利用できるようになりました。

1. 現在の番号付き履歴一覧を表示する。
2. 以前のコマンドを注意して呼び出す、または展開する。
3. `Ctrl+R` で履歴を対話的に検索する。
4. 履歴エントリを削除、消去、書き込みする。
5. コマンド履歴と端末表示を区別する。
