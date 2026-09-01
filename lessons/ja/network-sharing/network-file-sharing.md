---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "ja"
order_index: 1
title: "ファイル共有の概要"
description: "SSH を利用したファイル転送方法を選び、scp で安全にコピーする方法を学びます。"
meta_title: "ファイル共有の概要 - ネットワーク共有"
meta_description: "無料オンラインコースで Linux ファイル共有を探求しましょう。安全なネットワークファイル転送のための scp のような Linux コマンドを学ぶ最良の方法の一つです。Linux でのコーディングのための重要なリソース。"
meta_keywords: "linux ファイル共有，scp コマンド，セキュアコピー, linux コマンド学習，無料オンライン linux コース，linux でのコーディング，ネットワークファイル転送，linux 学習リソース"
---

ネットワーク経由のファイル移動には、一度きりのコピー、継続的にマウントする共有、同期するディレクトリツリーなどがあります。方向、データ量、更新頻度、認証モデル、ネットワークの信頼性、メタデータ要件、クライアントにライブ共有が必要かどうかに応じて方法を選びます。

## 転送方法を選ぶ

- `scp` または SFTP は、SSH で認証されたコピーまたは対話型転送を行う。
- `rsync` は、ローカルまたは SSH などのトランスポート経由でディレクトリツリーを効率よく同期する。
- NFS は、主に Unix 系ホスト間でサーバーの export をマウント済みファイルシステムとして提供する。
- Linux では Samba が実装する SMB は、多くの OS 間で共有アクセスを提供する。
- HTTP は単純なダウンロードに使えるが、一般的なマウント済みファイルシステムではない。

コピーしただけで自動的にバックアップになるわけではありません。バックアップ設計には、独立した保存世代、復元テスト、完全性検査、同じ削除や侵害からの保護も必要です。

:::single-choice{#file-sharing-one-time-ssh-copy} SSH 経由で一度だけファイルをコピーするのに適したツールはどれですか？

::option[`scp`]{#file-sharing-scp .correct explanation="SCP は SSH の認証とトランスポートを使ってファイルをコピーします。"}
::option[`uptime`]{#file-sharing-uptime explanation="uptime はホストの稼働時間と負荷を報告するもので、ファイルを転送しません。"}
::option[`logrotate`]{#file-sharing-logrotate explanation="logrotate はホスト上のファイルログ世代を管理します。"}
:::

## scp のパスを理解する

基本形は `scp SOURCE DESTINATION` です。リモートのオペランドは通常、`user@host:path` の形式を使います。

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

最初のコマンドはローカルファイルを送信し、二番目はリモートファイルを取得します。コロンがリモートホストとパスを区切ります。シェルにとって特別な文字を含むパスは引用し、信頼できない曖昧なファイル名を避けてください。

:::single-choice{#file-sharing-scp-pull-source} `scp` でファイルを取得する場合、リモート指定はどこに置きますか？

::option[ローカルのコピー先より前の、コピー元として。]{#file-sharing-pull-source .correct explanation="コピー方向は、コピー元からコピー先へというオペランド順で決まります。"}
::option[すべてのオプションより後の、ローカルコピー先として。]{#file-sharing-pull-destination explanation="取得するリモートオブジェクトはコピー元オペランドです。"}
::option[ユーザーの SSH 設定ファイル内だけに。]{#file-sharing-pull-config explanation="SSH 設定で既定値を指定できますが、コピーするリモートパスは引き続きオペランドとして必要です。"}
:::

## ディレクトリをコピーする

ディレクトリツリーには再帰モードを使います。

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

コピー前にデータ量、シンボリックリンク、権限、所有権要件、空き容量、コピー先での名前を確認します。SCP は同期ポリシーではないため、ディレクトリを繰り返しコピーしても、コピー元から消えたファイルがコピー先に残ることがあります。

:::single-choice{#file-sharing-scp-recursive} `scp -r` は何を要求しますか？

::option[コピー前にリモートのコピー先を削除する。]{#file-sharing-scp-remove explanation="再帰モードはディレクトリをたどるもので、後始末のポリシーを定義しません。"}
::option[ディレクトリツリーを再帰的にコピーする。]{#file-sharing-scp-tree .correct explanation="選択したコピー元がディレクトリの場合に必要なフラグです。"}
::option[SSH 設定への読み取り専用アクセスを行う。]{#file-sharing-scp-readonly explanation="このオプションが関係するのはディレクトリ探索であり、設定へのアクセスではありません。"}
:::

## 相手の身元と結果を検証する

SSH のホスト鍵検証は、誤ったサーバーへの接続を防ぎます。ホスト鍵が変わった場合は警告を回避せず、信頼できる経路で確認すべき事象として扱ってください。最小権限のアカウントを使い、環境に適した方法で鍵を管理します。

転送後は終了状態、想定ファイル、サイズ、メタデータを検証し、完全性要件があれば両端で独立して計算したハッシュも比較します。コピー先のアプリケーションが実際にデータを読めることも確認してください。

:::single-choice{#file-sharing-host-key-change} SSH が予期しないホスト鍵の変更を報告したら、どうすべきですか？

::option[今後の全転送でホスト鍵確認を無効にする。]{#file-sharing-disable-checking explanation="重要なサーバー身元確認機能を失うことになります。"}
::option[続行前に、信頼できる情報源で新しい鍵を検証する。]{#file-sharing-verify-key .correct explanation="警告は、ホスト再構築、宛先間違い、通信の傍受を示す可能性があるため、調査が必要です。"}
::option[秘密の認証鍵をコマンド出力で公開する。]{#file-sharing-publish-key explanation="秘密の認証情報を露出させてはいけません。"}
:::

## まとめ

これで、安全な一度きりのネットワークファイルコピーを選択し、検証できます。

1. アクセス要件と保存要件に共有方法を合わせる。
2. ローカルとリモートの `scp` オペランドを、コピー元とコピー先の順に読む。
3. ディレクトリツリーには意図して再帰モードを使う。
4. サーバーの身元、転送結果、コピー先での利用可否を検証する。
