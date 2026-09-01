---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "ja"
order_index: 9
title: "tail"
description: "入力の末尾を表示し、ファイルへ追記される新しい内容を継続して確認する方法を学びます。"
meta_title: "tail - テキスト操作"
meta_description: "tail コマンドの初心者向け Linux ガイド。Linux tail の使い方を学び、強力な tail -f オプションでファイルの末尾を表示したり、ログをリアルタイムで監視する方法を習得します。"
meta_keywords: "tail コマンド，Linux tail, tail -f, ログ表示，ログ監視，Linux チュートリアル，初心者 Linux, Linux ガイド，ファイル監視"
---

`tail` コマンドはファイルや入力ストリームの末尾を表示します。動作を続けてファイルへ追記されたデータを表示することもでき、ログの観察に便利です。

## 末尾の 10 行を表示する

件数オプションがなければ、`tail` は指定した各ファイルの末尾 10 行を表示します。

```bash
$ tail application.log
```

10 行未満なら存在する全行を表示し、ファイル自体は変更しません。

:::single-choice{#tail-default-lines} `tail application.log` は標準で何を表示しますか？

::option[ファイル先頭から最大 10 行。]{#tail-first-ten explanation="ファイル先頭を選ぶのは `head` で、`tail` は末尾から処理します。"}
::option[コマンド開始後に追加されたすべての行。]{#tail-follow-only explanation="継続的な追跡には `-f` などが必要で、通常の `tail` はスナップショットを表示して終了します。"}
::option[ファイル末尾から最大 10 行。]{#tail-last-ten .correct explanation="件数オプションがなければ末尾 10 行を選び、少ない場合は全行を表示します。"}
:::

## 行数またはバイト数を選ぶ

末尾から異なる行数を選ぶには `-n NUMBER`、バイト数なら `-c NUMBER` を使います。

```bash
$ tail -n 20 application.log
```

```bash
$ tail -c 100 payload.bin
```

バイトモードはテキスト行や符号化文字の途中から始まることがあるため、テキストには通常、行モードが明確です。

:::single-choice{#tail-twenty-lines} `application.log` の末尾 20 行を表示するコマンドはどれですか？

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="`-n` は行数を選び、`tail` は末尾からその行数を取得します。"}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="これは末尾ではなく先頭から 20 行を選びます。"}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="`-c` は末尾 20 バイトを選び、20 行とは異なります。"}
:::

## 特定の行から開始する

`+` の付いた件数は意味が変わり、`tail -n +N` は N 行目から末尾まで表示します。

```bash
$ tail -n +5 report.txt
```

これは先頭 4 行を飛ばして 5 行目から開始します。既知のヘッダー行数をストリームから除くときに便利です。

:::single-choice{#tail-start-line-five} `report.txt` を 5 行目から表示するコマンドはどれですか？

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="`+5` は 5 行目から開始し、末尾まで続けるよう `tail` に指示します。"}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="プラス記号がなければ、絶対的な行番号に関係なく末尾 5 行を選びます。"}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="これは `tail` の開始行指定ではありません。要求された範囲には `tail -n +5` を使います。"}
:::

## 追記されるデータを追跡する

`-f` を使うと最初の末尾を表示した後も動作を続け、追記されたデータを表示します。

```bash
$ tail -f application.log
```

`Ctrl+C` で `tail` を中断してシェルへ戻ります。ファイルの追跡は新しい内容を表示するだけで、ログを生成するアプリケーションの正常性や、すべての関連イベントがそのファイルへ入ることを保証しません。

:::single-choice{#tail-follow-file} `application.log` の現在の末尾を表示し、追記される内容を待ち続けるコマンドはどれですか？

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="`-f` は `tail` の動作を継続し、ファイルへ追記されたデータを表示します。"}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="最初に 0 行を表示し、追跡オプションがないため終了します。"}
::option[`less application.log`]{#less-log explanation="`less` は対話的にページ表示しますが、この形式は `tail` のような追跡モードを続けません。"}
:::

## ローテーションされたログを名前で追跡する

ログローテーションでは古いファイルを改名し、元のパスに新しいファイルを作ることがあります。GNU `tail -F` は名前で追跡しながら再試行するため、置換されたファイルや一時的に見つからないファイルを再度開けます。

```bash
$ tail -F application.log
```

現在開いているファイルを追跡するなら `-f`、名前付きログがローテーションされるなら `-F` を使います。これは GNU の動作で、他の実装は異なることがあります。

:::single-choice{#tail-follow-rotated-name} GNU/Linux で、一般的な改名と再作成によるローテーションをまたいで `application.log` を追うのに適したオプションはどれですか？

::option[`-n`]{#tail-rotation-lines explanation="`-n` は表示行数を変え、置き換えられたパスを再試行しません。"}
::option[`-c`]{#tail-rotation-bytes explanation="`-c` は選択単位をバイトへ変え、ローテーション対応の追跡はしません。"}
::option[`-F`]{#tail-follow-name .correct explanation="GNU の `-F` は名前で追跡して再試行し、置換または一時的に消えたログを開き直せます。"}
:::

ファイル名がなければ `tail` は stdin を読み、コマンド出力の末尾を選べます。複数ファイルには `head` と同様、標準で識別用ヘッダーが付きます。

ファイル末尾の表示と追跡を練習するには、次のラボを試してください。

1. **[Linux tail コマンド：ファイル末尾の表示](https://labex.io/ja/labs/linux-linux-tail-command-file-end-display-214303)** - `tail` と `-f` でテキストファイルの末尾を表示、監視します。
2. **[Linux でログと設定ファイルを表示する](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `tail`、`cat`、`more` でログや設定を確認します。
3. **[迅速な脅威検知](https://labex.io/ja/labs/linux-rapid-threat-detection-387930)** - `tail` で最近のログ項目を抽出し、分析します。

## まとめ

`tail` でファイル末尾を確認し、新しく追記された内容を観察できるようになりました。

1. 標準では末尾 10 行を表示する。
2. 行数またはバイト数を明示的に選ぶ。
3. `-n +N` で番号付きの行から出力を開始する。
4. `-f` で追記を追跡し、`Ctrl+C` で停止する。
5. 名前付きログがローテーションされる場合は GNU `-F` を使う。
