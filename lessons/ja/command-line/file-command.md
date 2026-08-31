---
lesson_id: "file-command"
course_id: "command-line"
lang: "ja"
order_index: 6
title: "file コマンド"
description: "名前や拡張子に頼らず、ファイルに含まれる可能性が高いデータの種類を識別する方法を学びます。"
meta_title: "file コマンド - コマンドライン"
meta_description: "Linuxのfileコマンドを使って、テキストファイル、画像、スクリプト、圧縮アーカイブ、バイナリ、MIMEタイプを識別する方法を例とともに学びましょう。"
meta_keywords: "linux file コマンド, file コマンド, ファイルタイプ識別 linux, mime タイプ linux, テキストファイル, バイナリファイル, アーカイブファイル"
---

前のレッスンでは `touch` を使い、拡張子を付けずにファイルを作成しました。Linux のファイル名は、内容を表す必要がありません。`funny.gif` というファイルが、必ずしも GIF 画像とは限りません。

`file` コマンドでファイルを調べ、種類の推定結果を報告できます。

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

## ファイル拡張子だけでは不十分な理由

Linux のツールは通常、ファイルの種類を判断するために拡張子を必要としません。シェルスクリプトを `backup`、テキストファイルを `README` と名付けることができ、画像に誤解を招く拡張子を付けることもできます。`file` コマンドは、ファイルシステムのメタデータや内容に含まれる認識可能なパターンなどを調べます。

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

結果は分類であり、保証ではありません。特殊、不完全、または損傷したファイルは、正確な種類ではなく `data` のような広い説明になる場合があります。

:::single-choice{#identify-misleading-extension}
`report.jpg` というファイルに画像が入っているとは限りません。内容の種類を推定するコマンドはどれですか？

::option[`ls report.jpg`]{#list-report explanation="`ls` は名前の存在を確認し、メタデータを表示できますが、ファイル内容の種類は分類しません。"}
::option[`file report.jpg`]{#inspect-report .correct explanation="`file` コマンドはファイルを調べ、推定した種類を報告します。`.jpg` という接尾辞だけには依存しません。"}
::option[`touch report.jpg`]{#touch-report explanation="`touch` はタイムスタンプを更新するか、存在しないファイルを作ります。内容の種類は識別しません。"}
:::

## 複数のファイルを確認する

一度に複数のファイルを確認できます。

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

シェルのワイルドカードも渡せます。シェルが `file` の実行前に `*` を一致する名前へ展開します。

```bash
$ file *
```

:::single-choice{#inspect-multiple-files}
現在のディレクトリで、`*` に一致する隠しファイル以外のすべての名前を `file` に調べさせるコマンドはどれですか？

::option[`file *`]{#file-wildcard .correct explanation="シェルが `*` を一致する隠しファイル以外の名前へ展開し、`file` が得られた各オペランドを調べます。"}
::option[`file .`]{#file-current-directory explanation="1 つのドットは現在のディレクトリ自体を表します。その中の各項目ではなく、そのディレクトリを分類します。"}
::option[`file -b`]{#file-brief-no-operand explanation="`-b` は出力形式を変えますが、このコマンドには調べるファイルが指定されていません。"}
:::

## MIME 情報を表示する

`-i` オプションは、メディアタイプと、分かる場合は文字セットを含む MIME 形式の情報を表示します。別のプログラムが `text/html` のような値を求める場合に便利です。

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

:::single-choice{#show-mime-information}
`index.html` の MIME 形式の情報を報告するコマンドはどれですか？

::option[`file -b index.html`]{#brief-index explanation="`-b` は通常の説明からファイル名を省きますが、MIME 形式の出力は要求しません。"}
::option[`file -i index.html`]{#mime-index .correct explanation="`-i` は `text/html` と文字セット情報のような MIME 形式の出力を要求します。"}
::option[`file -L index.html`]{#follow-index explanation="`-L` はシンボリックリンクの扱いを制御し、MIME 出力形式は選びません。"}
:::

## 便利な `file` オプション

- `-i`：MIME 形式の情報を表示する
- `-b`：簡潔なモードを使い、出力からファイル名を省く
- `-L`：シンボリックリンクをたどり、その対象を分類する
- `-z`：圧縮ファイルの内容を調べるよう試みる

たとえば次のようにします。

```bash
$ file -b notes.txt
ASCII text
```

:::single-choice{#omit-filename-from-output}
`notes.txt` を分類し、出力からファイル名を省くコマンドはどれですか？

::option[`file -i notes.txt`]{#mime-notes explanation="`-i` は MIME 形式の情報を要求し、通常は出力にファイル名も含みます。"}
::option[`file -z notes.txt`]{#compressed-notes explanation="`-z` は可能な場合に圧縮データの中を調べ、簡潔な出力は有効にしません。"}
::option[`file -b notes.txt`]{#brief-notes .correct explanation="`-b` で選ぶ簡潔なモードは、ファイル名の接頭辞なしで分類結果を表示します。"}
:::

## まとめ

これで `file` を使い、ファイルに何が含まれる可能性が高いかを調べられるようになりました。

1. 拡張子を信用せず、ファイルを分類する。
2. 1 つのコマンドで複数のパス名を調べる。
3. MIME 形式の情報を要求する。
4. リンク、圧縮データ、出力ラベルの扱いを調整する。
