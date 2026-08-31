---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "ja"
order_index: 2
title: "rsync"
description: "rsync によるローカルまたは SSH 経由のディレクトリ同期を、事前確認して安全に実行・検証する方法を学びます。"
meta_title: "rsync - ネットワーク共有"
meta_description: "強力な rsync コマンドを Linux で使用して、効率的なファイル同期、リモートデータ転送、信頼性の高いバックアップを行う方法を紹介します。このガイドでは、主要な rsync コマンドとオプションを解説します。"
meta_keywords: "rsync, linux rsync, ファイル同期，データバックアップ，リモート同期，rsync コマンド，linux ファイル転送，rsync チュートリアル"
---

`rsync` は、変更されていないデータを不必要に転送せず、ファイルやディレクトリツリーを同期します。ただし効率がよいからといって、すべての実行が安全なわけではありません。コピー元の構文、末尾スラッシュ、メタデータ、除外、削除ポリシーによって結果が決まります。

## コピー元とコピー先を読む

ローカルで `source/` の内容を `destination/` へ同期します。

```bash
$ rsync -a -- source/ destination/
```

`source/` の末尾スラッシュは「このディレクトリの内容をコピーする」という意味です。スラッシュがない `rsync -a source destination/` は、`destination/source` を作成または更新します。スラッシュの付け方を変えるときは、必ず結果のパスを事前確認してください。

:::single-choice{#rsync-source-trailing-slash}
`rsync -a source/ destination/` のコピー元にある末尾スラッシュは、何を意味しますか？

::option[転送成功後にコピー元を削除する。]{#rsync-delete-source explanation="コピー元を削除するには、別の明示的なオプションとポリシーが必要です。"}
::option[`source` の内容をコピー先へコピーする。]{#rsync-copy-contents .correct explanation="コピー元のスラッシュを外すと、コピー先の最上位レイアウトが変わります。"}
::option[コピー先をリモート Windows 共有として解釈する。]{#rsync-windows-share explanation="スラッシュが制御するのはディレクトリの内容であり、トランスポート方式ではありません。"}
:::

## アーカイブモードを理解する

アーカイブモード `-a` は、一般に `-rlptgoD` と要約される、再帰処理とメタデータ保持のオプション群に相当します。権限とプラットフォームの対応範囲内で、シンボリックリンク、権限、更新時刻、グループ、所有者、デバイスまたは特殊ファイルを保持します。

アーカイブモードだけでは、ハードリンク、ACL、拡張属性は保持しません。それぞれ通常は `-H`、`-A`、`-X` が必要です。また、履歴世代も自動的には作りません。

:::single-choice{#rsync-archive-limit}
`-a` だけでは保持されないメタデータはどれですか？

::option[ハードリンクの関係。]{#rsync-hard-links .correct explanation="ハードリンクの保持には、別途 `-H` オプションが必要です。"}
::option[ディレクトリの再帰処理。]{#rsync-archive-recursion explanation="アーカイブモードには再帰的な探索が含まれます。"}
::option[更新時刻。]{#rsync-archive-times explanation="アーカイブモードには時刻の保持が含まれます。"}
:::

## 転送を事前確認する

影響の大きい同期を行う前に、dry run で変更内容を項目別に表示します。

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

dry run は現在のスキャンに基づく動作を予測しますが、本番コマンドの前にファイルが変化しないとは保証しません。正確なコマンドを保存して出力を確認し、両エンドポイントを確認してから `--dry-run` を外して実行してください。

:::single-choice{#rsync-dry-run-purpose}
`--dry-run --itemize-changes` から何が得られますか？

::option[別デバイスに保持される永続スナップショット。]{#rsync-dry-backup explanation="dry run ではデータコピーも独立した保存も作成されません。"}
::option[コピー元ファイルが後で変化しないという保証。]{#rsync-dry-lock explanation="事前確認をしても、コピー元ツリーはロックされません。"}
::option[rsync が現時点で予定している変更のプレビュー。]{#rsync-dry-preview .correct explanation="項目別の dry-run 出力から、変更前にパスとメタデータの判断を確認できます。"}
:::

## SSH 経由で同期する

一般的なリモートオペランドを使って、リモートホストへ送信またはリモートホストから取得します。

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

現代の rsync はこの形式で通常 SSH を使いますが、設定済みリモートシェル、ホスト鍵、アカウント権限、リモート側の rsync の有無を確認してください。`-z` の圧縮は、帯域の狭い回線で圧縮しやすいデータには役立ちますが、圧縮済みデータには CPU を浪費する場合があります。

:::single-choice{#rsync-pull-direction}
リモートデータをローカルディレクトリへ取得するオペランド順はどれですか？

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="この順序はローカルの内容をリモートのコピー先へ送信します。"}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="示されたリモートパス構文になっておらず、無関係な破壊的オプションも追加されています。"}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="リモートツリーがコピー元、ローカルツリーがコピー先です。"}
:::

## 削除を破壊的操作として扱う

`--delete` は、同期対象範囲内でコピー元にないコピー先エントリを削除します。エンドポイントの逆指定、誤ったスラッシュ、不適切な除外によって、有効なデータを消す可能性があります。承認前にテスト用コピー先で事前確認し、復元可能なバックアップを確保し、マウント状態を確認して、最大削除数の制限も検討してください。

本番実行後は終了状態とログを調べ、想定ファイル数とメタデータを比較し、代表的な内容または復元をテストします。rsync の同期だけでは、望ましくない削除や破損も複製されるため、完全なバックアップ戦略にはなりません。

:::single-choice{#rsync-delete-effect}
同期中に `--delete` が行う可能性のある操作はどれですか？

::option[SSH ホスト鍵で全転送ファイルを暗号化する。]{#rsync-delete-encrypt explanation="削除ポリシーはファイル暗号化と無関係です。"}
::option[コピー先ファイルシステムへの全変更を防止する。]{#rsync-delete-readonly explanation="このオプションは、むしろ追加のコピー先変更を明示的に許可します。"}
::option[選択したコピー元範囲にないコピー先エントリを削除する。]{#rsync-delete-destination .correct explanation="コピー先の構成をコピー元へ合わせるオプションなので、確認済みプレビューと復旧計画が必要です。"}
:::

## まとめ

これで、破壊的になり得る例外を見落とさず、`rsync` 操作を事前確認して検証できます。

1. 末尾スラッシュで意図するディレクトリ配置を表す。
2. 必要に応じてアーカイブモードに含まれないメタデータオプションを追加する。
3. 本番同期前に項目別の dry-run 出力を確認する。
4. SSH の身元とエンドポイントの方向を検証する。
5. 削除とバックアップ保存を明示的なポリシーとして扱う。
