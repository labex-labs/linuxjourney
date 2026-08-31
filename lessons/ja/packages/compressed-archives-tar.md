---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "ja"
order_index: 3
title: "tar と gzip"
description: "`tar` でファイルをアーカイブし、`gzip` でストリームを圧縮し、安全な展開前にアーカイブを検査する方法を学びます。"
meta_title: "tar と gzip - パッケージ"
meta_description: "Linux での tar と gzip の使用に関する包括的なガイド。tar 圧縮、アーカイブの作成と抽出方法、gzip と tar の違いを学びます。tar.gz ファイルを圧縮し、ソフトウェアパッケージを効果的に管理するためのコマンドを習得しましょう。"
meta_keywords: "tar と gzip, tar 圧縮，gzip tar, tar gz 圧縮，gzip と tar, Linux アーカイブ，ファイル圧縮，tar コマンド，gzip コマンド，Linux チュートリアル"
---

アーカイブと圧縮は別の問題を解決します。アーカイブはディレクトリツリーとそのメタデータを一つのストリームへまとめます。圧縮はストリームを符号化してサイズを減らします。`.tar.gz` ファイルは慣例として、ストリームを gzip で圧縮した tar アーカイブです。

## `gzip` で一つのストリームを圧縮する

`gzip` は既定ではファイルを圧縮し、元の名前を `.gz` ファイルへ置き換えます。

```bash
$ gzip report.txt
```

通常、`report.txt.gz` の作成に成功すると `report.txt` は削除されます。展開には次を使います。

```bash
$ gunzip report.txt.gz
```

対応している環境で入力ファイルを残すには `gzip -k report.txt` を使い、明示的に制御する必要がある場合は標準ストリームを使います。ファイル名の拡張子は慣習であり、実際の形式の証明ではありません。`file` などのツールで内容を調べられます。

:::single-choice{#tar-gzip-gzip-role}
このレッスンにおける `gzip` の主な役割は何ですか？

::option[ファイルメタデータとともにディレクトリツリーを一つのアーカイブへまとめる。]{#tar-gzip-directory-archive explanation="gzip 圧縮を適用する前に、そのアーカイブ処理を行うのは tar です。"}
::option[一つの入力ストリームを圧縮する。]{#tar-gzip-compress-stream .correct explanation="Gzip は一つのバイトストリームを変換し、それ自体でディレクトリ階層を符号化しません。"}
::option[依存関係メタデータをパッケージデータベースへインストールする。]{#tar-gzip-package-install explanation="圧縮は、ネイティブパッケージのインストールや依存関係追跡とは別です。"}
:::

## Tar アーカイブを作成する

非圧縮アーカイブは次のように作成します。

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` は新しいアーカイブを作成します。
- `-v` は処理中のメンバーを一覧表示する任意のオプションです。
- `-f project.tar` はアーカイブファイルを指定します。`-f` は引数を一つ取るため、ファイル名をその隣に置きます。

パスはアーカイブのメンバー名として保存されます。意図した作業ディレクトリからアーカイブを作成し、機密情報、キャッシュ、ソケット、広範な絶対パスを誤って含めないようにしてください。

:::single-choice{#tar-gzip-create-option}
新しいアーカイブを作成する `tar` オプションはどれですか？

::option[`-x`]{#tar-gzip-option-extract explanation="`-x` 操作はアーカイブのメンバーを展開します。"}
::option[`-c`]{#tar-gzip-option-create .correct explanation="作成操作は、指定された入力から新しいアーカイブを書き出します。"}
::option[`-t`]{#tar-gzip-option-list explanation="`-t` 操作はメンバーを展開せずに一覧表示します。"}
:::

## Gzip で圧縮した Tar アーカイブを作成する

GNU tar をはじめ多くの実装では、`-z` で gzip を呼び出せます。

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

結果は、gzip で圧縮された一つの tar ストリームです。圧縮はアーカイブを暗号化せず、読み取って展開できる人から内容を隠しません。機密性が必要なら、適切な認証付き暗号化の手順を使い、鍵を別に管理してください。

:::single-choice{#tar-gzip-z-option}
示した `tar` コマンドの `-z` は何を要求しますか？

::option[ゼロ知識鍵でアーカイブを暗号化する。]{#tar-gzip-z-encrypt explanation="tar も gzip も、このオプションでは暗号化を提供しません。"}
::option[長さがゼロのメンバーをすべて破棄する。]{#tar-gzip-z-zero explanation="このオプションは gzip を選択し、サイズによるメンバーの絞り込みは行いません。"}
::option[アーカイブストリームを gzip で処理する。]{#tar-gzip-z-gzip .correct explanation="`z` オプションは tar のアーカイブ操作を gzip の圧縮または展開へ接続します。"}
:::

## 展開前に一覧表示する

別の相手から受け取ったアーカイブは、信頼できない入力として扱います。まずメンバー名を一覧表示してください。

```bash
$ tar -tzf download.tar.gz
```

予期しない絶対パス、`..` によるパストラバーサル、意外なシンボリックリンクやハードリンク、デバイスファイル、重要ファイルを上書きする名前がないか確認します。現代の tar 実装には保護機能がありますが、動作とオプションは異なり、展開すると攻撃者が選んだ名前と内容が作成されることに変わりはありません。

新しく作った非特権のステージングディレクトリへ展開します。

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

未確認のアーカイブを root として展開してはいけません。作成されたものを検証してから、選択したファイルを最終的な場所へ移動します。

:::single-choice{#tar-gzip-list-before-extract}
アーカイブのメンバーを展開せずに一覧表示する操作はどれですか？

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="これは現在のディレクトリからアーカイブを作成または置き換えます。"}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="`-x` 操作は対象ディレクトリへメンバーを書き出します。"}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="`-t` 操作はメンバー表を読み取って表示し、`-z` が gzip を処理します。"}
:::

## その他の圧縮形式

tar 実装は bzip2 や xz などの圧縮器も扱えます。GNU tar では一般にそれぞれ `-j` と `-J` で選択します。対応形式と自動検出の動作は異なるため、`tar --help` またはローカルマニュアルを参照してください。ZIP は別のアーカイブ形式であり、`zip` や `unzip` などのツールで操作します。

:::single-choice{#tar-gzip-archive-confidentiality}
gzip 圧縮によって tar アーカイブに機密性が加わりますか？

::option[いいえ。読み取れる人は通常、そのまま展開できる。]{#tar-gzip-not-encryption .correct explanation="圧縮は表現とサイズを変えますが、アクセス制御や暗号学的な秘匿性を提供しません。"}
::option[はい。gzip がファイル名から暗号鍵を導出する。]{#tar-gzip-filename-key explanation="Gzip はそのような暗号化機構を実装していません。"}
::option[はい。gzip が処理する前に tar が各メンバーを暗号化する。]{#tar-gzip-tar-encrypt explanation="Tar はメンバーをアーカイブしますが、内容を自動的に暗号化しません。"}
:::

[ファイルのパッケージ化と圧縮](https://labex.io/labs/linux-file-packaging-and-compression-385413)で破棄可能なファイルを使って練習し、[tar でバックアップを作成・復元する](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)で検査とステージングを実践してください。

## まとめ

tar のアーカイブと gzip の圧縮を安全に組み合わせられるようになりました。

1. tar アーカイブと gzip 圧縮を区別する。
2. `-c` でアーカイブを、`-z` で gzip ストリームを作成する。
3. `-x` で展開する前に `-t` でメンバーを一覧表示する。
4. 信頼できない内容は非特権のステージングディレクトリへ展開する。
5. 圧縮と暗号化を別のものとして扱う。
