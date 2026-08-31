---
lesson_id: "less-command"
course_id: "command-line"
lang: "ja"
order_index: 8
title: "less"
description: "`less` を使い、長いテキストファイルを対話的に移動、検索、追跡する方法を学びます。"
meta_title: "less - コマンドライン"
meta_description: "大きなファイルの閲覧、スクロール、検索、行ジャンプ、ログの追跡、終了方法など、Linuxのlessコマンドを例とともに学びましょう。"
meta_keywords: "less コマンド, linux less, 大きなファイル閲覧 linux, less で検索, less 終了, less -N, less +F, テキストビューア linux"
---

テキストファイルが 1 画面に収まらない場合、`less` を使うと、ファイル全体を端末へ流さずに読めます。`more` もページャーの 1 つであることから、名前は古い Unix の冗談「less is more」の由来になりました。

## ファイルを開く

ファイル名を渡してページャーを起動します。

```bash
$ less /home/pete/Documents/text1
```

`less` の動作中は、キー入力が通常のシェルコマンドを始めるのではなく、ページャーを制御します。ページャーを終了するとシェルへ戻ります。

:::single-choice{#open-long-file}
`/var/log/syslog` を対話型ページャーで開くコマンドはどれですか？

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less` はファイルをページャーで開き、その中を移動、検索し、終了してシェルへ戻れます。"}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat` はファイル全体を一度に標準出力へ送信し、対話型のページ操作は提供しません。"}
::option[`file /var/log/syslog`]{#classify-log explanation="`file` は内容の種類を推定して報告し、ログを対話的に読むためには開きません。"}
:::

## `less` 内を移動する

ページャーを開いている間は次のキーを使います。

- `上`、`下`、`Page Up`、`Page Down` で行または画面を単位に移動する
- `g` で先頭へ移動する
- `G` で末尾へ移動する
- `u` で半画面上、`d` で半画面下へ移動する
- `h` で組み込みヘルプを開く

:::single-choice{#jump-to-file-end}
`less` でファイル末尾へ直接移動するキーはどれですか？

::option[`g`]{#lowercase-g explanation="小文字の `g` はファイルの先頭へ移動し、大文字は反対方向へ移動します。"}
::option[`G`]{#uppercase-g .correct explanation="大文字の `G` は入力の末尾へ移動します。このコマンドは大文字と小文字を区別します。"}
::option[`h`]{#help-key explanation="`h` はページャーのヘルプ画面を開き、ファイル末尾へは移動しません。"}
:::

## `less` 内を検索する

`/` に続いてパターンを入力し Enter を押すと前方検索、`?` から始めると後方検索になります。

- `/search_term`：`search_term` を前方検索する
- `?search_term`：`search_term` を後方検索する
- `n`：同じ方向へ検索を繰り返す
- `N`：反対方向へ検索を繰り返す

:::single-choice{#repeat-search-direction}
`error` を前方検索した後、同じ方向へ検索を繰り返すキーはどれですか？

::option[`n`]{#same-search .correct explanation="小文字の `n` は直近の検索を元の方向へ繰り返します。ここでは前方です。"}
::option[`N`]{#opposite-search explanation="大文字の `N` は直近の検索を反対方向へ繰り返します。前方検索の後なら、一致箇所を後方へ移動します。"}
::option[`g`]{#search-to-start explanation="`g` は入力の先頭へ移動し、検索を繰り返しません。"}
:::

## `less` を終了する

`q` を押すと `less` を終了し、シェルプロンプトへ戻ります。

:::single-choice{#quit-less}
`less` を終了してシェルへ戻るキーはどれですか？

::option[`q`]{#less-quit .correct explanation="`q` コマンドはページャーを終了し、シェルプロンプトを復元します。"}
::option[`h`]{#less-help explanation="`h` は `less` 内のヘルプを開き、直接シェルへは戻りません。"}
::option[`G`]{#less-end explanation="大文字の `G` は入力末尾へ移動しますが、ページャーは開いたままです。"}
:::

## オプションを付けて `less` を起動する

オプションと初期コマンドで、ページャーの開始方法を変えられます。

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`：行番号を表示する
- `+G`：ファイル末尾から開く
- `+F`：`tail -f` のように、追加される新しい内容を追跡する

`+F` でファイルを追跡している間に `Ctrl+C` を押すと、追跡を止めて通常の移動へ戻ります。その後 `q` で終了します。`-i` はパターンに大文字が含まれない限り大文字と小文字を区別せず検索し、`-I` はパターンに関係なく区別しません。

コマンド出力をパイプで `less` へ送ることもできます。

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log}
`/var/log/syslog` を開き、新しい内容が届くたびに追跡するコマンドはどれですか？

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="`+F` 初期コマンドは追跡モードへ入り、ログへ追加された新しい内容を `less` が表示します。"}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="`+G` は末尾から開きますが、その後に届く内容を継続して追跡しません。"}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="`-N` は行番号を表示しますが、継続的な追跡は有効にしません。"}
:::

ページ操作、検索、システムテキストの読み取りを練習するには、次のハンズオンラボを利用してください。

1. **[Linux less コマンド：ファイルのページ表示](https://labex.io/ja/labs/linux-linux-less-command-file-paging-214301)**：検索、行番号、パターンマッチングを含め、`less` で効率よくテキストファイルを表示して移動する方法を学びます。
2. **[Linux でログと設定ファイルを表示する](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)**：`cat`、`more`、`less` などで、システムログと設定ファイルを効率よく表示、移動する方法を学びます。

## まとめ

これで端末を大量の出力で埋めず、`less` で長いファイルを調べられるようになりました。

1. ファイルまたはパイプで送られたコマンド出力をページャーで開く。
2. 入力内の特定の位置へ移動する。
3. 前方または後方を検索し、検索を繰り返す。
4. 行番号を表示するか、増え続ける内容を追跡する。
5. 安全に終了してシェルへ戻る。
