---
lesson_id: "exit-command"
course_id: "command-line"
lang: "ja"
order_index: 19
title: "exit コマンド"
description: "現在のシェルを終了し、呼び出し元へ返す終了状態を選ぶ方法を学びます。"
meta_title: "exit - コマンドライン"
meta_description: "Linuxのexitコマンドの使い方、シェルセッションの終了方法、logoutとの違い、終了ステータスの仕組みを学びましょう。"
meta_keywords: "exit コマンド, linux exit, logout コマンド, シェルセッション, ターミナル終了, 終了ステータス, bash exit"
---

シェルは入れ子にできます。グラフィカル端末がシェルを起動し、SSH 接続がリモートシェルを起動し、シェルから別のシェルを起動できます。1 つを終了すると、通常は現在のシェルを起動したものへ制御が戻ります。

## 現在のシェルを終了する

`exit` コマンドは現在のシェルへ終了を要求します。

```bash
$ exit
```

そのシェルがグラフィカル端末タブの主プロセスなら、端末の設定に従ってタブが閉じることがあります。SSH セッションでは、リモートシェルを終了すると通常はローカルシェルへ戻ります。入れ子のシェルを起動した場合、`exit` は親シェルへ戻ります。

:::single-choice{#leave-current-shell}
別のシェル内で Bash を起動し、親シェルへ戻りたい場合、入れ子の Bash セッションでどのコマンドを実行しますか？

::option[`clear`]{#clear-nested explanation="`clear` は見えている端末領域を更新しますが、現在のシェルを動作させたままにします。"}
::option[`exit`]{#exit-nested .correct explanation="`exit` は現在のシェルを終了し、親シェルが処理を再開できるようにします。"}
::option[`history -c`]{#clear-nested-history explanation="これは Bash のメモリ内履歴一覧を消去し、現在のシェルは終了しません。"}
:::

## 終了状態を返す

任意の数値引数で、シェルの呼び出し元へ返す状態を設定します。

```bash
$ exit 0
```

慣例として `0` は成功、0 以外の値は失敗またはプログラムが定義する別の状態を表します。数値引数なしの場合、Bash は `exit` より前に実行された最後のコマンドの状態で終了します。

:::single-choice{#return-success-status}
現在のシェルを終了し、呼び出し元へ明示的に成功を報告するコマンドはどれですか？

::option[`exit 0`]{#exit-zero .correct explanation="状態 `0` は慣例として、呼び出し元へ正常終了を報告します。"}
::option[`exit 1`]{#exit-one explanation="0 以外の状態は慣例として、成功ではなく失敗または別の例外的結果を示します。"}
::option[`logout 0`]{#logout-zero explanation="Bash の `logout` はログインシェル用で、この形式で要求された状態は設定しません。"}
:::

:::single-choice{#exit-without-number}
Bash で数値を指定しない `exit` は、どの状態を返しますか？

::option[常に成功状態の `0` を返します。]{#always-zero explanation="成功の慣例が、引数なしの `exit` を必ず 0 にするわけではありません。この場合 Bash は以前の状態を保持します。"}
::option[常に失敗状態の `1` を返します。]{#always-one explanation="Bash はすべての引数なし `exit` へ失敗状態 1 を割り当てず、直前のコマンドが値を決めます。"}
::option[直前のコマンドの終了状態を返します。]{#last-command-status .correct explanation="明示的な数値引数がなければ、Bash は直近のコマンド状態を使って終了します。"}
:::

## ログインシェルで `logout` を使う

Bash の `logout` 組み込みコマンドはログインシェルを終了します。

```bash
$ logout
```

非ログイン Bash シェルでは、`logout` はログインシェルではないと報告します。代わりに `exit` を使います。

:::single-choice{#leave-login-shell}
ログインシェルを終了するために特に用意された Bash 組み込みコマンドはどれですか？

::option[`logout`]{#logout-login .correct explanation="Bash はログインシェルを終了するために `logout` を提供します。"}
::option[`unalias`]{#unalias-login explanation="`unalias` は現在のシェルからエイリアス定義を削除し、セッションは終了しません。"}
::option[`source`]{#source-login explanation="`source` はファイルからコマンドを現在のシェルへ読み込み、そのシェルを終了しません。"}
:::

## `Ctrl+D` または端末を閉じる

空の対話型プロンプトで `Ctrl+D` を押すと、通常は端末のファイル終端入力文字が送られます。Bash は一般にその状態を終了要求として解釈します。シグナルではなく、Bash の `ignoreeof` などの設定で動作が変わることがあります。

グラフィカル端末のウィンドウを閉じると、端末アプリケーションがプロセスの終了を要求し、実行中のジョブに影響することがあります。可能なら秩序ある `exit` を使い、セッションを閉じる前に実行中の作業を確認してください。

## まとめ

これで現在のシェルを終了し、その完了状態を伝えられるようになりました。

1. `exit` で現在のシェルの呼び出し元へ戻る。
2. 成功には `0`、それ以外には定義済みの 0 以外の状態を指定する。
3. 引数なしの `exit` が使う状態を理解する。
4. `logout` はログインシェルだけに使う。
5. `Ctrl+D` をシグナルではなくファイル終端入力として認識する。
