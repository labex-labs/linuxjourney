---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "ja"
order_index: 3
title: "シンプルな HTTP サーバー"
description: "Python の HTTP サーバーを使い、管理されたディレクトリを一時的に公開する方法を学びます。"
meta_title: "シンプルな HTTP サーバー - ネットワーク共有"
meta_description: "Python の http.server モジュールを使用して、Linux でシンプルな HTTP サーバーを素早くセットアップする方法を学びます。このガイドでは、ネットワーク全体で簡単にファイルを共有するためのシンプルな Linux ウェブサーバーの作成方法を説明します。"
meta_keywords: "linux シンプル http サーバー, シンプル http サーバー linux, シンプル linux ウェブサーバー, python http.server, python simplehttpserver とは，ファイル共有，ネットワークサーバー"
---

Python の `http.server` モジュールは、短時間のテストや信頼できる相手への転送に静的ファイルを提供できます。これは本番用 Web サーバーではなく、認証、認可、TLS、レート制限、悪意ある通信に耐える堅牢な処理を備えていません。

## 共有ディレクトリを準備する

公開するファイルだけを入れた専用ディレクトリを作ります。起動前に隠しファイル、シンボリックリンク、権限、機密メタデータを確認してください。ホームディレクトリ、リポジトリのルート、認証情報ディレクトリ、システムパスを公開してはいけません。

`--directory` を使い、共有ルートを明示します。

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

index ファイルがない場合、通常このモジュールはディレクトリ一覧を生成します。リスナーへ到達できる人は、公開内容を列挙し、ダウンロードできる可能性があります。

:::single-choice{#http-server-directory-option}
`--directory /srv/temporary-share` を使うのはなぜですか？

::option[すべての HTTP 応答を自動的に暗号化するため。]{#http-server-directory-tls explanation="directory オプションは TLS を追加しません。"}
::option[ダウンロードする人ごとにアカウントを作るため。]{#http-server-directory-accounts explanation="基本モジュールにはユーザー認証がありません。"}
::option[意図するドキュメントルートを明確にするため。]{#http-server-explicit-root .correct explanation="確認済みのルートを明示すれば、誤った作業ディレクトリからファイルを公開する危険を減らせます。"}
:::

## 待ち受けアドレスを制御する

同じホストからだけ接続する場合は、ループバックへバインドします。

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

信頼できるネットワーク上で共有するなら、適切なインターフェースアドレスへ意図してバインドし、ファイアウォールポリシーを確認します。制限する bind 指定なしで実行すると、通常は利用可能な全インターフェースで待ち受け、意図したネットワークの外へディレクトリが露出する可能性があります。

:::single-choice{#http-server-loopback-bind}
`127.0.0.1` にバインドしたサーバーへ、通常誰が到達できますか？

::option[同じホスト上のクライアント。]{#http-server-local-clients .correct explanation="ループバックへの bind は、ローカルテストや、意図して設定したトンネルの背後で使うのに適しています。"}
::option[公開インターネット上の任意のホスト。]{#http-server-public explanation="ループバックは同じネットワーク名前空間内だけのもので、公開インターフェースではありません。"}
::option[Bluetooth で接続したデバイスだけ。]{#http-server-bluetooth explanation="このアドレスは Bluetooth のトランスポートとは無関係です。"}
:::

## アクセスをテストする

サーバーを動かしているホストから既知のファイルを要求し、応答を確認します。

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

許可されたリモートテストでは、ループバックではなく選択したインターフェースアドレスを使います。目的のファイルにアクセスできることと、ドキュメントルート外のファイルにはアクセスできないことの両方を確認してください。ブラウザーで成功しただけでは、公開範囲や機密性が適切だとは判断できません。

:::single-choice{#http-server-default-port-command}
`python3 -m http.server 8000` で明示的に選択されるポートはどれですか？

::option[22]{#http-server-port-22 explanation="ポート 22 は一般に SSH に関連し、このコマンドでは選択されていません。"}
::option[8000]{#http-server-port-8000 .correct explanation="位置引数のポート番号が、モジュールの待ち受け先を指定します。"}
::option[443]{#http-server-port-443 explanation="このコマンドはポート 443 の HTTPS を設定しません。"}
:::

## 停止して後片付けする

一時サービスは監視できる端末で実行し、転送が終わったら `Ctrl-C` で停止します。リスナーがなくなったことも確認します。

```bash
$ ss -ltn 'sport = :8000'
```

データ取扱方針に従って一時コピーを削除し、一時的なファイアウォールルールも元に戻します。永続的、認証付き、またはインターネット向けの配信には、アクセス制御と TLS を設定した、保守されているサーバーを使ってください。

:::single-choice{#http-server-completion-check}
一時転送が終わった後に行うべきことはどれですか？

::option[サーバーを停止し、ポートが待ち受けていないことを確認する。]{#http-server-stop-verify .correct explanation="確認することで、一時的なネットワークサービスが実際に終了したと分かります。"}
::option[後で誰かが必要とする場合に備え、リスナーを動かし続ける。]{#http-server-leave-running explanation="許可された目的が終わったら、不要な公開を取り除くべきです。"}
::option[ドキュメントルートへ追加の非公開ファイルをコピーする。]{#http-server-add-private explanation="公開ディレクトリに置くのは、意図して共有する内容だけです。"}
:::

## まとめ

これで、公開範囲を限定した一時的な Python HTTP サーバーを実行できます。

1. 専用の確認済みディレクトリだけを公開する。
2. 目的に合う最も限定的なアドレスへバインドする。
3. 意図したアクセスと、意図しない境界の両方をテストする。
4. 終了後にリスナーを停止し、一時アクセスを後片付けする。
