---
lesson_id: "head-command"
course_id: "text-fu"
lang: "ja"
order_index: 8
title: "head コマンド"
description: "入力の先頭から表示する行数またはバイト数を制御する方法を学びます。"
meta_title: "head コマンド - Text-Fu"
meta_description: "head コマンドを使用してファイルの先頭を表示する方法についての初心者向け Linux ガイド。行数を制御するための head -n オプションの使い方を学び、あらゆる Linux チュートリアルで不可欠なスキルを習得しましょう。"
meta_keywords: "head コマンド，Linux head, ファイル先頭表示，Linux チュートリアル，Linux コマンド，初心者 Linux, head -n, Linux ガイド，テキストファイル，コマンドライン"
---

`head` コマンドは、ファイルや入力ストリームの先頭を表示します。ヘッダーの確認、構造化データのプレビュー、出力全体を表示せずに一部を抽出するときに便利です。

## 先頭の 10 行を表示する

件数オプションを指定しない場合、`head` は指定した各ファイルの先頭 10 行を表示します。

```bash
$ head events.log
```

ファイルは変更されません。10 行未満なら、存在するすべての行が表示されます。

:::single-choice{#head-default-lines} `head events.log` は標準で何を表示しますか？

::option[末尾の 10 行。ファイルが短ければ全行。]{#head-last-ten explanation="入力の末尾を表示するのは `tail` の役割です。`head` は先頭から選びます。"}
::option[先頭の 10 行。ファイルが短ければ全行。]{#head-first-ten .correct explanation="件数オプションがなければ、`head` は入力の先頭から最大 10 行を選びます。"}
::option[ファイルの長さにかかわらず先頭の 1 行だけ。]{#head-first-one explanation="1 行には `-n 1` など明示的な件数が必要で、標準は 10 行です。"}
:::

## 行数を選ぶ

表示する行数は `-n NUMBER` で指定します。

```bash
$ head -n 15 events.log
```

GNU `head` は短縮形 `-15` も受け付けますが、`-n 15` のほうがオプションの意味を明確に表します。

:::single-choice{#head-five-lines} `report.txt` の先頭 5 行を表示するコマンドはどれですか？

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="`-c` は行ではなくバイトを数えるため、最初の行の途中で終わることがあります。"}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="`-n` は行数を選び、`5` は先頭 5 行を要求します。"}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="これは先頭ではなくファイル末尾の 5 行を表示します。"}
:::

## バイト数を選ぶ

完全な行ではなくバイトが必要な場合は `-c NUMBER` を使います。

```bash
$ head -c 20 archive.bin
```

これは先頭 20 バイトを表示します。テキスト行やマルチバイト文字の途中で出力が終わることがあるため、通常のテキストプレビューには行モードを使います。

:::single-choice{#head-first-bytes} `payload.bin` の先頭 100 バイトを stdout へ書くコマンドはどれですか？

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="`-c` はバイト数を選ぶため、存在する先頭 100 バイトを要求します。"}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="`-n` はバイトではなく行を数え、100 バイトより大幅に多くも少なくもなり得ます。"}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="入力全体の先頭 100 バイトではなく、各行の位置 100 を選びます。"}
:::

## stdin と複数ファイルから読む

ファイルオペランドがなければ `head` は stdin を読みます。

```bash
$ generate-report | head -n 5
```

複数ファイルを指定すると、通常は各ファイルの出力を識別するヘッダーが付きます。

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

ヘッダーを抑制するには `-q`、1 ファイルでも表示するには `-v` を使います。

:::single-choice{#head-pipeline-preview} `generate-report | head -n 5` で `head` は何を読みますか？

::option[stdin を通じて `generate-report` の stdout を読む。]{#head-pipe-input .correct explanation="パイプが生成側の stdout を `head` の stdin へ接続し、そこから先頭 5 行を選びます。"}
::option[現在のディレクトリにある先頭 5 個のファイル名を読む。]{#head-directory-names explanation="ディレクトリ一覧のコマンドはなく、`head` はパイプからストリームを受け取ります。"}
::option[`generate-report` というファイルから 5 バイト読む。]{#head-producer-file explanation="左側はコマンドとして実行され、`-n` はバイトではなく行を数えます。"}
:::

:::single-choice{#head-suppress-filename-headers} `head` が複数ファイルを読むとき、ファイル名ヘッダーを抑制するオプションはどれですか？

::option[`-v`]{#head-verbose explanation="`-v` は 1 ファイルだけでもヘッダーを表示するため、抑制とは逆です。"}
::option[`-c`]{#head-byte-option explanation="`-c` は選択単位をバイトへ変え、ファイル名ヘッダーは制御しません。"}
::option[`-q`]{#head-quiet .correct explanation="`-q`（quiet）は `head` がファイルごとのヘッダーラベルを表示しないようにします。"}
:::

ファイル先頭のプレビューを練習するには、次のラボを試してください。

1. **[Linux head コマンド：ファイル先頭の表示](https://labex.io/ja/labs/linux-linux-head-command-file-beginning-display-214302)** - `head` でテキストファイルの先頭行を表示し、行数を変更します。
2. **[Linux でログと設定ファイルを表示する](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `head` などでログや設定ファイルを効率よく確認します。
3. **[迅速な脅威検知](https://labex.io/ja/labs/linux-rapid-threat-detection-387930)** - `head` と `tail` でログ項目を抽出し分析します。

## まとめ

`head` でファイルやコマンド出力の先頭をプレビューできるようになりました。

1. 標準の先頭 10 行表示を使う。
2. `-n` で行数を選ぶ。
3. 必要に応じて `-c` でバイト数を選ぶ。
4. パイプラインで stdin から読む。
5. 複数ファイル表示時のヘッダーを制御する。
